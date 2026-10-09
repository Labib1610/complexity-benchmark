import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    mech = [0] * (k + 1)          # mech[x]
    adj = [[] for _ in range(k + 1)]   # pilot -> list of phases

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        if mech[x] == 0:
            mech[x] = y
        # otherwise y is guaranteed to be the same, no need to check
        adj[x].append(z)

    # ---------- Hopcroft–Karp ----------
    INF = 10 ** 9
    matchL = [0] * (k + 1)   # pilot -> phase
    matchR = [0] * (k + 1)   # phase -> pilot
    dist = [0] * (k + 1)

    def bfs() -> bool:
        q = deque()
        for u in range(1, k + 1):
            if matchL[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        reach_nil = INF
        while q:
            u = q.popleft()
            if dist[u] >= reach_nil:
                continue
            for v in adj[u]:
                mu = matchR[v]
                if mu == 0:
                    reach_nil = dist[u] + 1
                elif dist[mu] == INF:
                    dist[mu] = dist[u] + 1
                    q.append(mu)
        return reach_nil != INF

    sys.setrecursionlimit(10000)

    def dfs(u: int) -> bool:
        for v in adj[u]:
            mu = matchR[v]
            if mu == 0 or (dist[mu] == dist[u] + 1 and dfs(mu)):
                matchL[u] = v
                matchR[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if matchL[u] == 0 and dfs(u):
                matching += 1

    # ---------- Output ----------
    if matching == k:
        out_lines = ["YES"]
        for x in range(1, k + 1):
            out_lines.append(f"{x} {mech[x]} {matchL[x]}")
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()