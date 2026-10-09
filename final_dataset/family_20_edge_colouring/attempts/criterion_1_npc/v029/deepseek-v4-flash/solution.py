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

    # Find a perfect matching using simple greedy + augmenting paths
    match = [-1] * n
    match_edge = [-1] * n

    def augment(u, visited):
        for v, eid in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            if match[v] == -1 or augment(match[v], visited):
                match[v] = u
                match_edge[v] = eid
                return True
        return False

    for u in range(n):
        visited = [False] * n
        augment(u, visited)

    # Check if perfect matching exists
    if any(m == -1 for m in match):
        print("NO")
        return

    # Color matching edges with color 1
    color = [0] * m
    for v in range(n):
        if match_edge[v] != -1:
            color[match_edge[v]] = 1

    # Remaining edges form cycles; color them alternately 2 and 3
    # Build graph of remaining edges
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if color[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited = [False] * n
    for start in range(n):
        if not visited[start] and rem_adj[start]:
            # traverse cycle
            path = []
            stack = [(start, -1)]
            while stack:
                u, pe = stack.pop()
                if visited[u]:
                    continue
                visited[u] = True
                if pe != -1:
                    path.append(pe)
                for v, eid in rem_adj[u]:
                    if not visited[v]:
                        stack.append((v, eid))
            # color path alternately
            for i, eid in enumerate(path):
                color[eid] = 2 if i % 2 == 0 else 3

    # Verify
    for u in range(n):
        seen = set()
        for v, eid in adj[u]:
            seen.add(color[eid])
        if len(seen) != 3:
            print("NO")
            return

    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()