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
        dq = deque([i])
        color[i] = 0
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

    ans = ' '.join(str(color[i] + 1) for i in range(n))
    sys.stdout.write("YES\n" + ans + "\n")

if __name__ == "__main__":
    solve()