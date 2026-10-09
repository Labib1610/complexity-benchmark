import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = set()
    adj = [set() for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle (3 nodes fully connected) in the complement graph
    # That means, in the original graph, there should be no edges between these 3 nodes
    # But the condition is that the max safe set size for these 3 is exactly 1
    # This means in the subgraph induced by these 3 nodes, the max independent set size is 1
    # This happens iff the subgraph has no isolated nodes and is not a triangle
    # Wait, let's re-read the problem.
    
    # A safe set is a group where NO two materials are mutually volatile.
    # So a safe set is an independent set in the graph (where edges represent volatility)
    
    # We want 3 nodes such that the max independent set in the subgraph induced by them is 1
    # This means the subgraph has no independent set of size 2.
    # This happens when the subgraph is a triangle (3 nodes, 3 edges)
    # Because in a triangle, any two nodes are adjacent, so max independent set size is 1
    
    # So we need to find a triangle in the original graph
    
    # For each node, look at its neighbors
    # For every pair of neighbors of a node, check if they are connected
    # If so, we have a triangle
    
    found = False
    result = None
    
    for a in range(1, n + 1):
        if found:
            break
        neighbors = list(adj[a])
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                b = neighbors[i]
                c = neighbors[j]
                if b in adj[c]:  # There's an edge between b and c
                    # We found a triangle a-b, b-c, a-c
                    trio = sorted([a, b, c])
                    candidate = tuple(trio)
                    if result is None or candidate < result:
                        result = candidate
                        found = True
    if result is None:
        # Brute force check all combinations if the above fails
        for combo in combinations(range(1, n + 1), 3):
            a, b, c = combo
            edge_count = 0
            if (a, b) in edges or (b, a) in edges:
                edge_count += 1
            if (a, c) in edges or (c, a) in edges:
                edge_count += 1
            if (b, c) in edges or (c, b) in edges:
                edge_count += 1
            if edge_count == 3:  # It's a triangle
                result = (a, b, c)
                break
                
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()