import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # Since each operator is assigned exactly one terminal, we can simplify:
    # operator i is always paired with terminal term[i].
    # We need to select exactly one window for each operator.
    # The windows must be distinct (1 to k, each used exactly once).
    
    # Build bipartite graph: operators on left, windows on right
    # Edge exists if configuration (operator, terminal, window) is approved
    
    adj = [[] for _ in range(k + 1)]  # adj[operator] = list of windows
    configs = {}  # configs[(operator, window)] = terminal
    
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        adj[x].append(z)
        configs[(x, z)] = y
    
    # Hopcroft-Karp for maximum bipartite matching
    # Left side: operators 1..k, Right side: windows 1..k
    INF = float('inf')
    pair_u = [0] * (k + 1)  # pair_u[operator] = matched window
    pair_v = [0] * (k + 1)  # pair_v[window] = matched operator
    dist = [0] * (k + 1)
    
    def bfs():
        dq = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pair_v[v] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        dq.append(pair_v[v])
        return dist[0] != INF
    
    def dfs(u):
        for v in adj[u]:
            if pair_v[v] == 0 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    for x in range(1, k + 1):
        z = pair_u[x]
        y = configs[(x, z)]
        print(f"{x} {y} {z}")

if __name__ == "__main__":
    solve()