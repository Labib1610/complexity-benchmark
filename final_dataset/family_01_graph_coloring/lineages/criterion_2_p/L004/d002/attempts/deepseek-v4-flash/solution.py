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

color = [-1] * n  # -1 uncolored, 0 -> value 1, 1 -> value 2

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

# Try to assign 1 to smallest uncolored node first for lexicographic order
for i in range(n):
    if color[i] == -1:
        # Try color 0 (value 1) first
        color[i] = 0
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
            # Try color 1 (value 2) for this component
            # Reset this component
            comp = [i]
            q = deque([i])
            color[i] = 1
            ok2 = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                        comp.append(v)
                    elif color[v] == color[u]:
                        ok2 = False
                        break
                if not ok2:
                    break
            if not ok2:
                print("NO")
                sys.exit()
            # else keep this coloring

# Output
res = [1 if c == 0 else 2 for c in color]
print("YES")
print(" ".join(map(str, res)))