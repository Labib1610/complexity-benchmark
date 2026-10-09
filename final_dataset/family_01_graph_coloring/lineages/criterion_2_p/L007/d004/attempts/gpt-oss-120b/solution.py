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

    colour = [-1] * (n + 1)          # -1 = unvisited, 0 = flag 1, 1 = flag 2
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start new component, give smallest vertex flag 1 (colour 0)
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
                    sys.stdout.write("NO")
                    return

    # bipartite, construct answer
    out = ['YES\n']
    flags = [str(colour[i] + 1) for i in range(1, n + 1)]
    out.append(' '.join(flags))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()