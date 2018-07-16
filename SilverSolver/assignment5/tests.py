import unittest
from unknown_alphabet import *

class TestUnknownAlphabet(unittest.TestCase):

    def test_0(self):
        self.assertEqual(unknown_alphabet([]), [])

    def test_1(self):
        self.assertEqual(unknown_alphabet(["a"]), ["a"])
        self.assertEqual(unknown_alphabet(["1", "2", "3"]), ["1", "2", "3"])
        self.assertFalse(unknown_alphabet(["1", "2", "3", "2"]))

    def test_2(self):
        self.assertEqual(unknown_alphabet(["1a", "1b", "a1", "ab"]), ["1", "a", "b"])

    def test_3(self):
        self.assertTrue(unknown_alphabet(["ART", "RAT", "CAT", "CAR"]) == ["A", "T", "R", "C"] or
                        unknown_alphabet(["ART", "RAT", "CAT", "CAR"]) == ["T", "A", "R", "C"])

if __name__ == '__main__':
    unittest.main()
