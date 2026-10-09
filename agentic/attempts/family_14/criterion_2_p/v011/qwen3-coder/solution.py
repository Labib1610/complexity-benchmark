import sys
from collections import defaultdict
import heapq

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, t = map(int, sys.stdin.readline().split())
    vital = set(map(int, sys.stdin.readline().split()))
    
    # If there's only one vital module, we need 0 power
    if t <= 1:
        print(0)
        return
    
    # Build the graph
    graph = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Step 1: Find the subtree that spans all vital nodes (Steiner tree approach)
    # We'll use a modified Prim's algorithm starting from all vital nodes
    
    # To find the minimal subtree connecting all vital nodes:
    # This is essentially finding the Minimum Spanning Tree of the subgraph 
    # induced by the vital nodes and their connecting paths.
    
    # Better approach: Use the fact that we have a tree, so we can find the 
    # minimal subtree containing all vital nodes by:
    # 1. Marking all vital nodes
    # 2. Performing a traversal to find all edges that must be included
    
    # Let's build a spanning tree first (any spanning tree will do, since it's already a tree)
    # Actually, the given graph IS a tree since m = n-1 and it's connected.
    
    # So we just need to find the minimal subtree that connects all vital nodes.
    # This is called the Steiner tree problem on trees, which can be solved efficiently.
    
    # Algorithm:
    # 1. Root the tree at any node
    # 2. For each node, compute if its subtree contains any vital node
    # 3. An edge is needed if it separates vital nodes
    
    # Let's root the tree at node 1
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Mark which nodes are vital
    is_vital = [False] * (n+1)
    for node in vital:
        is_vital[node] = True
        
    # DFS to find the minimal subtree
    visited = [False] * (n+1)
    result = [0]
    
    def dfs(u):
        visited[u] = True
        # Count vital nodes in this subtree
        count = 1 if is_vital[u] else 0
        
        for v, w in adj[u]:
            if not visited[v]:
                sub_count = dfs(v)
                # If both sides of this edge have vital nodes, we need this edge
                if sub_count > 0 and (t - sub_count) > 0:
                    result[0] += w
                count += sub_count
                
        return count
    
    dfs(1)
    print(result[0])

if __name__ == "__main__":
    main()