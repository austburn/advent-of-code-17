import unittest
from main import captcha, HALF


class TestLineCaptcha(unittest.TestCase):
    def test_samples(self):
        self.assertEqual(captcha('1122'), 3)
        self.assertEqual(captcha('1111'), 4)
        self.assertEqual(captcha('1234'), 0)
        self.assertEqual(captcha('91212129'), 9)

    def test_jump(self):
        self.assertEqual(captcha('1212', jump_behavior=HALF), 6)
        self.assertEqual(captcha('1221', jump_behavior=HALF), 0)
        self.assertEqual(captcha('123425', jump_behavior=HALF), 4)
        self.assertEqual(captcha('123123', jump_behavior=HALF), 12)
        self.assertEqual(captcha('12131415', jump_behavior=HALF), 4)


if __name__ == '__main__':
    unittest.main()
