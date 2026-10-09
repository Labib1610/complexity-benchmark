import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(k + 1)]
    station = [0] * (k + 1)          # station[d] = c
    edge_exists = set()
    for _ in range(t):
        d = int(next(it)); c = int(next(it)); f = int(next(it))
        if station[d] == 0:
            station[d] = c
        # else station[d] is same by problem guarantee
        if (d, f) not in edge_exists:
            adj[d].append(f)
            edge_exists.add((d, f))

    # Hopcroft–Karp
    INF = k + 5
    pairU = [0] * (k + 1)   # drone -> frequency
    pairV = [0] * (k + 1)   # frequency -> drone
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
        print("NO")
        return

    print("YES")
    out_lines = []
    for d in range(1, k + 1):
        f = pairU[d]
        c = station[d]
        out_lines.append(f"{d} {c} {f}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()