#!/usr/bin/env python3


class TreeNode:
    def __init__(self, val, par=None):
        self.left = None
        self.right = None
        self.val = val
        self.parent = par

    def __iter__(self):
        yield self
        if self.left:
            yield from self.left
        if self.right:
            yield from self.right

    # adds val as left son of node
    def addLeft(self, val):
        if self.left:
            raise KeyError
        self.left = TreeNode(val, self)

    # adds val as right son of node
    def addRight(self, val):
        if self.right:
            raise KeyError
        self.right = TreeNode(val, self)

    # returns node in subtree with given value
    def __getitem__(self, val):
        for key in self:
            if key.val == val:
                return key
        raise KeyError

    # length of path to root from current node
    def height(self):
        ans = 0
        cnt = self.parent
        while cnt:
            ans += 1
            cnt = cnt.parent
        return ans

    # returns list of ancestors of current node
    # TODO - this and height look similar
    def ancestors(self):
        ans = []
        cnt = self.parent
        while cnt:
            ans.append(cnt.val)
            cnt = cnt.parent
        return ans

    # given two nodes in subtree, returns lca-node
    def lca(self, v1, v2):
        if v1 not in self or v2 not in self:
            raise KeyError
        height1 = v1.height()
        height2 = v2.height()

        for _ in range(height1 - height2):
            v1 = v1.parent
        for _ in range(height2 - height1):
            v2 = v2.parent
        while v1 != v2:
            v1 = v1.parent
            v2 = v2.parent

        return v1

# TODO - add unit tests!
if __name__ == "__main__":
    tree = TreeNode(5)
    tree.addRight("dog")
    tree.addLeft(None)
    tree.right.addRight(dict())
    for i in tree:
        print("{}'s ancestors: {}".format(i.val, i.ancestors()))
    assert tree.lca(tree[5], tree["dog"]).val == 5
    assert tree.lca(tree[dict()], tree["dog"]).val == "dog"
