import unittest
from islands import *

class TestIslandFill(unittest.TestCase):

    def test_0(self):
        self.assertEqual(island_fill(0, 0, [[0]]), [[0]])
        self.assertEqual(island_fill(0, 0, [[1]]), [[2]])

    def test_1(self):
        self.assertEqual(island_fill(0, 0, [[1, 1], [1, 0]]), [[2, 2], [2, 0]])
        self.assertEqual(island_fill(1, 1, [[1, 1], [1, 0]]), [[1, 1], [1, 0]])

class TestIslandsNum(unittest.TestCase):

    def test_0(self):
        self.assertEqual(get_number_of_islands([[0]]), 0)
        self.assertEqual(get_number_of_islands([[1]]), 1)

    def test_1(self):
        self.assertEqual(get_number_of_islands([[1,0,1,0]]), 2)

    def test_2(self):
        self.assertEqual(get_number_of_islands([[1,0,1,0],[0,1,1,1],[0,0,1,0]]), 2)
        self.assertEqual(get_number_of_islands( \
                [[1,0,1,0],[0,1,1,1],[0,0,1,0],[1,1,0,0],[0,1,0,1]]), 4)
        self.assertEqual(get_number_of_islands( \
                [[0,1,0,1,0],[0,0,1,1,1],[1,0,0,1,0],[0,1,1,0,0],[1,0,1,0,1]]), 6)
        self.assertEqual(get_number_of_islands( \
                [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]), 1)

if __name__ == '__main__':
    unittest.main()
