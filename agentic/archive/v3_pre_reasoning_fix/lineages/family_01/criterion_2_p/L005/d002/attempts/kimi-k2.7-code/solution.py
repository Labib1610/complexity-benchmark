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
    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0
        q = deque([i])
        ok = True
        while q:
            v = q.popleft()
            for w in adj[v]:
                if color[w] == -1:
                    color[w] = color[v] ^ 1
                    q.append(w)
                elif color[w] == color[v]:
                    ok = False
        if not ok:
            sys.stdout.write("NO")
            return

    out = [c + 1 for c in color]
    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(map(str, out)))

if __name__ == "__main__":
    solve()