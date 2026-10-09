import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    
    # Build adjacency list for operators (1..q) to vehicles (1..q, remapped from q+1..2q)
    adj = [[] for _ in range(q + 1)]
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]); b = int(input_data[idx+1])
        idx += 2
        adj[a].append(b - q)  # remap vehicle to 1..q
    
    # Hopcroft-Karp
    pair_u = [0] * (q + 1)  # operator -> matched vehicle
    pair_v = [0] * (q + 1)  # vehicle -> matched operator
    dist = [0] * (q + 1)
    from collections import deque
    
    INF = 10**9
    
    def bfs():
        dq = deque()
        for u in range(1, q + 1):
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
                    u2 = pair_v[v]
                    if dist[u2] == INF:
                        dist[u2] = dist[u] + 1
                        dq.append(u2)
        return dist[0] != INF
    
    def dfs(u):
        if u != 0:
            for v in adj[u]:
                u2 = pair_v[v]
                if dist[u2] == dist[u] + 1 and dfs(u2):
                    pair_v[v] = u
                    pair_u[u] = v
                    return True
            dist[u] = INF
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        out = ["YES"]
        for u in range(1, q + 1):
            out.append(f"{u} {pair_u[u] + q}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()