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

    color = [0] * n  # 0 uncolored, 1 or 2

    for i in range(n):
        if color[i] != 0:
            continue
        color[i] = 1
        dq = deque([i])
        while dq:
            v = dq.popleft()
            cv = color[v]
            for w in adj[v]:
                if color[w] == 0:
                    color[w] = 3 - cv
                    dq.append(w)
                elif color[w] == cv:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()