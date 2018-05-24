import unittest

def sort_characters(words):
    
    words = words.split(" ")
    words = sorted([''.join(sorted(i)) for i in words])
    
    return words
    

def is_anagram(str1, str2, case_sensitive):
    
    if not case_sensitive:
        str1.lower()
        str2.lower()
    
    str1 = sort_characters(str1)
    str2 = sort_characters(str2)
    
    return str1 == str2

class TestAnagram(unittest.TestCase):
    
    def test_word(self):
        self.assertTrue(is_anagram("banana", "nanaba", False))
        self.assertTrue(is_anagram("BaNana", "NaBana", True))
        self.assertFalse(is_anagram("apple", "elapa", False))
        self.assertFalse(is_anagram("oRaNge", "oarNge", True))
    
    def test_sentence(self):
        self.assertTrue(is_anagram("hello world", "rowld lehlo", False))
        self.assertTrue(is_anagram("Google CodeU", "gooGle UedoC", True))
        self.assertFalse(is_anagram("python test", "thypo sett", False))
        self.assertFalse(is_anagram("UnIt TeSt", "uNiT seTT", True))
    
if __name__ == '__main__':
    unittest.main()
