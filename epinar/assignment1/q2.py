class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, head):
        self.size = 1
        new_node = Node(head)
        self.curr, self.head = new_node, new_node

    def add(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            self.curr.next = new_node

        self.curr = new_node
        self.size += 1

        return True

    def print(self):
        ll = []
        node = self.head
        while node:
            # print(node.data)
            ll.append(node.data)
            node = node.next
        return ll

    def last_kth(self, k):

        stop = self.head
        get = self.head
        for i in range(k):
            if stop is None:
                return None
            stop = stop.next

        while stop.next:
            get = get.next
            stop = stop.next

        return get.data


def main():
    ll = LinkedList(5)
    ll.add(6)
    ll.add(7)
    ll.add(8)
    ll.add(12)
    ll.print()
    k = 4
    print(ll.print())
    print("Last {}th element:{}".format(k, ll.last_kth(k)))


if __name__ == '__main__':
    main()
