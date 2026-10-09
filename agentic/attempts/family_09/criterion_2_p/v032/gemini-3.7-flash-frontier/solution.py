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
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # 2-color the graph to find L and R
    color = [-1] * (n + 1)
    L = []
    R = []

    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            L.append(i)
            q = [i]
            for u in q:
                c = color[u]
                nc = 1 - c
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = nc
                        if nc == 0:
                            L.append(v)
                        else:
                            R.append(v)
                        q.append(v)

    # Orient edges from L to R
    adj_L = [[] for _ in range(n + 1)]
    for u in L:
        adj_L[u] = adj[u]

    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    INF = 10**9

    matching = 0

    while True:
        # BFS
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
                for v in adj_L[u]:
                    pu = pair_v[v]
                    if dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        q.append(pu)

        if dist[0] == INF:
            break

        # DFS with edge pointers
        ptr = [0] * (n + 1)

        def dfs(u):
            d = dist[u] + 1
            neighbors = adj_L[u]
            for i in range(ptr[u], len(neighbors)):
                ptr[u] = i
                v = neighbors[i]
                pu = pair_v[v]
                if dist[pu] == d:
                    if pu == 0 or dfs(pu):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            ptr[u] = len(neighbors)
            dist[u] = INF
            return False

        for u in L:
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    mis_size = n - matching
    if mis_size < k:
        print("NO")
        return

    # Find Z (reachable vertices from unmatched L in alternating paths)
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
        for v in adj_L[u]:
            if not visited_R[v] and pair_u[u] != v:
                visited_R[v] = True
                pu = pair_v[v]
                if pu != 0 and not visited_L[pu]:
                    visited_L[pu] = True
                    q.append(pu)

    res = []
    for u in L:
        if visited_L[u]:
            res.append(u)
    for v in R:
        if not visited_R[v]:
            res.append(v)

    print("YES")
    print(*(res[:k]))

if __name__ == '__main__':
    solve()