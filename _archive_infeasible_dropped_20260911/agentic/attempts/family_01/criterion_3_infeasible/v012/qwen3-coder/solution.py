import sys
from collections import defaultdict

def find_triangle(edges, n):
    # Build adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Also build adjacency list as sorted lists for fast intersection
    adj_list = {}
    for node in adj:
        adj_list[node] = sorted(list(adj[node]))
    
    best = None
    
    # For each node, check all pairs of its neighbors
    for a in range(1, n + 1):
        if a not in adj_list:
            continue
        neighbors = adj_list[a]
        # Check all pairs of neighbors of 'a'
        for i in range(len(neighbors)):
            b = neighbors[i]
            if b <= a:
                continue
            # Now we need to find a common neighbor of a and b that is > b
            # But actually, we just need c such that (a,b), (a,c), (b,c) exist
            # So c must be in both adj[b] and adj[a]
            # And we want the lexicographically smallest such triple
            for j in range(i + 1, len(neighbors)):
                c = neighbors[j]
                if c <= b:
                    continue
                # Check if b and c are connected
                if c in adj[b]:
                    candidate = (a, b, c)
                    if best is None or candidate < best:
                        best = candidate
    return best

# Read input
input_lines = []
for line in sys.stdin:
    input_lines.append(line.strip())

n, m = map(int, input_lines[0].split())
edges = []
for i in range(1, m + 1):
    u, v = map(int, input_lines[i].split())
    edges.append((u, v))

result = find_triangle(edges, n)
if result:
    print(result[0], result[1], result[2])
else:
    # Should not happen according to problem statement
    print("No triangle found")