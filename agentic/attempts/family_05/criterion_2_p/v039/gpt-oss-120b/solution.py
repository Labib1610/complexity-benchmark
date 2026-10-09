import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    pilot_to_aircraft = [0] * (k + 1)          # 1-indexed
    adj = [[] for _ in range(k + 1)]          # edges pilot -> path

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        if pilot_to_aircraft[x] == 0:
            pilot_to_aircraft[x] = y
        # input guarantees consistency, so we ignore further checks
        adj[x].append(z)

    # Hopcroft‑Karp
    N = k
    M = k
    pair_u = [0] * (N + 1)   # pilot -> path
    pair_v = [0] * (M + 1)   # path -> pilot
    dist = [0] * (N + 1)

    INF = 10 ** 9

    def bfs() -> bool:
        q = deque()
        for u in range(1, N + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pair_v[v] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return dist[0] != INF

    def dfs(u: int) -> bool:
        if u == 0:
            return True
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
        for u in range(1, N + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    if matching != k:
        print("NO")
        return

    print("YES")
    out_lines = []
    for pilot in range(1, k + 1):
        path = pair_u[pilot]
        aircraft = pilot_to_aircraft[pilot]
        out_lines.append(f"{pilot} {aircraft} {path}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()