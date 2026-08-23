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
        comp = []
        q = deque([start])
        color[start] = 0
        while q:
            v = q.popleft()
            comp.append(v)
            for w in adj[v]:
                if color[w] == -1:
                    color[w] = color[v] ^ 1
                    q.append(w)
                elif color[w] == color[v]:
                    sys.stdout.write("NO")
                    return

        mn = min(comp)
        one_color = color[mn]
        for v in comp:
            ans[v] = 1 if color[v] == one_color else 2

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()