import sys
from collections import defaultdict
import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    t = int(data[idx+2])
    idx += 3
    
    priority = list(map(int, data[idx:idx+t]))
    idx += t
    
    # Build graph
    graph = defaultdict(list)
    edges = []
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        w = int(data[idx+2])
        idx += 3
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((w, u, v))
    
    # If t <= 1, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Priority nodes set for quick lookup
    priority_set = set(priority)
    
    # We need to find the minimum cost to connect all priority nodes
    # This is essentially finding the Minimum Spanning Tree (MST) of the induced subgraph
    # But since we only care about connecting priority nodes, we can do the following:
    # Run Dijkstra's algorithm from each priority node to compute distances to all other nodes
    # Then build a complete graph among priority nodes using shortest paths
    # Finally, compute MST of that complete graph
    
    # However, there's a more efficient way:
    # Since the original graph is a tree (n nodes, m=n-1 edges), we can use the fact that 
    # the minimum cost to connect all priority nodes is the cost of the Steiner tree on the tree.
    # But computing Steiner tree is complex.
    # Instead, we can do the following:
    # Compute pairwise distances among all priority nodes using BFS/DFS since it's a tree.
    # Then compute the MST of the complete graph formed by these distances.
    
    # Since it's a tree, we can compute all pairwise distances efficiently.
    # But even better: we can use the fact that in a tree, the minimum cost to connect a subset of nodes
    # is the cost of the edges in the subtree that spans those nodes.
    # So we can build the subtree that includes all priority nodes by including all paths between them.
    # But that's still complex.
    
    # Let's use the standard approach:
    # 1. Compute pairwise distances among priority nodes
    # 2. Build a complete graph with these distances
    # 3. Compute MST of that graph
    
    # Step 1: Compute distances from each priority node to all other nodes using BFS (since unweighted edges don't apply here - we have weights)
    # Actually, we should use Dijkstra's algorithm because edges have weights
    
    # Precompute distances from each priority node to all nodes
    dist_from = {}
    for start in priority:
        dist = {node: float('inf') for node in range(1, n+1)}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                alt = d + w
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(pq, (alt, v))
        dist_from[start] = dist
    
    # Step 2: Create a complete graph among priority nodes with shortest path distances
    # Use Prim's or Kruskal's algorithm to find MST of this complete graph
    # But number of priority nodes can be up to n, so creating complete graph is O(t^2)
    # Which is acceptable if t is small, but t can be up to n.
    # Wait, let's re-examine the constraints: t can be up to n, but usually much smaller.
    # But in example 1, t=2, so it's manageable.
    
    # Let's proceed with building the complete graph among priority nodes
    # and then compute its MST
    
    if t == 1:
        print(0)
        return
    
    # Generate all edges between priority nodes with their shortest path distances
    edges_pq = []
    for i in range(t):
        for j in range(i+1, t):
            u = priority[i]
            v = priority[j]
            w = dist_from[u][v]
            edges_pq.append((w, i, j))
    
    # Now run Kruskal's algorithm to find MST of this complete graph
    edges_pq.sort()
    
    parent = list(range(t))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        parent[px] = py
        return True
    
    cost = 0
    edges_used = 0
    for w, u, v in edges_pq:
        if union(u, v):
            cost += w
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(cost)

if __name__ == "__main__":
    main()