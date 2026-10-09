import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n_left = q
    n_right = q
    offset = q  # right vertices are numbered q+1 .. 2q
    adj = [[] for _ in range(n_left + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        # a is controller (1..q), b is platform (q+1..2q)
        adj[a].append(b - offset)   # store right index 1..q

    INF = 10**9

    pair_u = [0] * (n_left + 1)   # matched right for left u
    pair_v = [0] * (n_right + 1)  # matched left for right v
    dist = [0] * (n_left + 1)

    def bfs() -> bool:
        dq = deque()
        for u in range(1, n_left + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pair_v[v] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        dq.append(pair_v[v])
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
        for u in range(1, n_left + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    if matching != q:
        sys.stdout.write("NO")
        return

    out_lines = ["YES"]
    for u in range(1, q + 1):
        v = pair_u[u] + offset
        out_lines.append(f"{u} {v}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()