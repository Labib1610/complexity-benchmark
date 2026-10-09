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
    # Lexicographically smallest: prefer 1 over 2
    # color 0 -> mode 1, color 1 -> mode 2
    # But we can flip each component if it gives smaller lexicographic order
    # Since we start with 0 for each component, we check if flipping gives smaller
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # BFS to collect component
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
            # Count zeros and ones in this component
            zeros = sum(1 for u in comp if color[u] == 0)
            ones = len(comp) - zeros
            # If flipping gives more zeros at the smallest index, flip
            # Actually we want lexicographically smallest overall.
            # We compare the first differing position.
            # Since we process components in order of smallest index,
            # we can decide per component.
            first = min(comp)
            if color[first] == 1:
                # flipping would make it 0, which is better
                for u in comp:
                    color[u] ^= 1
            # else keep as is

    res = [1 if c == 0 else 2 for c in color]
    print("YES")
    print(" ".join(map(str, res)))