import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    truck = [0] * (k + 1)          # truck[x]
    adj = [[] for _ in range(k + 1)]   # edges from driver to route
    # store triples for output
    edge_info = dict()            # (x, z) -> (x, y, z)

    for _ in range(t):
        x = int(next(it)); y = int(next(it)); z = int(next(it))
        if truck[x] == 0:
            truck[x] = y
        # add edge
        adj[x].append(z)
        edge_info[(x, z)] = (x, y, z)

    # Hopcroft‑Karp
    INF = 10 ** 9
    pairU = [0] * (k + 1)   # driver -> route
    pairV = [0] * (k + 1)   # route -> driver
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

    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for v in adj[u]:
            if pairV[v] == 0 or (dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])):
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

    if matching != k:
        sys.stdout.write("NO")
        return

    out_lines = ["YES"]
    for x in range(1, k + 1):
        z = pairU[x]
        # retrieve stored triple (x, truck[x], z)
        _, y, _ = edge_info[(x, z)]
        out_lines.append(f"{x} {y} {z}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()