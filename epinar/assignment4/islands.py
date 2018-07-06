import unittest


def visit_island(grid, k, l, M, N):
	""" Marks the visited island pieces to not to visit in the future again."""
	if 0 <= k < M and 0 <= l < N:
		if grid[k][l] is True:
			grid[k][l] = False
			visit_island(grid, k + 1, l, M, N)
			visit_island(grid, k - 1, l, M, N)
			visit_island(grid, k, l - 1, M, N)
			visit_island(grid, k, l + 1, M, N)
	return


def count_islands(grid):
	""" Counts the number of islands """
	visited = grid.copy()  # copy the grid in order not to lose the real information.
	M = len(grid)
	N = len(grid[0])
	c = 0
	for k in range(M):
		for l in range(N):
			if visited[k][l]:
				c += 1  # found a new island
				visit_island(visited, k, l, M, N)  # visit the connected pieces
	return c


class CountIslands(unittest.TestCase):

	def _setUp(self):
		self.map1 = [[False, True, False, True],
					 [True, True, False, False],
					 [False, False, True, False],
					 [False, False, True, False]]
		self.map2 = [[False]]
		self.map3 = [[True]]
		self.map4 = [[True, True]]
		self.map5 = [[True, False]]
		self.map6 = [[True, False],
					 [False, True]]
		self.map7 = [[True, False, True, False, True],
					 [False, True, False, True, False],
					 [True, False, True, False, True]]

	def test_count(self):
		self._setUp()
		self.assertEqual(3, count_islands(self.map1))
		self.assertEqual(0, count_islands(self.map2))
		self.assertEqual(1, count_islands(self.map3))
		self.assertEqual(1, count_islands(self.map4))
		self.assertEqual(1, count_islands(self.map5))
		self.assertEqual(2, count_islands(self.map6))
		self.assertEqual(8, count_islands(self.map7))
<<<<<<< HEAD
=======

>>>>>>> e64b7cc7c439cfff7ff7a676ad777ab65a178bc2
