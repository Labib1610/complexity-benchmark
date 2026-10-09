import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # mapping x -> y (must be consistent)
    p = [0] * (k + 1)          # y for each x
    used_y = [0] * (k + 1)     # which x uses a y
    adj = [[] for _ in range(k + 1)]   # edges x -> z
    # store existence for output
    exists = dict()  # (x,z) -> True

    for _ in range(t):
        x = int(next(it)); y = int(next(it)); z = int(next(it))
        if p[x] == 0:
            p[x] = y
            if used_y[y]:
                # should not happen per statement
                pass
            used_y[y] = x
        # else y must equal p[x]; guaranteed
        adj[x].append(z)
        exists[(x, z)] = True

    # quick check: every x must have a y and each y used exactly once
    if any(p[x] == 0 for x in range(1, k + 1)):
        print("NO")
        return
    if any(used_y[y] == 0 for y in range(1, k + 1)):
        print("NO")
        return

    # Hopcroft–Karp
    INF = 10 ** 9
    pair_u = [0] * (k + 1)   # x -> z
    pair_v = [0] * (k + 1)   # z -> x
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

    # construct answer
    print("YES")
    out_lines = []
    for x in range(1, k + 1):
        z = pair_u[x]
        y = p[x]
        out_lines.append(f"{x} {y} {z}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()