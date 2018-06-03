# python program to determine if two strings are anagrams of each other

# assumption: only using the 26 alphabets of the english language, sentence only uses alphabets and spaces
# method to split and sort words and change case if required
def sort(str, caseSensitive):
    if not caseSensitive:
        str = str.lower()
    return sorted(sorted(list(word)) for i, word in enumerate(str.split(' ')))

# method to check if two given strings are anagrams
def is_anagram(str1, str2, caseSensitive):
    return sort(str1, caseSensitive) == sort(str2, caseSensitive)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
caseSensitive = input("Enter Y if case sensitive else N: ")
# default value is False
caseSensitive = True if caseSensitive == 'Y' else False

is_it_or_not = 'NOT ' if not is_anagram(str1, str2, caseSensitive) else ''
print('"' + str1 + '" and "' + str2 + '" are ' + is_it_or_not + 'anagrams')
