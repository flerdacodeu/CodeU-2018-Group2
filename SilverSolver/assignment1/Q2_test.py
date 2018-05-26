import unittest
from Q2 import *

class TestQ2(unittest.TestCase):

    def test_1(self):
        test_node = from_iterable([i for i in range(5)])

        self.assertEqual(return_k_th_from_end_element(0, test_node), 0)
        self.assertEqual(return_k_th_from_end_element(4, test_node), 4)
        self.assertRaises(IndexError, return_k_th_from_end_element,  6, test_node)
        self.assertRaises(IndexError, return_k_th_from_end_element, -1, test_node)

    def test_2(self):
        test_node = single_linked_node("Node_value", None)
        self.assertRaises(IndexError, return_k_th_from_end_element,  6, test_node)
        self.assertEqual(return_k_th_from_end_element(0, test_node), "Node_value")

if __name__ == '__main__':
    unittest.main()
