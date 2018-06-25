#!/usr/bin/env python3

import unittest
from assignment3.dictionary import Dictionary
from assignment3.wordsearch import Grid
from assignment3.wordsearch import findMatch, findMatches


class TestDictionary(unittest.TestCase):
    def test_isprefix(self):
        dictionary = Dictionary(['CAR', 'CART', 'CARD', 'CAT'])
        self.assertEqual(dictionary.isPrefix('A'), False)
        self.assertEqual(dictionary.isPrefix('car'), False)
        self.assertEqual(dictionary.isPrefix('CARDS'), False)
        self.assertEqual(dictionary.isPrefix(''), True)
        self.assertEqual(dictionary.isPrefix('CARD'), True)
        self.assertEqual(dictionary.isPrefix('CAR'), True)

    def test_isword(self):
        dictionary = Dictionary(['CAR', 'CART', 'CARD', 'CAT'])
        self.assertEqual(dictionary.isWord('A'), False)
        self.assertEqual(dictionary.isWord('C'), False)
        self.assertEqual(dictionary.isWord('car'), False)
        self.assertEqual(dictionary.isWord('CARDS'), False)
        self.assertEqual(dictionary.isWord(''), False)
        self.assertEqual(dictionary.isWord('CARD'), True)
        self.assertEqual(dictionary.isWord('CAR'), True)


class TestGrid(unittest.TestCase):
    def test_getitem(self):
        array = ['AAR', 'TCD']
        grid = Grid(array)
        self.assertEqual(grid.n, 2)
        self.assertEqual(grid.m, 3)
        for i in range(grid.n):
            for j in range(grid.m):
                self.assertEqual(grid[i][j], array[i][j])

    def test_neighbors(self):
        grid = Grid(['AAR', 'TCD'])
        self.assertListEqual(grid.neighbors(0, 0), [(0, 1), (1, 0), (1, 1)])
        self.assertListEqual(grid.neighbors(1, 1),
                             [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)])
        self.assertListEqual(grid.neighbors(1, 2), [(0, 1), (0, 2), (1, 1)])


class TestFindMatches(unittest.TestCase):
    def test_findmatch(self):
        grid = Grid(['AAR', 'TCD'])
        dictionary = Dictionary(['CAR', 'CART', 'CARD', 'CAT'])
        self.assertSetEqual(findMatch(grid, dictionary, 0, 0), set())
        self.assertSetEqual(findMatch(grid, dictionary, 1, 1),
                            {'CAR', 'CAT', 'CARD'})
        dictionary = Dictionary(['CAR', 'CART', 'CARD',
                                'CAT', 'RAT', 'RCDAAT', 'RCDAATA'])
        self.assertSetEqual(findMatch(grid, dictionary, 0, 2),
                            {'RAT', 'RCDAAT'})

    def test_findmatches(self):
        grid = Grid(['AAR', 'TCD'])
        dictionary = Dictionary(['CAR', 'CART', 'CARD', 'CAT'])
        self.assertSetEqual(findMatches(grid, dictionary),
                            {'CAR', 'CAT', 'CARD'})
        dictionary = Dictionary(['CAR', 'CART', 'CARD',
                                'CAT', 'RAT', 'RCDAATA'])
        self.assertSetEqual(findMatches(grid, dictionary),
                            {'RAT', 'CAR', 'CAT', 'CARD'})

        self.assertSetEqual(findMatches(Grid(['A']),
                            Dictionary(['A', 'B'])), {'A'})
        self.assertSetEqual(findMatches(Grid(['A']),
                            Dictionary(['AA', 'B'])), set())


if __name__ == "__main__":
    unittest.main()
