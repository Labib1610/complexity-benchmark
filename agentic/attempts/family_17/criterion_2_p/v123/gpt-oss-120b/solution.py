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
    n_right = q  # vertices q+1 .. 2q, we will index them 1..q as well
    G = [[] for _ in range(n_left + 1)]  # 1‑based left vertices

    for _ in range(t):
        a = int(next(it))
        b = int(next(it)) - q          # shift right side to 1..q
        if 1 <= a <= q and 1 <= b <= q:
            G[a].append(b)

    # Hopcroft‑Karp
    INF = 10 ** 9
    pairU = [0] * (n_left + 1)
    pairV = [0] * (n_right + 1)
    dist = [0] * (n_left + 1)

    def bfs() -> bool:
        dq = deque()
        for u in range(1, n_left + 1):
            if pairU[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[0]:
                for v in G[u]:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        dq.append(pairV[v])
        return dist[0] != INF

    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for v in G[u]:
            if dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v]):
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
        for u in range(1, q + 1):
            v = pairU[u] + q          # restore original right id
            out.append(f"{u} {v}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()