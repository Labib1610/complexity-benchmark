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

    # order vertices by decreasing degree
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    color = [0] * n  # 0 = uncoloured, else 1..3

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        # try colours 1,2,3
        for col in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if color[nb] == col:
                    ok = False
                    break
            if ok:
                color[v] = col
                if dfs(pos + 1):
                    return True
                color[v] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c) for c in color)]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()