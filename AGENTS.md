# AGENTS.md

## Purpose

This file defines repository-wide instructions for Codex and other coding agents working on this project.

The project is evolving from an educational AMS-02 detector demo into a reproducible research study on physics-informed ECAL simulation and quantum machine learning. Preserve the educational history, but do not present legacy simulations as validated detector models.

The main research question is:

> Can quantum machine-learning classifiers provide competitive performance or useful generalization behavior relative to matched classical baselines for electron/positron versus proton classification using low-dimensional, physics-informed features extracted from a simplified AMS-02-like ECAL Monte Carlo simulation?

## Instruction hierarchy

When instructions disagree, follow this order:

1. The user's current request.
2. This `AGENTS.md` file.
3. `docs/research_plan.md` and `docs/scientific_scope.md`.
4. `docs/simulation_contract.md` and configuration files under `configs/`.
5. Existing implementation details.

Legacy notebooks, old generated datasets, and notebook outputs document earlier work. They are not authoritative specifications for new code.

If the planned documentation does not exist yet, create it during Phase 0 rather than inferring scientific requirements from legacy notebook code.

## Scientific scope

The primary classification task is binary:

- Signal: electrons and positrons grouped as `e±`.
- Background: protons.

Scientific guardrails:

- ECAL shower information cannot determine the sign of a unit-charge lepton. Electron/positron charge sign belongs to the tracker measurement.
- The planned ECAL representation is 18 longitudinal layers by 72 lateral cells, for 1296 cell-energy measurements.
- The fast simulator is a physics-informed parameterized Monte Carlo, not the official AMS-02 simulation and not an exact detector replica.
- Raw 1296-cell events are not the intended direct input to the first QML models. QML should initially use approximately 6–12 documented shower features or reduced components.
- Proton rejection at fixed electron efficiency is the primary classification metric. Ordinary accuracy is secondary.
- Do not claim quantum advantage without statistically convincing, reproducible evidence against fair matched classical baselines.

When adding detector constants or physics models, use primary papers, official AMS sources, PDG material, or official Geant4 documentation. Record sources and assumptions in `docs/references.md` or beside the relevant configuration parameter.

## Baseline roadmap

Treat this roadmap as the project baseline. Do not jump to later phases simply because a later task is more visually impressive.

### Phase 0 — Repository foundation

- Preserve Week 1 and Week 2 work on the GitHub `legacy` branch.
- Establish the `src/ams_qml` package.
- Separate code, notebooks, configuration, tests, data, generated artifacts, and documentation.
- Add reproducible environment and test instructions.
- Document known limitations of the legacy implementation.

### Phase 1 — Tracker repair and validation

- Correct detector geometry, field orientation, propagation timestep, and detector-scale stopping conditions.
- Reconstruct signed curvature or rigidity without using truth information in the estimator.
- Validate numerical motion against analytic trajectories in a uniform magnetic field.
- Add detector effects only after the basic propagation and reconstruction are validated.

### Phase 2 — ECAL fast Monte Carlo

- Implement geometry and a documented event schema.
- Implement and validate electron-only showers first.
- Add proton response only after electron validation passes.
- Add digitization, reconstruction, and shower-feature extraction.
- Generate independent Monte Carlo campaigns with explicit configurations and seeds.

### Phase 3 — Classical baselines

- Begin with logistic regression and boosted trees.
- Add a small MLP and, when useful, a small CNN for cell arrays.
- Evaluate proton rejection versus electron efficiency and versus energy.

### Phase 4 — Quantum machine learning

- Select a QML framework deliberately; do not add one merely to scaffold the repository.
- Compare quantum and classical models using identical reduced inputs and data splits.
- Report qubits, circuit depth, shots, parameters, seeds, runtime, and uncertainty.

### Phase 5 — Systematics and external validation

- Evaluate simulation-parameter shifts and train/test domain shifts.
- Compare a smaller sample with a simplified Geant4 model or suitable reference data.
- Prepare a reproducible final report with explicit limitations.

The old ideas concerning flux reconstruction, solar modulation, and broad multi-species PID may remain as historical or future directions, but they are not mandatory milestones for the focused ECAL/QML study.

