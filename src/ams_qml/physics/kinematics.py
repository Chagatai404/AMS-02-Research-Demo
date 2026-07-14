"""Relativistic kinematics in natural high-energy physics units.

The functions in this module use GeV, GeV/c, GeV/c^2, and GV conventions:
for a particle with charge number Z, momentum p[GeV/c] = |Z| R[GV].
Signed charge information belongs in tracker reconstruction, not in these
unsigned energy and speed helpers.
"""

from __future__ import annotations

from typing import TypeAlias

import numpy as np
from numpy.typing import ArrayLike, NDArray

NumberOrArray: TypeAlias = float | NDArray[np.float64]


def _as_float_array(value: ArrayLike) -> NDArray[np.float64]:
    return np.asarray(value, dtype=np.float64)


def momentum_from_rigidity(rigidity_GV: ArrayLike, charge_number: int) -> NumberOrArray:
    """Return total momentum in GeV/c from rigidity in GV.

    Parameters
    ----------
    rigidity_GV:
        Rigidity magnitude or signed rigidity in GV.
    charge_number:
        Particle charge number Z. Neutral particles do not have magnetic
        rigidity and are rejected.
    """

    abs_z = abs(charge_number)
    if abs_z == 0:
        raise ValueError("Magnetic rigidity is undefined for neutral particles.")
    result = abs_z * np.abs(_as_float_array(rigidity_GV))
    return float(result) if result.ndim == 0 else result


def total_energy(momentum_GeV_c: ArrayLike, mass_GeV_c2: float) -> NumberOrArray:
    """Return total energy in GeV from p and mass using E^2 = p^2 + m^2."""

    if mass_GeV_c2 <= 0:
        raise ValueError("Mass must be positive.")
    momentum = _as_float_array(momentum_GeV_c)
    result = np.sqrt(momentum**2 + mass_GeV_c2**2)
    return float(result) if result.ndim == 0 else result


def gamma_from_momentum(momentum_GeV_c: ArrayLike, mass_GeV_c2: float) -> NumberOrArray:
    """Return Lorentz gamma for a particle with momentum p and rest mass m."""

    result = _as_float_array(total_energy(momentum_GeV_c, mass_GeV_c2)) / mass_GeV_c2
    return float(result) if result.ndim == 0 else result


def beta_from_momentum(momentum_GeV_c: ArrayLike, mass_GeV_c2: float) -> NumberOrArray:
    """Return beta = v/c for a particle with momentum p and rest mass m."""

    momentum = np.abs(_as_float_array(momentum_GeV_c))
    energy = _as_float_array(total_energy(momentum, mass_GeV_c2))
    result = momentum / energy
    return float(result) if result.ndim == 0 else result


def beta_from_rigidity(
    rigidity_GV: ArrayLike,
    charge_number: int,
    mass_GeV_c2: float,
) -> NumberOrArray:
    """Return beta = v/c from rigidity, charge number, and rest mass."""

    momentum = momentum_from_rigidity(rigidity_GV, charge_number)
    return beta_from_momentum(momentum, mass_GeV_c2)
