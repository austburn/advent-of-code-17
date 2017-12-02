import unittest
from main import line_checksum, file_checksum


class TestLineChecksum(unittest.TestCase):
    def test_easy(self):
        self.assertEqual(line_checksum('1234'), 3)

    def test_samples(self):
        self.assertEqual(line_checksum('5195'), 8)

    def test_decr_string(self):
        self.assertEqual(line_checksum('753'), 4)

    def test_incr_string(self):
        self.assertEqual(line_checksum('2468'), 6)


class TestFileChecksum(unittest.TestCase):
    def test_easy(self):
        input = [
            '1 2 3 4\n',        # 3
            '20 50 60 10\n',    # 50
            '11 19 67 567\n',   # 556
            '5 8 7 2\n'         # 6
        ]
        self.assertEqual(file_checksum(input), 615)


if __name__ == '__main__':
    unittest.main()
