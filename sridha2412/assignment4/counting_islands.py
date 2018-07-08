from typing import List, Tuple
import unittest

def _find_land(grid: List, i: int, j: int):
    """ Method to find all neighbouring land of an island
    Args:
        grid: 2D array of tiles of either land or water
        i: i-th coord of current position (i, j)
        j: j-th coord of current position (i, j)
    """
    # mark current position as visited
    grid[i][j] = 0;
    # 4 possible positions - horizontal and vertical
    positions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

    for pos in positions:
        if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] == 1:
            _find_land(grid, pos[0], pos[1])


def count_island(grid: List) -> int:
    """ Method to count all islands in a given grid and return it
    Args:
        grid: 2D array of tiles of either land or water
    Returns:
        int: the count of islands in given grid
    """
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                _find_land(grid, i, j)
                count += 1
    return count


class Test(unittest.TestCase):
    def setUp(self):
        self.grid = [[0, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0]]
        self.grid2 = [[1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0]]
        self.grid3 = [[0, 0, 0], [0, 0, 0]]
        self.grid4 = [[1, 0, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]]

    def test_count_island(self):
        self.assertEqual(count_island(self.grid), 3)
        self.assertEqual(count_island(self.grid2), 1)
        self.assertEqual(count_island(self.grid3), 0)
        self.assertEqual(count_island(self.grid4), 5)
