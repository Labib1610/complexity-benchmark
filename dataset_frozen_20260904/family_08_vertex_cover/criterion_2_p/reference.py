import sys
from collections import deque


def main():
    sys.setrecursionlimit(300000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v); adj[v].append(u)

    # 2-colour to recover the bipartition (the graph is guaranteed to split into two wings).
    color = [-1] * (n + 1)
    for s in range(1, n + 1):
        if color[s] != -1:
            continue
        color[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = color[u] ^ 1
                    q.append(w)

    A = [v for v in range(1, n + 1) if color[v] == 0]
    INF = float("inf")
    matchA = {u: 0 for u in A}
    matchB = [0] * (n + 1)
    dist = {}

    def bfs():
        q = deque()
        for u in A:
            if matchA[u] == 0:
                dist[u] = 0; q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for w in adj[u]:
                x = matchB[w]
                if x == 0:
                    found = True
                elif dist.get(x, INF) == INF:
                    dist[x] = dist[u] + 1; q.append(x)
        return found

    def dfs(u):
        for w in adj[u]:
            x = matchB[w]
            if x == 0 or (dist.get(x, INF) == dist[u] + 1 and dfs(x)):
                matchA[u] = w; matchB[w] = u
                return True
        dist[u] = INF
        return False

    while bfs():
        for u in A:
            if matchA[u] == 0:
                dfs(u)

    # Koenig: Z = alternating-reachable from unmatched A. Minimum vertex cover = (A \ Z) U (B ∩ Z),
    # whose size equals the maximum matching.
    visA = {u: False for u in A}
    visB = [False] * (n + 1)
    q = deque()
    for u in A:
        if matchA[u] == 0:
            visA[u] = True; q.append(u)
    while q:
        u = q.popleft()
        for w in adj[u]:
            if matchA[u] == w:
                continue
            if not visB[w]:
                visB[w] = True
                x = matchB[w]
                if x != 0 and not visA.get(x, False):
                    visA[x] = True; q.append(x)

    cover = [u for u in A if not visA[u]] + [v for v in range(1, n + 1)
                                             if color[v] == 1 and visB[v]]

    if len(cover) <= k:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, sorted(cover))) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
