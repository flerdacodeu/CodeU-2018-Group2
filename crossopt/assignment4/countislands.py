#!/usr/bin/env python3


"""grid of tiles. stores islands via dsu"""
"""https://en.wikipedia.org/wiki/Disjoint-set_data_structure"""
class Grid(object):
    def __init__(self, n, m, grid):
        self.n = n
        self.m = m
        self.grid = grid
        self.__parents = dict()
        self.__sizes = dict()
        for i in range(n):
            for j in range(m):
                self.__parents[i, j] = (i, j)
                self.__sizes[i, j] = 1
                if i and self.grid[i][j] and self.grid[i - 1][j]:
                    self.join((i, j), ((i - 1, j)))
                if j and self.grid[i][j] and self.grid[i][j - 1]:
                    self.join((i, j), ((i, j - 1)))

    def get_id(self, u):
        """ returns unique id for each island """
        if self.__parents[u] != u:
            self.__parents[u] = self.get_id(self.__parents[u])
        return self.__parents[u]
    
    def join(self, u, v):
        u = self.get_id(u)
        v = self.get_id(v)
        if self.__sizes[u] < self.__sizes[v]:
            u, v = v, u
        self.__sizes[u] += self.__sizes[v]
        self.__parents[v] = u

    def countIslands(self):
        """ returns amount of islands in grid """
        colors = set()
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j]:
                    colors.add(self.get_id((i, j)))
        return len(colors)
