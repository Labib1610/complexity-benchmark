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

    for start in range(n):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        comp = [start]
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO\n")
                    return
        mn = min(comp)
        cmn = color[mn]
        for v in comp:
            ans[v] = 1 if color[v] == cmn else 2

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ans)) + "\n")

if __name__ == "__main__":
    solve()