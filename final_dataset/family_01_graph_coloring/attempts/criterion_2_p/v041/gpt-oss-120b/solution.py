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
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    colour = [0] * (n + 1)          # 0 = uncoloured, 1 or 2 otherwise

    for v in range(1, n + 1):
        if colour[v]:
            continue
        colour[v] = 1               # smallest vertex of this component gets 1
        q = deque([v])
        while q:
            x = q.popleft()
            cx = colour[x]
            nx = 3 - cx
            for y in g[x]:
                if colour[y] == 0:
                    colour[y] = nx
                    q.append(y)
                elif colour[y] == cx:
                    sys.stdout.write("NO")
                    return

    out = ["YES\n"]
    out.append(' '.join(str(colour[i]) for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()