import sys
from collections import deque

sys.setrecursionlimit(10000)

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    k, t = data[0], data[1]
    idx = 2

    y_of_x = [0] * (k + 1)          # solvent for each catalyst
    adj = [[] for _ in range(k + 1)]   # edges x -> z

    for _ in range(t):
        x = data[idx]; y = data[idx + 1]; z = data[idx + 2]
        idx += 3
        if y_of_x[x] == 0:
            y_of_x[x] = y
        # input guarantees consistency, no need to check
        adj[x].append(z)

    # every catalyst must appear at least once
    for x in range(1, k + 1):
        if y_of_x[x] == 0:
            print("NO")
            return

    # solvents must be a permutation
    if len(set(y_of_x[1:])) != k:
        print("NO")
        return

    # ---------- Hopcroft‑Karp ----------
    INF = 10 ** 9
    pair_u = [0] * (k + 1)   # match for X side (catalyst) -> Z
    pair_v = [0] * (k + 1)   # match for Z side (temperature) -> X
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
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return dist[0] != INF

    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for v in adj[u]:
            if dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v]):
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

    # ---------- output ----------
    if matching != k:
        print("NO")
        return

    out_lines = ["YES"]
    for x in range(1, k + 1):
        out_lines.append(f"{x} {y_of_x[x]} {pair_u[x]}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()