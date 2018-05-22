import unittest
import Q1

class TestQ1(unittest.TestCase):

    def test_words_anagram_0(self):
        self.assertEqual(Q1.are_words_anagram("1", "1"), True)
    def test_words_anagram_1(self):
        self.assertEqual(Q1.are_words_anagram("Aba", "baa"), True)
    def test_words_anagram_2(self):
        self.assertEqual(Q1.are_words_anagram("Aba", "baa", case_sensitive=True), False)
    def test_words_anagram_3(self):
        self.assertEqual(Q1.are_words_anagram("", ""), True)

    def test_sentences_anagram_1(self):
        self.assertEqual(Q1.are_sentences_anagram("abc xyz.", "xzy, cba"), True)
    def test_sentences_anagram_2(self):
        self.assertEqual(Q1.are_sentences_anagram("abc zyz.", "xzy, cba"), False)
    def test_sentences_anagram_3(self):
        self.assertEqual(Q1.are_sentences_anagram("", ""), True)
    def test_sentences_anagram_4(self):
        self.assertEqual(Q1.are_sentences_anagram("word", "drow"), True)
    def test_sentences_anagram_5(self):
        self.assertEqual(Q1.are_sentences_anagram("word word word", "word"), False)
    def test_sentences_anagram_6(self):
        self.assertEqual(Q1.are_sentences_anagram("1 1 1", "1 1 1"), True)

if __name__ == '__main__':
    unittest.main()
