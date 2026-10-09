import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n
possible = True

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
                    possible = False
                    break
            if not possible:
                break
    if not possible:
        break

if not possible:
    print("NO")
else:
    # Now we have a valid 2-coloring, but we need lexicographically smallest.
    # We can try to flip components if it makes earlier variables smaller.
    # Since colors are 0/1, we map 0 -> 1, 1 -> 2.
    # We'll do BFS/DFS to try flipping each component if it improves lexicographic order.
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # collect component
            comp = []
            q = deque([i])
            visited[i] = True
            while q:
                u = q.popleft()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            # Try both orientations, pick lexicographically smaller
            # orientation A: keep color as is
            # orientation B: flip colors
            # We'll compare resulting h arrays for this component
            # Since components are independent, we can decide per component
            # But lexicographic order is global, so we must decide in order of smallest index.
            # So we process components in order of their smallest index.
            comp.sort()
            # Build two possible assignments for this component
            assign1 = [0] * n
            assign2 = [0] * n
            for u in comp:
                assign1[u] = color[u] + 1  # 1 or 2
                assign2[u] = 3 - assign1[u]  # flip
            # Compare at the smallest index in comp
            first = comp[0]
            if assign2[first] < assign1[first]:
                for u in comp:
                    color[u] ^= 1

    # Output
    print("YES")
    print(' '.join(str(color[i] + 1) for i in range(n)))