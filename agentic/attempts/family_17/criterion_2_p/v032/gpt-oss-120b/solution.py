import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(q + 1)]          # 1-indexed left side
    edge_map = {}  # (a, b') -> original b
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        b_r = b - q                           # right side index 1..q
        adj[a].append(b_r)
        edge_map[(a, b_r)] = b

    # Hopcroft–Karp
    INF = 10 ** 9
    pair_u = [0] * (q + 1)    # left -> right
    pair_v = [0] * (q + 1)    # right -> left
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
        for a in range(1, q + 1):
            b_r = pair_u[a]
            b = edge_map[(a, b_r)]
            out.append(f"{a} {b}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()