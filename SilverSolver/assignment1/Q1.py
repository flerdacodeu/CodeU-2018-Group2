def are_words_anagram(s1, s2, case_sensitive=False, return_dicts=False):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if not case_sensitive:
        s1 = s1.lower()
        s2 = s2.lower()
    else:
        alphabet += alphabet.upper()
    alphabet += "0123456789"
    s1 = s1.strip()         # Ignoring spaces
    s2 = s2.strip()

    char_counter_1 = dict.fromkeys(list(alphabet), 0)
    char_counter_2 = char_counter_1.copy()
    for c in s1:
        if c in char_counter_1.keys():
            char_counter_1[c] += 1
    for c in s2:
        if c in char_counter_2.keys():
            char_counter_2[c] += 1

    if return_dicts:
        return (char_counter_1, char_counter_2)
    else:
        return char_counter_1 == char_counter_2

def are_sentences_anagram(s1, s2, case_sensitive=False):
    s1 = s1.strip()
    s2 = s2.strip()
    words1 = s1.split()
    words2 = s2.split()
    if len(words1) != len(words2):
        return False
    else:
        words_counter_1 = dict()
        words_counter_2 = dict()
        for i in range(len(words1)):
            w1, w2 = are_words_anagram(words1[i], words2[i], \
                     case_sensitive=case_sensitive, return_dicts=True)
            w1 = frozenset(w1.items())
            w2 = frozenset(w2.items())
            if w1 not in words_counter_1.keys():
                words_counter_1[w1] = 1
            else:
                words_counter_1[w1] += 1
            if w2 not in words_counter_2.keys():
                words_counter_2[w2] = 1
            else:
                words_counter_2[w2] += 1
        return words_counter_1 == words_counter_2
