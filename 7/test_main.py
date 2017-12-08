import unittest
from main import parse_program


class TestParseProgram(unittest.TestCase):
    def test_weight(self):
        self.assertEqual(parse_program('abcde (42)'), {'name': 'abcde', 'weight': '42', 'programs': None})

    def test_additional_programs(self):
        self.assertEqual(parse_program('abcde (42) -> bcdef, ghijkl, mnopq'), {'name': 'abcde', 'weight': '42', 'programs': ['bcdef', 'ghijkl', 'mnopq']})



if __name__ == '__main__':
    unittest.main()

