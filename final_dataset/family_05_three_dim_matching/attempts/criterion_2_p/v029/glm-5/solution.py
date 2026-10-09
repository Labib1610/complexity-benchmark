import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        adj[x].append(z)
    
    # Hopcroft-Karp for perfect matching between x (1..k) and z (1..k)
    INF = float('inf')
    pairU = [0] * (k + 1)  # pairU[x] = z matched to x
    pairV = [0] * (k + 1)  # pairV[z] = x matched to z
    dist = [0] * (k + 1)
    
    def bfs():
        queue = deque()
        found = False
        for u in range(1, k + 1):
            if pairU[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    pu = pairV[v]
                    if dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        queue.append(pu)
        return dist[0] != INF
    
    def dfs(u):
        if u == 0:
            return True
        for v in adj[u]:
            pu = pairV[v]
            if dist[pu] == dist[u] + 1:
                if dfs(pu):
                    pairU[u] = v
                    pairV[v] = u
                    return True
        dist[u] = INF
        return False
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pairU[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching != k:
        sys.stdout.write("NO\n")
        return
    
    # Build output: need y for each x. Since pairing is fixed, 
    # we can get y from any edge of x (all edges of x have same y)
    # But we stored only z. We need to recover y.
    # Re-read to build x->y mapping
    idx2 = 2
    x_to_y = [0] * (k + 1)
    for _ in range(t):
        x = int(input_data[idx2]); idx2 += 1
        y = int(input_data[idx2]); idx2 += 1
        z = int(input_data[idx2]); idx2 += 1
        if x_to_y[x] == 0:
            x_to_y[x] = y
    
    out = ["YES"]
    for x in range(1, k + 1):
        out.append(f"{x} {x_to_y[x]} {pairU[x]}")
    sys.stdout.write("\n".join(out) + "\n")

solve()