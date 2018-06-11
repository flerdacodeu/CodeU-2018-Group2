import unittest
from assignment2.ancestors import BinaryTree


class TestAncestor(unittest.TestCase):

	# Constructs the tree with the given example on assignment description.
	def construct_tree(self):
		t = BinaryTree(7)
		t.add_left(7, 3)
		t.add_left(3, 2)
		t.add_left(2, 1)
		t.add_right(2, 6)
		t.add_right(3, 5)
		t.add_right(7, 4)
		t.add_right(4, 8)
		return t

	def test_ancestors(self):
		tree = self.construct_tree()
		self.assertListEqual(tree.ancestors(7), [])
		self.assertListEqual(tree.ancestors(3), [7])
		self.assertListEqual(tree.ancestors(4), [7])
		self.assertListEqual(tree.ancestors(2), [3, 7])
		self.assertListEqual(tree.ancestors(5), [3, 7])
		self.assertListEqual(tree.ancestors(1), [2, 3, 7])
		self.assertListEqual(tree.ancestors(8), [4, 7])

	def test_common_ancestors(self):
		tree = self.construct_tree()
		self.assertEqual(tree.common_ancestors(3, 4), 7)
		self.assertEqual(tree.common_ancestors(2, 8), 7)
		self.assertEqual(tree.common_ancestors(3, 8), 7)
		self.assertEqual(tree.common_ancestors(1, 8), 7)
		self.assertEqual(tree.common_ancestors(2, 5), 3)
		self.assertEqual(tree.common_ancestors(1, 5), 3)
		self.assertEqual(tree.common_ancestors(1, 6), 2)

	def test_common_ancestors2(self):
		tree = self.construct_tree()
		self.assertEqual(tree.common_ancestors2(3, 4), 7)
		self.assertEqual(tree.common_ancestors2(2, 8), 7)
		self.assertEqual(tree.common_ancestors2(3, 8), 7)
		self.assertEqual(tree.common_ancestors2(1, 8), 7)
		self.assertEqual(tree.common_ancestors2(2, 5), 3)
		self.assertEqual(tree.common_ancestors2(1, 5), 3)
		self.assertEqual(tree.common_ancestors2(1, 6), 2)