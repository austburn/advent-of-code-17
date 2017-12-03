import unittest
from main import determine_layer


class TestDetermineLayer(unittest.TestCase):
    def test_layer_one(self):
        self.assertEqual(determine_layer(1), (1, [1]))

    def test_layer_two(self):
        expected = (2, range(2, 10))
        self.assertEqual(determine_layer(2), expected)
        self.assertEqual(determine_layer(5), expected)
        self.assertEqual(determine_layer(9), expected)

    def test_layer_three(self):
        expected = (3, range(10, 26))
        self.assertEqual(determine_layer(10), expected)
        self.assertEqual(determine_layer(17), expected)
        self.assertEqual(determine_layer(25), expected)


if __name__ == '__main__':
    unittest.main()

