import unittest
from volume_cuboid import Cuboid


class TestCuboid(unittest.TestCase):
    def test_volume(self):
        cuboid = Cuboid(2)
        self.assertAlmostEqual(cuboid.cuboid_volume(), 8)
        cuboid = Cuboid(0)
        self.assertAlmostEqual(cuboid.cuboid_volume(), 0)
        cuboid = Cuboid(1)
        self.assertAlmostEqual(cuboid.cuboid_volume(), 1)

    def test_input_value(self):
        cuboid = Cuboid("a")
        with self.assertRaises(TypeError, msg=" 'l' is not int or float"):
            cuboid.cuboid_volume()
