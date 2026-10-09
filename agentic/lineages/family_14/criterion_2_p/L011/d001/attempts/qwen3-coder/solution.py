import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    core = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    edges.sort()
    
    parent = list(range(n + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    total_cost = 0
    connected_cores = len(core)
    
    for w, u, v in edges:
        if union(u, v):
            if u in core and v in core:
                connected_cores -= 1
            elif u in core or v in core:
                if find(u) in core or find(v) in core:
                    pass
                else:
                    core.add(find(u))
                    core.add(find(v))
            if connected_cores == 1:
                break
    
    # Actually, let's rethink this with a better approach
    # We need to find the minimum spanning tree that connects all core nodes
    # This is essentially finding the minimum Steiner tree, which is NP-hard
    # But since the underlying graph is a tree (m = n-1), it's much simpler
    
    # In a tree, to connect all core nodes, we need the subtree that spans them
    # This is equivalent to finding the union of all paths between core nodes
    # Which is the same as finding the minimal subtree containing all core nodes
    
    # Approach:
    # 1. Build the tree
    # 2. Find all core nodes
    # 3. Find the minimal subtree that contains all core nodes
    
    from collections import defaultdict, deque
    
    adj = defaultdict(list)
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If there's only one core node, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Find the minimal subtree containing all core nodes
    # We can do this by:
    # 1. Starting from one core node
    # 2. Doing BFS/DFS to find all other core nodes
    # 3. Keeping track of the edges we use
    
    visited = [False] * (n + 1)
    edge_used = [False] * m
    core_list = list(core)
    
    # We'll use a multi-source BFS from all core nodes to find the minimal subtree
    # Actually, simpler approach:
    # Since it's a tree, the minimal subtree connecting all core nodes is unique
    # We can find it by:
    # 1. Rooting the tree at any node
    # 2. For each node, compute if its subtree contains any core node
    # 3. An edge is in the minimal subtree if it connects two subtrees that both contain core nodes
    
    # Let's build adjacency list with edge indices
    adj_with_idx = defaultdict(list)
    for idx, (w, u, v) in enumerate(edges):
        adj_with_idx[u].append((v, w, idx))
        adj_with_idx[v].append((u, w, idx))
    
    # Mark which nodes are core
    is_core = [False] * (n + 1)
    for c in core:
        is_core[c] = True
    
    # DFS to count core nodes in each subtree and mark needed edges
    def dfs(node, parent):
        core_count = 1 if is_core[node] else 0
        for neighbor, weight, edge_idx in adj_with_idx[node]:
            if neighbor == parent:
                continue
            child_core_count = dfs(neighbor, node)
            core_count += child_core_count
            # If this subtree has at least one core node and is not the full tree
            # then this edge should be included
            if child_core_count > 0 and child_core_count < t:
                edge_used[edge_idx] = True
        return core_count
    
    # Root at node 1
    dfs(1, -1)
    
    total_cost = 0
    for i in range(m):
        if edge_used[i]:
            total_cost += edges[i][0]
    
    print(total_cost)

threading.Thread(target=main).start()