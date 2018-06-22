
from collections import OrderedDict
from itertools import product

class Grid:

  def __init__(self, *grid, lexicon=None):
    self.grid, self.lexicon = grid, lexicon if lexicon else load_lexicon()
    self.x_max, self.y_max = len(grid[0]), len(grid)

  def __getitem__(self, position):
    """Returns the letter found at 'position'."""
    return self.grid[position[1]][position[0]]

  def words(self):
    """Returns words found on the grid."""
    words = set()
    for slot in product(range(self.x_max), range(self.y_max)):
      self._check_prefixes(slot, words)
    # the returned words are reverse-sorted by word length.
    return sorted(words, key=lambda w: (-len(w), w))

  def _check_prefixes(self, slot, words):
    traversal = self._traverse(slot)
    backtrack_request = None
    while True:
      try:
        path = traversal.send(backtrack_request)
      except StopIteration:
        return words

      prefix = ''.join(self[s] for s in path)
      if not self.lexicon.is_prefix(prefix):
        backtrack_request = True
      else:
        backtrack_request = False
        if self.lexicon.is_word(prefix):
          words.add(prefix)


  def _traverse(self, slot, path=None):
    """Traverses the paths starting from 'position'."""
    if path is None:
      path = OrderedDict()

    path[slot] = True

    backtrack_request = yield path
    if not backtrack_request:
      for slot in self._children(path, *slot):
        yield from self._traverse(slot, path)

    path.popitem()

  def _children(self, visited, x, y):
    """Generate the unvisited neighbors of 'position'."""
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        xn, yn = x + dx, y + dy
        if (0 <= xn < self.x_max and 0 <= yn < self.y_max and
            (xn, yn) not in visited):
          yield xn, yn


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


class TestBuggles(unittest.TestCase):

  def test_children(self):
    neighbors = list(Grid('abc', 'def', 'ghi', lexicon=True)
                     ._children(set(), 1, 0))
    self.assertIn((1, 1), neighbors)
    self.assertIn((0, 0), neighbors)
    self.assertNotIn((1, 2), neighbors)
    self.assertNotIn((1, -1), neighbors)

  def test_getitem(self):
    grid = Grid('abc', 'def', 'ghi', lexicon=True)
    for letter, position in zip('abcdefghi',
                                ((x, y) for y in range(3) for x in range(3))):
      self.assertEqual(grid[position], letter)

  def test_words(self):
    words = Grid('aar', 'tcd').words()
    for word in ['card', 'data', 'act', 'arc', 'cad', 'car', 'cat', 'rat',
                 'rca', 'tad', 'tar', 'ac', 'ad']:
      self.assertIn(word, words)
