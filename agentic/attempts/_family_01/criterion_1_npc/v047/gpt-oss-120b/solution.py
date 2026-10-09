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

    col = [0] * n                     # 0 = uncoloured, otherwise 1..3

    # ------------------------------------------------------------
    def dfs(coloured: int) -> bool:
        if coloured == n:
            return True

        # choose vertex with fewest possible colours
        best_v = -1
        best_opts = None

        for v in range(n):
            if col[v]:
                continue
            used = 0
            for nb in adj[v]:
                c = col[nb]
                if c:
                    used |= 1 << c          # bit 1<<c marks colour c as used
            opts = []
            for c in (1, 2, 3):
                if not (used & (1 << c)):
                    opts.append(c)
            if not opts:                     # dead end
                return False
            if best_v == -1 or len(opts) < len(best_opts):
                best_v = v
                best_opts = opts
                if len(best_opts) == 1:     # cannot be better
                    break

        # try all admissible colours
        for c in best_opts:
            col[best_v] = c
            if dfs(coloured + 1):
                return True
            col[best_v] = 0
        return False
    # ------------------------------------------------------------

    possible = dfs(0)

    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(c) for c in col))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()