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
        comp = []
        dq = deque([i])
        color[i] = 0
        while dq:
            u = dq.popleft()
            comp.append(u)
            cu = color[u]
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = cu ^ 1
                    dq.append(w)
                elif color[w] == cu:
                    sys.stdout.write("NO")
                    return
        min_id = min(comp)
        cmin = color[min_id]
        for v in comp:
            ans[v] = 1 if color[v] == cmin else 2

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()