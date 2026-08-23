import sys
from collections import deque

def solve():
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

    color = [-1] * n
    q = deque()

    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0
        q.append(i)
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return

    out = ['YES', ' '.join(str(c + 1) for c in color)]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()