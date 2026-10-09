import sys
sys.setrecursionlimit(10000)

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

    col = [0] * (n + 1)
    found = False

    def dfs(v: int):
        nonlocal found
        if found:
            return
        if v == n + 1:
            # all coloured
            print("YES")
            print(' '.join(str(col[i]) for i in range(1, n + 1)))
            found = True
            return
        for c in (1, 2, 3):
            ok = True
            for nb in g[v]:
                if col[nb] == c:
                    ok = False
                    break
            if ok:
                col[v] = c
                dfs(v + 1)
                if found:
                    return
                col[v] = 0

    dfs(1)
    if not found:
        print("NO")

if __name__ == "__main__":
    solve()