import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    critical = set(map(int, data[idx:idx+t]))
    idx += t
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u, v, w))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If all nodes are critical, return sum of all edges
    if len(critical) == n:
        total = sum(w for _, _, w in edges)
        print(total)
        return
    
    # Find connected components using Union-Find
    parent = list(range(n + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Kruskal's algorithm to build MST
    mst_edges = []
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))
    
    # Build adjacency list for MST
    mst_adj = [[] for _ in range(n + 1)]
    for u, v, w in mst_edges:
        mst_adj[u].append((v, w))
        mst_adj[v].append((u, w))
    
    # If there's only one critical node, cost is 0
    if len(critical) == 1:
        print(0)
        return
    
    # Function to find the minimal subtree that connects all critical nodes
    # This is essentially finding the Steiner tree for the critical nodes in the MST
    
    # We can do this by rooting the MST at any node and doing a DFS
    # Keep only the branches that lead to critical nodes
    
    # Root the tree at the first critical node
    root = next(iter(critical))
    
    # DFS to mark which nodes are needed
    visited = [False] * (n + 1)
    included = [False] * (n + 1)
    
    # Mark critical nodes
    for c in critical:
        included[c] = True
    
    # Post-order DFS to determine which nodes to keep
    def dfs(u, parent_node):
        visited[u] = True
        has_critical = included[u]
        for v, w in mst_adj[u]:
            if v == parent_node:
                continue
            if not visited[v]:
                child_has_critical = dfs(v, u)
                has_critical |= child_has_critical
                # If child subtree has critical nodes, we need this edge
                if child_has_critical:
                    included[u] = True
        return has_critical
    
    dfs(root, -1)
    
    # Now collect all edges in the minimal subtree
    visited = [False] * (n + 1)
    total_cost = 0
    
    def collect_edges(u, parent_node):
        nonlocal total_cost
        visited[u] = True
        for v, w in mst_adj[u]:
            if v == parent_node:
                continue
            # Only traverse edges that are part of our subtree
            if included[v]:
                if not visited[v]:
                    total_cost += w
                    collect_edges(v, u)
    
    collect_edges(root, -1)
    print(total_cost)

if __name__ == "__main__":
    main()