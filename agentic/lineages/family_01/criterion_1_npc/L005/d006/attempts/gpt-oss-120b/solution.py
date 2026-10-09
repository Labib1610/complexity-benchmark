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

    # allowed[a][b] : True if pair (a,b) does NOT cause a collision
    allowed = [[False] * 4 for _ in range(4)]
    for a in range(1, 4):
        for b in range(1, 4):
            allowed[a][b] = ((a * a + b * b) % (a + b) != 0)

    # order vertices by decreasing degree
    order = sorted(range(n), key=lambda x: -len(adj[x]))

    col = [0] * n  # 0 = uncoloured

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if col[nb] != 0 and not allowed[c][col[nb]]:
                    ok = False
                    break
            if ok:
                col[v] = c
                if dfs(pos + 1):
                    return True
                col[v] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(col[i]) for i in range(n))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()