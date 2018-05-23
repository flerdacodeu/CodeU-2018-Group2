
def isAnagram(str1, str2, caseSensitive = False):
	if not caseSensitive:
		str1 = str1.lower()
		str2 = str2.lower()

	return (sorted(list(str1)) == sorted(list(str2)))

def isSentenceAnagram(sent1, sent2):
	sent1 = sent1.split(' ')
	sent2 = sent2.split(' ')

	for i,v in enumerate(sent1):
		sent1[i] = sorted(list(v))

	for i,v in enumerate(sent2):
		sent2[i] = sorted(list(v))

	return sorted(sent1) == sorted(sent2)

def main():
	str1 = 'triangle'
	str2 = 'integraL'
	print(isAnagram(str1, str2, True))
	sent1 = 'ana baba'
	sent2 = 'baab aan'
	print(isSentenceAnagram(sent1, sent2))

if __name__ == '__main__':
    main()
