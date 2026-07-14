# Research Plan

## Research Question

Can quantum machine-learning classifiers provide competitive performance or
useful generalization behavior relative to matched classical baselines for
electron/positron versus proton classification using low-dimensional,
physics-informed features extracted from a simplified AMS-02-like ECAL Monte
Carlo simulation?

## Decision Log

- Primary task: electron-or-positron versus proton classification.
- ECAL event format: `18 x 72`, for 1296 scalar cell measurements.
- QML input: reduced physics-informed feature vector, not raw 1296 cells.
- Primary evaluation: proton rejection at fixed electron efficiency.
- Dataset separation: independent generation campaigns.
- First simulation milestone: electron-only ECAL fast Monte Carlo.
- Proton fast Monte Carlo is approximate until Geant4 or reference validation.
- QML framework selection is deferred.
- Legacy integrated tracker data must not be used as validated training data.
- The project will not claim quantum advantage without statistically convincing
  evidence.

## Phase 0: Repository Reorganization

Goals:

- Preserve the original Week 1 and Week 2 work as legacy material.
- Establish a Python package with a `src/` layout.
- Add environment and dependency management.
- Separate source code, notebooks, configurations, tests, generated data, and
  documentation.
- Document known weaknesses of the old implementation.
- Ensure the repository can be installed and tested from its root.

Completion criteria:

- Legacy notebooks, notes, data, figures, and references are preserved on the
  GitHub `legacy` branch.
- Root documentation describes the active ECAL/QML project.
- `pyproject.toml`, `configs/`, `src/ams_qml/`, and `tests/` exist.
- Foundational tests pass.

## Phase 1: Tracker Repair and Validation

Goals:

- Correct the tracker propagation timestep and detector-scale stopping
  condition.
- Use an AMS-like geometry in which particles propagate through tracker planes
  while the magnetic field bends them in the appropriate transverse plane.
- Reconstruct signed curvature and rigidity without using true rigidity or true
  pitch angle in the estimator.
- Validate numerical trajectories against analytic motion in a uniform magnetic
  field.
- Add multiple scattering and detector effects only after basic propagation and
  reconstruction pass validation.
- Keep the tracker modular so ECAL studies can use simulated tracker output or
  documented parameterized resolution.

This phase is intentionally not implemented in Phase 0 except for safe package
boundaries.

Completion criteria:

- Analytic-vs-numerical trajectory tests pass.
- Signed rigidity reconstruction is validated on independent simulated events.
- The tracker module documents the remaining detector effects and limitations.

## Phase 2: ECAL Physics-Informed Fast Monte Carlo

Develop an event-level ECAL simulator using published AMS-02-like detector
properties:

- 17 radiation lengths.
- Nine superlayers.
- 18 longitudinal samplings.
- 72 lateral cells per layer.
- Alternating x/y views.
- 1296 total cell measurements.
- Event representation compatible with an `18 x 72` energy-deposition array.

Electron and positron shower model requirements:

- Sampled true energy.
- Entry position and incident direction.
- Fluctuating longitudinal shower development.
- Energy-dependent shower maximum.
- Lateral core and tail behavior.
- Integration into detector cells.
- Sampling fluctuations.
- Electronic noise and thresholds.
- Finite detector depth and leakage.
- Reconstructed energy derived from cell deposits.

Electron validation target:

```text
sigma_E / E = sqrt(0.104^2 / E_GeV + 0.014^2)
```

Proton response should eventually include a mixture of:

- Non-interacting or MIP-like events.
- Early and late hadronic interactions.
- Broad and irregular showers.
- Electromagnetic subshowers.
- Invisible energy.
- Larger event-to-event fluctuations.

The proton model must be labeled approximate until compared with Geant4 or
suitable reference data.

Build order:

1. Geometry and event schema.
2. Electron-only showers.
3. Electron validation.
4. Proton response.
5. Digitization.
6. Reconstruction and shower-feature extraction.
7. Independent Monte Carlo campaigns.

Completion criteria:

- ECAL geometry and `18 x 72` event schema are tested.
- Electron-only simulation reproduces documented validation targets within
  stated tolerance.
- Proton model is documented as approximate and separately validated before
  being used for physics claims.

## Phase 3: Classical Baselines

The classification task is binary:

- Signal: electrons and positrons grouped as `e+/-`.
- Background: protons.

ECAL observables must not be used to claim electron/positron charge-sign
separation. Charge sign must come from the tracker.

Planned baselines:

- Logistic regression.
- Boosted decision trees.
- Small multilayer perceptron.
- Optional small CNN using ECAL cell arrays.

Evaluation priorities:

- ROC curve and ROC AUC.
- Proton efficiency.
- Proton rejection, `1 / epsilon_p`.
- Proton rejection at 90% electron efficiency.
- Performance versus energy.
- Uncertainty intervals.
- Stability under simulation-parameter shifts.

Ordinary accuracy is secondary.

Completion criteria:

- Baselines share the same train/validation/test campaigns.
- Metrics report proton rejection at fixed electron efficiency.
- Uncertainty and seed variation are included.

## Phase 4: Quantum Machine Learning

Raw 1296-cell ECAL events are too large for a fair small-scale QML experiment.
The QML pipeline should use approximately 6-12 inputs from physics-informed
shower observables, documented dimensionality reduction, or both.

Potential quantum approaches:

- Variational quantum classifier.
- Quantum kernel method.

The QML framework has not yet been selected. Do not add PennyLane, Qiskit, or
another quantum dependency until the selection is justified.

QML comparisons must:

- Give classical and quantum models the same inputs.
- Include simple matched classical baselines.
- Repeat experiments over multiple seeds.
- Report finite-shot effects when applicable.
- Report circuit size, qubit count, depth, and trainable parameters.
- Avoid claims of quantum advantage without strong evidence.

Completion criteria:

- QML results are compared to matched classical models on identical inputs.
- Circuit resource counts and finite-shot settings are reported.
- Any advantage claim is supported by statistically convincing evidence.

## Phase 5: Systematics, Geant4, and Final Report

After the fast Monte Carlo and classifiers work:

- Vary shower and detector parameters.
- Evaluate train/test domain shifts.
- Compare a smaller sample with a simplified Geant4 calorimeter.
- Consider Geant4 `FTFP_BERT` for hadronic calorimeter validation.
- Clearly separate statistical uncertainty from simulation-systematic
  uncertainty.
- Prepare a final reproducible research report.

Project completion criteria:

- Validated fast ECAL simulation.
- Reproducible dataset-generation pipeline.
- Classical baselines.
- At least one fair QML experiment.
- Systematic checks.
- Documented limitations.
- Final report or paper-style notebook.

Historical roadmap sections on flux reconstruction, solar modulation, and
unrelated multi-species PID are preserved on the GitHub `legacy` branch as
historical ideas, but they are not mandatory milestones for this focused
project.
