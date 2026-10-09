import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    y_of = [0] * (k + 1)          # filter for each emitter
    adj = [[] for _ in range(k + 1)]

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        if y_of[x] == 0:
            y_of[x] = y
        # else y must be same, guaranteed by statement
        adj[x].append(z)

    # Hopcroft‑Karp
    INF = 10 ** 9
    matchX = [0] * (k + 1)   # emitter -> detector
    matchZ = [0] * (k + 1)   # detector -> emitter
    dist = [0] * (k + 1)

    def bfs() -> bool:
        q = deque()
        for x in range(1, k + 1):
            if matchX[x] == 0:
                dist[x] = 0
                q.append(x)
            else:
                dist[x] = INF
        reachable = False
        while q:
            x = q.popleft()
            for z in adj[x]:
                nx = matchZ[z]
                if nx == 0:
                    reachable = True
                elif dist[nx] == INF:
                    dist[nx] = dist[x] + 1
                    q.append(nx)
        return reachable

    sys.setrecursionlimit(10000)
    def dfs(x: int) -> bool:
        for z in adj[x]:
            nx = matchZ[z]
            if nx == 0 or (dist[nx] == dist[x] + 1 and dfs(nx)):
                matchX[x] = z
                matchZ[z] = x
                return True
        dist[x] = INF
        return False

    matching = 0
    while bfs():
        for x in range(1, k + 1):
            if matchX[x] == 0 and dfs(x):
                matching += 1

    out = []
    if matching == k:
        out.append("YES")
        for x in range(1, k + 1):
            out.append(f"{x} {y_of[x]} {matchX[x]}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()