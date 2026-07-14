import unittest

import numpy as np

from ams_qml.physics.kinematics import (
    beta_from_momentum,
    beta_from_rigidity,
    gamma_from_momentum,
    momentum_from_rigidity,
    total_energy,
)
from ams_qml.physics.particles import ELECTRON, POSITRON, PROTON


class KinematicsTests(unittest.TestCase):
    def test_momentum_from_rigidity_uses_absolute_charge_number(self):
        self.assertAlmostEqual(momentum_from_rigidity(10.0, PROTON.charge_number), 10.0)
        self.assertAlmostEqual(momentum_from_rigidity(-10.0, POSITRON.charge_number), 10.0)
        self.assertAlmostEqual(momentum_from_rigidity(4.0, 2), 8.0)

    def test_energy_gamma_beta_relationships_for_proton(self):
        momentum = 3.0
        energy = total_energy(momentum, PROTON.mass_GeV_c2)
        gamma = gamma_from_momentum(momentum, PROTON.mass_GeV_c2)
        beta = beta_from_momentum(momentum, PROTON.mass_GeV_c2)

        self.assertAlmostEqual(energy**2, momentum**2 + PROTON.mass_GeV_c2**2)
        self.assertAlmostEqual(gamma, energy / PROTON.mass_GeV_c2)
        self.assertAlmostEqual(beta, momentum / energy)
        self.assertGreaterEqual(beta, 0.0)
        self.assertLess(beta, 1.0)

    def test_beta_vector_is_physical_interval(self):
        rigidities = np.array([0.1, 1.0, 10.0, 100.0])
        beta = beta_from_rigidity(rigidities, PROTON.charge_number, PROTON.mass_GeV_c2)

        self.assertTrue(np.all(beta >= 0.0))
        self.assertTrue(np.all(beta < 1.0))
        self.assertTrue(np.all(np.diff(beta) > 0.0))

    def test_electron_and_proton_masses_are_distinct_and_used(self):
        electron_beta = beta_from_rigidity(1.0, ELECTRON.charge_number, ELECTRON.mass_GeV_c2)
        proton_beta = beta_from_rigidity(1.0, PROTON.charge_number, PROTON.mass_GeV_c2)

        self.assertAlmostEqual(ELECTRON.mass_GeV_c2, POSITRON.mass_GeV_c2)
        self.assertGreater(PROTON.mass_GeV_c2, ELECTRON.mass_GeV_c2)
        self.assertGreater(electron_beta, proton_beta)

    def test_neutral_particle_rigidity_rejected(self):
        with self.assertRaises(ValueError):
            momentum_from_rigidity(1.0, 0)
