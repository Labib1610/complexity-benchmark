import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    k = next(it)
    t = next(it)

    # adjacency from pilot (1..k) to routes (1..k)
    adj = [[] for _ in range(k + 1)]
    aircraft = [0] * (k + 1)          # aircraft[p] will be fixed aircraft of pilot p

    for _ in range(t):
        x = next(it)   # pilot
        y = next(it)   # aircraft
        z = next(it)   # route
        if aircraft[x] == 0:
            aircraft[x] = y
        # else: by problem guarantee aircraft[x] == y
        adj[x].append(z)

    n = k          # left side size
    m = k          # right side size

    pair_u = [0] * (n + 1)   # pilot -> route
    pair_v = [0] * (m + 1)   # route -> pilot
    dist = [0] * (n + 1)
    INF = 10 ** 9

    def bfs() -> bool:
        q = deque()
        for u in range(1, n + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        d = INF
        while q:
            u = q.popleft()
            if dist[u] < d:
                for v in adj[u]:
                    pu = pair_v[v]
                    if pu == 0:
                        d = dist[u] + 1
                    elif dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        q.append(pu)
        return d != INF

    sys.setrecursionlimit(10000000)

    def dfs(u: int) -> bool:
        for v in adj[u]:
            pu = pair_v[v]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, n + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    if matching == k:
        out = ["YES"]
        for p in range(1, k + 1):
            out.append(f"{p} {aircraft[p]} {pair_u[p]}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()