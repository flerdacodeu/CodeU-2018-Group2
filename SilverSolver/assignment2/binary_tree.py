class BinaryNode:

    def __init__(self, value, parent=None, child1=None, child2=None):
        self.value  = value
        self.parent = parent
        self.child1 = child1
        self.child2 = child2

    def get_ancestors(self, prev_ancestors=None):
        if not prev_ancestors:
            prev_ancestors = []
        if not self.parent:
            return prev_ancestors
        else:
            prev_ancestors.append(self.parent.value)
            return self.parent.get_ancestors(prev_ancestors=prev_ancestors)

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
