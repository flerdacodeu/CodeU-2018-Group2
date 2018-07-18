import unittest
import string


def visit_island(grid, k, l, M, N):
	""" Marks the visited island pieces to not to visit in the future again."""
	if 0 <= k < M and 0 <= l < N:
		if (k, l) in grid:
			grid.remove((k, l))
			visit_island(grid, k + 1, l, M, N)
			visit_island(grid, k - 1, l, M, N)
			visit_island(grid, k, l - 1, M, N)
			visit_island(grid, k, l + 1, M, N)
	return


def count_islands(grid):
	""" Counts the number of islands """
	# visited = grid.copy()  # copy the grid in order not to lose the real information.
	unvisited = set()
	M = len(grid)
	N = len(grid[0])
	print(grid[0][0])
	for k in range(M):
		for l in range(N):
			if grid[k][l] == 'T':
				print("found!")
				set.add((k, l))

	c = 0
	for k in range(M):
		for l in range(N):
			if (k, l) in unvisited:
				c += 1  # found a new island
				visit_island(unvisited, k, l, M, N)  # visit the connected pieces
				print("islands:")
	return c

def main():
	map1 = ["FTFT",
					 "TTFF",
					 'FFTF',
					 'FFTF']

	print( count_islands(map1))


if __name__ == '__main__':
	main()


class CountIslands(unittest.TestCase):

	def _setUp(self):
		self.map1 = ["FTFT",
					 "TTFF",
					 'FFTF',
					 'FFTF']
		self.map2 = ['F']
		self.map3 = ['T']
		self.map4 = ['TT']
		self.map5 = ['TF']
		self.map6 = ['TF',
					 'FT']
		self.map7 = ['TFTFT',
					 'FTFTF',
					 'TFTFT']

	def test_count(self):
		self._setUp()
		self.assertEqual(3, count_islands(self.map1))
		self.assertEqual(0, count_islands(self.map2))
		self.assertEqual(1, count_islands(self.map3))
		self.assertEqual(1, count_islands(self.map4))
		self.assertEqual(1, count_islands(self.map5))
		self.assertEqual(2, count_islands(self.map6))
		self.assertEqual(8, count_islands(self.map7))
