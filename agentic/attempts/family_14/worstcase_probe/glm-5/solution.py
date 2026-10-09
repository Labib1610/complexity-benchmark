import sys
from heapq import heappop, heappush

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    B = int(next(it))
    
    required = set()
    if t > 0:
        for _ in range(t):
            required.add(int(next(it)))
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    # Store original edge index
    edges = []
    edge_index = 0
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w, edge_index))
        adj[v].append((u, w, edge_index))
        edges.append((u, v, w))
        edge_index += 1
    
    if t == 0:
        print("YES")
        return
    
    root = next(iter(required))
    
    # Prim's algorithm starting from a required site
    INF = 10**18
    min_edge = [INF] * (n + 1)
    min_edge_idx = [-1] * (n + 1)
    in_mst = [False] * (n + 1)
    total_cost = 0
    mst_edges = []
    
    min_edge[root] = 0
    pq = [(0, root)]
    
    while pq:
        cost, u = heappop(pq)
        if in_mst[u]:
            continue
        in_mst[u] = True
        total_cost += cost
        
        if min_edge_idx[u] != -1:
            mst_edges.append(min_edge_idx[u])
        
        for v, w, idx in adj[u]:
            if not in_mst[v] and w < min_edge[v]:
                min_edge[v] = w
                min_edge_idx[v] = idx
                heappush(pq, (w, v))
    
    # Check if all required sites are in the same component
    # They are all in MST component starting from root
    # Since MST connects all vertices in the graph's connected component,
    # all required sites must be reachable from root (same component)
    # Prim's algorithm naturally does this
    
    # Actually, we need to verify all required are in the same connected component
    # The MST will span the connected component of root
    # Check each required site is reachable
    possible = True
    for site in required:
        if not in_mst[site]:
            possible = False
            break
    
    if not possible or total_cost > B:
        print("NO")
    else:
        print("YES")
        for idx in mst_edges:
            u, v, w = edges[idx]
            print(u, v)

if __name__ == "__main__":
    solve()