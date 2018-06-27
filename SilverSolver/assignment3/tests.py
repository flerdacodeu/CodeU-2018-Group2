import unittest
from dictionary import *
from word_search import *

class TestDict(unittest.TestCase):

    def test_0(self):
        root = Dictionary()
        self.assertEqual(root.isPrefixOrWord('hackathon'), (False, False))
        self.assertEqual(root.isPrefixOrWord(''), (True, False))
        
    def test_1(self):
        root = Dictionary(iterable=["hackathon", "hack"])

        self.assertEqual(root.isPrefixOrWord('hac'), (True, False))
        self.assertEqual(root.isPrefixOrWord('hack'), (True, True))
        self.assertEqual(root.isPrefixOrWord('hackathon'), (True, True))
        self.assertEqual(root.isPrefixOrWord('ha'), (True, False))
        self.assertEqual(root.isPrefixOrWord('hammer'), (False, False))
 
class TestWordSearch(unittest.TestCase):

    def test_0(self):
        self.assertEqual(word_search([], Dictionary()), set())
        self.assertEqual(word_search([[]], Dictionary()), set())
        self.assertEqual(word_search([["a"]], Dictionary()), set())

    def test_1(self):
        self.assertEqual(word_search([["a"]], \
                         Dictionary(iterable=["a"])), \
                         {'a'})
        self.assertEqual(word_search([["a", "a", "r"], ["t", "c", "d"]], \
                         Dictionary(iterable=["car", "card", "cart", "cat"])), \
			 {'car', 'card', 'cat'})
if __name__ == '__main__':
    unittest.main()
