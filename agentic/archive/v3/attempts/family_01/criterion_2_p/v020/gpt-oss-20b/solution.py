import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n  # 0 -> bus 1, 1 -> bus 2

    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0
        dq = deque([i])
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    dq.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join('1' if c == 0 else '2' for c in color) + "\n")

if __name__ == "__main__":
    solve()