import unittest
from main import line_checksum_min_max, line_checksum_division, file_checksum


class TestLineChecksumMinMax(unittest.TestCase):
    def test_easy(self):
        self.assertEqual(line_checksum_min_max('1234'), 3)

    def test_samples(self):
        self.assertEqual(line_checksum_min_max('5195'), 8)

    def test_decr_string(self):
        self.assertEqual(line_checksum_min_max('753'), 4)

    def test_incr_string(self):
        self.assertEqual(line_checksum_min_max('2468'), 6)


class TestLineChecksumDivision(unittest.TestCase):
    def test_samples(self):
        self.assertEqual(line_checksum_division('5928'), 4)
        self.assertEqual(line_checksum_division('9473'), 3)
        self.assertEqual(line_checksum_division('3865'), 2)


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
