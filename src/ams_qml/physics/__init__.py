"""Shared particle definitions and relativistic kinematics."""

from ams_qml.physics.kinematics import (
    beta_from_momentum,
    beta_from_rigidity,
    gamma_from_momentum,
    momentum_from_rigidity,
    total_energy,
)
from ams_qml.physics.particles import ELECTRON, POSITRON, PROTON, ParticleSpecies

__all__ = [
    "ELECTRON",
    "POSITRON",
    "PROTON",
    "ParticleSpecies",
    "beta_from_momentum",
    "beta_from_rigidity",
    "gamma_from_momentum",
    "momentum_from_rigidity",
    "total_energy",
]
