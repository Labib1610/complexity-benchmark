import sys

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

    color = [0] * n
    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if nb < idx and color[nb] == c:
                    ok = False
                    break
            if ok:
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