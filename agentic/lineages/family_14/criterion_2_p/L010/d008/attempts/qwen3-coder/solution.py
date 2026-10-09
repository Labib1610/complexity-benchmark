import sys
from collections import defaultdict
import heapq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find_parent(parent, x), find_parent(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    targets = list(map(int, data[idx:idx+t]))
    idx += t
    
    # If only one target, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Create a mapping of target nodes to a contiguous range
    target_set = set(targets)
    target_map = {v: i for i, v in enumerate(targets)}
    num_targets = len(targets)
    
    # We need to find the minimum cost to connect all target nodes
    # This is a Steiner tree problem, but we can solve it by building a complete graph
    # where edge weights are the shortest path distances between targets in the original graph
    
    # First, build the graph from the given vectors
    adj = [[] for _ in range(n+1)]
    edges = []
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((w, u, v))
    
    # For each target node, run Dijkstra to find shortest paths to all other nodes
    # But we only need distances to other target nodes
    dist_to_targets = {}
    
    # Importing heapq inside function for performance
    import heapq
    
    for start in targets:
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        
        # Keep track of which target nodes we've reached
        reached_targets = 0
        target_dists = {}
        
        while pq and reached_targets < num_targets:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
                
            if u in target_set and u not in target_dists:
                target_dists[u] = d
                reached_targets += 1
                
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        
        dist_to_targets[start] = target_dists
    
    # Now build a complete graph of target nodes with edge weights as shortest paths
    # Then find the MST of this graph
    if num_targets == 1:
        print(0)
        return
        
    # Create edges for the target graph
    target_edges = []
    for i in range(num_targets):
        for j in range(i+1, num_targets):
            u = targets[i]
            v = targets[j]
            # Distance is the shortest path between u and v in original graph
            # We can get this from either dist_to_targets[u][v] or dist_to_targets[v][u]
            if v in dist_to_targets[u]:
                w = dist_to_targets[u][v]
                target_edges.append((w, i, j))
    
    # Find MST of target_edges using Kruskal's algorithm
    target_edges.sort()
    parent = list(range(num_targets))
    rank = [0] * num_targets
    
    cost = 0
    edges_used = 0
    
    for w, u, v in target_edges:
        if union(parent, rank, u, v):
            cost += w
            edges_used += 1
            if edges_used == num_targets - 1:
                break
                
    print(cost)

if __name__ == "__main__":
    main()