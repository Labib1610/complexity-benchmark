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

    color = [-1] * (n + 1)          # -1 = uncoloured, 0 or 1 otherwise
    q = deque()

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # start new component, give smallest vertex colour 0
        color[start] = 0
        q.append(start)
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - cu
                    q.append(v)
                elif color[v] == cu:
                    # conflict -> not bipartite
                    sys.stdout.write("NO")
                    return

    # feasible, produce lexicographically smallest schedule
    sys.stdout.write("YES\n")
    # shift = colour + 1
    out = ' '.join(str(color[i] + 1) for i in range(1, n + 1))
    sys.stdout.write(out)

if __name__ == "__main__":
    solve()