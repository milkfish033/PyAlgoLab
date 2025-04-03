# pyalgolab/utils.py
"""
Graph Utilities & Visualization
"""

import matplotlib.pyplot as plt
import networkx as nx
from typing import Dict, List

def print_graph(G: Dict[int, List[int]]):
    for u in G:
        print(f"{u}: {G[u]}")

def visualize_graph(G: Dict[int, List[int]], title="Graph"):
    graph = nx.DiGraph()
    for u in G:
        for v in G[u]:
            graph.add_edge(u, v)
    nx.draw(graph, with_labels=True, node_color="lightblue", arrows=True)
    plt.title(title)
    plt.show()
