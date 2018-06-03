def normalize(s, caseSensitive=True):
    if not caseSensitive:
        s = s.lower()

    s = s.split(' ')

    s = [sorted(list(v)) for v in s]

    return sorted(s)


def isAnagram(str1, str2, caseSensitive=True):

    return normalize(str1, caseSensitive) == normalize(str2, caseSensitive)

def main():
    str1 = 'triangle'
    str2 = 'integraL'
    print(isAnagram(str1, str2, False))
    sent1 = 'ana baba'
    sent2 = 'baaB aan'
    print(isAnagram(sent1, sent2))


if __name__ == '__main__':
    main()
