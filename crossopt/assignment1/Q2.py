#!/usr/bin/env python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # adds element to front of list
    def insert(self, new_elem):
        new_node = Node(new_elem)
        new_node.next = self.head
        self.head = new_node

    def __len__(self):
        ans = 0
        cnt = self.head
        while cnt:
            ans += 1
            cnt = cnt.next
        return ans

    def __str__(self):
        ans = []
        cnt = self.head
        while cnt:
            ans.append(str(cnt.data))
            cnt = cnt.next
        return "{" + ", ".join(ans) + "}"

    # list[-k] returns kth element from end of list, last element is -1
    def __getitem__(self, k):
        length = len(self)

        if k >= 0:
            raise NotImplementedError()
        elif k < -length:
            raise IndexError()

        cnt = self.head
        for i in range(length + k):
            cnt = cnt.next
        return cnt

if __name__ == "__main__":
    list = LinkedList()
    list.insert(5)
    list.insert('dog')
    list.insert(set([1, 2, 3]))
    print("list is {}".format(list))
    for k in range(1, 4):
        print("for k = {}, kth from last element is {}"
              .format(k, list[-k].data))
