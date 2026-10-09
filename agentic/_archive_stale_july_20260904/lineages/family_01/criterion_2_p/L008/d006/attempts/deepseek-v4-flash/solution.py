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

def try_assign(start_color):
    color = [-1] * n
    color[0] = start_color
    q = deque([0])
    ok = True
    while q and ok:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                ok = False
                break
    if not ok:
        return None
    # Check for disconnected components
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return None
    return color

# Try both starting colors for node 0
res1 = try_assign(0)
res2 = try_assign(1)

if res1 is None and res2 is None:
    print("NO")
else:
    # Choose the one with smaller weight
    def weight(arr):
        w = 0
        for val in arr:
            w = w * 3 + (val + 1)  # since codes are 1 or 2
        return w

    if res1 is not None and res2 is not None:
        if weight(res1) <= weight(res2):
            best = res1
        else:
            best = res2
    elif res1 is not None:
        best = res1
    else:
        best = res2

    print("YES")
    print(" ".join(str(x + 1) for x in best))