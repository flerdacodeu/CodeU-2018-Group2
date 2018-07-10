
import unittest
from itertools import product

class Dictionary:

	def __init__(self, words, prefixes):
		self.words = words
		self.prefixes = prefixes

	# Returns whether the given string is a valid word.
	def isWord(self, s):
		return s in self.words

	# Returns whether the given string is a prefix of at least one word in
	# the dictionary.
	def isPrefix(self, s):
		return s in self.prefixes


# Given a grid of letters and a dictionary, it finds all the words from the
# dictionary that can be formed in the grid.
def word_search(grid, dict):

	found_words = set()
	M = len(grid)
	N = len(grid[0])

	for k in range(M):
		for l in range(N):
			# visited_cache = [[False for _ in range(N)] for _ in range(M)]
			visited_cache = []
			for i in range(M):
				visited_cache.append([])
				for j in range(N):
					visited_cache[i].append(False)
			_search(grid, dict, "", k, l, visited_cache, found_words)

	return sorted(found_words)


def _search(grid, dict, s, i, j, isVisited, found_words):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
		return
	if isVisited[i][j]:
		return

	s = s + grid[i][j]

	if dict.isWord(s):
		# print(" word: ", str(s))
		found_words.add(str(s))

	if dict.isPrefix(s):
		# print("   prefix: ", s)
		isVisited[i][j] = True
		for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
			_search(grid, dict, s, i + dy, j + dx, isVisited, found_words)
		isVisited[i][j] = False

	return

def main():
	dict1 = Dictionary(['CAR', 'CARD', 'CART', 'CAT', 'CATAR'],
					   ['C', 'CA', 'CAR', 'CARD', 'CART', 'CAT', 'CATA', 'CATAR'])
	grid1 = [['A', 'A', 'R'], ['T', 'C', 'D']]

	k = word_search(grid1, dict1)

	print(k)


if __name__ == '__main__':
	main()


class SearchTest(unittest.TestCase):
	def setUp(self):
		self.dict1 = Dictionary(['CAR', 'CARD', 'CART', 'CAT'],
								['C', 'CA', 'CAR', 'CARD', 'CART', 'CAT'])
		self.dict2 = Dictionary(['CAR', 'CARD', 'CART', 'CAT', 'ART'],
								['C', 'CA', 'CAR', 'CARD', 'CART', 'CAT', 'A', 'AR', 'ART'])
		self.dict3 = Dictionary(['RAT', 'RAD', 'RAR'],
								['R', 'RA', 'RAT', 'RAD', 'RAR'])
		self.dict4 = Dictionary(['CAR', 'CARD', 'CART', 'CAT', 'CATAR'],
								['C', 'CA', 'CAR', 'CARD', 'CART', 'CAT', 'CATA', 'CATAR'])
		self.grid1 = [['A', 'A', 'R'], ['T', 'C', 'D']]

		self.dict5 = Dictionary(['CRASH', 'CRUSH'],
								['C', 'CR', 'CRU', 'CRUS', 'CRUSH', 'CRA', 'CRAS', 'CRASH'])

		self.grid2 = [['C', 'R', 'A', 'S', 'H'],
					  ['Z', 'Z', 'U', 'Z', 'Z']]

	def test_search(self):
		self.assertEqual(sorted(['CAR', 'CARD', 'CAT']), word_search(self.grid1, self.dict1))
		self.assertNotEqual(sorted(['CAR', 'CARD', 'CAT', 'ART']), word_search(self.grid1, self.dict2))
		self.assertEqual(sorted(['RAT', 'RAD']), word_search(self.grid1, self.dict3))
		self.assertEqual(sorted(['CAR', 'CARD', 'CAT', 'CATAR']), word_search(self.grid1, self.dict4))
		self.assertEqual(sorted(['CRASH', 'CRUSH']), word_search(self.grid2, self.dict5))
