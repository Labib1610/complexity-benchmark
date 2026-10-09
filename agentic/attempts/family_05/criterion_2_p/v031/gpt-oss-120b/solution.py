import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    y_of_x = [0] * (k + 1)
    adj = [[] for _ in range(k + 1)]

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        if y_of_x[x] == 0:
            y_of_x[x] = y
        # according to the statement all y for same x are equal, we ignore check
        adj[x].append(z)

    # Hopcroft‑Karp
    INF = 10 ** 9
    pair_u = [0] * (k + 1)   # match for X side, 0 = NIL
    pair_v = [0] * (k + 1)   # match for Z side
    dist = [0] * (k + 1)

    def bfs() -> bool:
        q = deque()
        for u in range(1, k + 1):
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
    out_lines = []
    for x in range(1, k + 1):
        out_lines.append(f"{x} {y_of_x[x]} {pair_u[x]}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()