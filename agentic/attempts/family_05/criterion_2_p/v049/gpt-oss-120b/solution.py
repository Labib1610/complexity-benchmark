import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    rig_of = [0] * (k + 1)          # y_x
    adj = [[] for _ in range(k + 1)]
    rec = {}                        # (x,z) -> (x,y,z)

    for _ in range(t):
        x = int(next(it)); y = int(next(it)); z = int(next(it))
        if rig_of[x] == 0:
            rig_of[x] = y
        # else: y must equal rig_of[x] by problem guarantee
        adj[x].append(z)
        rec[(x, z)] = (x, y, z)

    # ---------- Hopcroft‑Karp ----------
    INF = 10 ** 9
    pair_u = [0] * (k + 1)   # operator -> zone
    pair_v = [0] * (k + 1)   # zone -> operator
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
            pu = pair_v[v]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
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

    # ---------- Output ----------
    if matching < k:
        sys.stdout.write("NO\n")
        return

    out_lines = ["YES"]
    for x in range(1, k + 1):
        z = pair_u[x]
        out_lines.append("{} {} {}".format(*rec[(x, z)]))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()