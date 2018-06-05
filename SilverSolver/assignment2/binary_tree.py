class BinaryNode:

    def __init__(self, value, parent=None, child1=None, child2=None):
        self.value  = value
        self.parent = parent
        self.child1 = child1
        self.child2 = child2

    def get_ancestors(self, prev_ancestors=None, value=True):
        if not prev_ancestors:
            prev_ancestors = []
        if not self.parent:
            return prev_ancestors
        else:
            if value:
                prev_ancestors.append(self.parent.value)
            else:
                prev_ancestors.append(self.parent)
            return self.parent.get_ancestors(prev_ancestors=prev_ancestors, value=value)

    def get_lowest_common_ancestor(self, another_node, value=True):
        self_anc = self.get_ancestors(value=False)
        another_anc = another_node.get_ancestors(value=False)
        low_c_anc = None
        while(self_anc and another_anc):
            if self_anc[-1] == another_anc[-1]:
                low_c_anc = self_anc[-1]
                self_anc = self_anc[:-1]
                another_anc = another_anc[:-1]
            else:
                if value and low_c_anc:
                    return low_c_anc.value
                else:
                    return low_c_anc
        if value and low_c_anc:
            return low_c_anc.value
        else:
            return low_c_anc

class BinaryTree:

    def __init__(self, iterable=None):
        if iterable and len(iterable) > 0:
            iterable = list(map(BinaryNode, iterable))
            self.root = iterable[0]
            current_nodes = [self.root]
            iterable  = iterable[1:]
            while len(iterable) > 0:
                if not current_nodes[0].child1:
                    current_nodes[0].child1 = iterable[0]
                    current_nodes[0].child1.parent = current_nodes[0]
                    iterable = iterable[1:]
                elif not current_nodes[0].child2:
                    current_nodes[0].child2 = iterable[0]
                    current_nodes[0].child2.parent = current_nodes[0]
                    iterable = iterable[1:]
                else:
                    current_nodes += [current_nodes[0].child1, current_nodes[0].child2]
                    current_nodes = current_nodes[1:]
        else:
            self.root = None
