import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    critical = [int(next(it)) for _ in range(t)]
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Prim's algorithm for Steiner tree on critical nodes
    # Start with first critical node in the tree
    in_tree = [False] * (n + 1)
    min_edge = [float('inf')] * (n + 1)
    
    start = critical[0]
    in_tree[start] = True
    total_cost = 0
    num_in_tree = 1
    
    # Initialize edges from the start node
    for v, w in adj[start]:
        if w < min_edge[v]:
            min_edge[v] = w
    
    # Use a heap to efficiently get minimum edge
    # Rebuild heap when needed
    heap = []
    for v in range(1, n + 1):
        if not in_tree[v] and min_edge[v] < float('inf'):
            heappush(heap, (min_edge[v], v))
    
    while num_in_tree < t:
        # Find minimum edge to a critical node not yet in tree
        while heap:
            w, v = heappop(heap)
            if in_tree[v]:
                continue
            if min_edge[v] < w:
                continue
            # Check if this is a critical node
            if v in critical:
                in_tree[v] = True
                total_cost += w
                num_in_tree += 1
                # Update edges from newly added node
                for to, weight in adj[v]:
                    if not in_tree[to] and weight < min_edge[to]:
                        min_edge[to] = weight
                        heappush(heap, (min_edge[to], to))
                break
            else:
                # Non-critical node, add it to tree (Steiner node)
                in_tree[v] = True
                total_cost += w
                # Update edges from newly added node
                for to, weight in adj[v]:
                    if not in_tree[to] and weight < min_edge[to]:
                        min_edge[to] = weight
                        heappush(heap, (min_edge[to], to))
    
    print(total_cost)

solve()