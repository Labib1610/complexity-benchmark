import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = defaultdict(set)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Create a list of all nodes
    nodes = sorted(adj.keys())
    
    # Map node to index for faster lookup
    node_to_index = {node: i for i, node in enumerate(nodes)}
    node_count = len(nodes)
    
    # Create adjacency list based on the sorted nodes
    adj_list = [set() for _ in range(node_count)]
    for i, node in enumerate(nodes):
        for neighbor in adj[node]:
            if neighbor in node_to_index:
                adj_list[i].add(node_to_index[neighbor])
    
    # Iterate through all triplets in lexicographical order
    for i in range(node_count):
        for j in range(i+1, node_count):
            if j not in adj_list[i]:
                continue
            for k in range(j+1, node_count):
                if k not in adj_list[i]:
                    continue
                if k not in adj_list[j]:
                    continue
                # Found a triangle
                a, b, c = nodes[i], nodes[j], nodes[k]
                print(a, b, c)
                return

if __name__ == "__main__":
    main()