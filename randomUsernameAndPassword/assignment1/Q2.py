import unittest

class Node:
  
    def __init__(self, values):
        assert(values)
        head, tail = values[0], values[1:]
        self.data = head
        if tail:
            self.next = Node(tail)
        else:
            self.next = None
            
    def __getitem__(self, index):
        length = len(self)
        if (index >= length or index < -length):
            raise IndexError()
        if (index < 0):
            index = index + length
        
        elem = self
        for i in range(index):
            elem = elem.next
        return elem
            
    def __len__(self):
        counter = 0
        elem = self
        while (elem is not None):
            counter += 1
            elem = elem.next
        
        return counter


def get_kth_last(head, k):
    if (head == None or k < 0 or len(head) <= k):
        raise IndexError()
  
    index = (-k) - 1 
    return head[index].data


class TestKthLastElement(unittest.TestCase):
    
    def test(self):
        list = Node([4, 2, 5, 6, 9, 8])
        self.assertEqual(get_kth_last(list, 2), 6)
        self.assertEqual(get_kth_last(list, 0), 8)
        self.assertNotEqual(get_kth_last(list, 1), 8)
        with self.assertRaises(IndexError):
            get_kth_last(list, 10)
        with self.assertRaises(IndexError):
            get_kth_last(list, -1)
        

if __name__ == "__main__":
    unittest.main()
