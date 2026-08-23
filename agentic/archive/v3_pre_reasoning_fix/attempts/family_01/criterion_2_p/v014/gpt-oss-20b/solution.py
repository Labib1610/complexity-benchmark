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
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)  # -1: uncolored, 0 or 1

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        color[start] = 0  # lexicographically smallest: smallest vertex gets period 1
        q = deque([start])
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - cu
                    q.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(c + 1) for c in color[1:]))

if __name__ == "__main__":
    solve()