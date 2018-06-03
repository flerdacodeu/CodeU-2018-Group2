import unittest
from binary_tree import *

class TestQ1(unittest.TestCase):

    def test_empty_node(self):
        empty_node = BinaryNode(None)
        self.assertEqual(empty_node.value, None)
        self.assertEqual(empty_node.get_ancestors(), [])

    def test_binary_tree_0(self):
        my_tree = BinaryTree()
        self.assertEqual(my_tree.root, None)

    def test_binary_tree_1(self):
        my_tree = BinaryTree([1])
        self.assertEqual(my_tree.root.value, 1)
        self.assertEqual(my_tree.root.get_ancestors(), [])

    def test_binary_tree_2(self):
        my_tree = BinaryTree([i for i in range(10)])
        current_node = my_tree.root.child1.child1.child1
        self.assertEqual(current_node.get_ancestors(), [current_node.parent.value, \
                         current_node.parent.parent.value, current_node.parent.parent.parent.value])

    def test_binary_tree_3(self):
        my_tree = BinaryTree([i for i in range(15)])
        current_node = my_tree.root.child2.child1.child2
        self.assertEqual(current_node.get_ancestors(), [current_node.parent.value, \
                         current_node.parent.parent.value, current_node.parent.parent.parent.value])

if __name__ == '__main__':
    unittest.main()
