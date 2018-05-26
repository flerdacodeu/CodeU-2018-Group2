# python program to find the k-th to last element of a singly linked list

# node class
class Node:
    # constructor to initialize a node object
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list class
class LinkedList:
    # initialize head
    def __init__(self):
        self.head = None

    # method to insert a new node
    def push(self, new_data):
        # create new node with new data
        new_node = Node(new_data)
        # node points to the next node
        new_node.next = self.head
        # head is now new node
        self.head = new_node

    # find kth to last element of LinkedList
    def findKthElement(self, k):
        # store length of LinkedList = number of nodes
        list_len = 0
        # temporary node for traversal
        temp = self.head
        # count number of nodes in LinkedList
        while(temp!=None):
            # increment length
            list_len += 1
            # go to next node
            temp = temp.next

        # check if k is less than lenght of LinkedList
        if k >= list_len:
            print("Given k =", k, "should be less than length of linked list =", list_len)
            return

        temp = self.head
        # get the (length - k)th element from the beginning
        for i in range(0, (list_len - k - 1)):
            temp = temp.next
        print(k,"th to the last element: ",temp.data, sep="")
#
# ll = LinkedList()
# ll.push(12)
# ll.push(123)
# ll.push(1)
# ll.push(2)
# ll.findKthElement(0)
