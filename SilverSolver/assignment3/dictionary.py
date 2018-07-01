from typing import Tuple

class Dictionary:
    
    def __init__(self, first_char='*', iterable=None):
        self.char = first_char
        self.children = {}
        self.word_finished = False
        if iterable:
            for word in iterable:
                self.add(word)
    
    def add(self, word: str):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Dictionary()
            node = node.children[char]
        node.word_finished = True

    def isPrefixOrWord(self, prefix: str) -> Tuple[bool, bool]:
        # This helper function returns tuple with meaning (isWord, isPrefix)
        node = self
        for char in prefix:
            if char not in node.children:
                return False, False
            node = node.children[char]
        return True, node.word_finished

    def isWord(self, word: str) -> bool:
        return self.isPrefixOrWord(word)[1]

    def isPrefix(self, prefix: str) -> bool:
        return self.isPrefixOrWord(prefix)[0]

