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

    colour = [0] * (n + 1)          # 0 = unvisited, 1 or 2 = basis

    for i in range(1, n + 1):
        if colour[i]:
            continue
        colour[i] = 1               # smallest vertex of this component gets 1
        q = deque([i])
        while q:
            v = q.popleft()
            cv = colour[v]
            for w in adj[v]:
                if colour[w] == 0:
                    colour[w] = 3 - cv   # opposite colour
                    q.append(w)
                elif colour[w] == cv:
                    sys.stdout.write("NO")
                    return

    out = ["YES\n"]
    out.append(' '.join(str(colour[i]) for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()