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
    # adjacency for left vertices 1..q, store right ids (q+1..2q)
    adj = [[] for _ in range(n_left + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)

    # Hopcroft–Karp
    INF = 10 ** 9
    pair_u = [0] * (n_left + 1)          # left -> right
    pair_v = [0] * (2 * q + 1)           # right (actual ids) -> left
    dist = [0] * (n_left + 1)

    def bfs() -> bool:
        dq = deque()
        for u in range(1, n_left + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        reachable = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu == 0:
                    reachable = True
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
        return reachable

    def dfs(u: int) -> bool:
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
        for u in range(1, n_left + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    if matching != q:
        sys.stdout.write("NO")
        return

    out_lines = ["YES"]
    for u in range(1, n_left + 1):
        out_lines.append(f"{u} {pair_u[u]}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()