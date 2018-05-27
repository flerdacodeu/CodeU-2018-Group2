class Node:
  def __init__(self, value=None):
    self.value, self.next = value, None

# This implementation uses the iterator a lot, it is not better in
# terms of complexity:
# pros: shorter methods, more consistent with other Python containers list, dicts...
# cons: confusing to the reader unfamiliar with iterators
#
# resource on Python's iterators:
# https://www.programiz.com/python-programming/iterator
# http://www.diveintopython3.net/iterators.html

class LinkedList:
  def __init__(self, original_list):
    # __init__ loops over the input list: O(n)
    current = self.head = Node(original_list[0])
    for value in original_list[1:]:
      current.next = Node(value)
      current = current.next

  def __iter__(self):
    # - iter returns a interator object in constant time.
    # - then the caller of the iterator can call 'next()'
    #   and next will returns each Node, and once exhausted
    #   the iterator will raise a StopIteration exception.
    #
    # When using the for loop over an iterable, __iter__
    # then __next__ are called automatically (these steps
    # are called the iterator protocol).
    current = self.head
    while current:
      yield current
      current = current.next

  def __len__(self):
    # enumerate returns an iterator immediately, and the for
    # loop will call next() on the the enumerate iterator until
    # exhausted. You can call next on an enumerate iterator as
    # many times as there are elements in the iterator provided
    # to enumerate. __iter__ will yields the n elements, so enumerate
    # will also return n elements. __len__ is in O(n).
    for index, _ in enumerate(self): pass
    return index + 1

  def __getitem__(self, k):
    if k < 0:
      return self[len(self) + k]  # O(n) due to len()
    else:
      for index, node in enumerate(self):  # O(n) due to __iter__
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
