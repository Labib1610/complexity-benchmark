import sys
from collections import deque

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n  # 0 uncolored, 1 or 2

    for i in range(n):
        if color[i] != 0:
            continue
        color[i] = 1
        q = deque([i])
        while q:
            u = q.popleft()
            cu = color[u]
            other = 3 - cu
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = other
                    q.append(v)
                elif color[v] != other:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)))

solve()