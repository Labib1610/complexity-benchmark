import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(n, m, adj):
    # adj: list of lists for left side (0-indexed)
    INF = 10**9
    pairU = [-1] * n
    pairV = [-1] * m
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

    # We don't know which side is which, but we can color the graph.
    # Since it's bipartite, we can BFS to color.
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

    # Map right vertices to indices 0..len(right)-1
    right_index = {v: idx for idx, v in enumerate(right)}

    # Build adjacency for left side
    adj_left = [[] for _ in range(len(left))]
    for u, v in edges:
        if color[u] == 0:
            adj_left[u].append(right_index[v])
        else:
            adj_left[v].append(right_index[u])

    matching, pairU, pairV = hopcroft_karp(len(left), len(right), adj_left)

    max_independent = n - matching
    if k < max_independent:
        print("NO")
        return

    # Construct independent set of size k
    # Take all left vertices not matched, then all right vertices not matched,
    # then fill from matched pairs.
    chosen = []
    left_unmatched = [u for u in range(len(left)) if pairU[u] == -1]
    right_unmatched = [v for v in range(len(right)) if pairV[v] == -1]

    for u in left_unmatched:
        chosen.append(left[u])
    for v in right_unmatched:
        chosen.append(right[v])

    # Now add from matched pairs until we reach k
    for u in range(len(left)):
        if pairU[u] != -1:
            v = pairU[u]
            if len(chosen) < k:
                chosen.append(left[u])
            if len(chosen) < k:
                chosen.append(right[v])

    # If still not enough (shouldn't happen), add any remaining
    for i in range(n):
        if len(chosen) == k:
            break
        if i not in chosen:
            chosen.append(i)

    print("YES")
    print(" ".join(str(x + 1) for x in chosen[:k]))

if __name__ == "__main__":
    main()