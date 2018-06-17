from typing import Tuple

class Dictionary:
    """
    I used some code from here to implement the trie -
    https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
    then modified it for my purposes
    """
    
    def __init__(self, first_char='*', iterable=None):
        self.char = first_char
        self.children = []
        self.word_finished = False
        if iterable:
            for word in iterable:
                self.add(word)
    
    def add(self, word: str):
        node = self
        for char in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid
            if not found_in_child:
                new_node = Dictionary(char)
                node.children.append(new_node)
                node = new_node
        node.word_finished = True

    def isPrefixOrWord(self, prefix: str) -> Tuple[bool, bool]:
        # This helper function returns tuple with meaning (isWord, isPrefix)
        node = self
        # If the self node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        if not self.children:
            return False, False
        for char in prefix:
            char_not_found = True
            # Search through all the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found the char existing in the child.
                    char_not_found = False
                    node = child
                    break
            # Return False anyway when we did not find a char.
            if char_not_found:
                return False, False
        return True, node.word_finished

    def isWord(self, word: str) -> bool:
        return self.isPrefixOrWord(word)[1]

    def isPrefix(self, prefix: str) -> bool:
        return self.isPrefixOrWord(prefix)[0]

