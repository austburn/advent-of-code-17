import unittest
from main import parse_program, _determine_chain_length, determine_tree_root


class TestParseProgram(unittest.TestCase):
    def test_weight(self):
        self.assertEqual(parse_program('abcde (42)'), {'name': 'abcde', 'weight': '42', 'programs': []})

    def test_additional_programs(self):
        self.assertEqual(parse_program('abcde (42) -> bcdef, ghijkl, mnopq'), {'name': 'abcde', 'weight': '42', 'programs': ['bcdef', 'ghijkl', 'mnopq']})

    def test_recursive_determine_chain_length(self):
        programs = {
            'pbga': {
                'name': 'pbga',
                'weight': '66',
                'programs': []
            },
            'xhth': {
                'name': 'xhth',
                'weight': '57',
                'programs': []
            },
            'ebii': {
                'name': 'ebii',
                'weight': '61',
                'programs': []
            },
            'havc': {
                'name': 'havc',
                'weight': '66',
                'programs': []
            },
            'ktlj': {
                'name': 'ktlj',
                'weight': '57',
                'programs': []
            },
            'fwft': {
                'name': 'fwft',
                'weight': '72',
                'programs': ['ktlj', 'cntj', 'xhth']
            },
            'qoyq': {
                'name': 'qoyq',
                'weight': '66',
                'programs': []
            },
            'padx': {
                'name': 'padx',
                'weight': '45',
                'programs': ['pbga', 'havc', 'qoyq']
            },
            'tknk': {
                'name': 'tknk',
                'weight': '41',
                'programs': ['ugml', 'padx', 'fwft']
            },
            'jptl': {
                'name': 'jptl',
                'weight': '61',
                'programs': []
            },
            'ugml': {
                'name': 'ugml',
                'weight': '68',
                'programs': ['gyxo', 'ebii', 'jptl']
            },
            'gyxo': {
                'name': 'gyxo',
                'weight': '61',
                'programs': []
            },
            'cntj': {
                'name': 'cntj',
                'weight': '57',
                'programs': []
            }
        }
        self.assertEqual(_determine_chain_length('jptl', programs), 0)
        self.assertEqual(_determine_chain_length('ugml', programs), 1)
        self.assertEqual(_determine_chain_length('tknk', programs), 2)

        self.assertEqual(determine_tree_root(programs), ('tknk', 2))


if __name__ == '__main__':
    unittest.main()

