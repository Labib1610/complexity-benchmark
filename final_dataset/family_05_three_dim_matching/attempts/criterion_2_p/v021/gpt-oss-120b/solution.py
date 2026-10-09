import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # catalyst -> reagent (bijection)
    reagent_of = [0] * (k + 1)
    # ensure injective
    catalyst_of_reagent = [0] * (k + 1)

    # adjacency list from catalyst to solvents
    adj = [[] for _ in range(k + 1)]
    # store existence of triple for output
    triple_exists = dict()   # (x, z) -> (x, y, z)

    for _ in range(t):
        x = int(next(it)); y = int(next(it)); z = int(next(it))
        if reagent_of[x] == 0:
            reagent_of[x] = y
            if catalyst_of_reagent[y] != 0 and catalyst_of_reagent[y] != x:
                # violates injective, but problem guarantees not
                pass
            catalyst_of_reagent[y] = x
        # else already set, guaranteed same y
        adj[x].append(z)
        triple_exists[(x, z)] = (x, y, z)

    # quick check: every catalyst must have a reagent assigned
    for x in range(1, k + 1):
        if reagent_of[x] == 0:
            print("NO")
            return

    # Hopcroft–Karp
    INF = 10 ** 9
    pair_u = [0] * (k + 1)   # catalyst -> solvent
    pair_v = [0] * (k + 1)   # solvent -> catalyst
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
        # retrieve stored triple (x, reagent_of[x], z)
        triple = triple_exists.get((x, z))
        if triple is None:
            # should not happen
            triple = (x, reagent_of[x], z)
        out_lines.append(f"{triple[0]} {triple[1]} {triple[2]}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()