import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    critical = set()
    for _ in range(t):
        critical.add(int(next(it)))
    
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
    
    # Prim's algorithm for Steiner tree (variant)
    # Start with one critical node, grow the tree by adding the closest
    # unconnected node (critical or auxiliary) that connects to the tree
    
    # Pick first critical node
    first = next(iter(critical))
    
    in_tree = [False] * (n + 1)
    min_edge = [float('inf')] * (n + 1)
    
    # Initialize with first critical node
    min_edge[first] = 0
    pq = [(0, first)]
    
    total_cost = 0
    critical_in_tree = 0
    
    while pq and critical_in_tree < t:
        cost, u = heapq.heappop(pq)
        
        if in_tree[u]:
            continue
        
        in_tree[u] = True
        total_cost += cost
        
        if u in critical:
            critical_in_tree += 1
        
        for v, w in adj[u]:
            if not in_tree[v] and w < min_edge[v]:
                min_edge[v] = w
                heapq.heappush(pq, (w, v))
    
    print(total_cost)

if __name__ == "__main__":
    solve()