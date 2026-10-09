import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)
    for i in range(1, n + 1):
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
    sys.stdout.write(' '.join(str(color[i] + 1) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()