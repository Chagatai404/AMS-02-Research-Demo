import unittest
from pathlib import Path

from ams_qml.config import ecal_shape_from_config, load_config, rng_from_config
from ams_qml.ecal.geometry import ECalSegmentation


class ConfigTests(unittest.TestCase):
    def test_default_config_loads_and_resolves_paths(self):
        config = load_config()

        self.assertEqual(config["global"]["seed"], 20260214)
        self.assertEqual(ecal_shape_from_config(config), (18, 72))
        self.assertIsInstance(config["output_paths"]["generated_data"], Path)
        self.assertTrue(config["output_paths"]["generated_data"].is_absolute())

    def test_ecal_segmentation_from_config(self):
        segmentation = ECalSegmentation.from_config(load_config())

        self.assertEqual(segmentation.shape, (18, 72))
        self.assertEqual(segmentation.n_cells, 1296)

    def test_rng_from_config_is_deterministic(self):
        config = load_config()
        rng_a = rng_from_config(config)
        rng_b = rng_from_config(config)

        self.assertEqual(
            rng_a.integers(0, 1_000_000, size=5).tolist(),
            rng_b.integers(0, 1_000_000, size=5).tolist(),
        )
