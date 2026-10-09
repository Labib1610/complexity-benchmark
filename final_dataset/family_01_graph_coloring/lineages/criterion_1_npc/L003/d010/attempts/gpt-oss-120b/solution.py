import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    colour = [0] * n

    if n > 0:
        colour[0] = 1                       # symmetry breaking

    # depth‑first search with MRV heuristic
    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True

        best_v = -1
        best_opts = None

        # select vertex with minimum number of allowed colours
        for v in range(n):
            if colour[v] != 0:
                continue
            used = 0
            for nb in adj[v]:
                c = colour[nb]
                if c:
                    used |= 1 << c
            opts = []
            for col in (1, 2, 3):
                if not (used >> col) & 1:
                    opts.append(col)
            if not opts:          # dead end
                return False
            if best_v == -1 or len(opts) < len(best_opts):
                best_v = v
                best_opts = opts
                if len(opts) == 1:
                    break

        for col in best_opts:
            colour[best_v] = col
            if dfs(coloured_cnt + 1):
                return True
            colour[best_v] = 0
        return False

    possible = dfs(1 if n > 0 else 0)

    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(colour[i]) for i in range(n)))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()