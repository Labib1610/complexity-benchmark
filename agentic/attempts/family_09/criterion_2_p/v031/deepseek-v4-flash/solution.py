import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(n, m, adj):
    # adj: list of lists for left side (0-indexed)
    INF = 10**9
    pairU = [-1] * n
    pairV = [-1] m
    dist = [0] * n

    def bfs():
        q = deque()
        for u in range(n):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(n):
            if pairU[u] == -1 and dfs(u):
                matching += 1
    return matching, pairU, pairV

def main():
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    edges = []
    color = [-1] * n
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)

    # Bipartite coloring
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)

    left = [i for i in range(n) if color[i] == 0]
    right = [i for i in range(n) if color[i] == 1]
    left_index = {v: i for i, v in enumerate(left)}
    right_index = {v: i for i, v in enumerate(right)}

    adj_left = [[] for _ in range(len(left))]
    for u, v in edges:
        if color[u] == 0:
            adj_left[left_index[u]].append(right_index[v])
        else:
            adj_left[left_index[v]].append(right_index[u])

    matching_size, pairU, pairV = hopcroft_karp(len(left), len(right), adj_left)

    max_independent = n - matching_size
    if k > max_independent:
        print("NO")
        return

    # Find minimum vertex cover
    # From unmatched left vertices, BFS alternating paths
    visited_left = [False] * len(left)
    visited_right = [False] * len(right)

    q = deque()
    for u in range(len(left)):
        if pairU[u] == -1:
            visited_left[u] = True
            q.append(u)

    while q:
        u = q.popleft()
        for v in adj_left[u]:
            if not visited_right[v]:
                visited_right[v] = True
                pu = pairV[v]
                if pu != -1 and not visited_left[pu]:
                    visited_left[pu] = True
                    q.append(pu)

    # Minimum vertex cover: right visited + left not visited
    cover = set()
    for v in range(len(right)):
        if visited_right[v]:
            cover.add(right[v])
    for u in range(len(left)):
        if not visited_left[u]:
            cover.add(left[u])

    # Independent set = all vertices not in cover
    independent = [i for i in range(n) if i not in cover]

    # If we have more than k, we can remove some
    if len(independent) >= k:
        ans = independent[:k]
    else:
        # Need to add from cover side, but must ensure no edges among added
        # Since cover is a vertex cover, adding any vertex from cover may create edges
        # But we can add vertices from cover that are not connected to current independent set
        # Actually, we can add any vertex from cover that has no edges to current set.
        # Since we only need exactly k, and independent set size is max, we can just
        # take any k from independent set if len >= k, else impossible (but we already checked)
        ans = independent[:k]

    print("YES")
    print(" ".join(str(x+1) for x in ans))

if __name__ == "__main__":
    main()