#!/usr/bin/env python3

from collections import deque
from itertools import combinations


def _common_prefix(s1, s2):
    """ given two strings, returns position of first difference
            or -1 if strings are the same """
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            return i
    return -1


def _make_graph(dictionary):
    """ creates graph of lex order from dictionary """
    alphabet = set()
    for word in dictionary:
        alphabet |= set(word)

    graph = {key: set() for key in alphabet}

    for word1, word2 in zip(dictionary, dictionary[1:]):
        cp = _common_prefix(word1, word2)
        if cp != -1:
            graph[word1[cp]].add(word2[cp])

    return graph


def _is_cycle(v, graph, color):
    """ dfs checking whether cycle exists """
    color[v] = 1
    for u in graph[v]:
        if color[u] == 1:
            return True
        elif not color[u] and _is_cycle(u, graph, color):
            return True
    color[v] = 2
    return False


def _topsort(v, graph, used, order):
    """ computes topsort of acyclic graph """
    used.add(v)
    for u in graph[v]:
        if u not in used:
            _topsort(u, graph, used, order)
    order.append(v)


def _find_cycle(graph, start):
    """ finds shortest cycle from start vertex via bfs """
    prev = dict.fromkeys(graph.keys(), None)
    prev[start] = start
    queue = deque(start)
    while len(queue):
        v = queue.pop()
        for u in graph[v]:
            if prev[u]:
                # found cycle
                cycle = [u]
                while prev[v] != v:
                    cycle.append(v)
                    v = prev[v]
                return cycle
            else:
                prev[u] = v
                queue.appendleft(u)


def is_correct(words):
    """ returns boolean value - whether dictionary is correct """
    graph = _make_graph(words)
    color = dict.fromkeys(graph.keys(), 0)
    for v in graph.keys():
        if not color[v] and _is_cycle(v, graph, color):
            return False
    return True


def find_incorrect(words):
    """ returns minimal proof for incorrect alphabet
        returns list of letters each of which should be before next """
    graph = _make_graph(words)
    shortest_cycle = list(graph.keys()) + [None]  # longer than longest cycle
    for v in graph.keys():
        cycle = _find_cycle(graph, v)
        if cycle and len(cycle) < len(shortest_cycle):
            shortest_cycle = cycle

    return shortest_cycle


def find_one_alphabet(words):
    """ returns any correct alphabet for list of words """
    graph = _make_graph(words)
    used = set()
    order = list()

    for v in graph.keys():
        if v not in used:
            _topsort(v, graph, used, order)

    return order[::-1]


def fix_incorrect(words):
    """ fixes incorrect alphabet by removing minimal amount of words """
    for dict_size in range(len(words), 0, -1):
        for new_dict in combinations(words, dict_size):
            if is_correct(new_dict):
                return list(new_dict)
