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
    n_right = q  # vertices q+1 .. 2q, we will index them by their actual numbers

    G = [[] for _ in range(n_left + 1)]  # 1‑based left vertices
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        G[a].append(b)

    pairU = [0] * (n_left + 1)          # left -> right
    pairV = [0] * (2 * q + 1)           # right -> left
    dist = [0] * (n_left + 1)
    INF = 10 ** 9

    def bfs() -> bool:
        qd = deque()
        for u in range(1, n_left + 1):
            if pairU[u] == 0:
                dist[u] = 0
                qd.append(u)
            else:
                dist[u] = INF
        found = False
        while qd:
            u = qd.popleft()
            for v in G[u]:
                pu = pairV[v]
                if pu == 0:
                    found = True          # we can reach a free right vertex
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    qd.append(pu)
        return found

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
        for u in range(1, n_left + 1):
            if pairU[u] == 0 and dfs(u):
                matching += 1

    out = []
    if matching == q:
        out.append(b"YES")
        for u in range(1, n_left + 1):
            out.append(f"{u} {pairU[u]}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()