## Known legacy limitations

Keep these limitations visible when interpreting or migrating old work:

- The Week 1 Boris integration uses steps tied to a fraction of a complete gyroperiod. At relevant rigidities, a single numerical step can exceed the detector scale.
- Tracker-layer intersections are therefore interpolated from under-resolved trajectories.
- The saved integrated tracker dataset has approximately 99% absolute relative rigidity error at the 68th percentile and a true/reconstructed rigidity correlation near 0.12.
- The simpler parameterized tracker is more stable, with an observed 68th-percentile absolute relative error near 2%, but it remains a hand-defined toy response.
- The current tracker geometry is educational rather than AMS-like.
- Legacy rigidity estimation depends on truth information and is not a valid reconstruction pipeline.
- The Week 2 ECAL response consists of hand-selected scalar distributions rather than cell-level shower simulation.
- `E_ecal` and `E_over_p` were sampled independently. New code must derive ratios from reconstructed quantities.
- Lightly smeared truth-charge proxies make legacy nuclear classification artificially easy.
- Overall multiclass accuracy obscures the physically relevant proton-rejection task.

Do not use the integrated legacy dataset as validated training or calibration data.

## Repository organization

The intended package layout is:

```text
src/ams_qml/
    physics/
    tracker/
    ecal/
    datasets/
    models/
    evaluation/
```

Supporting directories should include:

```text
configs/
data/
docs/
notebooks/
tests/
legacy branch
```

Rules:

- Authoritative implementations belong under `src/ams_qml`, not in notebooks.
- Notebooks should import the package and focus on explanation, experiments, and figures.
- Configuration belongs under `configs/`; do not scatter tunable physics constants across notebooks.
- Tests belong under `tests/` and should exercise public behavior.
- Generated data, trained models, and experiment outputs should not be committed by default.
- Historical generated files may remain on the GitHub `legacy` branch for provenance.
- Do not create meaningless placeholder modules containing only `pass`.
- Do not add a QML dependency until the framework decision is made.

## Legacy preservation

Unless the user explicitly requests otherwise:

- Preserve all old notebooks, Python notebook exports, notes, figures, data, and reference PDFs.
- Move files with `git mv` when possible so history remains understandable.
- Do not rewrite legacy numerical outputs to make them appear correct.
- Do not silently copy unvalidated legacy algorithms into the clean package.
- If legacy logic is reused, state exactly what was migrated, what was changed, and how it was validated.
- Do not remove historical files merely because they are large. First explain the tradeoff and obtain direction if removal would affect repository history.

New work should normally avoid modifying archived legacy material except on the
dedicated GitHub `legacy` branch.

## Coding standards

- Target Python 3.11 or newer.
- Use a `src/` package layout.
- Add type hints to public functions and data structures.
- Use concise docstrings that state units, coordinate conventions, shapes, and assumptions.
- Include units in variable names where ambiguity is possible, such as `energy_GeV`, `time_s`, or `position_m`.
- Use `numpy.random.Generator` supplied through an explicit seed or dependency. Avoid hidden global random state.
- Do not perform simulation, plotting, network access, or file writes at import time.
- Do not hard-code user-specific absolute paths.
- Resolve output paths from a configuration file or explicit project root.
- Keep truth-level, detector-level, and reconstructed quantities distinct in names and schemas.
- Prefer small composable functions and dataclasses over large notebook classes with mixed responsibilities.
- Do not suppress numerical warnings without documenting why the result remains valid.
- Fail clearly on invalid configuration, shape, unit, or non-finite data.

If a model or module is not implemented, document its intended interface without fabricating output that resembles real simulation.

## Simulation rules

Every generated event must be reproducible from:

- a committed configuration;
- a recorded generator version;
- a campaign identifier;
- an explicit random seed;
- documented units and coordinate conventions.

Maintain a clear event pipeline:

```text
truth generation
    -> particle or shower response
    -> detector segmentation
    -> digitization
    -> reconstruction
    -> feature extraction
    -> dataset export
```

Required invariants include:

