import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        g[u].append(v)
        g[v].append(u)

    col = [-1] * n
    for i in range(n):
        if col[i] != -1:
            continue
        col[i] = 0
        dq = deque([i])
        while dq:
            u = dq.popleft()
            cu = col[u]
            for v in g[u]:
                if col[v] == -1:
                    col[v] = cu ^ 1
                    dq.append(v)
                elif col[v] == cu:
                    sys.stdout.write("NO\n")
                    return

    out = ["YES", " ".join(str(c + 1) for c in col)]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()