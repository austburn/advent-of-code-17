import unittest
from main import determine_layer, determine_coordinates, taxicab_distance


class TestDetermineLayer(unittest.TestCase):
    def test_layer_zero(self):
        self.assertEqual(determine_layer(1), (0, [1]))

    def test_layer_one(self):
        expected = (1, list(range(2, 10)))
        self.assertEqual(determine_layer(2), expected)
        self.assertEqual(determine_layer(5), expected)
        self.assertEqual(determine_layer(9), expected)

    def test_layer_two(self):
        expected = (2, list(range(10, 26)))
        self.assertEqual(determine_layer(10), expected)
        self.assertEqual(determine_layer(17), expected)
        self.assertEqual(determine_layer(25), expected)


class TestDetermineCoordinates(unittest.TestCase):
    def test_origin(self):
        self.assertEqual(determine_coordinates(1), (0, 0))

    def test_layer_one(self):
        self.assertEqual(determine_coordinates(2), (1, 0))
        self.assertEqual(determine_coordinates(3), (1, 1))
        self.assertEqual(determine_coordinates(4), (0, 1))
        self.assertEqual(determine_coordinates(5), (-1, 1))
        self.assertEqual(determine_coordinates(6), (-1, 0))
        self.assertEqual(determine_coordinates(7), (-1, -1))
        self.assertEqual(determine_coordinates(8), (0, -1))
        self.assertEqual(determine_coordinates(9), (1, -1))

    def test_layer_two(self):
        self.assertEqual(determine_coordinates(10), (2, -1))
        self.assertEqual(determine_coordinates(11), (2, 0))
        self.assertEqual(determine_coordinates(12), (2, 1))
        self.assertEqual(determine_coordinates(13), (2, 2))
        self.assertEqual(determine_coordinates(14), (1, 2))
        self.assertEqual(determine_coordinates(15), (0, 2))
        self.assertEqual(determine_coordinates(16), (-1, 2))
        self.assertEqual(determine_coordinates(17), (-2, 2))
        self.assertEqual(determine_coordinates(18), (-2, 1))
        self.assertEqual(determine_coordinates(19), (-2, 0))
        self.assertEqual(determine_coordinates(20), (-2, -1))
        self.assertEqual(determine_coordinates(21), (-2, -2))
        self.assertEqual(determine_coordinates(22), (-1, -2))
        self.assertEqual(determine_coordinates(23), (0, -2))
        self.assertEqual(determine_coordinates(24), (1, -2))
        self.assertEqual(determine_coordinates(25), (2, -2))


class TestTaxicabDistance(unittest.TestCase):
    def test_origin(self):
        self.assertEqual(taxicab_distance(1), 0)

    def test_level_one_sample(self):
        self.assertEqual(taxicab_distance(12), 3)

    def test_level_two_sample(self):
        self.assertEqual(taxicab_distance(23), 2)

    def test_large_sample(self):
        self.assertEqual(taxicab_distance(1024), 31)


if __name__ == '__main__':
    unittest.main()

