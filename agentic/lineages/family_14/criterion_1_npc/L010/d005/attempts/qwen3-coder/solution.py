import sys
from itertools import combinations

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def kruskal(n, edges, must_connect):
    parent = list(range(n))
    rank = [0] * n
    cost = 0
    edge_count = 0
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # First, add all edges with weight 0 (no cost)
    for u, v, w in edges:
        if w == 0:
            if union(parent, rank, u, v):
                edge_count += 1
    
    # Then process remaining edges
    for u, v, w in edges:
        if w > 0 and union(parent, rank, u, v):
            cost += w
            edge_count += 1
            if edge_count == n - 1:
                break
                
    # Check if all required nodes are connected
    components = {}
    for node in must_connect:
        root = find(parent, node)
        if root not in components:
            components[root] = []
        components[root].append(node)
    
    # If all required nodes are in the same component, it's valid
    return len(components) <= 1, cost

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    targets = list(map(int, sys.stdin.readline().split()))
    
    # Convert to 0-indexed
    targets = [x - 1 for x in targets]
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1, w))  # Convert to 0-indexed
    
    # If there are no edges, check if targets are already the same
    if not edges:
        if len(set(targets)) == 1:
            print(0)
        else:
            # This shouldn't happen according to problem statement
            print(0)
        return
    
    min_cost = float('inf')
    
    # Try all possible subsets of targets to be connected
    # But we need at least all targets to be in same component
    # So we just need to connect all targets together
    
    # We'll use a different approach:
    # Find minimum cost to connect all target nodes in a spanning tree
    
    # Add a virtual node that connects to all targets with cost 0
    # Then find MST of the whole graph
    
    # Actually, let's think differently:
    # We want to make all targets have the same value
    # This means they must be in the same connected component
    # So we need to find the minimum cost to connect all targets
    
    # Use a modified Kruskal's algorithm
    parent = list(range(n))
    rank = [0] * n
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    cost = 0
    connected_targets = {targets[0]}
    target_set = set(targets)
    
    while len(connected_targets) < len(targets):
        added_edge = False
        for i, (u, v, w) in enumerate(edges):
            # Check if this edge connects a new target
            if (u in connected_targets and v in target_set and v not in connected_targets) or \
               (v in connected_targets and u in target_set and u not in connected_targets):
                # Connect them
                pu, pv = find(parent, u), find(parent, v)
                if pu != pv:
                    # Union
                    if rank[pu] < rank[pv]:
                        pu, pv = pv, pu
                    parent[pv] = pu
                    if rank[pu] == rank[pv]:
                        rank[pu] += 1
                    
                    cost += w
                    connected_targets.add(u)
                    connected_targets.add(v)
                    added_edge = True
                    break
        
        if not added_edge:
            # Need to look for any edge that can extend our component
            for i, (u, v, w) in enumerate(edges):
                pu, pv = find(parent, u), find(parent, v)
                if pu != pv:
                    # One of them should be in our component
                    if u in connected_targets or v in connected_targets:
                        # Union
                        if rank[pu] < rank[pv]:
                            pu, pv = pv, pu
                        parent[pv] = pu
                        if rank[pu] == rank[pv]:
                            rank[pu] += 1
                        
                        cost += w
                        connected_targets.add(u)
                        connected_targets.add(v)
                        break
            else:
                break
    
    print(cost)

def solve_correct():
    import sys
    from collections import defaultdict
    
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, rank, x, y):
        px, py = find(parent, x), find(parent, y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    n, m, t = map(int, sys.stdin.readline().split())
    targets = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))  # 0-indexed
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1, w))  # Convert to 0-indexed
    
    # We want to find minimum cost to connect all targets
    # This is essentially finding the minimum spanning tree that connects all targets
    
    # Method: Try all possible ways to connect targets and find minimum cost
    # But that's too complex. Instead, we can use the fact that we want to connect
    # all targets in one component with minimum cost.
    
    # We can model this as finding the minimum cost to make all targets connected
    # in a graph. This is the Steiner tree problem, but since t is small (<=10),
    # we can try a different approach.
    
    # Let's build a complete graph on targets where edge weights are shortest paths
    # between targets in the original graph, then find MST of this graph.
    
    # Floyd-Warshall to get all-pairs shortest paths
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Now we have distances between all pairs of nodes
    # Build a complete graph on targets
    target_edges = []
    for i in range(len(targets)):
        for j in range(i+1, len(targets)):
            u, v = targets[i], targets[j]
            target_edges.append((i, j, dist[u][v]))
    
    # Find MST of target graph using Kruskal
    parent = list(range(len(targets)))
    rank = [0] * len(targets)
    
    target_edges.sort(key=lambda x: x[2])
    
    cost = 0
    edge_count = 0
    
    for u_idx, v_idx, w in target_edges:
        if union(parent, rank, u_idx, v_idx):
            cost += w
            edge_count += 1
            if edge_count == len(targets) - 1:
                break
    
    print(cost)

solve_correct()