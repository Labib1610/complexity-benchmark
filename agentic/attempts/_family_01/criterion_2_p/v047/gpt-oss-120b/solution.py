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

    colour = [0] * (n + 1)          # 0 = unvisited, 1 or 2 otherwise
    q = deque()

    for start in range(1, n + 1):
        if colour[start]:
            continue
        # start new component, give smallest vertex colour 1
        colour[start] = 1
        q.append(start)
        while q:
            v = q.popleft()
            cv = colour[v]
            nxt = 2 if cv == 1 else 1
            for nb in adj[v]:
                if colour[nb] == 0:
                    colour[nb] = nxt
                    q.append(nb)
                elif colour[nb] != nxt:
                    # conflict -> not bipartite
                    sys.stdout.write("NO")
                    return

    # all good
    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(colour[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()