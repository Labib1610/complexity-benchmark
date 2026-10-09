import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # For each enzyme x, we have a fixed RNA y.
    # We need to select exactly one cell z for each x.
    # Each z must be used exactly once.
    
    # Build bipartite graph: enzymes (left) to cells (right)
    # Edge exists if (x, fixed_y, z) is viable
    
    # fixed_y[x] = y paired with enzyme x
    fixed_y = [0] * (k + 1)
    
    # adj[x] = list of viable cells z for enzyme x
    adj = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        if fixed_y[x] == 0:
            fixed_y[x] = y
        adj[x].append(z)
    
    # Hopcroft-Karp for maximum matching
    # Left side: enzymes 1..k
    # Right side: cells 1..k
    
    INF = k + 5
    pairU = [0] * (k + 1)
    pairV = [0] * (k + 1)
    dist = [0] * (k + 1)
    
    def bfs():
        dq = deque()
        for u in range(1, k + 1):
            if pairU[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        dq.append(pairV[v])
        return dist[0] != INF
    
    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pairV[v]] == dist[u] + 1:
                    if dfs(pairV[v]):
                        pairV[v] = u
                        pairU[u] = v
                        return True
            dist[u] = INF
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pairU[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == k:
        print("YES")
        for x in range(1, k + 1):
            z = pairU[x]
            y = fixed_y[x]
            print(f"{x} {y} {z}")
    else:
        print("NO")

if __name__ == "__main__":
    solve()