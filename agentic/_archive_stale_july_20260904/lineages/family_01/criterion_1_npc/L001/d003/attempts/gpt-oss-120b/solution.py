import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        neighbors[u].append(v)
        neighbors[v].append(u)

    col = [0] * (n + 1)          # 0 = uncoloured

    def dfs(v: int) -> bool:
        if v == n + 1:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in neighbors[v]:
                if col[nb] == c:
                    ok = False
                    break
            if not ok:
                continue
            col[v] = c
            if dfs(v + 1):
                return True
            col[v] = 0
        return False

    if dfs(1):
        out = ['YES', ' '.join(str(col[i]) for i in range(1, n + 1))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()