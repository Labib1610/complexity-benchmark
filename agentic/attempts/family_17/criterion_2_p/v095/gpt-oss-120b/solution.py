import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(q + 1)]  # 1-indexed left side
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        # a in [1,q], b in [q+1,2q]
        adj[a].append(b - q)  # store right index as 1..q

    # Hopcroft–Karp
    INF = 10 ** 9
    pair_u = [0] * (q + 1)   # left -> right (0 if free)
    pair_v = [0] * (q + 1)   # right -> left (0 if free)
    dist = [0] * (q + 1)

    def bfs() -> bool:
        dq = deque()
        for u in range(1, q + 1):
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

    sys.setrecursionlimit(1 << 25)

    def dfs(u: int) -> bool:
        if u == 0:
            return True
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