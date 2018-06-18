#!/usr/bin/env python3


class _DictionaryNode:
    def __init__(self):
        self.children = dict()
        self.is_terminal = False

    def add(self, letter):
        if letter not in self.children:
            self.children[letter] = _DictionaryNode()


# stores dictionary as Trie of DictionaryNodes
# addWord, isPrefix, isWord are O(len(word))
class Dictionary:
    def __init__(self, word_list=[]):
        self.root = _DictionaryNode()
        for word in word_list:
            self.addWord(word)

    def addWord(self, word):
        cnt = self.root
        for letter in word:
            cnt.add(letter)
            cnt = cnt.children[letter]
        cnt.is_terminal = True

    def isPrefix(self, prefix):
        cnt = self.root
        for letter in prefix:
            if letter not in cnt.children:
                return False
            cnt = cnt.children[letter]
        return True

    def isWord(self, word):
        cnt = self.root
        for letter in word:
            if letter not in cnt.children:
                return False
            cnt = cnt.children[letter]
        return cnt.is_terminal
