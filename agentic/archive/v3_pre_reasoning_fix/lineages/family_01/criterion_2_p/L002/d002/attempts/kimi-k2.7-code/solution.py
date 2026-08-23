import sys
from collections import deque

def solve() -> None:
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

    color = [-1] * n  # 0 -> state 1, 1 -> state 2
    for i in range(n):
        if color[i] != -1:
            continue
        q = deque([i])
        color[i] = 0
        while q:
            v = q.popleft()
            cv = color[v]
            for w in adj[v]:
                if color[w] == -1:
                    color[w] = cv ^ 1
                    q.append(w)
                elif color[w] == cv:
                    sys.stdout.write("NO")
                    return

    states = [str(c + 1) for c in color]
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(states))

solve()