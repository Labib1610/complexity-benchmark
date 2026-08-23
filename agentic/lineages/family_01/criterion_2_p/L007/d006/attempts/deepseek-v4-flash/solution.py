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

color = [-1] * n  # -1 uncolored, 0 -> state 1, 1 -> state 2

def bfs(start):
    q = deque([start])
    color[start] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

# Try to assign lexicographically smallest
for i in range(n):
    if color[i] == -1:
        # Try assigning 0 (state 1) first
        # Temporarily set and check
        temp_color = color[:]
        temp_color[i] = 0
        # BFS from i with this assignment
        q = deque([i])
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if temp_color[v] == -1:
                    temp_color[v] = 1 - temp_color[u]
                    q.append(v)
                elif temp_color[v] == temp_color[u]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            color = temp_color
        else:
            # Must assign 1 (state 2)
            color[i] = 1
            if not bfs(i):
                print("NO")
                sys.exit()

# Final check
for u in range(n):
    for v in adj[u]:
        if color[u] == color[v]:
            print("NO")
            sys.exit()

print("YES")
print(' '.join(str(c + 1) for c in color))