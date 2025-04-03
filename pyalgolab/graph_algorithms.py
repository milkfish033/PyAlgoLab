# pyalgolab/graph_algorithms.py
"""
Graph Algorithms: Dijkstra, Prim, Kruskal, Bellman-Ford, Ford-Fulkerson
"""

from typing import Dict, List, Tuple
import numpy as np
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class TupleMinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2

    def _swap(self, i, j): self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i):
        while i > 0 and self.heap[i][0] < self.heap[self._parent(i)][0]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _heapify_down(self, i):
        smallest = i
        left, right = self._left(i), self._right(i)
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != i:
            self._swap(i, smallest)
            self._heapify_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        min_value = self.heap[0]
        self._swap(0, -1)
        self.heap.pop()
        self._heapify_down(0)
        return min_value

    def get(self): return self.heap

def dijkstra(G: Dict[int, List[Tuple[int, int]]], s: int):
    n = len(G)
    distances = [np.inf] * n
    parents = [None] * n
    visited = [False] * n
    heap = TupleMinHeap()
    heap.insert((0, s))
    distances[s] = 0

    while heap.get():
        dist, u = heap.extract_min()
        if visited[u]: continue
        visited[u] = True
        for weight, v in G[u]:
            if not visited[v] and dist + weight < distances[v]:
                distances[v] = dist + weight
                parents[v] = u
                heap.insert((distances[v], v))
    return distances, parents

def prim(G: Dict[int, List[Tuple[int, int]]], s: int):
    n = len(G)
    distances = [np.inf] * n
    parents = [None] * n
    visited = [False] * n
    heap = TupleMinHeap()
    heap.insert((0, s))
    distances[s] = 0

    while heap.get():
        dist, u = heap.extract_min()
        visited[u] = True
        for weight, v in G[u]:
            if not visited[v] and weight < distances[v]:
                distances[v] = weight
                parents[v] = u
                heap.insert((distances[v], v))
    return parents

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

def kruskal(G: Dict[int, List[Tuple[int, int]]]):
    edges = []
    for u in G:
        for w, v in G[u]:
            edges.append((w, u, v))
    edges.sort()
    uf = UnionFind(len(G))
    MST = []

    for w, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            MST.append((u, v, w))

    return MST

def bellman_ford(G: Dict[int, List[Tuple[int, int]]], s: int):
    n = len(G)
    dist = [float("inf")] * n
    dist[s] = 0

    for _ in range(n - 1):
        for u in G:
            for weight, v in G[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    for u in G:
        for weight, v in G[u]:
            if dist[u] + weight < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return dist

def ford_fulkerson(G: Dict[int, Dict[int, int]], s: int, t: int):
    parent = {}

    def bfs_residual(R):
        visited = {s}
        queue = deque([s])
        parent.clear()
        while queue:
            u = queue.popleft()
            for v in R[u]:
                if v not in visited and R[u][v] > 0:
                    parent[v] = u
                    if v == t:
                        return True
                    queue.append(v)
                    visited.add(v)
        return False

    R = {u: dict(v) for u, v in G.items()}
    max_flow = 0
    while bfs_residual(R):
        path_flow = float("inf")
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, R[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            R[u][v] -= path_flow
            R.setdefault(v, {}).setdefault(u, 0)
            R[v][u] += path_flow
            v = u
        max_flow += path_flow
    return max_flow

def visualize_weighted_graph(G: Dict[int, List[Tuple[int, int]]], title="Graph"):
    graph = nx.Graph()
    for u in G:
        for w, v in G[u]:
            graph.add_edge(u, v, weight=w)
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightgreen")
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title(title)
    plt.show()
