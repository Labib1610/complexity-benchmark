import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    ans = [1] * n

    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        comp = [start]
        min_v = start
        while q:
            x = q.popleft()
            for y in adj[x]:
                if color[y] == -1:
                    color[y] = color[x] ^ 1
                    q.append(y)
                    comp.append(y)
                    if y < min_v:
                        min_v = y
                elif color[y] == color[x]:
                    sys.stdout.write("NO")
                    return
        min_color = color[min_v]
        for v in comp:
            ans[v] = 1 if color[v] == min_color else 2

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ans)))

solve()