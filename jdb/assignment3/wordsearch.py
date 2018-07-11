
from collections import OrderedDict
from itertools import product

class Grid:

  def __init__(self, *grid, lexicon=None):
    self.grid, self.lexicon = grid, lexicon if lexicon else load_lexicon()
    self.x_max, self.y_max = len(grid[0]), len(grid)
    
  def words(self):
    """Yields the words found on the Grid."""
    words = set()
    traversal = self._traverse()
    backtrack_request = None
    while True:
      try:
        path = traversal.send(backtrack_request)
      except StopIteration:
        return words
      prefix = ''.join(self.grid[p[1]][p[0]] for p in path)
      if self.lexicon.is_prefix(prefix):
        backtrack_request = False
        if self.lexicon.is_word(prefix):
          words.add(prefix)
      else:
        backtrack_request = True
    return words

  def _traverse(self, path=None):
    """Yields all possible path through the grid."""
    # There is two cases:
    # - path empty: first position from which to start prefix is any position
    # - path non-empty: the next position must be picked from the neighbors
    if path is None:
      path = OrderedDict()
      for position in product(range(self.x_max), range(self.y_max)):
        path[position] = True
        backtrack_request = yield path
        if not backtrack_request:
          yield from self._traverse(path)
        path.popitem()
    else:
      last, _ = path.popitem()
      path[last] = True
      for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        x, y = last[0] + dx, last[1] + dy
        if (0 <= x < self.x_max and 0 <= y < self.y_max and (x, y) not in path):
          path[(x, y)]= True
          backtrack_request = yield path
          if not backtrack_request:
            yield from self._traverse(path)
          path.popitem()


def load_lexicon():
  trie = Trie()
  # On linux, install the file below with:
  # $ sudo apt-get install wamerican
  with open('/usr/share/dict/american-english') as f:
    for word in [w.strip().lower() for w in f
                 if not w.strip().endswith("'s") and len(w.strip())>1]:
      trie.add(word)
  return trie


class Trie:

  def __init__(self):
    self.children = {}
    self.full_word = False

  def add(self, letters):
    first, *rest = letters
    if first not in self.children:
      self.children[first] = Trie()
    if rest:
      self.children[first].add(rest)
    else:
      self.children[first].full_word = True

  def __getitem__(self, letters):
    first, *rest = letters
    if first not in self.children:
      return False
    return self.children[first][rest] if rest else self.children[first]

  def is_word(self, letters):
    trie = self[letters]
    return trie.full_word if trie else False

  def is_prefix(self, letters):
    return bool(self[letters])


# run the unittest with python -m unittest wordsearch.py
import unittest

class TestTrie(unittest.TestCase):

  def test_trie(self):
    trie = Trie()
    for word in 'car', 'card', 'cart', 'cat':
      trie.add(word)
    for word in 'car', 'card', 'cart', 'cat':
      self.assertTrue(trie.is_word(word))
      self.assertTrue(trie.is_prefix(word))
    for word in 'c', 'ca':
      self.assertFalse(trie.is_word(word))
      self.assertTrue(trie.is_prefix(word))
    self.assertFalse(trie['NoTfOuNd'])


class TestGrid(unittest.TestCase):

  def test_traverse(self):
    neighbors = set(
      tuple(p) for p in Grid('abc', 'def', 'ghi', lexicon=True)._traverse())
    self.assertIn(((1, 1),), neighbors)
    self.assertIn(((0, 0),), neighbors)
    self.assertIn(((1, 2),), neighbors)
    self.assertNotIn(((1, -1),), neighbors)

  def test_grid(self):
    grid = Grid('abc', 'def', 'ghi', lexicon=True)
    for letter, position in zip('abcdefghi',
                                ((x, y) for y in range(3) for x in range(3))):
      self.assertEqual(grid.grid[position[1]][position[0]], letter)

  def test_words(self):
    words = Grid('aar', 'tcd').words()
    for word in ['card', 'data', 'act', 'arc', 'cad', 'car', 'cat', 'rat',
                 'rca', 'tad', 'tar', 'ac', 'ad']:
      self.assertIn(word, words)
      
