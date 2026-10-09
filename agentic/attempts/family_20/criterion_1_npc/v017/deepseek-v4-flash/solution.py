import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    # Find a perfect matching using simple greedy + augmenting path (since n <= 2000)
    match = [-1] * n
    used = [False] * n

    def augment(u):
        for v, idx in adj[u]:
            if used[v]:
                continue
            used[v] = True
            if match[v] == -1 or augment(match[v]):
                match[v] = u
                match[u] = v
                return True
        return False

    for u in range(n):
        used = [False] * n
        augment(u)

    if any(m == -1 for m in match):
        print("NO")
        return

    color = [0] * m
    matched_edge = [False] * m

    # Color matching edges with 1
    for u in range(n):
        if match[u] != -1 and u < match[u]:
            for v, idx in adj[u]:
                if v == match[u]:
                    color[idx] = 1
                    matched_edge[idx] = True
                    break

    # Remaining graph is 2-regular (cycles). Color alternately 2 and 3.
    visited = [False] * n
    for start in range(n):
        if not visited[start] and match[start] == -1 or (match[start] != -1 and not visited[start]):
            # Actually we need to traverse only non-matching edges
            pass

    # Better: build graph of non-matching edges
    adj2 = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if not matched_edge[idx]:
            adj2[u].append((v, idx))
            adj2[v].append((u, idx))

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # traverse cycle
            stack = [(i, -1, 2)]  # node, parent, color_to_assign
            visited[i] = True
            while stack:
                u, parent, c = stack.pop()
                for v, idx in adj2[u]:
                    if v == parent:
                        continue
                    if not visited[v]:
                        visited[v] = True
                        color[idx] = c
                        stack.append((v, u, 5 - c))  # switch between 2 and 3
                    else:
                        # already visited, assign color if not set
                        if color[idx] == 0:
                            color[idx] = c

    # Check if all edges colored
    if any(c == 0 for c in color):
        print("NO")
        return

    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()