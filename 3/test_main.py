import unittest
from main import determine_layer


class TestDetermineLayer(unittest.TestCase):
    def test_layer_one(self):
        self.assertEqual(determine_layer(1), 1)

    def test_layer_two(self):
        self.assertEqual(determine_layer(2), 2)
        self.assertEqual(determine_layer(5), 2)
        self.assertEqual(determine_layer(9), 2)

    def test_layer_three(self):
        self.assertEqual(determine_layer(10), 3)
        self.assertEqual(determine_layer(17), 3)
        self.assertEqual(determine_layer(25), 3)


if __name__ == '__main__':
    unittest.main()

