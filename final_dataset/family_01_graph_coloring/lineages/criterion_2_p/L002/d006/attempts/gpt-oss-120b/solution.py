import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    col = [-1] * (n + 1)          # provisional colours 0 / 1
    ans = [0] * (n + 1)           # final tiers 1 / 2

    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        # BFS for this component
        q = deque([start])
        col[start] = 0
        comp = []
        while q:
            v = q.popleft()
            comp.append(v)
            cv = col[v]
            for to in adj[v]:
                if col[to] == -1:
                    col[to] = 1 - cv
                    q.append(to)
                elif col[to] == cv:
                    sys.stdout.write("NO")
                    return
        # decide orientation: smallest index gets tier 1
        m_idx = min(comp)
        flip = col[m_idx]          # 0 -> no flip, 1 -> flip
        for v in comp:
            final_colour = col[v] ^ flip
            ans[v] = final_colour + 1   # 0->1, 1->2

    out = ["YES", " ".join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()