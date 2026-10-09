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

def bfs(start, c):
    q = deque([start])
    color[start] = c
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

# Try to color each component with starting color 1 if possible
for i in range(n):
    if color[i] == -1:
        # try starting with 1
        temp_color = color[:]
        temp_color[i] = 1
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
            # try starting with 2
            color[i] = 2
            q = deque([i])
            ok = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
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