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

    color = [0] * n  # 0 = uncolored, 1 or 2

    for i in range(n):
        if color[i]:
            continue
        color[i] = 1
        dq = deque([i])
        while dq:
            u = dq.popleft()
            cu = color[u]
            nv = 3 - cu
            for w in adj[u]:
                if color[w] == 0:
                    color[w] = nv
                    dq.append(w)
                elif color[w] == cu:
                    print("NO")
                    return

    out = ["YES", " ".join(str(color[i]) for i in range(n))]
    sys.stdout.write("\n".join(out))

solve()