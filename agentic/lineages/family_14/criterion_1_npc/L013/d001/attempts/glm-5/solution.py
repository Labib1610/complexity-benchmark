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
    
    core = [int(next(it)) for _ in range(t)]
    
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
    
    # Prim's algorithm for Steiner tree approximation
    # Start with first core node, iteratively add nearest core node
    INF = 10**18
    in_tree = [False] * (n + 1)
    min_edge = [INF] * (n + 1)
    
    # Start from first core node
    start = core[0]
    min_edge[start] = 0
    
    total = 0
    tree_size = 0
    core_in_tree = set()
    
    # Priority queue: (weight, node)
    pq = [(0, start)]
    
    while pq and len(core_in_tree) < t:
        w, u = heappop(pq)
        if in_tree[u]:
            continue
        in_tree[u] = True
        total += w
        tree_size += 1
        if u in core:
            core_in_tree.add(u)
        
        for v, weight in adj[u]:
            if not in_tree[v] and weight < min_edge[v]:
                min_edge[v] = weight
                heappush(pq, (weight, v))
    
    print(total)

if __name__ == "__main__":
    solve()