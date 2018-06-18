from typing import List

class TrieNode:
    def __init__(self):
        """ Constructor to initlalize a trie node """
        self.children = {}
        self.is_word = False

class Dictionary:
    def __init__(self, words: List[str] = []):
        """ Constructor to initlalize a dictionary """
        self.root = TrieNode()
        for word in words:
            self.add_word(word)

    def add_word(self, word: str):
        """ Method to add a word to dictionary if not already present """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word = True

    def is_prefix(self, prefix: str) -> bool:
        """ Method to return true if prefix found in dictionary """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def is_word(self, word: str) -> bool:
        """ Method to return true if word found in dictionary """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word


class Grid:
    def __init__(self, grid: List):
        """ Constructor to initlalize a grid """
        self.grid = grid

    def _get_neighbours(self, x: int, y: int) -> List:
        """ Method to find all possible neighbouring cells given position (x, y) in a grid """
        # 8 possible positions - vertical, horizontal and diagonal
        positions = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1)]
        return [pos for pos in positions if 0 <= pos[0] < len(self.grid) and 0 <= pos[1] < len(self.grid[0])]

    def _get_word(self, positions: List) -> str:
        """ Method to find corresponding word given a list of positions in grid """
        return ''.join(self.grid[pos[0]][pos[1]] for pos in positions)

    def _find_words(self, dictionary: Dictionary, position: List) -> List[str]:
        """ Method to return all words from given position """
        words = []

        word = self._get_word(position)
        if (not dictionary.is_prefix(word)):
            return []
        if (dictionary.is_word(word)):
            words.append(word)

        neighbours = self._get_neighbours(position[-1][0], position[-1][1])
        for pos in neighbours:
            if pos not in position:
                position.append(pos)
                words.extend(self._find_words(dictionary, position))
                position.remove(pos)

        return words

    def find_all_words(self, dictionary: Dictionary) -> List[str]:
        """ Method to return List of all words found in grid """
        words = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                for word in self._find_words(dictionary, [(i, j)]):
                    if word not in words:
                        words.append(word)
        return words


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary(['CAR', 'CARD', 'CART', 'CAT'])
        self.grid = Grid([['A', 'A', 'R'], ['T', 'C', 'D']])

    def test_is_prefix(self):
        self.assertEqual(self.dictionary.is_prefix('C'), True)
        self.assertEqual(self.dictionary.is_prefix('CA'), True)
        self.assertEqual(self.dictionary.is_prefix('CART'), True)
        self.assertEqual(self.dictionary.is_prefix('A'), False)
        self.assertEqual(self.dictionary.is_prefix('TAC'), False)
        self.assertEqual(self.dictionary.is_prefix('CARS'), False)

    def test_is_word(self):
        self.assertEqual(self.dictionary.is_word('CAR'), True)
        self.assertEqual(self.dictionary.is_word('CART'), True)
        self.assertEqual(self.dictionary.is_word('CAT'), True)
        self.assertEqual(self.dictionary.is_word('CARS'), False)
        self.assertEqual(self.dictionary.is_word('ACT'), False)
        self.assertEqual(self.dictionary.is_word('CARDS'), False)

    def test__get_neighbours(self):
        self.assertCountEqual(self.grid._get_neighbours(0, 0), [(0, 1), (1, 1), (1, 0)])
        self.assertCountEqual(self.grid._get_neighbours(1, 1), [(0, 0), (0, 1), (0, 2), (1, 2), (1, 0)])

    def test_get_word(self):
        self.assertEqual(self.grid._get_word([(1, 1), (0, 1), (0, 2)]), 'CAR')
        self.assertEqual(self.grid._get_word([(1, 1), (0, 1), (0, 2), (1, 2)]), 'CARD')
        self.assertEqual(self.grid._get_word([(1, 1), (0, 1), (1, 0)]), 'CAT')

    def test_find_words(self):
        self.assertEqual(self.grid._find_words(self.dictionary, [(1, 1)]), ['CAT', 'CAR', 'CARD', 'CAT'])
        self.assertEqual(self.grid._find_words(self.dictionary, [(0, 0)]), [])

    def test_find_all_words(self):
        self.assertEqual(self.grid.find_all_words(self.dictionary), ['CAT', 'CAR', 'CARD'])
