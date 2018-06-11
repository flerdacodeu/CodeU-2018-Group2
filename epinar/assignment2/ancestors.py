class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Initiates a tree with an input value. Keeps the nodes in a dictionary for fast reach.
# Each data(key) value should be unique.
class BinaryTree:
	def __init__(self, data):
		self.tree = {}
		node = TreeNode(data)
		self.head = node
		self.tree[data] = node
		self.a =[] # shared variable between classes
	# We assume that parent node exists and the right/left child is free.
	def add_left(self, parent, data):
		p = self.tree[parent]
		node = TreeNode(data)
		p.left = node
		self.tree[data] = node
	def add_right(self, parent, data):
		p = self.tree[parent]
		node = TreeNode(data)
		p.right = node
		self.tree[data] = node

	# Prints in dictionary order.
	def print_dict(self):
		for k, v in self.tree.items():
			print("node: ", v.data)
			if v.right:
				print(" r: ", v.right.data)
			if v.left:
				print(" l: ", v.left.data)

	# Prints the tree in order.
	def print(self):
		self._print(self.head)

	def _print(self, curr):
		if not curr:
			return
		print(curr.data)
		self._print(curr.left)
		self._print(curr.right)

	# Returns the ancestors ordered from lowest to highest in tree.
	def ancestors(self, data):
		self.a = []
		if self._ancestors(self.head, data):
			return self.a
		else:
			self.a = []

	def _ancestors(self, root, data):
		if root is None:
			return False

		if root.data is data:
			return True

		if self._ancestors(root.right, data) or self._ancestors(root.left, data):
			self.a.append(root.data)
			return True

	# Compares the ancestors of two nodes starting from the end.
	def common_ancestors(self, data1, data2):
		a1 = self.ancestors(data1)
		a2 = self.ancestors(data2)
		ca = a1[-1]
		while len(a1) > 0 and len(a2) > 0:
			if a1[-1] == a2[-1]:
				ca = a1[-1]
				a1 = a1[:-1]
				a2 = a2[:-1]
			else:
				return ca
		return ca

	# Recursively iterates on the tree until it reaches to query nodes,
	# while keeping track of their closest common parents.
	def common_ancestors2(self, data1, data2):
		return self._common_ancestors(self.head, data1, data2).data

	def _common_ancestors(self, root, data1, data2):
		if root is None:
			return None
		if root.data is data1 or root.data is data2:
			return root

		left = self._common_ancestors(root.left, data1, data2)
		right = self._common_ancestors(root.right, data1, data2)

		if left and right:
			return root
		if left:
			return left
		else:
			return right

def main():
	t = BinaryTree(5)
	t.add_left(5, 3)
	t.add_left(3, 2)
	t.add_right(5, 4)
	t.add_right(3, 6)
	t.print()
	print(t.common_ancestors2(2, 6))


if __name__ == '__main__':
	main()
