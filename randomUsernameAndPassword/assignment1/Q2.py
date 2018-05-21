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

  def get_next(self):
    return self.next

  def get_data(self):
    return self.data

def get_kth_last(head, k):
  if (head == None or k < 0):
    return None
  
  elem = head
  counter = 0
  
  while (elem is not None):
    counter += 1
    elem = elem.get_next()
  
  if counter <= k:
      return None
  
  dist = counter - k - 1
  elem = head
  for i in range(0, dist):
      elem = elem.get_next()
  
  return elem.get_data()


class TestKthLastElement(unittest.TestCase):
    
    def test(self):
        list = Node([4, 2, 5, 6, 9, 8])
        self.assertEqual(get_kth_last(list, 2), 6)
        self.assertEqual(get_kth_last(list, 0), 8)
        self.assertNotEqual(get_kth_last(list, 1), 8)
        self.assertIsNone(get_kth_last(list, 10))
        self.assertIsNone(get_kth_last(list, -1))
        

if __name__ == "__main__":
    unittest.main()

