import unittest
from main import determine_maze_exit, determine_maze_exit_alternate


class TestDetermineMazeExit(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(determine_maze_exit([0, 3, 0, 1, -3]), 5)

    def test_sample_with_alternate(self):
        self.assertEqual(determine_maze_exit_alternate([0, 3, 0, 1, -3]), 10)


if __name__ == '__main__':
    unittest.main()

