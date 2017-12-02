import unittest
from main import checksum


class TestChecksum(unittest.TestCase):
    def test_easy(self):
        self.assertEqual(checksum('1234'), 3)

    def test_samples(self):
        self.assertEqual(checksum('5195'), 8)
        self.assertEqual(checksum('753'), 4)
        self.assertEqual(checksum('2468'), 6)


if __name__ == '__main__':
    unittest.main()
