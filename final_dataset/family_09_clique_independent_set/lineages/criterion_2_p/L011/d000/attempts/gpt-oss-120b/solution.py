import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # bipartition via BFS coloring
    side = [-1]*(n+1)   # 0 = left, 1 = right
    for start in range(1, n+1):
        if side[start] != -1:
            continue
        side[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if side[v] == -1:
                    side[v] = side[u]^1
                    q.append(v)

    # build adjacency from left to right
    left_nodes = [i for i in range(1, n+1) if side[i]==0]
    right_nodes = [i for i in range(1, n+1) if side[i]==1]
    L = len(left_nodes)
    R = len(right_nodes)

    # map node id to index in left/right arrays
    l_idx = {v:i for i,v in enumerate(left_nodes)}
    r_idx = {v:i for i,v in enumerate(right_nodes)}

    G = [[] for _ in range(L)]
    for u,v in edges:
        if side[u]==0:
            G[l_idx[u]].append(r_idx[v])
        else:
            G[l_idx[v]].append(r_idx[u])

    # Hopcroft–Karp
    INF = 10**9
    pairU = [-1]*L
    pairV = [-1]*R
    dist = [0]*L

    def bfs():
        q = deque()
        for u in range(L):
            if pairU[u]==-1:
                dist[u]=0
                q.append(u)
            else:
                dist[u]=INF
        d = INF
        while q:
            u = q.popleft()
            if dist[u] < d:
                for v in G[u]:
                    if pairV[v]==-1:
                        d = dist[u]+1
                    elif dist[pairV[v]]==INF:
                        dist[pairV[v]] = dist[u]+1
                        q.append(pairV[v])
        return d!=INF

    def dfs(u):
        for v in G[u]:
            pu = pairV[v]
            if pairV[v]==-1 or (dist[pu]==dist[u]+1 and dfs(pu)):
                pairU[u]=v
                pairV[v]=u
                return True
        dist[u]=INF
        return False

    matching = 0
    while bfs():
        for u in range(L):
            if pairU[u]==-1 and dfs(u):
                matching+=1

    max_independent_size = n - matching
    if max_independent_size < k:
        print("NO")
        return

    # find minimum vertex cover
    # BFS from unmatched left vertices on alternating graph
    visL = [False]*L
    visR = [False]*R
    q = deque()
    for u in range(L):
        if pairU[u]==-1:
            q.append(u)
            visL[u]=True
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visR[v] and pairU[u]!=v:   # edge not in matching
                visR[v]=True
                pu = pairV[v]
                if pu!=-1 and not visL[pu]:
                    visL[pu]=True
                    q.append(pu)

    # minimum vertex cover = (left not visited) U (right visited)
    # independent set = complement
    independent = []
    for i,u in enumerate(left_nodes):
        if not visL[i]:
            independent.append(u)
    for i,v in enumerate(right_nodes):
        if not visR[i]:
            independent.append(v)

    # output any k of them
    print("YES")
    print(' '.join(map(str, independent[:k])))

if __name__ == "__main__":
    solve()