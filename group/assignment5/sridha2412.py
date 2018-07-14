from typing import List, Tuple

def common_prefix(word1: str, word2: str) -> int:
    """ A method to find the common prefix in two words and return the end position
    Args:
        word1: first word
        word2: second word
    Returns:
        int: position end of common prefix
    """

    for i in range(0, min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            break
    return i


def create_DAG(words: List[str]) -> dict:
    """ A method to create a direct acyclic graph from a list of words
    Args:
        words: list of words e.g ['ART', 'RAT', 'CAT', 'CAR']
    Returns:
        dict: a DAG e.g. {'A': [R], 'R': ['C'], 'C', 'T': ['R']}
    """

    alphabets = set()
    for word in words:
        alphabets = alphabets.union(word)

    graph = {alpha: {"set": set(), "visited": False} for alpha in alphabets}

    for word1, word2 in zip(words, words[1:]):
        cp = common_prefix(word1, word2)
        if(word1[cp] != word2[cp]):
            graph[word1[cp]]["set"].add(word2[cp])

    return graph

def _topological_sort(alpha: str, alphabets: List[str], graph: dict):
    """ A recursive method to topologically sort a graph
    Args:
        alpha: character to check all outgoing nodes for
        alphabets: list to store order of alphabets
        graph: a DAG with all the graph vertices
    """
    graph[alpha]["visited"] = True

    for char in graph[alpha]["set"]:
        if not graph[char]["visited"]:
            _topological_sort(char, alphabets, graph)

    alphabets.insert(0, alpha)

def find_alphabets(words: str) -> List[str]:
    """ A method to find order of alphabets of unknown language using topological sort
    Args:
        words: list of words
    Returns:
        List[str]: list of order of alphabets
    """

    alphabets = []

    graph = create_DAG(words)
    for char in graph:
        if not graph[char]["visited"]:
            _topological_sort(char, alphabets, graph)

    return alphabets

print(find_alphabets(['ART', 'RAT', 'CAT', 'CAR']))
