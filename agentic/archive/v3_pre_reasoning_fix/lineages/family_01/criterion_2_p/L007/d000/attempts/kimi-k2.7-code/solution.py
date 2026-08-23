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

    colors = [0] * n  # 0 unvisited, 1 or 2 assigned
    for i in range(n):
        if colors[i] != 0:
            continue
        colors[i] = 1
        dq = deque([i])
        ok = True
        while dq:
            u = dq.popleft()
            cu = colors[u]
            for w in adj[u]:
                if colors[w] == 0:
                    colors[w] = 3 - cu
                    dq.append(w)
                elif colors[w] == cu:
                    ok = False
                    dq.clear()
                    break
        if not ok:
            sys.stdout.write("NO")
            return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(map(str, colors)))

if __name__ == "__main__":
    solve()