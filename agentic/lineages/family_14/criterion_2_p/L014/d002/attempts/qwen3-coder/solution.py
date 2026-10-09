import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # Since m = n - 1 and all nodes can be connected, the graph is a tree
    # We need to find the minimal subtree that connects all critical nodes
    # This is essentially finding the minimal Steiner tree
    
    # However, since the graph is already a tree (m = n-1 and connected),
    # we just need to find the edges in the tree that connect all critical nodes
    
    # Build adjacency list
    adj = [[] for _ in range(n+1)]
    for i, (w, u, v) in enumerate(edges):
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
    
    # If there is 0 or 1 critical node, cost is 0
    if len(critical) <= 1:
        print(0)
        return
    
    # We will use a different approach:
    # Since the graph is a tree, we can find the minimal subtree that spans all critical nodes
    # This is equivalent to finding the union of paths between all pairs of critical nodes,
    # but more efficiently, we can find the minimal connected subgraph containing all critical nodes
    
    # Approach:
    # 1. Root the tree at any node
    # 2. For each node, compute the number of critical nodes in its subtree
    # 3. An edge should be included if it separates two parts each containing at least one critical node
    
    parent = [0] * (n+1)
    depth = [0] * (n+1)
    children = [[] for _ in range(n+1)]
    subtree_critical_count = [0] * (n+1)
    
    # Root the tree at node 1
    def dfs(node, par, d):
        parent[node] = par
        depth[node] = d
        count = 1 if node in critical else 0
        for nei, w, idx in adj[node]:
            if nei == par:
                continue
            children[node].append((nei, w, idx))
            dfs(nei, node, d+1)
            count += subtree_critical_count[nei]
        subtree_critical_count[node] = count
    
    dfs(1, 0, 0)
    
    # Now, collect all edges that are needed
    # An edge from u to v (where v is deeper) is needed if 
    # subtree_critical_count[v] > 0 and (total_critical - subtree_critical_count[v]) > 0
    total_critical = len(critical)
    visited_edge_idx = set()
    result = 0
    
    # BFS/DFS to mark edges in the paths between critical nodes
    # But since it's a tree, we can do it more simply:
    # Include an edge if removing it disconnects critical nodes
    
    # For each edge (u,v) where v is child of u:
    # If subtree_critical_count[v] > 0 and subtree_critical_count[v] < total_critical
    # Then this edge must be included
    
    def dfs_edges(node):
        nonlocal result
        for nei, w, idx in children[node]:
            dfs_edges(nei)
            cnt = subtree_critical_count[nei]
            if cnt > 0 and cnt < total_critical:
                result += w
    
    dfs_edges(1)
    print(result)

threading.Thread(target=main).start()