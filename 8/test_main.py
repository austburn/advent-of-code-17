import unittest
from main import parse_instruction, run_instruction_set


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

    def test_parse_instruction_with_negative_num(self):
        self.assertEqual(parse_instruction('b inc -5 if a > 1'), {
            'register': 'b',
            'operation': 'inc',
            'value': -5,
            'condition': {
                'register': 'a',
                'operation': '>',
                'value': 1
            }
        })

    def test_parse_instruction_with_complex_comparison(self):
        self.assertEqual(parse_instruction('b inc -5 if a >= 1'), {
            'register': 'b',
            'operation': 'inc',
            'value': -5,
            'condition': {
                'register': 'a',
                'operation': '>=',
                'value': 1
            }
        })

    def test_run_instruction_set(self):
        instructions = [
            'b inc 5 if a > 1',
            'a inc 1 if b < 5',
            'c dec -10 if a >= 1',
            'c inc -20 if c == 10'
        ]
        self.assertEqual(run_instruction_set(instructions), ('a', 1))


if __name__ == '__main__':
    unittest.main()

