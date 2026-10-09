import sys
import collections

def solve() -> None:
    sys.setrecursionlimit(1 << 25)
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
    left_nodes = []
    right_nodes = []
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        dq = collections.deque([start])
        color[start] = 0
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    dq.append(v)
    for v in range(1, n + 1):
        if color[v] == 0:
            left_nodes.append(v)
        else:
            right_nodes.append(v)

    # 2. Hopcroft‑Karp
    INF = 10 ** 9
    pairU = [0] * (n + 1)   # only meaningful for left side
    pairV = [0] * (n + 1)   # only for right side
    dist = [0] * (n + 1)

    left_set = set(left_nodes)   # for quick side test

    def bfs() -> bool:
        q = collections.deque()
        for u in left_nodes:
            if pairU[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                if pairV[v] == 0:
                    found = True          # we can reach free right vertex
                else:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return found

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
        for u in left_nodes:
            if pairU[u] == 0 and dfs(u):
                matching += 1

    # 3. Build Z (vertices reachable from free left vertices via alternating paths)
    visitedL = [False] * (n + 1)
    visitedR = [False] * (n + 1)
    q = collections.deque()
    for u in left_nodes:
        if pairU[u] == 0:
            visitedL[u] = True
            q.append(u)
    while q:
        u = q.popleft()
        # u is in L side
        for v in adj[u]:
            if not visitedR[v] and pairU[u] != v:   # edge not in matching
                visitedR[v] = True
                # from R we can go only via matched edge
                pu = pairV[v]
                if pu and not visitedL[pu]:
                    visitedL[pu] = True
                    q.append(pu)

    # 4. Independent set = (L ∩ Z) ∪ (R \ Z)
    indep = []
    for u in left_nodes:
        if visitedL[u]:
            indep.append(u)
    for v in right_nodes:
        if not visitedR[v]:
            indep.append(v)

    if len(indep) >= k:
        print("YES")
        print(' '.join(map(str, indep[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()