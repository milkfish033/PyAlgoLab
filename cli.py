# cli.py (增强)
import json

def parse_input(raw):
    try:
        return json.loads(raw)
    except:
        return list(map(int, raw.split()))
        
def main():
    ...
    input_data = parse_input(args.input)
    
    if args.algo == "bubble_sort":
        sorting.bubble_sort(input_data)
        print("Sorted:", input_data)
        
    elif args.algo == "bfs":
        result = graph_traversal.bfs(input_data, 0)
        print("BFS Tree:", result)
        if args.plot:
            utils.visualize_graph(result)

    ...
