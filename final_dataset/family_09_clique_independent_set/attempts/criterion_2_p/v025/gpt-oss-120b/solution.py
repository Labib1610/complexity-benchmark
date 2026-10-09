import sys
import collections

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # 1. bipartition
    colour = [-1] * (n + 1)
    left_nodes = []
    right_nodes = []
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        colour[start] = 0
        q = collections.deque([start])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if colour[y] == -1:
                    colour[y] = colour[x] ^ 1
                    q.append(y)
    for v in range(1, n + 1):
        if colour[v] == 0:
            left_nodes.append(v)
        else:
            right_nodes.append(v)

    # map original ids to 0‑based indices inside each side
    left_id = {v: i+1 for i, v in enumerate(left_nodes)}   # 1‑based for HK
    right_id = {v: i+1 for i, v in enumerate(right_nodes)}

    L = len(left_nodes)
    R = len(right_nodes)
    g = [[] for _ in range(L + 1)]
    for u, v in edges:
        if colour[u] == 0:
            g[left_id[u]].append(right_id[v])
        else:
            g[left_id[v]].append(right_id[u])

    # 2. Hopcroft‑Karp
    INF = 10 ** 9
    pairU = [0] * (L + 1)
    pairV = [0] * (R + 1)
    dist = [0] * (L + 1)

    def bfs() -> bool:
        q = collections.deque()
        for u in range(1, L + 1):
            if pairU[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in g[u]:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return dist[0] != INF

    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for v in g[u]:
            if dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v]):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, L + 1):
            if pairU[u] == 0 and dfs(u):
                matching += 1

    # 3. minimum vertex cover
    # BFS from free left vertices in the alternating graph
    visited_left = [False] * (L + 1)
    visited_right = [False] * (R + 1)
    q = collections.deque()
    for u in range(1, L + 1):
        if pairU[u] == 0:
            q.append(('L', u))
            visited_left[u] = True
    while q:
        side, x = q.popleft()
        if side == 'L':
            for v in g[x]:
                if not visited_right[v] and pairU[x] != v:  # unmatched edge
                    visited_right[v] = True
                    q.append(('R', v))
        else:  # side == 'R'
            pu = pairV[x]
            if pu and not visited_left[pu]:
                visited_left[pu] = True
                q.append(('L', pu))

    # min cover = (left \ Z) ∪ (right ∩ Z)
    in_cover = [False] * (n + 1)
    for i, v in enumerate(left_nodes, start=1):
        if not visited_left[i]:
            in_cover[v] = True
    for i, v in enumerate(right_nodes, start=1):
        if visited_right[i]:
            in_cover[v] = True

    independent = [v for v in range(1, n + 1) if not in_cover[v]]

    if len(independent) < k:
        print("NO")
        return
    print("YES")
    print(' '.join(map(str, independent[:k])))

if __name__ == "__main__":
    solve()