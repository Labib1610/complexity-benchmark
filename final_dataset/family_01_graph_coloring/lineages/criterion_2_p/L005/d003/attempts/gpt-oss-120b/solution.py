import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    col = [-1] * (n + 1)          # -1 = unvisited, 0/1 = parity
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        col[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for to in g[v]:
                if col[to] == -1:
                    col[to] = col[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif col[to] == col[v]:
                    print("NO")
                    return
        # decide orientation: smallest vertex gets mode 1
        v0 = min(comp)
        p = col[v0]
        for v in comp:
            ans[v] = 1 if col[v] == p else 2

    # output
    out = ["YES", " ".join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()