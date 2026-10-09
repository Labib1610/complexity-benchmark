import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    B = int(next(it))
    required = [int(next(it)) - 1 for _ in range(t)]
    
    INF = 10**12
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    # DP
    full_mask = (1 << t) - 1
    dp = [[INF]*n for _ in range(1 << t)]
    parent = [[None]*n for _ in range(1 << t)]
    
    for i, r in enumerate(required):
        dp[1 << i][r] = 0
    
    # Combine subsets
    for mask in range(1 << t):
        # combine
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
                        parent[mask][v] = (sub, other, v, 'combine')
            sub = (sub - 1) & mask
        
        # relax with shortest paths
        # Dijkstra-like relaxation using priority queue
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[mask][u]:
                continue
            for v in range(n):
                nd = d + dist[u][v]
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    parent[mask][v] = (u, v, 'relax')
                    heapq.heappush(pq, (nd, v))
    
    # Find best root
    best_cost = INF
    best_root = -1
    for v in range(n):
        if dp[full_mask][v] < best_cost:
            best_cost = dp[full_mask][v]
            best_root = v
    
    if best_cost > B:
        print("NO")
        return
    
    # Reconstruct edges
    used_edges = set()
    def reconstruct(mask, v):
        if mask == 0:
            return
        p = parent[mask][v]
        if p is None:
            return
        if p[2] == 'combine':
            sub, other, _, _ = p
            reconstruct(sub, v)
            reconstruct(other, v)
        else:  # relax
            u, _, _ = p
            # find actual edge on shortest path from u to v
            # we can just add the direct edge if exists, else reconstruct path
            # For simplicity, we add the direct edge if it's the shortest path edge
            # But we need actual edges; we can store path reconstruction separately.
            # Here we'll just add the edge (u,v) if it's in original edges with that weight,
            # otherwise we need to find intermediate nodes.
            # To keep it simple, we'll add the direct edge if it exists with that weight,
            # else we'll add all edges along the shortest path.
            # We'll do a BFS/DFS to find path.
            # For now, we'll just add the direct edge if it's in edges list with that weight.
            # But that might not be correct if shortest path uses intermediate nodes.
            # So we'll reconstruct path using Floyd-Warshall predecessor.
            # Let's implement path reconstruction.
            pass
    
    # Better: store predecessor matrix for Floyd-Warshall
    # We'll do that now.
    
    # Re-run Floyd with predecessor
    pred = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] < INF:
                pred[i][j] = i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    
    # Now reconstruct path edges
    def get_path_edges(u, v):
        if u == v:
            return []
        if pred[u][v] == -1:
            return []
        path = []
        while v != u:
            p = pred[u][v]
            path.append((p, v))
            v = p
        return path
    
    # Now reconstruct tree edges
    used_edges = set()
    def reconstruct(mask, v):
        if mask == 0:
            return
        p = parent[mask][v]
        if p is None:
            return
        if p[2] == 'combine':
            sub, other, _, _ = p
            reconstruct(sub, v)
            reconstruct(other, v)
        else:
            u, _, _ = p
            # add edges along shortest path from u to v
            for a, b in get_path_edges(u, v):
                if a > b:
                    a, b = b, a
                used_edges.add((a, b))
            reconstruct(mask, u)
    
    reconstruct(full_mask, best_root)
    
    # Output
    print("YES")
    for u, v in sorted(used_edges):
        print(u+1, v+1)

if __name__ == "__main__":
    solve()