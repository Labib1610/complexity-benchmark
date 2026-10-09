import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    high_priority = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Union-Find data structure
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
    
    # Sort edges by weight
    edges.sort()
    
    # First, connect all high-priority nodes among themselves using MST
    # We will build a virtual tree connecting all high-priority nodes
    # The minimal cost is the MST of the subgraph induced by high-priority nodes
    # But since we have a tree already, we can do better.
    
    # Build a spanning tree of the whole graph first (it's already a tree, so take all edges)
    # Then find the minimal subtree that connects all high priority nodes
    # This is essentially finding the Steiner tree, but on a tree it's solvable optimally
    
    # On a tree, the minimal cost to connect a subset of nodes is:
    # Sum of weights of edges in the minimal subtree that spans all those nodes
    
    # Algorithm:
    # 1. Root the tree at any node
    # 2. For each node, compute whether it's needed in the subtree:
    #    A node is needed if it's high-priority or has two or more subtrees containing high-priority nodes
    # 3. The edges in the minimal subtree are those whose both endpoints are needed
    
    # Let's implement this properly
    
    # Since the input guarantees m=n-1 and connected, it's a tree
    from collections import defaultdict
    
    adj = defaultdict(list)
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Mark which nodes are high priority
    is_high = [False] * (n + 1)
    for x in high_priority:
        is_high[x] = True
    
    # If there's only one high-priority node, cost is 0
    if len(high_priority) <= 1:
        print(0)
        return
    
    # DFS to find the minimal subtree
    # For each node, we return:
    # - whether this subtree contains any high-priority node
    # - the total cost of edges needed in this subtree
    
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        has_high = is_high[u]
        total_cost = 0
        needed_children = 0
        
        for v, w in adj[u]:
            if not visited[v]:
                child_has_high, child_cost = dfs(v)
                if child_has_high:
                    total_cost += child_cost + w
                    needed_children += 1
                    has_high = True
                    
        return has_high, total_cost
    
    # Start DFS from any node, say node 1
    _, result = dfs(1)
    print(result)

threading.Thread(target=main).start()