import sys
from collections import deque

def hopcroft_karp(adj, n_left, n_right):
    """adj[u] = list of right vertices (1‑based). Returns pairU, pairV, matching size."""
    pairU = [0] * (n_left + 1)
    pairV = [0] * (n_right + 1)
    dist = [0] * (n_left + 1)

    INF = 10 ** 9

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
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    k = next(it)
    t = next(it)

    tag = [0] * (k + 1)
    adj = [[] for _ in range(k + 1)]

    for _ in range(t):
        u = next(it)
        v = next(it)
        w = next(it)
        if tag[u] == 0:
            tag[u] = v
        # consistency guaranteed, no need to check
        adj[u].append(w)

    # every container must have at least one possible vessel
    for u in range(1, k + 1):
        if tag[u] == 0 or not adj[u]:
            print("NO")
            return

    pairU, _, size = hopcroft_karp(adj, k, k)

    if size == k:
        out_lines = ["YES"]
        for u in range(1, k + 1):
            w = pairU[u]
            out_lines.append(f"{u} {tag[u]} {w}")
        sys.stdout.write("\n".join(out_lines))
    else:
        print("NO")


if __name__ == "__main__":
    solve()