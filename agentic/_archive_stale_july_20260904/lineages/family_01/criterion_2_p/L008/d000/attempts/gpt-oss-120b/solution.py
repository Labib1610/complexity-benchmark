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

    colour = [-1] * (n + 1)          # -1 = unvisited, 0/1 = temporary colours

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start is the smallest vertex of its component
        colour[start] = 0
        q = deque([start])
        while q:
            x = q.popleft()
            cx = colour[x]
            for y in g[x]:
                if colour[y] == -1:
                    colour[y] = cx ^ 1
                    q.append(y)
                elif colour[y] == cx:
                    # not bipartite
                    sys.stdout.write("NO")
                    return

    # feasible, produce lexicographically smallest assignment
    out = ['YES\n']
    shifts = [str(colour[i] + 1) for i in range(1, n + 1)]
    out.append(' '.join(shifts))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()