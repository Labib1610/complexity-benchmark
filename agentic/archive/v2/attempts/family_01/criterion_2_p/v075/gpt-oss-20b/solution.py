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

    color = [-1] * n  # 0 -> shift 1, 1 -> shift 2

    for i in range(n):
        if color[i] != -1:
            continue
        stack = [i]
        color[i] = 0
        while stack:
            u = stack.pop()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    stack.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return

    out = ['YES', '\n', ' '.join(str(c + 1) for c in color)]
    sys.stdout.write(''.join(out))

if __name__ == "__main__":
    solve()