# tests/test_graph_traversal.py

from pyalgolab import graph_traversal

def test_bfs():
    G = {0: [1,2], 1: [3], 2: [3], 3: []}
    T = graph_traversal.bfs(G, 0)
    assert 0 in T and 1 in T[0] and 2 in T[0]

def test_dfs():
    G = {0: [1,2], 1: [3], 2: [3], 3: []}
    T = graph_traversal.dfs(G, 0)
    assert 0 in T
