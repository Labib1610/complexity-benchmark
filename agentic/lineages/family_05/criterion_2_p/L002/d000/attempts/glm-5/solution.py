import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # Build adjacency: for each (x,y) pair, list of z values
    # Since x->y is fixed and bijective, we can use x as identifier for the pair
    adj = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        adj[x].append(z)
    
    # Hopcroft-Karp: left = specialists (1..k), right = time slots (1..k)
    pair_u = [0] * (k + 1)  # pair_u[u] = v (0 means unmatched)
    pair_v = [0] * (k + 1)  # pair_v[v] = u
    dist = [0] * (k + 1)
    INF = float('inf')
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    pu = pair_v[v]
                    if dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        queue.append(pu)
        return dist[0] != INF
    
    def dfs(u):
        if u == 0:
            return True
        for v in adj[u]:
            pu = pair_v[v]
            if dist[pu] == dist[u] + 1:
                if dfs(pu):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
        dist[u] = INF
        return False
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == k:
        out = []
        out.append("YES")
        for u in range(1, k + 1):
            v = pair_u[u]
            # y is determined by x (bijective), but we need to find y
            # Since x->y is a bijection and we stored adj by x, we need y
            # Actually we need to recover y. Let's re-read to get the mapping.
            pass
        # We need the x->y mapping
        # Re-parse input to get y for each x
        idx2 = 2
        xy_map = {}
        for _ in range(t):
            x = int(input_data[idx2]); idx2 += 1
            y = int(input_data[idx2]); idx2 += 1
            z = int(input_data[idx2]); idx2 += 1
            xy_map[x] = y
        
        for u in range(1, k + 1):
            v = pair_u[u]
            out.append(f"{u} {xy_map[u]} {v}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()