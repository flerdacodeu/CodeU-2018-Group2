class Node:
  def __init__(self, value=None):
    self.value, self.next = value, None


class LinkedList:
  def __init__(self, original_list):
    current = self.head = Node(original_list[0])
    for value in original_list[1:]:
      current.next = Node(value)
      current = current.next

  def __iter__(self):
    current = self.head
    while current:
      yield current
      current = current.next

  def __len__(self):
    for index, _ in enumerate(self): pass
    return index + 1

  def __getitem__(self, k):
    if k < 0:
      return self[len(self) + k]
    else:
      for index, node in enumerate(self):
        if index == k:
          return node
      else:
        raise IndexError('LinkedList only has %s elements, no %sth element'
                         % (index + 1, k))

# run the unittest with python -m unittest ex1-1-linkedlist
import unittest

class TestLinkedList(unittest.TestCase):

  def test_construct_iter(self):
    list_ = [1,2,3,4,5,6,6]
    self.assertEqual([n.value for n in LinkedList(list_)], list_)

  def test_len(self):
    """len() of a LinkedList must be equal to the len of the input list."""
    # for 2 sample lists, I test that the len of the list is the len
    # of the LinkedList that is constructed with the list.
    l1 = [1]
    self.assertEqual(len(LinkedList(l1)), len(l1))
    l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    self.assertEqual(len(LinkedList(l2)), len(l2))
       

  def test_forward(self):
    ll = LinkedList(range(10))
    for index_value in range(10):
      self.assertEqual(ll[index_value].value, index_value)

  def test_get_negative_k(self):
    ll = LinkedList(range(-10, 0))
    for v in range(-10, 0):
      self.assertEqual(ll[v].value, v)

  def test_None_is_an_acceptable_value(self):
    ll = LinkedList([1, None, 2])
