import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))

    G = [[] for _ in range(q + 1)]          # 1‑based left side
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        G[a].append(b - q)                  # right side indexed 1..q

    NIL = 0
    INF = 10 ** 9
    pairU = [0] * (q + 1)   # left -> right (0 if free)
    pairV = [0] * (q + 1)   # right -> left
    dist = [0] * (q + 1)

    def bfs() -> bool:
        dq = deque()
        for u in range(1, q + 1):
            if pairU[u] == NIL:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        dist[NIL] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[NIL]:
                for v in G[u]:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        dq.append(pairV[v])
        return dist[NIL] != INF

    sys.setrecursionlimit(1 << 25)
    def dfs(u: int) -> bool:
        if u != NIL:
            for v in G[u]:
                if dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v]):
                    pairU[u] = v
                    pairV[v] = u
                    return True
            dist[u] = INF
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pairU[u] == NIL and dfs(u):
                matching += 1

    out = []
    if matching == q:
        out.append(b"YES")
        for u in range(1, q + 1):
            v = pairU[u]
            out.append(f"{u} {v + q}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()