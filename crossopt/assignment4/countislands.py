#!/usr/bin/env python3


# disjoint set union for grid components
class _GridDSU:
    def __init__(self, n, m):
        self.parent = dict()
        self.size = dict()
        for i in range(n):
            for j in range(m):
                self.parent[(i, j)] = (i, j)
                self.size[(i, j)] = 1

    def __getitem__(self, u):
        if self.parent[u] != u:
            self.parent[u] = self[self.parent[u]]
        return self.parent[u]

    def join(self, u, v):
        u = self[u]
        v = self[v]
        if self.size[u] < self.size[v]:
            u, v = v, u
        self.size[u] += self.size[v]
        self.parent[v] = u


class Grid(object):
    def __init__(self, n, m, grid):
        self.n = n
        self.m = m
        self.grid = grid

    # returns DSU for grid where all islands are components
    def colorIslands(self):
        dsu = _GridDSU(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                if i and self.grid[i][j] and self.grid[i - 1][j]:
                    dsu.join((i, j), ((i - 1, j)))
                if j and self.grid[i][j] and self.grid[i][j - 1]:
                    dsu.join((i, j), ((i, j - 1)))
        return dsu

    # returns amount of islands in grid
    def countIslands(self):
        color = self.colorIslands()
        colors = set()
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j]:
                    colors.add(color[(i, j)])
        return len(colors)
