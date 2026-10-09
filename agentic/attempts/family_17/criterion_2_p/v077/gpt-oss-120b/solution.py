import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    q = next(it)
    t = next(it)

    adj = [[] for _ in range(q + 1)]  # 1-indexed left side
    for _ in range(t):
        a = next(it)
        b = next(it)
        adj[a].append(b - q)  # store right index 1..q

    INF = q + 5
    pair_u = [0] * (q + 1)   # left -> right
    pair_v = [0] * (q + 1)   # right -> left
    dist = [0] * (q + 1)

    def bfs() -> bool:
        dq = deque()
        for u in range(1, q + 1):
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
        for u in range(1, q + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    if matching != q:
        sys.stdout.write("NO")
        return

    out_lines = ["YES"]
    for u in range(1, q + 1):
        v = pair_u[u] + q
        out_lines.append(f"{u} {v}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()