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
    colour = [0] * n  # 0 = uncoloured, else 1..3

    # helper: check if we can colour v with c
    def can_color(v: int, c: int) -> bool:
        for nb in adj[v]:
            if colour[nb] == c:
                return False
        return True

    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True
        # pick first uncoloured vertex in order
        for v in order:
            if colour[v] == 0:
                break
        else:
            return True  # should not happen
        for c in (1, 2, 3):
            if can_color(v, c):
                colour[v] = c
                if dfs(coloured_cnt + 1):
                    return True
                colour[v] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(colour[i]) for i in range(n))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()