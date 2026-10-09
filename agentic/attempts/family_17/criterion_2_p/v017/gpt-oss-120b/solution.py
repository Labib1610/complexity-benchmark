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
    adj = [[] for _ in range(nL)]
    for _ in range(t):
        a = int(next(it)) - 1          # 0‑based left
        b = int(next(it)) - (q + 1)    # 0‑based right
        if 0 <= a < nL and 0 <= b < nR:
            adj[a].append(b)

    INF = 10**9
    pairU = [-1] * nL
    pairV = [-1] * nR
    dist = [0] * nL

    def bfs() -> bool:
        dq = deque()
        for u in range(nL):
            if pairU[u] == -1:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        reachable = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
                elif pu == -1:
                    reachable = True
        return reachable

    def dfs(u: int) -> bool:
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
        for u in range(nL):
            if pairU[u] == -1 and dfs(u):
                matching += 1

    out = []
    if matching == q:
        out.append(b"YES")
        for u in range(nL):
            v = pairU[u]
            out.append(f"{u+1} {v+q+1}".encode())
    else:
        out.append(b"NO")
    sys.stdout.buffer.write(b"\n".join(out))

if __name__ == "__main__":
    solve()