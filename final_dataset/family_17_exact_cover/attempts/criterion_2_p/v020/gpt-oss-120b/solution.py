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
    adj = [[] for _ in range(nL + 1)]  # 1-indexed left
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        # b is in [q+1,2q], map to 1..q
        adj[a].append(b - q)

    # Hopcroft–Karp
    INF = 10 ** 9
    pairU = [0] * (nL + 1)   # left -> right
    pairV = [0] * (nR + 1)   # right -> left
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
                    if pairV[v] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    elif dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        dq.append(pairV[v])
        return dist[0] != INF

    sys.setrecursionlimit(1 << 25)
    def dfs(u: int) -> bool:
        if u == 0:
            return True
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
        for u in range(1, nL + 1):
            if pairU[u] == 0 and dfs(u):
                matching += 1

    out = []
    if matching == q:
        out.append("YES")
        for u in range(1, nL + 1):
            v = pairU[u]
            out.append(f"{u} {v + q}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()