import sys
import collections

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
        G[a].append(b - q)                  # map right vertex to 1..q

    INF = 10 ** 9
    matchL = [0] * (q + 1)
    matchR = [0] * (q + 1)
    dist = [0] * (q + 1)

    def bfs() -> bool:
        dq = collections.deque()
        for u in range(1, q + 1):
            if matchL[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        found = False
        while dq:
            u = dq.popleft()
            for v in G[u]:
                w = matchR[v]
                if w == 0:
                    found = True          # free right vertex reachable
                elif dist[w] == INF:
                    dist[w] = dist[u] + 1
                    dq.append(w)
        return found

    sys.setrecursionlimit(1 << 25)
    def dfs(u: int) -> bool:
        for v in G[u]:
            w = matchR[v]
            if w == 0 or (dist[w] == dist[u] + 1 and dfs(w)):
                matchL[u] = v
                matchR[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if matchL[u] == 0 and dfs(u):
                matching += 1

    out = []
    if matching == q:
        out.append(b"YES")
        for u in range(1, q + 1):
            v = matchL[u] + q
            out.append(f"{u} {v}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()