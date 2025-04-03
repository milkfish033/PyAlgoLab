# pyalgolab/graph_traversal.py
"""
Graph Traversal Algorithms: BFS, DFS, Topological Sort
"""

from collections import deque
from typing import Dict, List
import matplotlib.pyplot as plt
import networkx as nx

def bfs(G: Dict[int, List[int]], s: int):
    q = deque()
    q.append(s)
    T = {}
    visited = [False] * len(G)
    visited[s] = True

    while q:
        p = q.popleft()
        T[p] = []
        for c in G[p]:
            if not visited[c]:
                visited[c] = True
                T[p].append(c)
                q.append(c)
    return T

def dfs(G: Dict[int, List[int]], s: int):
    n = len(G)
    stack = []
    T = {}
    visited = [False] * n
    stack.append(s)
    last_node = None
    while stack:
        p = stack[-1]
        if visited[p]:
            stack.pop()
        else:
            visited[p] = True
            T[p] = last_node
            last_node = p
            for c in G[p]:
                if not visited[c]:
                    stack.append(c)
    return T

def topological_sort(G: Dict[int, List[int]]):
    n = len(G)
    visited = [False] * n
    stack = []

    def dfs_visit(v):
        visited[v] = True
        for u in G.get(v, []):
            if not visited[u]:
                dfs_visit(u)
        stack.append(v)

    for i in range(n):
        if not visited[i]:
            dfs_visit(i)

    stack.reverse()
    return stack

# ---------- Visualization Helper ----------

def visualize_graph(G: Dict[int, List[int]], title="Graph"):
    graph = nx.DiGraph()
    for u in G:
        for v in G[u]:
            graph.add_edge(u, v)
    nx.draw(graph, with_labels=True, node_color="lightblue", arrows=True)
    plt.title(title)
    plt.show()
