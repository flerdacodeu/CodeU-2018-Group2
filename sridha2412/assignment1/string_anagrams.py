# python program to determine if two strings are anagrams of each other

# assumption: only using the 26 alphabets of the english language
# method to check if two strings are anagrams
# method takes two strings and a boolean value. If true, check case sensitive anagrams else ignore case
def is_anagram(str1, str2, caseSensitive):
    # if ignoring case, convert both strings to lower case
    if not caseSensitive:
        str1 = str1.lower()
        str2 = str2.lower()
    # sort and compare the strings
    return sorted(str1) == sorted(str2)

# assumption: sentence can only include alphabets and spaces
# method to check if two sentences are anagrams
# method takes two sentences and a boolean value. If true, check case sensitive anagrams else ignore case
def is_sentence_anagram(str1, str2, caseSensitive):
    # split sentence into words
    str1 = str1.split(' ')
    str2 = str2.split(' ')
    # check both have equal number of words
    if len(str1) != len(str2):
        return False
    # iterate over both lists
    for i in range(0, len(str1)):
        # check if an anagram exists in second list
        for j in range(0, len(str2)):
            if is_anagram(str1[i], str2[j], caseSensitive):
                # if yes, delete item from list and check for next element
                del(str2[j])
                break
        # check anagram has been found
        if len(str2) != len(str1) - i - 1:
            return False
    return True

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
caseSensitive = input("Enter Y if case sensitive else N: ")
# default value is False
caseSensitive = True if caseSensitive == 'Y' else False

is_it_or_not = 'NOT ' if not is_sentence_anagram(str1, str2, caseSensitive) else ''
print('"' + str1 + '" and "' + str2 + '" are ' + is_it_or_not + 'anagrams')
