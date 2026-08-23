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
    ans = [0] * n

    for i in range(n):
        if color[i] != -1:
            continue
        dq = deque([i])
        color[i] = 0
        while dq:
            u = dq.popleft()
            ans[u] = color[u] + 1
            desired = color[u] ^ 1
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = desired
                    dq.append(w)
                elif color[w] != desired:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()