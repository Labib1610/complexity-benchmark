import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    nL = q
    nR = q
    adj = [[] for _ in range(nL + 1)]
    edges = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        # map right vertex to 1..q
        b -= q
        adj[a].append(b)
        edges.append((a, b))
    # Hopcroft–Karp
    INF = 10**9
    pairU = [0] * (nL + 1)
    pairV = [0] * (nR + 1)
    dist = [0] * (nL + 1)

    def bfs() -> bool:
        dq = deque()
        for u in range(1, nL + 1):
            if pairU[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        dq.append(pairV[v])
        return dist[0] != INF

    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for v in adj[u]:
            if dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v]):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, nL + 1):
            if pairU[u] == 0 and dfs(u):
                matching += 1

    if matching != q:
        sys.stdout.write("NO")
        return

    # Build output list
    out = ["YES"]
    for u in range(1, nL + 1):
        v = pairU[u]
        out.append(f"{u} {v + q}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()