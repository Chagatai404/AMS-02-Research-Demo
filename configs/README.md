# Configurations

Configuration files define reproducible fast-MC and analysis settings. They
should describe seeds, geometry, generation campaigns, output locations, and
future-tunable physics parameters without embedding machine-specific paths.

Relative output paths are resolved by `ams_qml.config.load_config` against the
project root declared in the config metadata.
