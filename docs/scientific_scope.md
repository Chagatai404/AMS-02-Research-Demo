# Scientific Scope

## Binary Task

The active classification task is:

- Signal: electrons and positrons grouped as `e+/-`.
- Background: protons.

This grouping is intentional. Electromagnetic calorimeter observables can
separate electromagnetic showers from many hadronic responses, but ECAL shower
shape and energy deposition do not determine the sign of the lepton charge.
Electron versus positron charge-sign separation requires tracker curvature.

## Fast Monte Carlo Versus Full Transport

The planned simulator is a fast, physics-informed parameterized Monte Carlo. It
should encode detector geometry, shower-shape assumptions, stochastic
fluctuations, digitization, and reconstruction in a reproducible way.

It is not a full particle-transport Monte Carlo. A full Geant4 model tracks
particles and secondaries through materials using detailed interaction models,
geometry, and production thresholds. The fast simulator can be useful for
controlled ML and QML experiments, but any physics claim must state its
parameterized nature and validation status.

## Intended QML Comparison

QML experiments should use a reduced feature vector, roughly 6-12 inputs, built
from documented shower observables or dimensionality reduction. Classical and
quantum models must receive the same inputs. The comparison target is not
"quantum advantage" by default; it is whether QML provides competitive
performance or useful generalization behavior under matched, reproducible
conditions.

## Claims Not Supported Yet

- The repository is not an official AMS-02 Monte Carlo.
- The repository is not an exact detector replica.
- Legacy Week 1 and Week 2 datasets are not validated training data.
- Proton fast-MC behavior is not validated until compared with Geant4 or
  suitable reference data.
