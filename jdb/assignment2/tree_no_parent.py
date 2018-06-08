import unittest
from typing import Generator, List, Tuple, TypeVar

T = TypeVar('T')
TAncestors = Tuple[T]
_StackOfT = List[T]

class Node:
    def __init__(self, value: T, left = None, right = None):
        self.left = Node(*left) if left else None
        self.value = value
        self.right = Node(*right) if right else None
        
    def _ancestry_lines(self, stack: _StackOfT = None) -> Generator[_StackOfT, None, None]:
        """yields ancestry lines for current and sub- nodes.

        Args:
          stack: a Stack of T. If missing, a new empty stack is created and used.

        Yields:
          the same stack eventually holding all sub ancestry lines, as the sub
            nodes are visited.

            Note: the *same* mutated stack object is yielded, with younger nodes
            appended to the left, then popped. Make sure to make a frozen copy
            if you want to keep a list of the ancestry lines of interest.
        """
        if stack is None: stack = []

        stack.append(self.value)
        
        if self.left: yield from self.left._ancestry_lines(stack)
        yield stack
        if self.right: yield from self.right._ancestry_lines(stack)
        
        stack.pop()

    def find_ancestors(self, values: List[T]) -> List[TAncestors]:
        """Return the list of ancestry lines, one for each input value.

        Visiting the tree stops as soon as ancestry line is found for each
        value. If multiple nodes holds the same value, then the last ancestry
        line seen for that value is returned.
        """
        # Among all ancestry lines, filter in those ending with any of the input values.
        ancestors_dict = {}
        for stack in self._ancestry_lines():
            if stack[-1] in values:
                ancestors_dict[stack[-1]] = tuple(stack)  # "freeze" the ever-mutating stack.
                if len(ancestors_dict) == len(values):
                    return sorted(ancestors_dict.values())
        else:
            raise KeyError("Not all values '%s' found in the tree." % values)


    def common_ancestors(self, value1: T, value2: T) -> Generator[T, None, None]:
        """Returns the list of ancestors common to value1 and value2."""
        for ancestor1, ancestor2 in zip(*self.find_ancestors([value1, value2])):
            if ancestor1 != ancestor2:
                return
            yield ancestor1

# run the static type checker: mypy tree.py
# run the unittest: python3 -m unittest tree
class NodeTest(unittest.TestCase):

    def setUp(self):
        self.tree = Node(
            6,
            (3,
             (1,
              (2,)),
             (4, 
              (5,))),
            (8,
             (7,),
             (9,
              (0,))))

    def test_init(self):
        self.assertEqual(self.tree.value, 6)
        self.assertEqual(self.tree.left.value, 3)
        self.assertEqual(self.tree.right.value, 8)

    def test_ancestry_lines(self):
        self.assertEqual(sum(1 for i in self.tree._ancestry_lines()), 10)
        
    def test_ancestors(self):
        self.assertEqual(self.tree.find_ancestors([0]),
                         [(6, 8, 9, 0)])
        self.assertEqual(self.tree.find_ancestors([0, 7]),
                         [(6, 8, 7), (6, 8, 9, 0)])

    def test_common_common(self):
        self.assertEqual(tuple(self.tree.common_ancestors(0, 7)),
                         (6, 8))
    
