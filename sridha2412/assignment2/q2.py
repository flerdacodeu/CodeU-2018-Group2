# finds lowest common ancestor of two nodes in a binary tree

# node class`
class Node:
    # constuctor to initlalize a node object
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# method to find node is present in tree
def find_node(root, node):
    if root is None:
        return False

    if root.data == node or find_node(root.right, node) or find_node(root.left, node):
        return True

    return False

# method to find least common ancestor of two given nodes
# note: if one key is ancestor of another, it returns the key
def find_lca(root, node1, node2):
    # base cases
    if root is None:
        return None
    if root.data == node1:
        return root
    if root.data == node2:
        return root

    # search for keys in left and right subtrees
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    # if both return non None values, one key is present in left subtree and the other in right
    if left_lca and right_lca:
        return root

    # else check right subtree if left is None and vice-versa
    return right_lca if left_lca is None else left_lca


root = Node(7)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(8)
root.left.left.left = Node(1)
root.left.left.right = Node(6)

node1 = 6
node2 = 5

# check both nodes are present in tree
if not find_node(root, node1) or not find_node(root, node2):
    print ("Given nodes are not present")
else:
    print("LCA(", node1, ", ", node2, " = ", find_lca(root, node1, node2).data, ")", sep = "")
