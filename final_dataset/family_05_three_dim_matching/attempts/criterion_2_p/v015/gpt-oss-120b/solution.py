import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    driver_truck = [0] * (k + 1)          # 1‑based
    adj = [[] for _ in range(k + 1)]     # routes reachable from driver

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        if driver_truck[x] == 0:
            driver_truck[x] = y
        # edge driver x -> route z
        adj[x].append(z)

    # ---------- Hopcroft‑Karp ----------
    INF = 10 ** 9
    pairU = [0] * (k + 1)   # driver -> route
    pairV = [0] * (k + 1)   # route  -> driver
    dist = [0] * (k + 1)

    def bfs() -> bool:
        q = deque()
        for u in range(1, k + 1):
            if pairU[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pairV[v] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    elif dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return dist[0] != INF

    sys.setrecursionlimit(10000)
    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for v in adj[u]:
            pu = pairV[v]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pairU[u] == 0 and dfs(u):
                matching += 1

    # ---------- Output ----------
    out = []
    if matching == k:
        out.append(b"YES")
        for x in range(1, k + 1):
            y = driver_truck[x]
            z = pairU[x]
            out.append(f"{x} {y} {z}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()