import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    adj_all = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj_all[u].append(v)
        adj_all[v].append(u)
        idx += 2

    # 2-color the bipartite graph
    color = [-1] * (n + 1)
    L = []
    R = []
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            L.append(i)
            queue = [i]
            for u in queue:
                c = color[u]
                nc = 1 - c
                for v in adj_all[u]:
                    if color[v] == -1:
                        color[v] = nc
                        if nc == 0:
                            L.append(v)
                        else:
                            R.append(v)
                        queue.append(v)

    adj = [[] for _ in range(n + 1)]
    for u in L:
        adj[u] = adj_all[u]

    # Hopcroft-Karp algorithm for Maximum Bipartite Matching
    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    INF = 10**9

    sys.setrecursionlimit(200000)

    def bfs():
        q = []
        for u in L:
            if pair_u[u] == 0:
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
                    u2 = pair_v[v]
                    if dist[u2] == INF:
                        dist[u2] = dist[u] + 1
                        q.append(u2)
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                u2 = pair_v[v]
                if dist[u2] == dist[u] + 1:
                    if dfs(u2):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    matching = 0
    while bfs():
        for u in L:
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    mis_size = n - matching
    if mis_size < k:
        print("NO")
        return

    # Find reachable vertices Z from unmatched vertices in L
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)
    q = []
    for u in L:
        if pair_u[u] == 0:
            visited_L[u] = True
            q.append(u)

    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        for v in adj[u]:
            if v != pair_u[u] and not visited_R[v]:
                visited_R[v] = True
                u2 = pair_v[v]
                if u2 != 0 and not visited_L[u2]:
                    visited_L[u2] = True
                    q.append(u2)

    mis = []
    for u in L:
        if visited_L[u]:
            mis.append(u)
    for v in R:
        if not visited_R[v]:
            mis.append(v)

    print("YES")
    print(*(mis[:k]))


if __name__ == "__main__":
    solve()