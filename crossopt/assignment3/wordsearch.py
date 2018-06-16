#!/usr/bin/env python3

from assignment3.dictionary import Dictionary


# stores grid as 2d array
class Grid:
    def __init__(self, array):
        self.grid = array
        self.n = len(array)
        self.m = 0 if not len(array) else len(array[0])

    def __getitem__(self, i):
        return self.grid[i]

    def neighbors(self, i, j):
        ans = []
        for newi in range(i - 1, i + 2):
            for newj in range(j - 1, j + 2):
                if newi == i and newj == j:
                    continue
                if 0 <= newi < self.n and 0 <= newj < self.m:
                    ans.append((newi, newj))
        return ans


# finds set of words from dictionary beginning in grid[i][j], via dfs
def findMatch(grid, dictionary, i, j, used=set(), prefix=""):
    ans = set()
    used.add((i, j))
    prefix += grid[i][j]
    if dictionary.isWord(prefix):
        ans.add(prefix)
    for i1, j1 in grid.neighbors(i, j):
        if (i1, j1) not in used and dictionary.isPrefix(prefix + grid[i1][j1]):
            ans |= findMatch(grid, dictionary, i1, j1, used, prefix)
    used.remove((i, j))
    prefix = prefix[:-1]
    return ans


# finds set of words from dictionary in grid
def findMatches(grid, dictionary):
    ans = set()
    for i in range(grid.n):
        for j in range(grid.m):
            ans |= findMatch(grid, dictionary, i, j)
    return ans
