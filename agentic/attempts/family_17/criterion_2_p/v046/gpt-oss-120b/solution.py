import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b - q)          # right side indexed 1..q

    INF = q + 5
    matchL = [0] * (q + 1)   # left -> right
    matchR = [0] * (q + 1)   # right -> left
    dist = [0] * (q + 1)

    def bfs() -> bool:
        dq = deque()
        for u in range(1, q + 1):
            if matchL[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        reachable = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                mu = matchR[v]
                if mu == 0:
                    reachable = True
                elif dist[mu] == INF:
                    dist[mu] = dist[u] + 1
                    dq.append(mu)
        return reachable

    sys.setrecursionlimit(1 << 25)
    def dfs(u: int) -> bool:
        for v in adj[u]:
            mu = matchR[v]
            if mu == 0 or (dist[mu] == dist[u] + 1 and dfs(mu)):
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
        out.append("YES")
        for u in range(1, q + 1):
            out.append(f"{u} {q + matchL[u]}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()