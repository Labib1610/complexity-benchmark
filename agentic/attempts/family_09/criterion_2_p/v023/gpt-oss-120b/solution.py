import sys
from collections import deque

sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # 1. bipartition
    colour = [-1] * (n + 1)          # 0 = left, 1 = right
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        colour[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if colour[v] == -1:
                    colour[v] = colour[u] ^ 1
                    q.append(v)

    # build adjacency from left to right only
    left_adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        if colour[u] == 0:
            left_adj[u].append(v)
        else:
            left_adj[v].append(u)

    # 2. Hopcroft‑Karp
    pairU = [0] * (n + 1)   # left -> right
    pairV = [0] * (n + 1)   # right -> left
    dist = [0] * (n + 1)

    INF = 10 ** 9

    def bfs() -> bool:
        q = deque()
        for u in range(1, n + 1):
            if colour[u] != 0:
                continue
            if pairU[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in left_adj[u]:
                pu = pairV[v]
                if pu == 0:
                    found = True
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
        return found

    def dfs(u: int) -> bool:
        for v in left_adj[u]:
            pu = pairV[v]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, n + 1):
            if colour[u] == 0 and pairU[u] == 0:
                if dfs(u):
                    matching += 1

    # 3. minimum vertex cover / maximum independent set
    visL = [False] * (n + 1)
    visR = [False] * (n + 1)
    stack = []

    for u in range(1, n + 1):
        if colour[u] == 0 and pairU[u] == 0:
            stack.append(u)
            visL[u] = True

    while stack:
        u = stack.pop()
        if colour[u] == 0:          # left, follow unmatched edges
            for v in left_adj[u]:
                if not visR[v] and pairU[u] != v:   # edge not in matching
                    visR[v] = True
                    stack.append(v)
        else:                       # right, follow matched edge only
            pu = pairV[u]
            if pu and not visL[pu]:
                visL[pu] = True
                stack.append(pu)

    independent = []
    for v in range(1, n + 1):
        if (colour[v] == 0 and visL[v]) or (colour[v] == 1 and not visR[v]):
            independent.append(v)

    if len(independent) >= k:
        out = ['YES', ' '.join(map(str, independent[:k]))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()