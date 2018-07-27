import unittest
from move_cars import *

class TestMoveCars(unittest.TestCase):

    def test_0(self):
        self.assertEqual(return_output([1], [0]), ["Unsolvable"])
        self.assertEqual(return_output([1, 2, 0], [1, 3, 0]), ["Unsolvable"])
        self.assertEqual(return_output([1], [1]), [])
        self.assertEqual(return_output([1, 2, 0], [1, 2, 0]), [])

    def test_1(self):
        self.assertEqual(return_output([1, 0], [0, 1]), ['Move car number 1 from 0 to 1'])
        self.assertEqual(return_output([1, 2, 0], [1, 0, 2]), ['Move car number 2 from 1 to 2'])

if __name__ == '__main__':
    unittest.main()
