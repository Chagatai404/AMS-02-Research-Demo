# Data

The clean pipeline should not commit large regenerated datasets by default.
Generated files should be reproducible from configuration files, code version,
and deterministic seeds.

Planned local directories:

- `data/generated/`: raw fast-MC campaign outputs.
- `data/processed/`: reconstructed features and analysis-ready tables.
- `data/external/`: externally obtained reference data, with provenance.

Legacy CSV files from the Week 1 and Week 2 learning work are preserved in
`legacy/data/` and should not be used as validated training data.
