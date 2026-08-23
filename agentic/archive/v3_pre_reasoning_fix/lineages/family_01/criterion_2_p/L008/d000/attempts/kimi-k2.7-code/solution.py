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
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        comp = []
        while q:
            v = q.popleft()
            comp.append(v)
            cv = color[v]
            for nb in adj[v]:
                if color[nb] == -1:
                    color[nb] = cv ^ 1
                    q.append(nb)
                elif color[nb] == cv:
                    sys.stdout.write("NO\n")
                    return

        min_v = min(comp)
        flip = color[min_v]  # make the smallest-index vertex team 1
        for v in comp:
            ans[v] = (color[v] ^ flip) + 1

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ans[1:])))

if __name__ == "__main__":
    solve()