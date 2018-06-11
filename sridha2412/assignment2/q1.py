# print ancestors of given key in a binary tree

# node class`
class Node:
    def __init__(self, data: int):
        """ constuctor to initlalize a node object """
        self.data = data
        self.left = None
        self.right = None

def find_ancestors(root: Node, key: int, ancestors: list) -> bool:
    """ if key is present, return list of ancestors else return false """
    # base cases
    if root is None:
        return False
    if root.data == key:
        return True

    # store all nodes in list
    ancestors.append(root.data)

    # search for key in left and right subtrees
    if find_ancestors(root.left, key, ancestors) or find_ancestors(root.right, key, ancestors) :
        return ancestors

    # if not ancestor, delete from list
    ancestors.pop()

    return False

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        #       7
        #      / \
        #     3   4
        #    / \   \
        #   2   5   8
        #  / \
        # 1   6
        self.root = Node(7)
        self.root.left = Node(3)
        self.root.right = Node(4)
        self.root.left.left = Node(2)
        self.root.left.right = Node(5)
        self.root.right.right = Node(8)
        self.root.left.left.left = Node(1)
        self.root.left.left.right = Node(6)

    def test_init(self):
        self.assertEqual(self.root.data, 7)
        self.assertEqual(self.root.right.data, 4)
        self.assertEqual(self.root.left.data, 3)

    def test_ancestors(self):
        self.assertEqual(find_ancestors(self.root, 6, []), [7, 3, 2])
        self.assertEqual(find_ancestors(self.root, 8, []), [7, 4])
        self.assertEqual(find_ancestors(self.root, 10, []), False)
