import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    k = int(data[0])
    t = int(data[1])

    adj = [[] for _ in range(k + 1)]
    y_val = [0] * (k + 1)

    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx + 1])
        z = int(data[idx + 2])
        idx += 3
        y_val[x] = y
        adj[x].append(z)

    # Hopcroft-Karp algorithm for maximum bipartite matching
    pair_u = [0] * (k + 1)
    pair_v = [0] * (k + 1)
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
        if u != 0:
            for v in adj[u]:
                pu = pair_v[v]
                if dist[pu] == dist[u] + 1:
                    if dfs(pu):
                        pair_v[v] = u
                        pair_u[u] = v
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
            out.append(f"{u} {y_val[u]} {pair_u[u]}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()