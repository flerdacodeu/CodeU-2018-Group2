#!/usr/bin/env python3

import unittest
from assignment4.countislands import Grid


class TestGrid(unittest.TestCase):
    def test_countislands(self):
        grid = Grid(4, 4, [[0, 1, 0, 1], [1, 1, 0, 0],
                           [0, 0, 1, 0], [0, 0, 1, 0]])
        self.assertEqual(3, grid.countIslands())
        grid = Grid(3, 4, [[1, 0, 1, 0],
                    [0, 1, 0, 1], [1, 0, 1, 0]])
        self.assertEqual(6, grid.countIslands())
        grid = Grid(3, 2, [[0, 0], [0, 0], [0, 0]])
        self.assertEqual(0, grid.countIslands())


if __name__ == "__main__":
    unittest.main()
