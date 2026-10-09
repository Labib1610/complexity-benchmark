import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # archive for each scholar (1-indexed)
    arch = [0] * (k + 1)
    # adjacency list from scholar to manuscripts
    adj = [[] for _ in range(k + 1)]
    # store edge existence to retrieve later
    edge_present = dict()  # (x,z) -> True

    for _ in range(t):
        x = int(next(it)); y = int(next(it)); z = int(next(it))
        if arch[x] == 0:
            arch[x] = y
        # else y must equal arch[x] by problem guarantee
        adj[x].append(z)
        edge_present[(x, z)] = True

    # Hopcroft–Karp
    INF = 10 ** 9
    pair_u = [0] * (k + 1)   # scholar -> manuscript
    pair_v = [0] * (k + 1)   # manuscript -> scholar
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

    if matching != k:
        print("NO")
        return

    # construct answer
    print("YES")
    out_lines = []
    for x in range(1, k + 1):
        y = arch[x]
        z = pair_u[x]
        # edge must exist; guaranteed by matching construction
        out_lines.append(f"{x} {y} {z}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()