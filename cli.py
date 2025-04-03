# cli.py
"""
PyAlgoLab CLI Entry
"""

import argparse
from pyalgolab import sorting, graph_traversal, graph_algorithms, dp, matching, heap, union_find, utils

def main():
    parser = argparse.ArgumentParser(description="PyAlgoLab CLI Tool")
    parser.add_argument("--algo", required=True, type=str, help="Algorithm name")
    parser.add_argument("--input", required=True, type=str, help="Input as a list or graph")
    parser.add_argument("--plot", action="store_true", help="Visualize if applicable")
    args = parser.parse_args()

    if args.algo == "bubble_sort":
        arr = list(map(int, args.input.split()))
        sorting.bubble_sort(arr)
        print("Sorted:", arr)
    
    elif args.algo == "bfs":
        G = eval(args.input)
        result = graph_traversal.bfs(G, 0)
        print("BFS Tree:", result)
        if args.plot:
            utils.visualize_graph(result)
    
    elif args.algo == "dfs":
        G = eval(args.input)
        result = graph_traversal.dfs(G, 0)
        print("DFS Tree:", result)
        if args.plot:
            utils.visualize_graph({k: [v] for k, v in result.items() if v is not None})
    
    elif args.algo == "dijkstra":
        G = eval(args.input)
        dist, parent = graph_algorithms.dijkstra(G, 0)
        print("Distances:", dist)
        print("Parents:", parent)
    
    else:
        print("Algorithm not implemented yet!")

if __name__ == "__main__":
    main()
