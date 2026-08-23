from collections import deque
import sys

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
    # Now lexicographically smallest: for each comp, try starting with hall 1
    final = [-1] * n
    for i in range(n):
        if final[i] != -1:
            continue
        # try color 0 (hall 1) for i
        c1 = [-1] * n
        c1[i] = 0
        q = deque([i])
        ok1 = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if c1[v] == -1:
                    c1[v] = c1[u] ^ 1
                    q.append(v)
                elif c1[v] == c1[u]:
                    ok1 = False
                    break
            if not ok1:
                break
        if ok1:
            for j in range(n):
                if c1[j] != -1:
                    final[j] = c1[j]
        else:
            c2 = [-1] * n
            c2[i] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if c2[v] == -1:
                        c2[v] = c2[u] ^ 1
                        q.append(v)
            for j in range(n):
                if c2[j] != -1:
                    final[j] = c2[j]

    print("YES")
    print(' '.join(str(x + 1) for x in final))