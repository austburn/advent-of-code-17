import unittest
from main import parse_instruction


class TestMain(unittest.TestCase):
    def test_parse_instruction(self):
        self.assertEqual(parse_instruction('b inc 5 if a > 1'), {
            'register': 'b',
            'operation': 'inc',
            'value': 5,
            'condition': {
                'register': 'a',
                'operation': '>',
                'value': 1
            }
        })


if __name__ == '__main__':
    unittest.main()

