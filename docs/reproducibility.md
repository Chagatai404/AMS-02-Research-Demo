# Reproducibility

## Configuration

Default settings live in `configs/fastmc_default.yaml`. Configuration files
should include seeds, detector geometry, generation settings, output paths, and
campaign definitions. Relative output paths are resolved by the package loader,
not by the current working directory.

## Seeds

The clean package uses `numpy.random.Generator`. Future simulation code should
derive independent streams from explicit campaign seeds and record provenance in
the generated metadata.

## Independent Campaigns

Training, validation, and final test samples should be generated as independent
Monte Carlo campaigns or seed streams. A random row split from one generated
dataset is not sufficient for the final study.

## Data Provenance

Generated artifacts should record:

- Code version or commit identifier when available.
- Config file path and config content hash.
- Campaign identifier.
- Base seed and seed offsets.
- Number of generated events.
- Simulator version and validation status.

## Artifact Generation

Large generated files, processed datasets, model checkpoints, and experiment
outputs should stay out of version control by default. The repository should
store code, configs, and small documentation needed to regenerate them.

## Legacy Outputs

Legacy notebook outputs on the GitHub `legacy` branch may contain
machine-specific absolute paths. They are preserved as historical records and
are not rewritten during reorganization. New code and new documentation should
not introduce machine-specific paths.
