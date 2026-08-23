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
        if u != v:
            adj[v].append(u)

    color = [-1] * n
    ans = [0] * n
    ok = True

    for i in range(n):
        if color[i] != -1:
            continue
        comp = []
        dq = deque([i])
        color[i] = 0
        comp_min = i
        while dq and ok:
            v = dq.popleft()
            comp.append(v)
            if v < comp_min:
                comp_min = v
            cv = color[v]
            for w in adj[v]:
                if color[w] == -1:
                    color[w] = 1 - cv
                    dq.append(w)
                elif color[w] == cv:
                    ok = False
                    break
        if not ok:
            break
        min_color = color[comp_min]
        for v in comp:
            ans[v] = 1 if color[v] == min_color else 2

    out = sys.stdout
    if not ok:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(" ".join(map(str, ans)))
        out.write("\n")

if __name__ == "__main__":
    solve()