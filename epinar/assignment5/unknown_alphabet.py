#!/usr/bin/env python3

class GraphNode:

	def __init__(self, v):
		self.value = v
		self.indegree = 0
		self.edges = set()
		self.is_visited = False

	def add_edge(self, w):
		self.edges.add(w)
		w.indegree += 1


class WordGraph:

	def __init__(self, dictionary):
		letters = set()
		for word in dictionary:
			letters = letters.union(word)

		self.nodes = {alpha: GraphNode(alpha) for alpha in letters}

		for word1, word2 in zip(dictionary, dictionary[1:]):
			cp = _common_prefix(word1, word2)
			if cp != -1:
				self.nodes[word1[cp]].add_edge(self.nodes[word2[cp]])

	def __iter__(self):
		for node in self.nodes.values():
			yield node


def _topsort1(v, graph, alphabet):
	""" computes topsort of acyclic graph """
	v.is_visited = True
	for u in v.edges:
		if not u.is_visited:
			_topsort1(u, graph, alphabet)
	alphabet.append(v.value)


def find_alphabet(words):
	""" returns any correct alphabet for list of words """
	graph = WordGraph(words)
	alphabet = list()

	for v in graph:
		if not v.is_visited:
			_topsort1(v, graph, alphabet)

	return alphabet[::-1]


def _common_prefix(s1, s2):
	""" given two strings, returns position of first difference or -1 if strings are the same """
	for i in range(min(len(s1), len(s2))):
		if s1[i] != s2[i]:
			return i
	return -1


def _topsort2(graph, alphabets, curr_alphabet):
	""" finds all possible sorts from the graph """
	isDone = False

	for v in graph:
		if not v.is_visited and not v.indegree:
			for u in v.edges:
				u.indegree -= 1

			curr_alphabet.extend(v.value)
			v.is_visited = True
			_topsort2(graph, alphabets, curr_alphabet)

			v.is_visited = False
			curr_alphabet.pop()
			for u in v.edges:
				u.indegree += 1

			isDone = True

	if not isDone:
		alphabets.append(curr_alphabet.copy())


def find_alphabets(words):
	graph = WordGraph(words)
	alphabets = []

	_topsort2(graph, alphabets, [])

	return alphabets


print(find_alphabets(['S', 'ART', 'RAT', 'CAT', 'CAR']))
# print(find_alphabet(["1a", "1b", "a1", "ab"]))
