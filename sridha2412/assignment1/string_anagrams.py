# python program to determine if two strings are anagrams of each other

# assumption: only using the 26 alphabets of the english language

# method to check if two strings are anagrams
# method takes two strings and a boolean value. If true, check case sensitive anagrams else ignore case
def isAnagram(str1, str2, caseSensitive):
    # if ignoring case, convert both strings to lower case
    if not caseSensitive:
        str1 = str1.lower()
        str2 = str2.lower()
    # sort and compare the strings
    return sorted(str1) == sorted(str2)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
caseSensitive = input("Enter Y if check case sensitive anagram else N: ")
# default value is False
caseSensitive = True if caseSensitive == 'Y' else False

if isAnagram(str1, str2, caseSensitive):
    print("\""+str1+"\" and \""+str2+"\" are anagrams")
else:
    print("\""+str1+"\" and \""+str2+"\" are NOT anagrams")
