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
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)

    colour = [0] * (n + 1)  # 1‑based

    def dfs(v: int) -> bool:
        if v == n + 1:
            return True
        for col in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if colour[nb] == col:
                    ok = False
                    break
            if not ok:
                continue
            colour[v] = col
            if dfs(v + 1):
                return True
            colour[v] = 0
        return False

    if dfs(1):
        out = ['YES', ' '.join(str(colour[i]) for i in range(1, n + 1))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()