import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[False]*n for _ in range(n)]
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        if u==v: continue
        adj[u][v] = adj[v][u] = True

    color = [0]*n  # 0 uncolored, 1-3 colored
    solution = []

    def dfs(idx: int) -> bool:
        if idx == n:
            solution.extend(color)
            return True
        for c in (1,2,3):
            ok = True
            for nb in range(n):
                if adj[idx][nb] and color[nb] == c:
                    ok = False
                    break
            if ok:
                color[idx] = c
                if dfs(idx+1):
                    return True
                color[idx] = 0
        return False

    if dfs(0):
        out = ['YES', '\n', ' '.join(str(x) for x in solution)]
        sys.stdout.write(''.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()