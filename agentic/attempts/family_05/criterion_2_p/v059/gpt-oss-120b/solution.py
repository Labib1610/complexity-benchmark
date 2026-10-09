import sys
from collections import deque

def hopcroft_karp(adj, n_left, n_right):
    # vertices are 1..n_left on left, 1..n_right on right
    INF = 10 ** 9
    pair_u = [0] * (n_left + 1)   # matched right vertex for left u
    pair_v = [0] * (n_right + 1)  # matched left vertex for right v
    dist = [0] * (n_left + 1)

    def bfs():
        q = deque()
        for u in range(1, n_left + 1):
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

    def dfs(u):
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
        for u in range(1, n_left + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1
    return matching, pair_u, pair_v

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    adj = [[] for _ in range(k + 1)]
    y_of = [0] * (k + 1)          # navigation unit for each chassis
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        if y_of[x] == 0:
            y_of[x] = y
        # else y_of[x] already set, guaranteed equal
        adj[x].append(z)

    # quick impossibility check: any chassis without edges
    for x in range(1, k + 1):
        if not adj[x]:
            print("NO")
            return

    match_size, pair_u, _ = hopcroft_karp(adj, k, k)

    if match_size != k:
        print("NO")
        return

    print("YES")
    out_lines = []
    for x in range(1, k + 1):
        z = pair_u[x]
        out_lines.append(f"{x} {y_of[x]} {z}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()