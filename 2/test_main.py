import unittest
from main import checksum


class TestChecksum(unittest.TestCase):
    def test_easy(self):
        self.assertEqual(checksum('1234'), 3)


if __name__ == '__main__':
    unittest.main()
