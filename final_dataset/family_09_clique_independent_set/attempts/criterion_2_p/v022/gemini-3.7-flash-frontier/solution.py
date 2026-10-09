import sys
from collections import deque

# Increase recursion depth for DFS
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

    # 2-color the graph to partition into L and R
    color = [-1] * (n + 1)
    L = []
    R = []

    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                c = color[u]
                if c == 0:
                    L.append(u)
                else:
                    R.append(u)
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - c
                        q.append(v)

    # Hopcroft-Karp algorithm
    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    INF = 10**9

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
                for v in adj[u]:
                    pu = pair_v[v]
                    if dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        q.append(pu)
        return dist[0] != INF

    # Pointer for current edge to ensure linear time per phase
    ptrs = [0] * (n + 1)

    def dfs(u):
        for i in range(ptrs[u], len(adj[u])):
            ptrs[u] = i + 1
            v = adj[u][i]
            pu = pair_v[v]
            if dist[pu] == dist[u] + 1:
                if dfs(pu):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
        return False

    # For node 0 (dummy node representing unmatched in R)
    # dfs(0) should return True
    # We can handle dfs: if u == 0: return True
    def dfs_full(u):
        if u == 0:
            return True
        for i in range(ptrs[u], len(adj[u])):
            ptrs[u] = i + 1
            v = adj[u][i]
            pu = pair_v[v]
            if dist[pu] == dist[u] + 1:
                if dfs_full(pu):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
        dist[u] = INF
        return False

    while bfs():
        for u in L:
            ptrs[u] = 0
        for u in L:
            if pair_u[u] == 0:
                dfs_full(u)

    # König's theorem to find Maximum Independent Set
    # Start BFS from all unmatched vertices in L
    # Directed edges:
    # From L to R: unmatched edges in the bipartite graph
    # From R to L: matched edges
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)
    q = deque()

    for u in L:
        if pair_u[u] == 0:
            visited_L[u] = True
            q.append(('L', u))

    while q:
        side, u = q.popleft()
        if side == 'L':
            for v in adj[u]:
                if pair_u[u] != v:  # unmatched edge L -> R
                    if not visited_R[v]:
                        visited_R[v] = True
                        q.append(('R', v))
        else:
            # v is in R, matched edge goes to pair_v[u]
            pu = pair_v[u]
            if pu != 0 and not visited_L[pu]:
                visited_L[pu] = True
                q.append(('L', pu))

    mis = []
    for u in L:
        if visited_L[u]:
            mis.append(u)
    for v in R:
        if not visited_R[v]:
            mis.append(v)

    if len(mis) < k:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, mis[:k])) + "\n")


if __name__ == '__main__':
    solve()