import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    color = [0] * (n + 1)  # 0 unvisited, 1 or 2 assigned

    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        color[start] = 1
        q = deque([start])
        while q:
            v = q.popleft()
            cv = color[v]
            other = 3 - cv
            for to in g[v]:
                if color[to] == 0:
                    color[to] = other
                    q.append(to)
                elif color[to] == cv:
                    sys.stdout.write("NO")
                    return

    out = ["YES"]
    out.append(" ".join(map(str, color[1:])))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()