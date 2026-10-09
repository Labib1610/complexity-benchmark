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
    limit = 3 * q
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        if a + b <= limit:
            G[a].append(b - q)               # right vertex in 1..q

    # Hopcroft‑Karp
    INF = 10 ** 9
    pairU = [0] * (q + 1)    # left -> right
    pairV = [0] * (q + 1)    # right -> left
    dist = [0] * (q + 1)

    def bfs() -> bool:
        dq = deque()
        for u in range(1, q + 1):
            if pairU[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        reachable = False
        while dq:
            u = dq.popleft()
            for v in G[u]:
                pu = pairV[v]
                if pu == 0:
                    reachable = True
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
        return reachable

    sys.setrecursionlimit(1 << 25)
    def dfs(u: int) -> bool:
        for v in G[u]:
            pu = pairV[v]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pairU[u] == 0 and dfs(u):
                matching += 1

    out = []
    if matching == q:
        out.append(b"YES")
        for a in range(1, q + 1):
            b = pairU[a] + q
            out.append(f"{a} {b}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()