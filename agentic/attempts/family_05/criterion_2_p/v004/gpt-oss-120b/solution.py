import sys
from collections import deque

def hopcroft_karp(adj, n, m):
    """adj: list (1..n) of list of right vertices (1..m)
       returns matchL (size n+1) where matchL[u]=v or 0
    """
    INF = 10 ** 9
    matchL = [0] * (n + 1)
    matchR = [0] * (m + 1)
    dist = [0] * (n + 1)

    def bfs():
        q = deque()
        for u in range(1, n + 1):
            if matchL[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if matchR[v] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    elif dist[matchR[v]] == INF:
                        dist[matchR[v]] = dist[u] + 1
                        q.append(matchR[v])
        return dist[0] != INF

    sys.setrecursionlimit(10000)
    def dfs(u):
        if u == 0:
            return True
        for v in adj[u]:
            if matchR[v] == 0 or (dist[matchR[v]] == dist[u] + 1 and dfs(matchR[v])):
                matchL[u] = v
                matchR[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, n + 1):
            if matchL[u] == 0 and dfs(u):
                matching += 1
    return matchL, matching

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    M = [0] * (k + 1)          # machine of each specialist
    adj = [[] for _ in range(k + 1)]

    for _ in range(t):
        x = int(next(it)); y = int(next(it)); z = int(next(it))
        if M[x] == 0:
            M[x] = y
        # else: guaranteed y == M[x]
        adj[x].append(z)

    # check every specialist has at least one allowed triple
    for x in range(1, k + 1):
        if M[x] == 0 or not adj[x]:
            print("NO")
            return

    matchL, size = hopcroft_karp(adj, k, k)

    if size != k:
        print("NO")
        return

    out_lines = ["YES"]
    for x in range(1, k + 1):
        out_lines.append(f"{x} {M[x]} {matchL[x]}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()