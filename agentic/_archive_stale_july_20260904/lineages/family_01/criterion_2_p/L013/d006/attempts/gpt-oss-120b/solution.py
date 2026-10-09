import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # -1 = unvisited, 0 or 1 = two sides

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start a new component, give the smallest vertex colour 0
        colour[start] = 0
        q = deque([start])
        while q:
            v = q.popleft()
            cv = colour[v]
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    q.append(to)
                elif colour[to] == cv:
                    # not bipartite
                    sys.stdout.write("NO")
                    return

    # all components bipartite, build answer
    out = ['YES\n']
    ans = ['1' if colour[i] == 0 else '2' for i in range(1, n + 1)]
    out.append(' '.join(ans))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()