import unittest
from main import captcha


class TestLineCaptcha(unittest.TestCase):
    def test_samples(self):
        self.assertEqual(line_checksum('1122'), 3)
        self.assertEqual(line_checksum('1111'), 4)
        self.assertEqual(line_checksum('1234'), 0)
        self.assertEqual(line_checksum('91212129'), 9)


if __name__ == '__main__':
    unittest.main()
