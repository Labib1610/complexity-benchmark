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

    colour = [-1] * (n + 1)          # 0 / 1 temporary colours
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        while q:
            v = q.popleft()
            cv = colour[v]
            for to in g[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    q.append(to)
                    comp.append(to)
                elif colour[to] == cv:
                    sys.stdout.write("NO")
                    return
        # orient so that minimal vertex gets colour 0
        vmin = min(comp)
        if colour[vmin] == 1:
            for v in comp:
                colour[v] ^= 1

    # build answer
    out = ['YES\n']
    out.append(' '.join(str(colour[i] + 1) for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()