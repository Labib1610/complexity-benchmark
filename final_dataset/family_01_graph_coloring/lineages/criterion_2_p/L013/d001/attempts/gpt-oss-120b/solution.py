import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        g[u].append(v)
        g[v].append(u)

    colour = [-1] * (n + 1)          # -1 = unvisited, 0/1 = internal colour
    q = deque()

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        colour[start] = 0            # smallest vertex of this component gets 0
        q.append(start)
        while q:
            v = q.popleft()
            cv = colour[v]
            for to in g[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    q.append(to)
                elif colour[to] == cv:
                    sys.stdout.write("NO")
                    return

    # successful colouring
    sys.stdout.write("YES\n")
    out = ' '.join(str(colour[i] + 1) for i in range(1, n + 1))
    sys.stdout.write(out)

if __name__ == "__main__":
    solve()