"""AMS-02-like ECAL segmentation metadata for future fast Monte Carlo work."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class ECalSegmentation:
    """Cell-array layout for an AMS-02-like ECAL event representation."""

    longitudinal_samplings: int = 18
    lateral_cells_per_layer: int = 72

    @property
    def shape(self) -> tuple[int, int]:
        """Energy-deposition array shape as ``(longitudinal, lateral)``."""

        return self.longitudinal_samplings, self.lateral_cells_per_layer

    @property
    def n_cells(self) -> int:
        """Total number of scalar cell measurements."""

        return self.longitudinal_samplings * self.lateral_cells_per_layer

    @classmethod
    def from_config(cls, config: dict[str, Any]) -> "ECalSegmentation":
        """Build segmentation metadata from the ``ecal`` config section."""

        ecal = config["ecal"]
        return cls(
            longitudinal_samplings=int(ecal["longitudinal_samplings"]),
            lateral_cells_per_layer=int(ecal["lateral_cells_per_layer"]),
        )
