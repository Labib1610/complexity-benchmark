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
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)

    # Color the graph
    color = [-1] * n
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)

    left = [i for i in range(n) if color[i] == 0]
    right = [i for i in range(n) if color[i] == 1]

    # Build adjacency for left side only
    left_index = {u: idx for idx, u in enumerate(left)}
    right_index = {v: idx for idx, v in enumerate(right)}
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

    # Build maximum independent set
    # Vertices not matched on left + all right vertices not matched? Actually:
    # In bipartite graph, min vertex cover = matching size.
    # Max independent set = complement of min vertex cover.
    # We can find min vertex cover from matching:
    # Start from unmatched left vertices, do alternating BFS/DFS to mark reachable.
    # Left vertices not reachable + right vertices reachable form min vertex cover.
    # Independent set = all other vertices.

    # Mark reachable
    visited_left = [False] * len(left)
    visited_right = [False] * len(right)
    q = deque()
    for u in range(len(left)):
        if pairU[u] == -1:
            visited_left[u] = True
            q.append(('L', u))
    while q:
        typ, idx = q.popleft()
        if typ == 'L':
            for v in adj_left[idx]:
                if not visited_right[v]:
                    visited_right[v] = True
                    q.append(('R', v))
        else:
            u = pairV[idx]
            if u != -1 and not visited_left[u]:
                visited_left[u] = True
                q.append(('L', u))

    # Min vertex cover: left not visited + right visited
    # Independent set: left visited + right not visited
    independent = []
    for u in range(len(left)):
        if visited_left[u]:
            independent.append(left[u])
    for v in range(len(right)):
        if not visited_right[v]:
            independent.append(right[v])

    # Now take any k from independent
    if len(independent) < k:
        print("NO")
        return
    print("YES")
    print(" ".join(str(x+1) for x in independent[:k]))

if __name__ == "__main__":
    main()