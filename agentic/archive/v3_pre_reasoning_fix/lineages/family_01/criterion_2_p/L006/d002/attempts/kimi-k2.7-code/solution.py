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

    color = [0] * n  # 0 = unvisited, 1 or 2 = band

    for i in range(n):
        if color[i] != 0:
            continue
        dq = deque([i])
        color[i] = 1
        while dq:
            u = dq.popleft()
            cu = color[u]
            other = 3 - cu
            for w in adj[u]:
                if color[w] == 0:
                    color[w] = other
                    dq.append(w)
                elif color[w] == cu:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)))

solve()