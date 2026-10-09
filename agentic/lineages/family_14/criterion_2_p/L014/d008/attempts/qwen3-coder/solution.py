import sys
from collections import defaultdict, deque

def find_critical_edges(n, edges, key_holders):
    # Build the tree
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Convert key_holders to a set for fast lookup
    key_set = set(key_holders)
    
    # First DFS to compute subtree key counts
    subtree_keys = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    def dfs1(node, parent):
        visited[node] = True
        count = 1 if node in key_set else 0
        for neighbor, _ in adj[node]:
            if neighbor != parent and not visited[neighbor]:
                count += dfs1(neighbor, node)
        subtree_keys[node] = count
        return count
    
    # Start DFS from node 1
    dfs1(1, -1)
    
    # Total number of key holders
    total_keys = len(key_set)
    
    # Second DFS to identify critical edges
    visited = [False] * (n + 1)
    critical_edges = []
    
    def dfs2(node, parent, parent_edge_weight):
        visited[node] = True
        # Check if the edge from parent to node is critical
        if parent != -1:
            # One component has subtree_keys[node] keys
            # The other has total_keys - subtree_keys[node] keys
            if subtree_keys[node] > 0 and (total_keys - subtree_keys[node]) > 0:
                critical_edges.append(parent_edge_weight)
        
        for neighbor, weight in adj[node]:
            if neighbor != parent and not visited[neighbor]:
                dfs2(neighbor, node, weight)
    
    dfs2(1, -1, 0)
    
    return sum(critical_edges)

# Read input
n, m, t = map(int, sys.stdin.readline().split())
key_holders = list(map(int, sys.stdin.readline().split()))
edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

# Solve and output
result = find_critical_edges(n, edges, key_holders)
print(result)