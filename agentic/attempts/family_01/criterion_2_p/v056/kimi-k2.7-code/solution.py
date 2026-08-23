import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n  # 0 or 1, output as 1 or 2

    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            cu = color[u]
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = cu ^ 1
                    q.append(w)
                elif color[w] == cu:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join('1' if c == 0 else '2' for c in color))

if __name__ == "__main__":
    solve()