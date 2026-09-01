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

color = [-1] * n  # 0 -> level 1, 1 -> level 2

def bfs(start):
    q = deque([start])
    color[start] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            print("NO")
            sys.exit()

# Now we have a valid bipartition, but we need lexicographically smallest.
# We'll re-run with greedy assignment: try 1 (0) first, if conflict, use 2 (1).
color = [-1] * n

def bfs_greedy(start):
    q = deque([start])
    # Try assigning level 1 (0) to start
    color[start] = 0
    q.append(start)
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

for i in range(n):
    if color[i] == -1:
        # Try with 0 first
        temp_color = color[:]
        temp_color[i] = 0
        q = deque([i])
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if temp_color[v] == -1:
                    temp_color[v] = temp_color[u] ^ 1
                    q.append(v)
                elif temp_color[v] == temp_color[u]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            color = temp_color
        else:
            # Must assign 1 (level 2)
            color[i] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)

print("YES")
print(" ".join(str(c + 1) for c in color))