- finite numerical outputs;
- nonnegative cell energies after digitization unless a documented pedestal representation requires otherwise;
- explicit handling of thresholds, clipping, leakage, and saturation;
- no direct use of class labels or truth-only variables in reconstructed ML features;
- `E/p` or `E/R` calculated from reconstructed measurements, not independently sampled;
- physically valid beta values;
- explicit distinction between signed and absolute rigidity;
- energy accounting checks at each simulation stage.

Do not tune the generator solely until a classifier reaches a desired rejection value. Detector validation and classifier evaluation must remain separate.

## Data and experiment design

- Training, validation, and test sets should come from independent generation campaigns or seeds.
- Preserve event IDs and campaign IDs through preprocessing.
- Avoid random row splitting when correlated events, augmented copies, or shared latent showers may cross partitions.
- Keep energy distributions and class priors explicit.
- A balanced training sample may be used, but evaluation priors and event weights must be documented.
- Record data schemas and units in `docs/simulation_contract.md`.
- Store large generated artifacts outside Git by default and document how to reproduce them.
- Never commit credentials, tokens, local environment files, or private data.

## ML and QML evaluation

For binary `e±` versus proton classification, report at least:

- ROC AUC;
- electron efficiency;
- proton efficiency;
- proton rejection `1 / epsilon_p`;
- proton rejection at 90% electron efficiency;
- energy-binned performance;
- sample counts and uncertainty intervals.

High rejection requires enough proton events to measure it. If zero protons survive a threshold, report a statistically justified bound rather than infinite rejection.

For model comparisons:

- use the same train, validation, and test definitions;
- give matched baselines the same input features;
- separate model selection from final testing;
- repeat stochastic experiments over multiple seeds;
- retain negative results;
- report preprocessing and hyperparameter selection;
- do not describe simulator-label recovery as detector discovery.

For QML specifically:

- document feature scaling and encoding;
- document qubit count, ansatz, circuit depth, entanglement pattern, shots, optimizer, and trainable parameters;
- compare against simple classical models of appropriate capacity;
- distinguish ideal statevector results from finite-shot or hardware results;
- avoid broad claims based on one split or one seed.

## Testing and validation

Add tests in proportion to the scientific risk of a change.

Foundational checks should include:

- package imports have no side effects;
- relativistic kinematics agree with analytic relationships;
- seeded simulation is deterministic;
- output arrays have the documented shapes;
- units and coordinate conventions are consistent;
- energy deposits are finite and physically bounded;
- reconstruction never reads truth-only fields;
- configuration paths work from outside the repository root.

For simulation changes, add distribution-level validation in addition to unit tests. Examples include energy resolution, shower maximum, containment fractions, rigidity residuals, and pull distributions.

Before handing off code, run the relevant subset of:

```bash
python -m compileall src
pytest
git diff --check
```

Also search new non-legacy code for machine-specific paths, top-level execution, unseeded random calls, and unintended generated files.

If a validation command cannot run because a dependency or external tool is unavailable, report that directly. Do not claim success based only on code inspection.

## Git and workspace safety

Before editing:

- inspect `git status`;
- inspect relevant files and nearby tests;
- preserve unrelated changes;
- use `rg` or `rg --files` for searches.

Do not:

- use destructive Git commands;
- reset or discard user changes;
- commit, push, merge, or open a pull request unless requested;
- rewrite large groups of notebooks mechanically without checking the result;
- add generated environments, caches, datasets, or secrets.

Keep changes scoped to the requested milestone. If completing a task requires a meaningful change to the research question or baseline roadmap, stop and explain the decision before expanding scope.

## Completion and handoff

A task is complete only when:

- requested code or documentation exists in the intended location;
- relevant tests and validation checks pass, or blockers are explicitly reported;
- generated files are not accidentally staged;
- scientific assumptions and limitations are documented;
- the final response identifies what changed, what was tested, and what remains deferred.

When suggesting the next task, choose the smallest validated next milestone. After repository reorganization, the default next milestone is:

> Implement and validate the ECAL geometry plus an electron-only 18 x 72 fast Monte Carlo, without adding proton showers or QML yet.
