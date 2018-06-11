
"""A solution for the CodeU Emea assignment #2: binary trees.

There are two important elements, extracted from the exercice, that drove this
implementation:

1. no mentions of mutations on the tree once it is built, the tree is read-only,
   this makes it easy and worthwhile to precompute as much things as possible so
   they are available when needed, and they are only computed once:
   - Nodes keep a pointer to the parent
   - Nodes keep a int representing the depth of a Node in the tree.

   If the tree was mutable, we could still make sure mutations would keep these
   2 signals correct, but it would be more work.

2. the exercise requests no storing of the nodes: this code does not create any
   list to which nodes get appended, instead, this code uses generators which
   are comparable to index pointer being moved. They are baked into the Python
   language with the yield keyword so they are less verbose than in other
   languages like C++ or Java.

By construction, the two tree properties are guaranteed: connected graph and no
loops. In addition, one large assumption in this code, is that values held by
the nodes are unique. The unit test uses ints, there are no 2 nodes with the
value 2, for example.

Additional note about Python type annotations: Python 3.5 introduced optional
typing, and types complement unit tests:
1. they help the readers of the code,
2. they help the author to design a good consistent API,
3. type checkers find errors statically, thus saving some class of errors
   before the code is sent to production.
4. static analysis helps with refactoring, and refactoring is a fact of life for
    medium to big sized project.
We suggest and warmly support the use of Python type annotations :)
More info at: https://docs.python.org/3/library/typing.html

To run the mypy static type checker (http://mypy-lang.org/):
$ mypy tree.py
"""

import unittest
from typing import Generator, Tuple, TypeVar

T = TypeVar('T')  # the generic type of values held in each node.

class Node:
  def __init__(self, value : T,
               left: Tuple = None,
               right: Tuple = None,
               parent: 'Node' = None,
               depth: int = 0):

    self.value = value
    self.parent = parent
    self.depth = depth
    self.left = Node(*left, parent=self, depth=depth+1) if left else None
    self.right = Node(*right, parent=self, depth=depth+1) if right else None

  def _ancestors(self) -> Generator['Node', None, None]:
    """Yields the current node, then the ancestor nodes up to the root.

    The first element yield is the node itself (in this sense, the node is
    considered an ancestor of itself).
    """
    yield self
    if self.parent:
      yield from self.parent._ancestors()

  def print_ancestors(self):
    print(' '.join(str(i) for i in self._ancestors()))

  def lowest_common_ancestor(self, node1: 'Node', node2: 'Node') -> 'Node':
    """Returns the node that is the lowest common ancestor of node1, node2."""
    deeper, shallower  = ((node2, node1)
                          if node2.depth > node1.depth else (node1, node2))
    for _ in range(deeper.depth - shallower.depth):
      deeper = deeper.parent

    # Note: because _ancestors() returns an iterator, and the iterator behaves
    # lazily, ancestors() will not reach to the top of the tree, unless
    # required. Each iterator will be pulled just enough times to find the
    # common ancestor.
    for a1, a2 in zip(deeper._ancestors(), shallower._ancestors()):
      if a1 == a2:
        return a1
    raise ValueError('The two nodes have no common ancestor, '
                     'Did you check the graph is actually connected?')


def search(root: Node, value: T):
  """Helper function handy for the unit tests: find the node with 'value'."""
  for subtree in root.left, root.right:
    if subtree:
      try:
        return search(subtree, value)
      except KeyError:
        pass
  if root.value == value:
    return root
  raise KeyError("Value '%s' not found in the tree." % value)


def check_loops(value: T,
                left: tuple = None,
                right: tuple = None,
                seen: set =None):
  """Helper function handy to validate a Node input against loop."""
  if seen is None:
    seen = set()
  for subtree in left, right:
    if not subtree:
      continue
    if id(subtree) in seen:
      raise ValueError('Loop detected, the input is not a real tree.')
    else:
      seen.add(id(subtree))
    check_loops(*subtree, seen=seen)
    

class NodeTest(unittest.TestCase):
  """To run the unittest:
  $ python3 -m unittest tree
  """

  def setUp(self):
    self.input = (
        6, # value
        (3, # left subtree...
         (1,
          (2,)),
         (4,
          (5,))),
        (8,  # right subtree...
         (7,),
         (9,
          (0,))))
    self.tree = Node(*self.input)

  def test_init(self):
    self.assertEqual(self.tree.value, 6)
    self.assertEqual(self.tree.left.value, 3)
    self.assertEqual(self.tree.right.value, 8)

  def test_search(self):
    self.assertEqual(search(self.tree, 1).parent, search(self.tree, 3))
    self.assertEqual(search(self.tree, 0).parent.parent, search(self.tree, 8))
    with self.assertRaises(KeyError):
      search(self.tree, 9999)

  def test_ancestors(self):
    self.assertEqual([node.value for node in search(self.tree, 0)._ancestors()],
                     [0, 9, 8, 6])

  def test_lowest_common_common(self):
    self.assertEqual(
        self.tree.lowest_common_ancestor(search(self.tree, 0),
                                         search(self.tree, 3)).value,
        6,'Two nodes must have a common root')

    self.assertEqual(
        self.tree.lowest_common_ancestor(search(self.tree, 0),
                                         search(self.tree, 6)).value,
        6, 'The direct ancestor of another node is the lca.')

    self.assertEqual(
        self.tree.lowest_common_ancestor(search(self.tree, 7),
                                         search(self.tree, 0)).value,
        8, 'The common ancestor of two nodes is not the root')

    self.assertEqual(
        self.tree.lowest_common_ancestor(search(self.tree, 4),
                                         search(self.tree, 4)).value,
        4, 'The common ancestor of the exact same node is the node.')

    with self.assertRaises(ValueError,
                           msg='Disconnected trees raise a ValueError'):
      self.tree.lowest_common_ancestor(search(self.tree, 0), Node(999))

  def test_loop(self):
    looping_graph = [2, [1, ], [3, ]]

    # Note that this is a contrived unit test that only works because the type
    # checks are optional: the construction of a looping graph is only possible
    # because the Python list is used here, and the Python list is mutable.
    # one can only append to the list because the list is mutable.  Should the
    # type annotations of the Node constructor be respected, only Python tuples
    # would be used. Because Python tuples are immutable, and it is impossible
    # to construct an input looping graph in the first place, out of tuples
    # only.

    # tree's right node is appended tree itself on the left: not a tree anymore
    looping_graph[2].append(looping_graph)

    with self.assertRaises(ValueError, msg='Looping graphs are detected.'):
      check_loops(*looping_graph)
