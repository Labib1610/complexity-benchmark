import sys
from collections import deque

def hopcroft_karp(adj, n):
    """adj: list of lists, left side size n, right side also n.
       returns pairU (size n) where pairU[u] = matched right index or -1,
               and size of matching."""
    INF = 10 ** 9
    pairU = [-1] * n
    pairV = [-1] * n
    dist = [0] * n

    def bfs():
        q = deque()
        for u in range(n):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                if pu == -1:
                    found = True
        return found

    sys.setrecursionlimit(1 << 25)
    def dfs(u):
        for v in adj[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(n):
            if pairU[u] == -1 and dfs(u):
                matching += 1
    return pairU, matching

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(q)]
    for _ in range(t):
        a = int(next(it)) - 1          # left 0‑based
        b = int(next(it)) - (q + 1)    # right 0‑based
        if 0 <= a < q and 0 <= b < q:
            adj[a].append(b)

    pairU, size = hopcroft_karp(adj, q)
    out = []
    if size == q:
        out.append(b"YES")
        for u in range(q):
            v = pairU[u]
            out.append(f"{u+1} {v+q+1}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()