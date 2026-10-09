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

def bfs(start):
    q = deque([start])
    color[start] = 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 3 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

# Try to color each component
for i in range(n):
    if color[i] == -1:
        # If this component can start with color 1 (smallest)
        # We must check both possibilities and pick the lexicographically best.
        # Temporarily color this component starting with 1 and 2, then compare
        tmp_color = color[:]
        color[i] = 1
        q = deque([i])
        ok1 = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 3 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    ok1 = False
                    break
            if not ok1:
                break
        if ok1:
            continue
        # If starting with 1 fails, restore and try starting with 2
        color = tmp_color
        color[i] = 2
        q = deque([i])
        ok2 = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 3 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    ok2 = False
                    break
            if not ok2:
                break
        if not ok2:
            print("NO")
            sys.exit()

print("YES")
print(" ".join(str(c) for c in color))