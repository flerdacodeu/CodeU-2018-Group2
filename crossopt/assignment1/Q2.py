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

    def length(self):
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

    # return kth element from end of list
    def getKth(self, k):
        len = self.length()
        if k >= len:
            raise IndexError()

        cnt = self.head
        for i in range(len - k - 1):
            cnt = cnt.next
        return cnt

if __name__ == "__main__":
    list = LinkedList()
    list.insert(5)
    list.insert('dog')
    list.insert(set([1, 2, 3]))
    print("list is {}".format(list))
    for k in range(3):
        print("for k = {}, kth from last element is {}"
              .format(k, list.getKth(k).data))
