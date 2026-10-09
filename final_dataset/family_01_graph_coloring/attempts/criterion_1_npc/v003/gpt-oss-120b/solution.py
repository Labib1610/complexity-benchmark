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
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)

    col = [0] * n                     # 0 = uncoloured, 1..3 = colour

    # symmetry breaking: colour vertex 0 with 1
    if n > 0:
        col[0] = 1
        coloured_cnt = 1
    else:
        coloured_cnt = 0

    # pre‑compute degrees for tie‑breaking
    degree = [len(adj[v]) for v in range(n)]

    # ------------------------------------------------------------
    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True

        # ---- DSATUR: choose vertex with maximal saturation ----------
        best_v = -1
        best_sat = -1
        best_deg = -1

        for v in range(n):
            if col[v] != 0:
                continue
            used_mask = 0
            for nb in adj[v]:
                c = col[nb]
                if c:
                    used_mask |= 1 << c
            sat = (used_mask & 0b10) >> 1   # count bits 1..3
            sat += (used_mask & 0b100) >> 2
            sat += (used_mask & 0b1000) >> 3
            # popcount of three bits, faster than bin()
            if sat > best_sat or (sat == best_sat and degree[v] > best_deg):
                best_sat = sat
                best_deg = degree[v]
                best_v = v

        v = best_v

        # ---- compute allowed colours for v -------------------------
        forbidden = 0
        for nb in adj[v]:
            c = col[nb]
            if c:
                forbidden |= 1 << c

        for colour in (1, 2, 3):
            if forbidden & (1 << colour):
                continue
            col[v] = colour
            if dfs(coloured_cnt + 1):
                return True
            col[v] = 0

        return False
    # ------------------------------------------------------------

    possible = dfs(coloured_cnt)

    out = sys.stdout
    if not possible:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(" ".join(str(c) for c in col) + "\n")

if __name__ == "__main__":
    solve()