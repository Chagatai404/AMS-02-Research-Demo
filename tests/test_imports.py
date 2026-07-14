import unittest


class ImportTests(unittest.TestCase):
    def test_package_imports_without_side_effects(self):
        import ams_qml
        import ams_qml.ecal
        import ams_qml.physics

        self.assertTrue(ams_qml.__version__)
