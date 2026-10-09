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
    color[start] = 0  # 0 means flag 1, 1 means flag 2
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

# Try to assign lexicographically smallest
for i in range(n):
    if color[i] == -1:
        # Try assigning 0 (flag 1) first
        color[i] = 0
        q = deque([i])
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            # Try assigning 1 (flag 2) instead
            # Reset this component
            stack = [i]
            color[i] = -1
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] != -1:
                        color[v] = -1
                        stack.append(v)
            color[i] = 1
            q = deque([i])
            ok = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                print("NO")
                sys.exit()

print("YES")
print(' '.join(str(c + 1) for c in color))