import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, k, edges

def solve():
    n, m, k, edges = read_input()
    
    # Build adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # If no edges, any k nodes will work
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, k+1))))
        return
    
    # Find one node and its neighbors to determine bipartition
    start_node = next(iter(adj.keys()))
    visited = set()
    color = {}
    color[start_node] = 0
    queue = deque([start_node])
    visited.add(start_node)
    
    # BFS to check if graph is bipartite and get colors
    is_bipartite = True
    while queue and is_bipartite:
        u = queue.popleft()
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                is_bipartite = False
                break
    
    # Collect nodes by color
    set_0 = [node for node in color if color[node] == 0]
    set_1 = [node for node in color if color[node] == 1]
    
    # Add isolated nodes (nodes with no edges) to both sets
    isolated_nodes = set(range(1, n+1)) - set(color.keys())
    set_0.extend(isolated_nodes)
    
    # Check which set can provide k nodes
    if len(set_0) >= k:
        print("YES")
        print(' '.join(map(str, set_0[:k])))
    elif len(set_1) >= k:
        print("YES")
        print(' '.join(map(str, set_1[:k])))
    else:
        print("NO")

solve()