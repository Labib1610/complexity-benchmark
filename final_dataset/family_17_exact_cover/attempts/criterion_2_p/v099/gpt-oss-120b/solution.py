import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it)) - q  # shift platform index to 1..q
        adj[a].append(b)

    # Hopcroft–Karp
    NIL = 0
    INF = q + 5
    pair_u = [NIL] * (q + 1)   # left -> right
    pair_v = [NIL] * (q + 1)   # right -> left
    dist = [0] * (q + 1)

    def bfs() -> bool:
        dq = deque()
        for u in range(1, q + 1):
            if pair_u[u] == NIL:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        dist[NIL] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[NIL]:
                for v in adj[u]:
                    if pair_v[v] == NIL:
                        if dist[NIL] == INF:
                            dist[NIL] = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        dq.append(pair_v[v])
        return dist[NIL] != INF

    def dfs(u: int) -> bool:
        if u != NIL:
            for v in adj[u]:
                pu = pair_v[v]
                if pu == NIL or (dist[pu] == dist[u] + 1 and dfs(pu)):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
            dist[u] = INF
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == NIL and dfs(u):
                matching += 1

    if matching != q:
        sys.stdout.write("NO")
        return

    out_lines = ["YES"]
    for u in range(1, q + 1):
        out_lines.append(f"{u} {pair_u[u] + q}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()