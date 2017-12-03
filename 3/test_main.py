import unittest
from main import determine_layer


class TestDetermineLayer(unittest.TestCase):
    def test_layer_one(self):
        self.assertEqual(determine_layer(1), 1)

    def test_layer_two(self):
        self.assertEqual(determine_layer(5), 2)

if __name__ == '__main__':
    unittest.main()

