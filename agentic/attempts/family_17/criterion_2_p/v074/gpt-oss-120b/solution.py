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
    n_right = q  # vertices q+1 .. 2q mapped to 1..q
    adj = [[] for _ in range(n_left + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        # map right vertex to 1..q
        adj[a].append(b - q)

    INF = 10 ** 9

    pair_u = [0] * (n_left + 1)   # left -> right
    pair_v = [0] * (n_right + 1)  # right -> left
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

    sys.setrecursionlimit(1 << 25)
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

    out = []
    if matching == q:
        out.append("YES")
        for u in range(1, q + 1):
            v = pair_u[u]
            out.append(f"{u} {v + q}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()