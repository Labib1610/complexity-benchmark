import sys
sys.setrecursionlimit(300000)
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

color = [-1] * n

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

# first try assigning '1' (0) lexicographically
for i in range(n):
    if color[i] == -1:
        # try color 0 first
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
            # need to flip this component
            # reset component
            comp = []
            stack = [i]
            color[i] = -1
            comp.append(i)
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] != -1:
                        color[v] = -1
                        stack.append(v)
                        comp.append(v)
            # now assign with start color 1
            color[i] = 1
            q = deque([i])
            ok2 = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        ok2 = False
                        break
                if not ok2:
                    break
            if not ok2:
                print("NO")
                sys.exit()

# convert: 0 -> 1, 1 -> 2
print("YES")
print(' '.join(str(c+1) for c in color))