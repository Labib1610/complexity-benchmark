import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    idx = 2
    adj = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        adj[x].append(z)

    # Hopcroft-Karp for bipartite matching: left = chefs 1..k, right = menus 1..k
    INF = 10**9
    pair_u = [0] * (k + 1)
    pair_v = [0] * (k + 1)
    dist = [0] * (k + 1)

    from collections import deque

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
                    pu = pair_v[v]
                    if dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        dq.append(pu)
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                pu = pair_v[v]
                if dist[pu] == dist[u] + 1:
                    if dfs(pu):
                        pair_u[u] = v
                        pair_v[v] = u
                        return True
            dist[u] = INF
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    if matching == k:
        out = ["YES"]
        for u in range(1, k + 1):
            out.append(f"{u} {u} {pair_u[u]}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()