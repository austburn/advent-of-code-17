import unittest
from main import realloc_memory


class TestReallocMemory(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(realloc_memory([0, 2, 7, 0]), [2, 4, 1, 2])


if __name__ == '__main__':
    unittest.main()

