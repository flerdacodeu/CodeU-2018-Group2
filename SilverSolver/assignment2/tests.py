import unittest
from binary_tree import *

class TestBinaryTreeFunctions(unittest.TestCase):

    def test_empty_node(self):
        empty_node = BinaryNode(None)
        self.assertEqual(empty_node.value, None)
        self.assertEqual(empty_node.get_ancestors(), [])

    def test_binary_tree_0(self):
        my_tree = BinaryTree()
        self.assertEqual(my_tree.root, None)

    def test_binary_tree_1_and_get_anc(self):
        my_tree = BinaryTree([1])
        self.assertEqual(my_tree.root.value, 1)
        self.assertEqual(my_tree.root.get_ancestors(), [])

    def test_binary_tree_2_and_get_anc(self):
        my_tree = BinaryTree([i for i in range(15)])
        #     0
        #    / \
        #   1   2
        #  / \ / \
        #  3 4 5 6 
        # .........
        self.assertEqual(my_tree.root.child1.child1.value, 3)
        self.assertEqual(my_tree.root.child1.child2.value, 4)
        self.assertEqual(my_tree.root.child2.child1.value, 5)
        self.assertEqual(my_tree.root.child2.child2.value, 6)

        current_node = my_tree.root.child1.child1.child1
        self.assertEqual(current_node.get_ancestors(), [current_node.parent.value, \
                         current_node.parent.parent.value, current_node.parent.parent.parent.value])

        current_node = my_tree.root.child2.child1.child2
        self.assertEqual(current_node.get_ancestors(), [current_node.parent.value, \
                         current_node.parent.parent.value, current_node.parent.parent.parent.value])

    def test_lowest_ancestor_0(self):
        node1 = BinaryNode("some value")
        node2 = BinaryNode("another value")
        self.assertEqual(node1.get_lowest_common_ancestor(node2), None)

    def test_lowest_ancestor_1a(self):
        my_tree = BinaryTree(["parent", "child"])
        # lowest_common_ancestor of a node with itself is it's parent
        self.assertEqual(my_tree.root.child1.get_lowest_common_ancestor(my_tree.root.child1), \
                         "parent")
    
    def test_lowest_ancestor_1b(self):
        my_tree = BinaryTree(["parent", "child1", "child2"])
        self.assertEqual(my_tree.root.child1.get_lowest_common_ancestor(my_tree.root.child2), \
                         "parent")

    def test_lowest_ancestor_2_and_tree(self):
        my_tree = BinaryTree([c for c in "abcdefgh"])
        #     a
        #    / \
        #   b   c
        #  / \ / \
        #  d e f g
        #  |
        #  h
        self.assertEqual(my_tree.root.child1.value, "b")
        self.assertEqual(my_tree.root.child2.value, "c")
        # different level nodes
        self.assertEqual(my_tree.root.child1.child2.get_lowest_common_ancestor( \
                         my_tree.root.child2),        my_tree.root.value)
        self.assertEqual(my_tree.root.child1.child1.child1.get_lowest_common_ancestor( \
                         my_tree.root.child1.child2), my_tree.root.child1.value)
        # same level nodes
        self.assertEqual(my_tree.root.child2.child2.get_lowest_common_ancestor( \
                         my_tree.root.child1.child1), my_tree.root.value)
        self.assertEqual(my_tree.root.child2.child1.get_lowest_common_ancestor( \
                         my_tree.root.child1.child2), my_tree.root.value)

if __name__ == '__main__':
    unittest.main()
