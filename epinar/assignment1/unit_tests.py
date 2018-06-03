import unittest
from q2 import *
from q1 import *


def from_list_(list_):
	ll = LinkedList(list_[0])
	for v in list_[1:]:
		ll.add(v)
	return ll


class TestLinkedList(unittest.TestCase):

	# Takes a list and constructs LinkedList

	def test_construct_iter(self):
		list_ = [1, 2, 3, 4, 5, 6, 6]
		self.assertEqual(from_list_(list_).print(), list_)

	def test_len(self):
		"""len() of a LinkedList must be equal to the len of the input list."""
		# for 2 sample lists, I test that the len of the list is the len
		# of the LinkedList that is constructed with the list.
		l1 = [1]
		self.assertEqual(len(from_list_(l1).print()), len(l1))
		l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
		self.assertEqual(len(from_list_(l2).print()), len(l2))

	def test_get_negative_k(self):
		ll = from_list_(range(-10, 0))
		for v in range(-10, 0):
			val = ll.last_kth(-v - 1)
			self.assertEqual(val, v)


class TestAnagram(unittest.TestCase):

	def test_word(self):
		self.assertTrue(isAnagram("banana", "nanaba", False))
		self.assertTrue(isAnagram("BaNana", "NaBana", True))
		self.assertFalse(isAnagram("apple", "elapa", False))
		self.assertFalse(isAnagram("oRaNge", "oarNge", True))

	def test_sentence(self):
		self.assertTrue(isAnagram("hello world", "rowld lehlo", False))
		self.assertTrue(isAnagram("Google CodeU", "gooGle UedoC", True))
		self.assertFalse(isAnagram("python test", "thypo sett", False))
		self.assertFalse(isAnagram("UnIt TeSt", "uNiT seTT", True))
