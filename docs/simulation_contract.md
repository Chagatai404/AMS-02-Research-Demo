# Simulation Contract

This contract defines the planned clean interfaces for the future fast-MC
pipeline. It is a target contract, not a claim that the simulator is already
implemented.

## Truth-Level Fields

Planned truth-level event fields:

- `event_id`: integer event identifier unique within a campaign.
- `campaign_id`: independent generation campaign identifier.
- `particle`: one of `electron`, `positron`, or `proton`.
- `label_binary`: `signal` for `e+/-`, `background` for proton.
- `charge_number`: particle charge in units of elementary charge.
- `true_energy_GeV`: incident total or kinetic energy, explicitly documented.
- `true_momentum_GeV_c`: incident momentum.
- `true_rigidity_GV`: true rigidity magnitude or signed rigidity, documented.
- `entry_x_m`, `entry_y_m`: ECAL entry position.
- `dir_x`, `dir_y`, `dir_z`: incident direction unit vector.
- `rng_seed`: event-level or stream-level seed provenance.

## Reconstructed Fields

Planned reconstructed fields:

- `reco_energy_GeV`: reconstructed ECAL energy from cell deposits.
- `energy_over_rigidity`: reconstructed ECAL energy divided by tracker
  rigidity or parameterized momentum proxy.
- `longitudinal_centroid`: energy-weighted longitudinal shower position.
- `longitudinal_rms`: shower depth spread.
- `lateral_rms`: shower lateral spread.
- `max_layer_fraction`: fraction of energy in the hottest longitudinal layer.
- `tail_fraction`: late-layer energy fraction.
- `n_cells_above_threshold`: digitized occupancy.
- `finite_output`: boolean validation marker for feature-generation checks.

## ECAL Cell Array

The canonical event representation is:

```text
shape = (18, 72)
units = GeV deposited energy per cell
```

The 18 longitudinal samplings correspond to nine superlayers with alternating
x/y views. The 72 lateral cells per layer provide 1296 scalar measurements per
event.

## Units

- Energy: GeV.
- Momentum: GeV/c.
- Mass: GeV/c^2.
- Rigidity: GV.
- Distance: metres unless a field explicitly states otherwise.
- Magnetic field: tesla.
- Time: seconds.
- Angles: radians in code; degrees only in user-facing configuration if named
  with `_deg`.

## Randomness and Seeds

- Use `numpy.random.Generator`, not hidden global random state.
- Every campaign has a base seed.
- Train, validation, and test data come from independent campaigns or seed
  streams.
- Event-level reproducibility should be possible from campaign metadata and
  event identifier.

## Invariants

- ECAL cell energies are finite and nonnegative after digitization.
- Reconstructed scalar features are finite or explicitly marked missing.
- Array shape is always `(18, 72)` unless a future contract revision changes it.
- `E_over_p` or `E_over_R` is derived from reconstructed quantities, not sampled
  independently.
- ECAL-only observables cannot assign electron versus positron charge sign.

## Validation Targets

Validation targets are not yet achieved by this repository. Planned targets
include:

- Electron reconstructed energy resolution:
  `sigma_E / E = sqrt(0.104^2 / E_GeV + 0.014^2)`.
- Analytic-vs-numerical trajectory checks for Phase 1 tracker repair.
- Conservation and positivity checks for ECAL shower generation.
- Independent-campaign stability checks for ML and QML comparisons.
- Geant4 or suitable reference comparison before proton-response claims.
