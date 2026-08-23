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
    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0
        q = deque([i])
        while q:
            x = q.popleft()
            cx = color[x]
            for y in adj[x]:
                if color[y] == -1:
                    color[y] = cx ^ 1
                    q.append(y)
                elif color[y] == cx:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(c + 1) for c in color))

if __name__ == '__main__':
    solve()