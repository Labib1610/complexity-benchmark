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
        if u == v:
            sys.stdout.write("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    ans = [0] * n

    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0
        ans[i] = 1
        dq = deque([i])
        while dq:
            u = dq.popleft()
            cu = color[u]
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = cu ^ 1
                    ans[w] = color[w] + 1
                    dq.append(w)
                elif color[w] == cu:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n" + " ".join(map(str, ans)))

if __name__ == "__main__":
    solve()