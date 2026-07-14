"""Particle species metadata used by the clean research package.

Masses are expressed in GeV/c^2 and charge is expressed in units of the
elementary charge. These constants are safe to reuse in future simulation
modules because they are simple physical metadata, not legacy reconstruction
logic.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ParticleSpecies:
    """A particle species with charge and rest-mass metadata."""

    name: str
    charge_number: int
    mass_GeV_c2: float
    pdg_id: int

    @property
    def abs_charge_number(self) -> int:
        """Absolute charge number, useful for rigidity-momentum conversion."""

        return abs(self.charge_number)


ELECTRON = ParticleSpecies(
    name="electron",
    charge_number=-1,
    mass_GeV_c2=0.00051099895000,
    pdg_id=11,
)

POSITRON = ParticleSpecies(
    name="positron",
    charge_number=1,
    mass_GeV_c2=0.00051099895000,
    pdg_id=-11,
)

PROTON = ParticleSpecies(
    name="proton",
    charge_number=1,
    mass_GeV_c2=0.93827208816,
    pdg_id=2212,
)
