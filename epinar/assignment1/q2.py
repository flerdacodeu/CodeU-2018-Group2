
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self, head = None):
		self.head = head
		self.curr = head
		self.size = 1 if head else 0

	def add(self, data):
		new_node = Node(data)
		if self.size == 0 : 
			self.head = new_node
		else:
			self.curr.next = new_node

		self.curr = new_node
		self.size += 1

		return True

	def print(self):
		node = self.head
		while node:
			print(node.data)
			node = node.next

	def lastKth(self, k):

		stop = self.head
		get = self.head
		for i in range(k):
			if stop == None:
				return None
			stop = stop.next

		while stop.next:
			get = get.next
			stop = stop.next

		return get.data

def main():
	n = Node(5)
	list = LinkedList(n)
	list.add(6)
	list.add(7)
	list.add(8)
	list.add(12)
	list.print()
	k = 1
	print("Last {}th element:{}".format(k, list.lastKth(k)))

if __name__ == '__main__':
    main()



