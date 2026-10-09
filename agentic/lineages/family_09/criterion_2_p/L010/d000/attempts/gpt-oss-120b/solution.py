import sys
import collections

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # 1. bipartition
    color = [-1] * (n + 1)          # 0 = left, 1 = right
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = collections.deque([start])
        color[start] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)

    left = [i for i in range(1, n + 1) if color[i] == 0]
    right = [i for i in range(1, n + 1) if color[i] == 1]

    # 2. Hopcroft‑Karp
    pairU = [0] * (n + 1)   # only meaningful for left vertices
    pairV = [0] * (n + 1)   # only for right vertices
    dist = [0] * (n + 1)

    INF = 10 ** 9

    def bfs() -> bool:
        q = collections.deque()
        for u in left:
            if pairU[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        reachable = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                if pairV[v] == 0:
                    reachable = True          # free vertex on right reachable
                else:
                    pu = pairV[v]
                    if dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        q.append(pu)
        return reachable

    def dfs(u: int) -> bool:
        for v in adj[u]:
            if pairV[v] == 0 or (dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in left:
            if pairU[u] == 0 and dfs(u):
                matching += 1

    # 3. minimum vertex cover via alternating BFS
    visL = [False] * (n + 1)
    visR = [False] * (n + 1)
    q = collections.deque()
    for u in left:
        if pairU[u] == 0:
            visL[u] = True
            q.append(u)
    while q:
        u = q.popleft()
        if color[u] == 0:          # left vertex, follow non‑matched edges
            for v in adj[u]:
                if not visR[v] and pairU[u] != v:   # edge not in matching
                    visR[v] = True
                    q.append(v)
        else:                     # right vertex, follow matched edge only
            v = pairV[u]
            if v and not visL[v]:
                visL[v] = True
                q.append(v)

    # vertex cover
    cover = set()
    for u in left:
        if not visL[u]:
            cover.add(u)
    for v in right:
        if visR[v]:
            cover.add(v)

    independent = [i for i in range(1, n + 1) if i not in cover]

    if len(independent) >= k:
        print("YES")
        print(' '.join(map(str, independent[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()