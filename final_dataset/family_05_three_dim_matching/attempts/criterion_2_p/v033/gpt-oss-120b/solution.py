import sys
from collections import deque

def hopcroft_karp(adj, n_left, n_right):
    """adj[u] = list of right vertices (1‑based) reachable from left vertex u (1‑based)
       returns pairU[1..n_left], pairV[1..n_right], size of matching
    """
    INF = 10 ** 9
    pairU = [0] * (n_left + 1)
    pairV = [0] * (n_right + 1)
    dist = [0] * (n_left + 1)

    def bfs():
        q = deque()
        for u in range(1, n_left + 1):
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

    def dfs(u):
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
        for u in range(1, n_left + 1):
            if pairU[u] == 0 and dfs(u):
                matching += 1
    return pairU, pairV, matching


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    x_to_y = [0] * (k + 1)
    y_to_x = [0] * (k + 1)
    Z = [[] for _ in range(k + 1)]          # Z[x] = list of allowed time slots

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        if x_to_y[x] == 0:
            x_to_y[x] = y
        elif x_to_y[x] != y:
            # contradictory input – not possible per statement
            print("NO")
            return
        if y_to_x[y] == 0:
            y_to_x[y] = x
        elif y_to_x[y] != x:
            print("NO")
            return
        Z[x].append(z)

    # every specialist and every machine must appear
    for i in range(1, k + 1):
        if x_to_y[i] == 0 or y_to_x[i] == 0:
            print("NO")
            return

    # build adjacency for Hopcroft‑Karp
    adj = [[] for _ in range(k + 1)]   # 1‑based left side (specialists)
    for x in range(1, k + 1):
        adj[x] = Z[x]

    pairU, pairV, match_sz = hopcroft_karp(adj, k, k)

    if match_sz != k:
        print("NO")
        return

    out_lines = ["YES"]
    for x in range(1, k + 1):
        y = x_to_y[x]
        z = pairU[x]
        out_lines.append(f"{x} {y} {z}")
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()