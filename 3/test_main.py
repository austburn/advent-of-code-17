import unittest
from main import determine_layer, determine_coordinates


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

    def test_layer_two(self):
        self.assertEqual(determine_coordinates(10), (2, 0))

if __name__ == '__main__':
    unittest.main()

