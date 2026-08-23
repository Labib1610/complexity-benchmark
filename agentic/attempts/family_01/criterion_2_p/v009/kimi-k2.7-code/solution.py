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

    color = [0] * n  # 0 = unvisited, 1 or 2

    for start in range(n):
        if color[start]:
            continue
        dq = deque([start])
        color[start] = 1
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    dq.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return

    out = ["YES", " ".join(str(c) for c in color)]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()