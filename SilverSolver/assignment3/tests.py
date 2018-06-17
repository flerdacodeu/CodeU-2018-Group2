import unittest
from dictionary import *

class TestDict(unittest.TestCase):

    def test_0(self):
        root = Dictionary()
        self.assertEqual(root.isPrefixOrWord('hackathon'), (False, False))
        self.assertEqual(root.isPrefixOrWord(''), (False, False))
        
    def test_1(self):
        root = Dictionary(iterable=["hackathon", "hack"])

        self.assertEqual(root.isPrefixOrWord('hac'), (True, False))
        self.assertEqual(root.isPrefixOrWord('hack'), (True, True))
        self.assertEqual(root.isPrefixOrWord('hackathon'), (True, True))
        self.assertEqual(root.isPrefixOrWord('ha'), (True, False))
        self.assertEqual(root.isPrefixOrWord('hammer'), (False, False))

if __name__ == '__main__':
    unittest.main()
