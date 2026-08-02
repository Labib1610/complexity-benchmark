import sys
sys.setrecursionlimit(1000000)

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        if u == v:
            continue
        adj[u].add(v)
        adj[v].add(u)

    color = [0] * n  # 0 uncolored, 1-3 colors

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[idx]:
                if color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            color[idx] = c
            if dfs(idx + 1):
                return True
            color[idx] = 0
        return False

    if dfs(0):
        out = ['YES', '\n', ' '.join(map(str, color))]
        sys.stdout.write(''.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()