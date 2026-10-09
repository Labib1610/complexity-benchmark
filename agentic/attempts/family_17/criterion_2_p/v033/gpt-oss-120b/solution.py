import sys
from collections import deque

def hopcroft_karp(adj, n_left, n_right):
    # vertices: left 1..n_left, right 1..n_right (we will store original ids)
    pair_u = [0] * (n_left + 1)
    pair_v = [0] * (n_right + 1)
    dist = [0] * (n_left + 1)

    INF = 10 ** 9

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
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return dist[0] != INF

    sys.setrecursionlimit(1 << 25)
    def dfs(u):
        if u == 0:
            return True
        for v in adj[u]:
            if dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v]):
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
    return matching, pair_u

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n_left = q
    n_right = q
    adj = [[] for _ in range(n_left + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        # map platform id to 1..q
        adj[a].append(b - q)
    matching, pair_u = hopcroft_karp(adj, n_left, n_right)
    out = []
    if matching == q:
        out.append(b"YES")
        for u in range(1, q + 1):
            v = pair_u[u] + q  # restore original platform id
            out.append(f"{u} {v}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()