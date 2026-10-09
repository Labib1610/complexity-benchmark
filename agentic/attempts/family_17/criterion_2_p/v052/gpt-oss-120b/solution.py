import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))

    # left vertices: 0 .. q-1   (original ids 1..q)
    # right vertices: 0 .. q-1  (original ids q+1..2q)
    G = [[] for _ in range(q)]
    for _ in range(t):
        a = int(next(it)) - 1          # 0‑based left
        b = int(next(it)) - (q + 1)    # 0‑based right
        if 0 <= a < q and 0 <= b < q:
            G[a].append(b)

    INF = 10 ** 9
    pairU = [-1] * q
    pairV = [-1] * q
    dist = [0] * q

    def bfs() -> bool:
        dq = deque()
        for u in range(q):
            if pairU[u] == -1:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        found = False
        while dq:
            u = dq.popleft()
            for v in G[u]:
                pu = pairV[v]
                if pu == -1:
                    found = True          # we can reach a free right vertex
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
        return found

    sys.setrecursionlimit(1 << 25)

    def dfs(u: int) -> bool:
        for v in G[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(q):
            if pairU[u] == -1 and dfs(u):
                matching += 1

    out = []
    if matching == q:
        out.append(b"YES")
        for u in range(q):
            v = pairU[u]
            out.append(f"{u+1} {v+q+1}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()