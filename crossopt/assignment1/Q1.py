#!/usr/bin/env python3
# coding: utf-8
from re import split


# countsorts elements in container, elements must be hashable
def countSort(container):
    count = dict()
    for i in container:
        count[i] = count.get(i, 0) + 1
    return count


# checks whether strings are anagrams
def isStringAnagram(str1, str2, caseSensitive=False):
    if not caseSensitive:
        str1 = str1.lower()
        str2 = str2.lower()

    return countSort(str1) == countSort(str2)


# checks whether sentences are anagrams. Punctuation is ignored
def isSentenceAnagram(str1, str2, caseSensitive=False):
    if not caseSensitive:
        str1 = str1.lower()
        str2 = str2.lower()

    punctuation = '[! "#$%&()*+,\./:;<=>?@[\\]^`{|}~]'
    # get list of words in sentence
    words1 = [word for word in split(punctuation, str1) if word]
    # replace all words with their CountSort, make it hashable
    words1 = [(tuple(sorted(countSort(word).items()))) for word in words1]
    words2 = [word for word in split(punctuation, str2) if word]
    words2 = [(tuple(sorted(countSort(word).items()))) for word in words2]

    return countSort(words1) == countSort(words2)


if __name__ == "__main__":
    str1 = "triangle"
    str2 = "Integral"
    assert not isStringAnagram(str1, str2, 1)
    assert isStringAnagram(str1, str2)

    str1 = "посеять: клоповник"
    str2 = "полковник опьется"
    assert isSentenceAnagram(str1, str2, 1)
    assert isSentenceAnagram(str1, str2, 0)
