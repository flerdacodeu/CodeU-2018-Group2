#!/usr/bin/env python3
# coding: utf-8
from re import split
from collections import Counter


# return hashable count of elements
def hashCount(container):
    return tuple(sorted(Counter(container).items()))


# checks whether strings are anagrams
def isStringAnagram(str1, str2, case_sensitive=False):
    if not case_sensitive:
        str1 = str1.lower()
        str2 = str2.lower()

    return Counter(str1) == Counter(str2)


# checks whether sentences are anagrams. Punctuation is ignored
def isSentenceAnagram(str1, str2, case_sensitive=False):
    if not case_sensitive:
        str1 = str1.lower()
        str2 = str2.lower()

    # TODO - figure out apostrophes
    # get list of words, replace all words with their count, make it hashable
    words1 = [hashCount(word) for word in split('\W', str1) if word]
    words2 = [hashCount(word) for word in split('\W', str2) if word]
    return Counter(words1) == Counter(words2)


if __name__ == "__main__":
    str1 = "triangle"
    str2 = "Integral"
    assert not isStringAnagram(str1, str2, 1)
    assert isStringAnagram(str1, str2)

    str1 = "посеять: клоповник"
    str2 = "полковник опьется"
    assert isSentenceAnagram(str1, str2, 1)
    assert isSentenceAnagram(str1, str2, 0)
