from collections import defaultdict

def dfs(ordered_vertices, edges, color, v):
    if color[v] == 1:
        return (ordered_vertices, None)
    if color[v] == 2:
        return (ordered_vertices, color)
    color[v] = 1
    if v in edges.keys():
        for v_ in edges[v]:
            ordered_vertices, color = dfs(ordered_vertices, edges, color, v_)
            if v_ in edges.keys() and color == None:
                return (ordered_vertices, None)
    ordered_vertices.append(v)
    color[v] = 2
    return (ordered_vertices, color)

def topological_sort(edges, symbols):
    ordered_vertices = []
    N = len(symbols)
    color = dict()
    for v in symbols:
        color[v] = 0
    for v in symbols:
        ordered_vertices, color = dfs(ordered_vertices, edges, color, v)
        if color == None:
            return False # False if there is no correct alphabet possible
    residual_symbols = list(symbols.difference(set(ordered_vertices)))
    ordered_vertices.extend(residual_symbols)
    return ordered_vertices[::-1]

def unknown_alphabet(dictionary):
    if len(dictionary) < 1:
        return []
    edges = defaultdict(set)
    symbols = set()
    symbols.update(dictionary[0])

    for w1, w2 in zip(dictionary[:-1], dictionary[1:]):
        for i in range(min(len(w1), len(w2))):
            symbols.add(w1[i])
            if w1[i] != w2[i]:
                edges[w1[i]].add(w2[i])
                symbols.add(w2[i])
                break
        symbols.update(w2)

    alphabet = topological_sort(edges, symbols)
    return alphabet
