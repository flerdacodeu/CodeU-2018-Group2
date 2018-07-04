#!/usr/bin/env python3


"""grid of tiles. stores islands via dsu"""
"""https://en.wikipedia.org/wiki/Disjoint-set_data_structure"""
class Grid(object):
    def __init__(self, n, m, grid):
        self.n = n
        self.m = m
        self.grid = grid
        self.parents = dict()
        self.sizes = dict()
        for i in range(n):
            for j in range(m):
                self.parents[i, j] = (i, j)
                self.sizes[i, j] = 1
                if i and self.grid[i][j] and self.grid[i - 1][j]:
                    self.join((i, j), ((i - 1, j)))
                if j and self.grid[i][j] and self.grid[i][j - 1]:
                    self.join((i, j), ((i, j - 1)))

    # returns unique id for each island
    def __getitem__(self, u):
        if self.parents[u] != u:
            self.parents[u] = self[self.parents[u]]
        return self.parents[u]
    
    def join(self, u, v):
        u = self[u]
        v = self[v]
        if self.sizes[u] < self.sizes[v]:
            u, v = v, u
        self.sizes[u] += self.sizes[v]
        self.parents[v] = u

    # returns amount of islands in grid
    def countIslands(self):
        colors = set()
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j]:
                    colors.add(self[(i, j)])
        return len(colors)
