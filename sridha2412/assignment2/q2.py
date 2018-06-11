# finds lowest common ancestor of two nodes in a binary tree

# node class`
class Node:
    def __init__(self, data: int):
        """ constuctor to initlalize a node object """
        self.data = data
        self.left = None
        self.right = None

def is_present(root: Node, key: int) -> bool:
    """ method to check if node is present in tree """
    if root is None:
        return False

    if root.data == key or is_present(root.right, key) or is_present(root.left, key):
        return True

    return False

def find_lca(root: Node, node1: int, node2: int) -> int:
    """ method to find least common ancestor of two given nodes
        note: if one key is ancestor of another, it returns the key
        e.g we had lca(3,2) and 3 was the ancestor of 2, it would return 3"""

    # base cases
    if root is None:
        return None
    # if either of the nodes are found, it implies that one is the ancestor of another
    # this algorithm returns the node and doesn't try finding the ancestor of said node
    if root.data == node1:
        return root.data
    if root.data == node2:
        return root.data

    # search for keys in left and right subtrees
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    # if both return non None values, one key is present in left subtree and the other in right
    if left_lca and right_lca:
        return root.data

    # else check right subtree if left is None and vice-versa
    return right_lca if left_lca is None else left_lca


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

    def test_is_present(self):
        self.assertEqual(is_present(self.root, 1), True)
        self.assertEqual(is_present(self.root, 10), False)

    def test_lca(self):
        self.assertEqual(find_lca(self.root, 5, 6), 3)
        self.assertEqual(find_lca(self.root, 3, 2), 3)
