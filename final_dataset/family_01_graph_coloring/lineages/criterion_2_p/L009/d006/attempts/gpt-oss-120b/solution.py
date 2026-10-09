import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # temporary 0 / 1
    ans = [0] * (n + 1)              # final 1 / 2

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # new component, BFS
        q = deque([start])
        colour[start] = 0
        comp = [start]

        while q:
            v = q.popleft()
            cv = colour[v]
            for nb in adj[v]:
                if colour[nb] == -1:
                    colour[nb] = cv ^ 1
                    q.append(nb)
                    comp.append(nb)
                elif colour[nb] == cv:
                    sys.stdout.write("NO")
                    return

        # decide orientation: smallest index = start
        if colour[start] == 0:      # keep mapping 0->1, 1->2
            for v in comp:
                ans[v] = 1 if colour[v] == 0 else 2
        else:                       # swap
            for v in comp:
                ans[v] = 1 if colour[v] == 1 else 2

    out = ["YES\n"]
    out.append(' '.join(str(ans[i]) for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()