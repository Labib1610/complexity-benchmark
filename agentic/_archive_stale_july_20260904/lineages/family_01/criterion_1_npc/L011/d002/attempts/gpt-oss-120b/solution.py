import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    colors = [0] * (n + 1)
    found = False

    def dfs(v: int) -> bool:
        if v > n:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if colors[nb] == c:
                    ok = False
                    break
            if not ok:
                continue
            colors[v] = c
            if dfs(v + 1):
                return True
            colors[v] = 0
        return False

    if dfs(1):
        out = ['YES', ' '.join(str(colors[i]) for i in range(1, n + 1))]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()