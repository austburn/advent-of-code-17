import unittest
from main import is_group, is_trash, traverse_groups


class TestMain(unittest.TestCase):
    def test_is_group(self):
        self.assertTrue(is_group('{}'))

    def test_is_trash(self):
        self.assertTrue(is_trash('<>'))

    def test_traverse_groups(self):
        # self.assertEqual(traverse_groups('{}'), 1)
        # self.assertEqual(traverse_groups('{{{}}}'), 6)
        # self.assertEqual(traverse_groups('{{},{}}'), 5)
        # self.assertEqual(traverse_groups('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)
        # self.assertEqual(traverse_groups('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)
        self.assertEqual(traverse_groups('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)


if __name__ == '__main__':
    unittest.main()

