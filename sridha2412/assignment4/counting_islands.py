from typing import List, Tuple
import unittest

class Grid:
    def __init__(self, grid: List):
        """ Constructor to initialize a grid """
        self.grid = grid
        self.row = len(self.grid)
        self.col = len(self.grid[0])

    def _get_neighbours(self, x: int, y: int) -> List[Tuple[int, int]]:
        """ Method to find all horizontal and vertical neighbouring cells given position (x, y) """
        # 4 possible positions - horizontal and vertical
        positions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [pos for pos in positions if 0 <= pos[0] < self.row and 0 <= pos[1] < self.col]

    def _find_land(self, i: int, j: int, visited: List[Tuple[int, int]]):
        """ Method to find all neighbouring land of an island """
        visited.append((i, j))
        neighbours = self._get_neighbours(i, j)
        for pos in neighbours:
            if pos not in visited and self.grid[pos[0]][pos[1]] == 1:
                self._find_land(pos[0], pos[1], visited)

    def count_island(self) -> int:
        """ Method to count all islands in a given grid and return it """
        visited = []
        count = 0

        for i in range(self.row):
            for j in range(self.col):
                if (i, j) not in visited and self.grid[i][j] == 1:
                    self._find_land(i, j, visited)
                    count += 1

        return count


class Test(unittest.TestCase):
    def setUp(self):
        self.grid = Grid([[0, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0]])

    def test__get_neighbours(self):
        self.assertCountEqual(self.grid._get_neighbours(0, 0), [(1, 0), (0, 1)])
        self.assertCountEqual(self.grid._get_neighbours(1, 1), [(0, 1), (2, 1), (1, 0), (1, 2)])

    def test_count_island(self):
        self.assertEqual(self.grid.count_island(), 3)
