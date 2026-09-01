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

    col = [0] * n          # 0 = unassigned, otherwise 1,2,3

    def dfs(v: int) -> bool:
        if v == n:
            return True
        for code in (1, 2, 3):          # try smallest first
            ok = True
            if code == 3:               # only need to check when both are 3
                for nb in adj[v]:
                    if col[nb] == 3:
                        ok = False
                        break
            # if code != 3, no forbidden pair can appear
            if ok:
                col[v] = code
                if dfs(v + 1):
                    return True
                col[v] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c) for c in col)]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()