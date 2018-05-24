from collections import Counter
import re

def are_words_anagram(s1, s2, case_sensitive=False, return_dicts=False):
    if not case_sensitive:
        s1 = s1.lower()
        s2 = s2.lower()
    s1 = re.sub(r'[\W\s]', '', s1)
    s2 = re.sub(r'[\W\s]', '', s2)

    char_counter_1 = Counter(s1)
    char_counter_2 = Counter(s2)

    if return_dicts:
        return (char_counter_1, char_counter_2)
    else:
        return char_counter_1 == char_counter_2

def are_sentences_anagram(s1, s2, case_sensitive=False):
    s1 = re.sub(r'[\W]', ' ', s1)
    s2 = re.sub(r'[\W]', ' ', s2)
    words1 = s1.split()
    words2 = s2.split()

    if len(words1) != len(words2):
        return False
    else:
        words_1 = []
        words_2 = []
        for i in range(len(words1)):
            w1, w2 = are_words_anagram(words1[i], words2[i], \
                     case_sensitive=case_sensitive, return_dicts=True)
            w1 = frozenset(w1.items())
            w2 = frozenset(w2.items())
            words_1.append(w1)
            words_2.append(w2)

        words_counter_1 = Counter(words_1)
        words_counter_2 = Counter(words_2)

        return words_counter_1 == words_counter_2
