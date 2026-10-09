import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
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
        adj[v].append(u)

    col = [0] * n          # 0 = uncoloured, else 1/2/3
    answer = None
    found = False

    def dfs(v: int) -> bool:
        nonlocal answer, found
        if v == n:
            answer = col.copy()
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
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

    if dfs(0):
        out = ['YES', ' '.join(map(str, answer))]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()