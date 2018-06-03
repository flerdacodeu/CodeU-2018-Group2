# print ancestors of given key in a binary tree

# node class`
class Node:
    # constuctor to initlalize a node object
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# if key is present, print ancestors else return false
def print_ancestors(root, key):
    # base case
    if root is None:
        return False

    if root.data == key:
        return True

    # search for key in left and right subtrees
    if print_ancestors(root.left, key) or print_ancestors(root.right, key) :
        print (root.data, end = " ")
        return True

    return False


root = Node(7)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(8)
root.left.left.left = Node(1)
root.left.left.right = Node(6)
print_ancestors(root, 10)
