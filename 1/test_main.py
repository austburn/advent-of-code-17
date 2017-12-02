import unittest
from main import captcha


class TestLineCaptcha(unittest.TestCase):
    def test_samples(self):
        self.assertEqual(captcha('1122', 1), 3)
        self.assertEqual(captcha('1111', 1), 4)
        self.assertEqual(captcha('1234', 1), 0)
        self.assertEqual(captcha('91212129', 1), 9)


if __name__ == '__main__':
    unittest.main()
