# AMS-02 ECAL Fast-MC and QML Research Foundation

This repository is being reorganized into a reproducible research project for
physics-informed AMS-02-like ECAL simulation and quantum machine-learning
comparisons.

## Research Question

Can quantum machine-learning classifiers provide competitive performance or
useful generalization behavior relative to matched classical baselines for
electron/positron versus proton classification using low-dimensional,
physics-informed features extracted from a simplified AMS-02-like ECAL Monte
Carlo simulation?

## Status

This is a research foundation, not a validated AMS-02 detector simulation. The
old Week 1 and Week 2 work is preserved on the GitHub `legacy` branch as
educational history. This branch contains the clean research foundation. The
package under `src/ams_qml/` currently contains only safe foundational pieces:
particle metadata, relativistic kinematics, configuration loading, and ECAL
segmentation metadata.

## Scope

The active project focuses on:

1. A simplified AMS-02-like ECAL fast Monte Carlo.
2. Reconstructed shower observables from an `18 x 72` energy-deposition array.
3. Classical electron-or-positron versus proton baselines.
4. Small-input QML experiments using the same reduced features as matched
   classical models.

It does not claim to be the official AMS-02 Monte Carlo, a full Geant4 detector
model, or a validated reproduction of AMS-02 performance.

## Planned Workflow

```text
configuration and seeds
  -> physics-informed fast Monte Carlo
  -> detector-like ECAL cell arrays
  -> reconstruction and shower features
  -> independent train/validation/test campaigns
  -> classical ML baselines
  -> matched QML experiments
  -> systematics and Geant4/reference validation
```

## Current Limitations

- The tracker repair is not implemented yet.
- The ECAL shower generator is not implemented yet.
- Proton response modeling is deferred until electron validation exists.
- No ML or QML model has been trained in the reorganized package.
- Archived legacy datasets and plots are historical outputs, not validated
  training data.

## Repository Structure

```text
configs/      Documented default configuration.
docs/         Research plan, scope, simulation contract, audit, references.
src/ams_qml/  Clean Python package foundation.
tests/        Foundational package/config/kinematics tests.
legacy branch Archived Week 1 and Week 2 notebooks, notes, data, figures, PDFs.
```

## Setup

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install -e ".[dev,notebooks]"
```

## Tests

```powershell
python -m compileall src
python -m pytest
git diff --check
```

## Reproducibility Principles

- Use explicit YAML configuration.
- Use deterministic `numpy.random.Generator` instances.
- Keep generated data out of version control by default.
- Separate train, validation, and test datasets by independent campaigns or
  seeds, not only by random row splits.
- Record provenance for generated artifacts.
- Keep archived legacy outputs readable on the `legacy` branch, but do not treat
  them as validated physics.

## Roadmap

- Phase 0: repository reorganization and clean package foundation.
- Phase 1: tracker propagation and signed-rigidity validation.
- Phase 2: ECAL geometry plus electron-only `18 x 72` fast Monte Carlo.
- Phase 3: classical baselines and proton-rejection metrics.
- Phase 4: matched QML experiments on reduced physics-informed features.
- Phase 5: systematics, Geant4/reference comparison, and final report.

## Key Documents

- [Research plan](docs/research_plan.md)
- [Scientific scope](docs/scientific_scope.md)
- [Legacy audit](docs/legacy_audit.md)
- [Simulation contract](docs/simulation_contract.md)
- [Reproducibility](docs/reproducibility.md)
- [References](docs/references.md)

# NOTE: AI-assisted development tools were used for code organization, implementation support, and documentation in this project. All scientific assumptions, simulations, results, and interpretations were reviewed and validated by the author.
