import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))

    G = [[] for _ in range(q)]          # left side: 0..q-1
    for _ in range(t):
        a = int(next(it)) - 1           # 0‑based Alpha
        b = int(next(it)) - (q + 1)     # 0‑based Beta
        if 0 <= a < q and 0 <= b < q:
            G[a].append(b)

    pairU = [-1] * q   # left -> right
    pairV = [-1] * q   # right -> left
    dist = [-1] * q

    INF = 10 ** 9

    def bfs() -> bool:
        dq = deque()
        for u in range(q):
            if pairU[u] == -1:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = -1
        found = False
        while dq:
            u = dq.popleft()
            for v in G[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
                elif pu == -1:
                    found = True
        return found

    sys.setrecursionlimit(1 << 25)

    def dfs(u: int) -> bool:
        for v in G[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = -1
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
            out.append(f"{u+1} {q+1+v}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()