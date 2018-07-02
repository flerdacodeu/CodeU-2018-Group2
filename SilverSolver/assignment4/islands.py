from collections import deque
from typing import List

def neighbourhood(i: int, j: int, islandMatrix: List[List[int]]) -> List[List[int]]:
    # helper function, returns the neighbourhood of (i, j) cell in islandMatrix
    neigh = []
    if i > 0:
        if islandMatrix[i - 1][j] == 1:
            neigh.append((i - 1, j))
    if i < len(islandMatrix) - 1:
        if islandMatrix[i + 1][j] == 1:
            neigh.append((i + 1, j))
    if j > 0:
        if islandMatrix[i][j - 1] == 1:
            neigh.append((i, j - 1))
    if j < len(islandMatrix[0]) - 1:
        if islandMatrix[i][j + 1] == 1:
            neigh.append((i, j + 1))
    return neigh

def island_fill(i: int, j: int, islandMatrix: List[List[int]]) -> List[List[int]]:
    # helper function, fills the island, to which (i, j) belongs, with "2"
    # it will help to distinct it with the islands in which we've never been
    q = deque()
    q.append((i, j))
    while q:
        element = q.pop()
        if islandMatrix[element[0]][element[1]] == 1:
            for e in neighbourhood(element[0], element[1], islandMatrix):
                q.append(e)
            islandMatrix[element[0]][element[1]] = 2
    return islandMatrix

def get_number_of_islands(islandMatrix: List[List[int]]) -> int:
    # the essential function
    islandNum = 0
    for i in range(len(islandMatrix)):
        for j in range(len(islandMatrix[0])):
            if islandMatrix[i][j] != 1:
                pass
            else:
                islandNum += 1
                islandMatrix = island_fill(i, j, islandMatrix)
    return islandNum
