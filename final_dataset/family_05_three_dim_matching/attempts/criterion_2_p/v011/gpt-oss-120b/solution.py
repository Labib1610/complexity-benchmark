import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    # mapping e -> d (must be consistent)
    e_to_d = [0] * (k + 1)
    # adjacency list from e to i
    adj = [[] for _ in range(k + 1)]
    # store config for output
    config = {}
    for _ in range(t):
        e = int(next(it)); d = int(next(it)); i = int(next(it))
        if e_to_d[e] == 0:
            e_to_d[e] = d
        elif e_to_d[e] != d:
            # inconsistent input per problem statement shouldn't happen
            pass
        adj[e].append(i)
        config[(e, i)] = (e, d, i)

    # quick check: any e without edges -> impossible
    for e in range(1, k + 1):
        if not adj[e]:
            print("NO")
            return

    # Hopcroft–Karp
    INF = k + 5
    pair_u = [0] * (k + 1)   # e -> i
    pair_v = [0] * (k + 1)   # i -> e
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

    print("YES")
    out_lines = []
    for e in range(1, k + 1):
        i = pair_u[e]
        e_out, d_out, i_out = config[(e, i)]
        out_lines.append(f"{e_out} {d_out} {i_out}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()