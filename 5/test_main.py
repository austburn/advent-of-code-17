import unittest
from main import determine_maze_exit


class TestDetermineMazeExit(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(determine_maze_exit([0, 3, 0, 1, -3]), 5)


if __name__ == '__main__':
    unittest.main()

