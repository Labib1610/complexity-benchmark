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

    color = [0] * n  # 0 uncolored, 1 or 2 assigned
    for i in range(n):
        if color[i] != 0:
            continue
        color[i] = 1
        q = deque([i])
        while q:
            u = q.popleft()
            nxt = 3 - color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = nxt
                    q.append(v)
                elif color[v] != nxt:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()