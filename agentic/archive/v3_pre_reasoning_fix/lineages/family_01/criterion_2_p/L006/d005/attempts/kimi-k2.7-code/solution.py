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

    color = [-1] * (n + 1)  # 0 -> channel 1, 1 -> channel 2
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            v = q.popleft()
            cv = color[v]
            for nb in adj[v]:
                if color[nb] == -1:
                    color[nb] = cv ^ 1
                    q.append(nb)
                elif color[nb] == cv:
                    sys.stdout.write("NO")
                    return
    out = ["YES"]
    out.append(" ".join(str(color[i] + 1) for i in range(1, n + 1)))
    sys.stdout.write("\n".join(out))

solve()