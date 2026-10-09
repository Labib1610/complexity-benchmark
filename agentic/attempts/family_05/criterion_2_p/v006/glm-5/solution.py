import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # For each operator x, store list of available shifts z
    # Also store the fixed station y for each operator
    op_shifts = [[] for _ in range(k + 1)]
    op_station = [0] * (k + 1)
    
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        op_shifts[x].append(z)
        op_station[x] = y
    
    # Bipartite matching: operators (1..k) to shifts (1..k)
    # Build adjacency list
    adj = [[] for _ in range(k + 1)]
    for x in range(1, k + 1):
        adj[x] = op_shifts[x][:]
    
    # Hopcroft-Karp
    pair_u = [0] * (k + 1)  # pair_u[x] = shift matched to operator x
    pair_v = [0] * (k + 1)  # pair_v[z] = operator matched to shift z
    dist = [0] * (k + 1)
    NIL = 0
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[NIL] = float('inf')
        while queue:
            u = queue.popleft()
            if dist[u] < dist[NIL]:
                for v in adj[u]:
                    if pair_v[v] == NIL:
                        if dist[NIL] == float('inf'):
                            dist[NIL] = dist[u] + 1
                    elif dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[NIL] != float('inf')
    
    def dfs(u):
        if u != NIL:
            for v in adj[u]:
                if pair_v[v] == NIL or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
            dist[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == NIL and dfs(u):
                matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    for x in range(1, k + 1):
        z = pair_u[x]
        y = op_station[x]
        print(f"{x} {y} {z}")

if __name__ == "__main__":
    solve()