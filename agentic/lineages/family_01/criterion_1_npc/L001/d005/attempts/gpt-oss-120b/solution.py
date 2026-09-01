import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    col = [0] * (n + 1)          # 1‑based

    sys.setrecursionlimit(10000)

    def dfs(v: int) -> bool:    # v stations already coloured (0..n)
        if v == n:
            return True
        idx = v + 1
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if nb <= v and col[nb] == c:
                    ok = False
                    break
            if not ok:
                continue
            col[idx] = c
            if dfs(v + 1):
                return True
            col[idx] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(col[i]) for i in range(1, n + 1))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()