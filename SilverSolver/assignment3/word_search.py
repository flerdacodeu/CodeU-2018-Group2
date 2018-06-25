from bisect import bisect_left
from dictionary import Dictionary
from typing import List, Tuple

def word_search(grid: List[List[str]], dictionary: Dictionary) -> List[str]: 
    # From there, we suppose that grid is correct
    def neighbours(coords: Tuple[int]) -> Tuple[Tuple[int]]:
        a, b = coords
        neigh_coords = [(a + i, b + j) for i in [-1, 1, 0] for j in [-1, 1, 0] if (i, j) != (0, 0)]
        #return filter(lambda x: x[0] >= 0 and x[1] >= 0 and x[0] < m and x[1] < n, neigh_coords)
        return [(x, y) for x, y in neigh_coords if 0 <= x < m and 0 <= y < n]
    
    def search(coords: Tuple[int, int]):
        # coords = tuple of grid indices
        # Run depth-first search starting from the given point.
        if history[coords[0]][coords[1]]:
            return
        history[coords[0]][coords[1]] = True
        c = grid[coords[0]][coords[1]]
        prefix.append(c)
        if dictionary.isWord(prefix):
            words.add(''.join(prefix))
        if dictionary.isPrefix(prefix):
            for new_coords in neighbours(coords):
                search(new_coords)
        del prefix[-1]
        history[coords[0]][coords[1]] = False

    words = set()
    if len(grid) > 0:
        m, n = len(grid), len(grid[0])
    else:
        return set()
    
    history = [[False] * n for _ in range(m)] # used to track if grid point was visited to avoid cycles.
    prefix  = []                              # list of chars to store current prefix. 
    # We use list instead of str because it allows adding and removing last element at cost of O(1).
        
    for i in range(m):
        for j in range(n):
            search((i, j))
    return words
