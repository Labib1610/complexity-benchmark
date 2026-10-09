import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # -1 = unvisited, 0 or 1 otherwise

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start a new component, give smallest vertex colour 0 (-> tier 1)
        colour[start] = 0
        q = deque([start])
        while q:
            x = q.popleft()
            cx = colour[x]
            for y in adj[x]:
                if colour[y] == -1:
                    colour[y] = cx ^ 1
                    q.append(y)
                elif colour[y] == cx:
                    # not bipartite
                    sys.stdout.write("NO")
                    return

    # all good
    sys.stdout.write("YES\n")
    out = ' '.join(str(colour[i] + 1) for i in range(1, n + 1))
    sys.stdout.write(out)

if __name__ == "__main__":
    solve()