from copy import deepcopy
from typing import List

def neighbourhood(i: int, j: int, islandMatrix: List[List[int]]) -> List[List[int]]:
    "helper function, returns the neighbourhood of (i, j) cell in islandMatrix"

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = di + i, dj + j # ni, nj are a neighbor candidates for i, j
        if 0 <= ni < len(islandMatrix) and 0 <= nj < len(islandMatrix[0]) and islandMatrix[ni][nj]:
            yield ni, nj

def island_fill(i: int, j: int, islandMatrix: List[List[int]]) -> List[List[int]]:
    """
    helper function, fills the island, to which (i, j) belongs, with "2"
    it will help to distinct it with the islands in which we've never been
    """
    q = [(i, j)]
    while q:
        element = q.pop()
        if islandMatrix[element[0]][element[1]] == 1:
            for e in neighbourhood(element[0], element[1], islandMatrix):
                q.append(e)
            islandMatrix[element[0]][element[1]] = 2
    return islandMatrix

def get_number_of_islands(islandMatrix: List[List[int]]) -> int:
    "the essential function"
    
    islandMatrix_r = deepcopy(islandMatrix)
    islandNum = 0
    for i in range(len(islandMatrix_r)):
        for j in range(len(islandMatrix_r[0])):
            if islandMatrix_r[i][j] == 1:
                islandNum += 1
                islandMatrix_r = island_fill(i, j, islandMatrix_r)
    return islandNum
