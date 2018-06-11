#!/usr/bin/env python3

import unittest
from assignment2.treenode import TreeNode


class TestTreeNode(unittest.TestCase):

    def test_one_node(self):
        tree = TreeNode("OK")
        self.assertEqual(tree.val, "OK")
        self.assertEqual(tree.ancestors(), [])
        self.assertEqual(tree.lca(tree, tree), tree)

    # constructs tree from assignment sample
    def construct_sample(self):
        t = TreeNode(7)
        t.addLeft(3)
        t.left.addLeft(2)
        t.left.left.addLeft(1)
        t.left.left.addRight(6)
        t.left.addRight(5)
        t.addRight(4)
        t.right.addRight(8)
        return t

    def test_sample_ancestors(self):
        tree = self.construct_sample()
        self.assertListEqual(tree.ancestors(), [])
        self.assertListEqual(tree[3].ancestors(), [7])
        self.assertListEqual(tree[2].ancestors(), [3, 7])
        self.assertListEqual(tree[1].ancestors(), [2, 3, 7])
        self.assertListEqual(tree[5].ancestors(), [3, 7])
        self.assertListEqual(tree[4].ancestors(), [7])
        self.assertListEqual(tree[8].ancestors(), [4, 7])

    def test_sample_lca(self):
        tree = self.construct_sample()
        self.assertEqual(tree.lca(tree[3], tree[4]), tree[7])
        self.assertEqual(tree.lca(tree[2], tree[3]), tree[3])
        self.assertEqual(tree.lca(tree[1], tree[7]), tree[7])
        self.assertEqual(tree.lca(tree[1], tree[6]), tree[2])
        self.assertEqual(tree.lca(tree[2], tree[5]), tree[3])
        self.assertEqual(tree.lca(tree[1], tree[8]), tree[7])
        self.assertEqual(tree.lca(tree[6], tree[4]), tree[7])
        self.assertEqual(tree.lca(tree[6], tree[6]), tree[6])


if __name__ == "__main__":
    unittest.main()
