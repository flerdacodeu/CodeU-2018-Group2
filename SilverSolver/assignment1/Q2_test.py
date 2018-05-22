import unittest
from Q2 import *

class TestQ2(unittest.TestCase):

    def test_1(self):
        test_list = [single_linked_node(0, None)]
        for i in range(1, 5):
            test_list.append(single_linked_node(i, test_list[-1]))
            # 0 <- 1 <- 2 <- 3 <- 4 for example
            current_node = test_list[-1]
            while (current_node):
                current_node = current_node.child

        self.assertEqual(return_k_th_from_end_element(0, test_list[-1]), 0)
        self.assertEqual(return_k_th_from_end_element(4, test_list[-1]), 4)
        self.assertEqual(return_k_th_from_end_element(5, test_list[-1]), None)
        self.assertEqual(return_k_th_from_end_element(-1, test_list[-1]), None)

    def test_2(self):
        test_node = single_linked_node("Node_value", None)
        self.assertEqual(return_k_th_from_end_element(5, test_node), None)
        self.assertEqual(return_k_th_from_end_element(0, test_node), "Node_value")

if __name__ == '__main__':
    unittest.main()
