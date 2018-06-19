import string
import unittest


class Dictionary:

	def __init__(self, words, prefixes):
		"""
		The dictionary class to keep the values.
		:param words: Valid entries in a dictionary.
		:type words: Array of strings.
		:param prefixes: Valid prefixes of each words in the dictionary.
		:type prefixes: Array of strings.
		"""
		self.words = words
		self.prefixes = prefixes

	def isWord(self, s):
		"""
		Returns whether the given string is a valid word.
		:param s: Word query.
		:type s: String
		:return: If the string is valid.
		:rtype: bool
		"""
		return s in self.words

	def isPrefix(self, s):
		"""
		Returns whether the given string is a prefix of at least one word in
		the dictionary.
		:param s: Prefix query.
		:type s: String
		:return: If the string is valid.
		:rtype: bool
		"""
		return s in self.prefixes


def word_search(grid, dict):
	"""
	Given a grid of letters and a dictionary, it finds all the words from the
	dictionary that can be formed in the grid.
	:param grid: The grid of characters to search in.
	:type grid: 2 dimensional array of characters, M x N .
	:param dict: The dictionary of words and prefixes.
	:type dict: Dictionary class object.
	:return: Set of all words found in the grid.
	:rtype: Array of strings
	"""

	found_words = []
	new_words = []
	M = len(grid)
	N = len(grid[0])

	for k in range(M):
		for l in range(N):
			visited_cache = [[False for _ in range(N)] for _ in range(M)]
			print("Start looking... ", k, l)
			new_words += _search(grid, dict, "", k, l, visited_cache, [])
			found_words += list(set(new_words))
			print("looked! ", k , l )

	return sorted(found_words)


def _search(grid, dict, s, i, j, isVisited, found_words):
	print("<search call")
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
		return found_words
	if isVisited[i][j]:
		isVisited[i][j] = False
		return found_words

	if dict.isWord(s):
		found_words.append(str(s))

	s = s + grid[i][j]

	if dict.isPrefix(s):
		isVisited[i][j] = True
		print("Prefix found! ", i, ' ', j, ' ', s)
		print("  :::", isVisited)
		vis = isVisited[:]
		for v in [-1, 0, 1]:
			for h in [-1, 0, 1]:
				print('for: ', s, " search start at: ", i + h, j + v, 'visited:', vis)
				found_words += _search(grid, dict, s, i + h, j + v, vis, found_words)
				print('for: ', s, " search end at: ", i + h, j + v, 'visited:', vis)

		print("End of search for prefix! ", i, ' ', j, ' ', s)
		print("  :::", isVisited)

	print(" --- return")
	return found_words

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

	def test_search(self):
		self.assertEqual(sorted(['CAR', 'CARD', 'CAT']), word_search(self.grid1, self.dict1))
		self.assertNotEqual(sorted(['CAR', 'CARD', 'CAT', 'ART']), word_search(self.grid1, self.dict2))
		self.assertEqual(sorted(['RAT', 'RAD']), word_search(self.grid1, self.dict3))
		self.assertEqual(sorted(['CAR', 'CARD', 'CAT', 'CATAR']), word_search(self.grid1, self.dict4))
