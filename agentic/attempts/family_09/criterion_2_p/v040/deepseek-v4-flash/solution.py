import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(n, m, adj, U):
    # U: list of left side vertices (0-indexed)
    pairU = [-1] * n
    pairV = [-1] * m
    dist = [0] * n

    def bfs():
        q = deque()
        for u in U:
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = float('inf')
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == float('inf'):
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
        dist[u] = float('inf')
        return False

    matching = 0
    while bfs():
        for u in U:
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
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # Bipartite coloring
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
                    elif color[v] == color[u]:
                        # Should not happen per problem statement
                        pass

    left = [i for i in range(n) if color[i] == 0]
    right = [i for i in range(n) if color[i] == 1]

    if len(left) >= k:
        print("YES")
        print(" ".join(str(x+1) for x in left[:k]))
        return
    if len(right) >= k:
        print("YES")
        print(" ".join(str(x+1) for x in right[:k]))
        return

    # Need to construct maximum independent set
    # Build adjacency for left side only
    left_index = {v: i for i, v in enumerate(left)}
    right_index = {v: i for i, v in enumerate(right)}
    adj_left = [[] for _ in range(len(left))]
    for u, v in edges:
        if color[u] == 0:
            adj_left[left_index[u]].append(right_index[v])
        else:
            adj_left[left_index[v]].append(right_index[u])

    matching_size, pairU, pairV = hopcroft_karp(len(left), len(right), adj_left, list(range(len(left))))

    max_independent_size = n - matching_size
    if max_independent_size < k:
        print("NO")
        return

    # Build min vertex cover via König's theorem
    # Mark vertices reachable from unmatched left vertices
    visited_left = [False] * len(left)
    visited_right = [False] * len(right)

    q = deque()
    for i, u in enumerate(left):
        if pairU[i] == -1:
            visited_left[i] = True
            q.append(i)

    while q:
        i = q.popleft()
        for j in adj_left[i]:
            if not visited_right[j]:
                visited_right[j] = True
                if pairV[j] != -1 and not visited_left[pairV[j]]:
                    visited_left[pairV[j]] = True
                    q.append(pairV[j])

    # Min vertex cover: left not visited + right visited
    cover = set()
    for i in range(len(left)):
        if not visited_left[i]:
            cover.add(left[i])
    for j in range(len(right)):
        if visited_right[j]:
            cover.add(right[j])

    independent = [v for v in range(n) if v not in cover]
    if len(independent) >= k:
        print("YES")
        print(" ".join(str(x+1) for x in independent[:k]))
    else:
        print("NO")

if __name__ == "__main__":
    main()