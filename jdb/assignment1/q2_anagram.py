from collections import Counter
import re


def _normalize(s, case_sensitive=True):
  if not case_sensitive:
    s = s.lower()
  return [Counter(word) for word in sorted(re.split('\W+', s))]

def is_anagram(a, b, case_sensitive=True):
  if len(a) != len(b):
    return False
  return _normalize(a, case_sensitive) == _normalize(b, case_sensitive)


# run the unittest with python -m unittest q2_anagrams
import unittest

class TestAnagrams(unittest.TestCase):
  """Tests shamelessly stolen from Laida (thank you!)."""

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
    
