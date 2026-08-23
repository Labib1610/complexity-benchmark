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
    color[start] = 0
    q = deque([start])
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
        # attempt to assign color 0 (value 1) first for lexicographic smallest
        # We'll test if we can use 0 for this component's root
        tmp_color = [-1] * n
        tmp_color[i] = 0
        q = deque([i])
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if tmp_color[v] == -1:
                    tmp_color[v] = tmp_color[u] ^ 1
                    q.append(v)
                elif tmp_color[v] == tmp_color[u]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            # try with root = 1
            tmp_color2 = [-1] * n
            tmp_color2[i] = 1
            q = deque([i])
            ok2 = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if tmp_color2[v] == -1:
                        tmp_color2[v] = tmp_color2[u] ^ 1
                        q.append(v)
                    elif tmp_color2[v] == tmp_color2[u]:
                        ok2 = False
                        break
                if not ok2:
                    break
            if not ok2:
                print("NO")
                sys.exit()
            else:
                for j in range(n):
                    if tmp_color2[j] != -1:
                        color[j] = tmp_color2[j]
        else:
            for j in range(n):
                if tmp_color[j] != -1:
                    color[j] = tmp_color[j]

# After this, check consistency overall (safety)
for u in range(n):
    for v in adj[u]:
        if color[u] == color[v]:
            print("NO")
            sys.exit()

print("YES")
print(" ".join(str(c + 1) for c in color))