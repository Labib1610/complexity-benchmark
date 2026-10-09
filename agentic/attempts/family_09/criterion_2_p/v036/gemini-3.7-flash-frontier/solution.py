import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    k = int(data[2])

    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    # 2-color the graph to split into L and R
    color = [-1] * (n + 1)
    L = []
    R = []

    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            queue = [i]
            L.append(i)
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                c = color[u]
                nc = 1 - c
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = nc
                        if nc == 0:
                            L.append(v)
                        else:
                            R.append(v)
                        queue.append(v)

    # Direct edges from L to R
    adj_L = [[] for _ in range(n + 1)]
    for u in L:
        adj_L[u] = adj[u]

    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    INF = 10**9

    from collections import deque

    def bfs():
        q = deque()
        for u in L:
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF

        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj_L[u]:
                    pu = pair_v[v]
                    if dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        q.append(pu)
        return dist[0] != INF

    # Iterative DFS for Hopcroft-Karp
    ptr = [0] * (n + 1)

    def dfs(u):
        if u != 0:
            adj_u = adj_L[u]
            while ptr[u] < len(adj_u):
                v = adj_u[ptr[u]]
                ptr[u] += 1
                pu = pair_v[v]
                if dist[pu] == dist[u] + 1:
                    if dfs(pu):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    sys.setrecursionlimit(200000)

    while bfs():
        for u in L:
            ptr[u] = 0
        for u in L:
            if pair_u[u] == 0:
                dfs(u)

    # Konig's theorem to find maximum independent set
    # Z: vertices visited in alternating BFS from unmatched vertices in L
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)

    q = deque()
    for u in L:
        if pair_u[u] == 0:
            visited_L[u] = True
            q.append((u, 0))  # 0 means in L

    while q:
        u, side = q.popleft()
        if side == 0:
            # from L to R along non-matching edges
            for v in adj_L[u]:
                if v != pair_u[u] and not visited_R[v]:
                    visited_R[v] = True
                    q.append((v, 1))
        else:
            # from R to L along matching edges
            pu = pair_v[u]
            if pu != 0 and not visited_L[pu]:
                visited_L[pu] = True
                q.append((pu, 0))

    # Maximum independent set: (L & Z) | (R \ Z)
    independent_set = []
    for u in L:
        if visited_L[u]:
            independent_set.append(u)
    for v in R:
        if not visited_R[v]:
            independent_set.append(v)

    if len(independent_set) >= k:
        print("YES")
        print(*(independent_set[:k]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()