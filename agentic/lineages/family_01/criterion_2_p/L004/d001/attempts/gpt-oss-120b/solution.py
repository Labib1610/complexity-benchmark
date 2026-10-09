import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it)
        g[u].append(v)
        g[v].append(u)

    parity = [-1] * (n + 1)          # 0 / 1
    ans = [0] * (n + 1)              # final 1 / 2

    for start in range(1, n + 1):
        if parity[start] != -1:
            continue
        # new component
        q = deque([start])
        parity[start] = 0
        comp = []
        while q:
            u = q.popleft()
            comp.append(u)
            pu = parity[u]
            for v in g[u]:
                if parity[v] == -1:
                    parity[v] = pu ^ 1
                    q.append(v)
                elif parity[v] == pu:
                    # not bipartite
                    sys.stdout.write("NO")
                    return
        # decide orientation: smallest index gets colour 1
        minv = min(comp)
        if parity[minv] == 0:
            for v in comp:
                ans[v] = 1 if parity[v] == 0 else 2
        else:
            for v in comp:
                ans[v] = 2 if parity[v] == 0 else 1

    out = ["YES", " ".join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()