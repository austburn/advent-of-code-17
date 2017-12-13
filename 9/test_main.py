import unittest
from main import traverse_groups


class TestMain(unittest.TestCase):
    def test_traverse_groups(self):
        self.assertEqual(traverse_groups('{}'), (1, 0))
        self.assertEqual(traverse_groups('{{{}}}'), (6, 0))
        self.assertEqual(traverse_groups('{{},{}}'), (5, 0))
        self.assertEqual(traverse_groups('{{<ab>},{<ab>},{<ab>},{<ab>}}'), (9, 8))
        self.assertEqual(traverse_groups('{{<!!>},{<!!>},{<!!>},{<!!>}}'), (9, 0))
        self.assertEqual(traverse_groups('{{{},{},{{}}}}'), (16, 0))
        self.assertEqual(traverse_groups('{{<a!>},{<a!>},{<a!>},{<ab>}}'), (3, 17))

if __name__ == '__main__':
    unittest.main()

