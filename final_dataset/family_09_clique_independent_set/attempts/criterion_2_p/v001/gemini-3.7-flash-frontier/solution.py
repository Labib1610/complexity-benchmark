import sys

# Increase recursion depth for DFS in Hopcroft-Karp
sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    # 2-color the bipartite graph
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            q = [i]
            for u in q:
                c = color[u]
                nc = 1 - c
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = nc
                        q.append(v)

    # Hopcroft-Karp algorithm
    match_L = [0] * (n + 1)
    match_R = [0] * (n + 1)
    dist = [0] * (n + 1)
    ptr = [0] * (n + 1)
    INF = 10**9

    def bfs():
        q = []
        for u in range(1, n + 1):
            if color[u] == 0:
                if match_L[u] == 0:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = INF
        dist[0] = INF

        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            if dist[u] < dist[0]:
                for v in adj[u]:
                    w = match_R[v]
                    if dist[w] == INF:
                        dist[w] = dist[u] + 1
                        q.append(w)
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            adj_u = adj[u]
            for i in range(ptr[u], len(adj_u)):
                ptr[u] = i
                v = adj_u[i]
                w = match_R[v]
                if dist[w] == dist[u] + 1:
                    if dfs(w):
                        match_L[u] = v
                        match_R[v] = u
                        return True
            ptr[u] = len(adj_u)
            dist[u] = INF
            return False
        return True

    matching_size = 0
    while bfs():
        for u in range(1, n + 1):
            ptr[u] = 0
        for u in range(1, n + 1):
            if color[u] == 0 and match_L[u] == 0:
                if dfs(u):
                    matching_size += 1

    max_is_size = n - matching_size
    if max_is_size < k:
        print("NO")
        return

    # Find reachable vertices from unmatched L to construct Maximum Independent Set
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)

    q = []
    for u in range(1, n + 1):
        if color[u] == 0 and match_L[u] == 0:
            visited_L[u] = True
            q.append((u, 0))

    head = 0
    while head < len(q):
        u, side = q[head]
        head += 1
        if side == 0:
            for v in adj[u]:
                if v != match_L[u] and not visited_R[v]:
                    visited_R[v] = True
                    q.append((v, 1))
        else:
            v = match_R[u]
            if v != 0 and not visited_L[v]:
                visited_L[v] = True
                q.append((v, 0))

    res = []
    for u in range(1, n + 1):
        if color[u] == 0:
            if visited_L[u]:
                res.append(u)
        else:
            if not visited_R[u]:
                res.append(u)

    print("YES")
    print(*(res[:k]))


if __name__ == "__main__":
    solve()