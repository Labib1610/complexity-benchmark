import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)  # 0 unvisited, 1 or 2
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        color[start] = 1
        q = deque([start])
        while q:
            v = q.popleft()
            cv = color[v]
            for w in adj[v]:
                if color[w] == 0:
                    color[w] = 3 - cv
                    q.append(w)
                elif color[w] == cv:
                    sys.stdout.write("NO")
                    return
    out = ["YES", " ".join(str(color[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

solve()