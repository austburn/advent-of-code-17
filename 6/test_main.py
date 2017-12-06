import unittest
from main import realloc_memory, track_states


class TestReallocMemory(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(realloc_memory([0, 2, 7, 0]), [2, 4, 1, 2])

    def test_sample_state_tracking(self):
        self.assertEqual(track_states([0, 2, 7, 0]), 5)


if __name__ == '__main__':
    unittest.main()

