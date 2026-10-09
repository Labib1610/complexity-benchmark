import sys
import collections

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))

    adj = [[] for _ in range(q + 1)]          # 1‑based left vertices
    for _ in range(t):
        a = int(next(it))
        b = int(next(it)) - q                 # map right side to 1..q
        if 1 <= a <= q and 1 <= b <= q:
            adj[a].append(b)

    # Hopcroft‑Karp
    INF = 10 ** 9
    pairU = [0] * (q + 1)   # left -> right
    pairV = [0] * (q + 1)   # right -> left
    dist = [0] * (q + 1)

    def bfs() -> bool:
        qd = collections.deque()
        for u in range(1, q + 1):
            if pairU[u] == 0:
                dist[u] = 0
                qd.append(u)
            else:
                dist[u] = INF
        found = False
        while qd:
            u = qd.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu == 0:
                    found = True          # free right reachable
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    qd.append(pu)
        return found

    sys.setrecursionlimit(1 << 25)
    def dfs(u: int) -> bool:
        for v in adj[u]:
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
        for u in range(1, q + 1):
            v = pairU[u] + q
            out.append(f"{u} {v}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()