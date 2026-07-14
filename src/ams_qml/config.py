"""Configuration loading for reproducible local research runs."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - exercised only in minimal envs
    yaml = None


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "configs" / "fastmc_default.yaml"


def load_config(config_path: str | Path | None = None) -> dict[str, Any]:
    """Load a YAML configuration and resolve declared output paths.

    Relative paths under ``output_paths`` are resolved against the project root
    declared in the config metadata. If no project root is declared, the parent
    of the configuration file is used. This keeps scripts independent of the
    caller's current working directory.
    """

    path = Path(config_path) if config_path is not None else DEFAULT_CONFIG_PATH
    path = path.expanduser().resolve()
    with path.open("r", encoding="utf-8") as handle:
        config = _load_yaml(handle.read())

    metadata = config.setdefault("metadata", {})
    project_root_value = metadata.get("project_root")
    project_root = (path.parent / project_root_value).resolve() if project_root_value else path.parent
    metadata["config_path"] = path
    metadata["project_root_resolved"] = project_root

    output_paths = config.get("output_paths", {})
    if isinstance(output_paths, dict):
        config["output_paths"] = {
            key: _resolve_path(value, project_root)
            for key, value in output_paths.items()
        }

    return config


def global_seed(config: dict[str, Any]) -> int:
    """Return the configured global seed as an integer."""

    try:
        return int(config["global"]["seed"])
    except KeyError as exc:
        raise KeyError("Configuration is missing global.seed.") from exc


def rng_from_config(config: dict[str, Any]) -> np.random.Generator:
    """Create a deterministic NumPy random generator from ``global.seed``."""

    return np.random.default_rng(global_seed(config))


def ecal_shape_from_config(config: dict[str, Any]) -> tuple[int, int]:
    """Return the expected ECAL cell-array shape from configuration."""

    ecal = config["ecal"]
    return int(ecal["longitudinal_samplings"]), int(ecal["lateral_cells_per_layer"])


def _resolve_path(value: Any, base_dir: Path) -> Any:
    if not isinstance(value, str):
        return value
    path = Path(value)
    return path if path.is_absolute() else (base_dir / path).resolve()


def _load_yaml(text: str) -> dict[str, Any]:
    if yaml is not None:
        return yaml.safe_load(text) or {}
    return _parse_simple_yaml(text)


def _parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the simple YAML subset used by the default config.

    This fallback keeps configuration loading usable in minimal Python
    environments. It supports nested mappings, block lists, strings, booleans,
    integers, and floats; full YAML syntax still requires PyYAML.
    """

    lines: list[tuple[int, str]] = []
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        lines.append((indent, raw_line.strip()))

    parsed, index = _parse_yaml_block(lines, 0, 0)
    if index != len(lines) or not isinstance(parsed, dict):
        raise ValueError("Could not parse configuration YAML.")
    return parsed


def _parse_yaml_block(
    lines: list[tuple[int, str]],
    index: int,
    indent: int,
) -> tuple[Any, int]:
    if index >= len(lines):
        return {}, index

    if lines[index][1].startswith("- "):
        items: list[Any] = []
        while index < len(lines) and lines[index][0] == indent:
            content = lines[index][1]
            if not content.startswith("- "):
                break
            items.append(_parse_scalar(content[2:].strip()))
            index += 1
        return items, index

    mapping: dict[str, Any] = {}
    while index < len(lines) and lines[index][0] == indent:
        content = lines[index][1]
        if ":" not in content:
            raise ValueError(f"Invalid config line: {content}")
        key, raw_value = content.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        index += 1

        if raw_value:
            mapping[key] = _parse_scalar(raw_value)
            continue

        if index < len(lines) and lines[index][0] > indent:
            mapping[key], index = _parse_yaml_block(lines, index, lines[index][0])
        else:
            mapping[key] = {}

    return mapping, index


def _parse_scalar(value: str) -> Any:
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value
