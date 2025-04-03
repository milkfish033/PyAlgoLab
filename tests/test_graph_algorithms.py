# tests/test_graph_algorithms.py

from pyalgolab import graph_algorithms

def test_dijkstra():
    G = {0: [(1,1)], 1: [(1,2)], 2: []}
    dist, _ = graph_algorithms.dijkstra(G, 0)
    assert dist[2] == 2

def test_prim():
    G = {0: [(1,1)], 1: [(1,2)], 2: []}
    parent = graph_algorithms.prim(G, 0)
    assert parent[1] == 0
