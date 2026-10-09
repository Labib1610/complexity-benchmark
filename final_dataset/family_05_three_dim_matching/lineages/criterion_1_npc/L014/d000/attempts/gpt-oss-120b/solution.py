import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    rows_mask = []          # mask of the three columns
    rows_trip = []          # original triple (x,y,z)
    cols_to_rows = [[] for _ in range(3 * k)]

    for idx in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        c_base = x
        c_cat = k + y
        c_ther = 2 * k + z
        mask = (1 << c_base) | (1 << c_cat) | (1 << c_ther)
        rows_mask.append(mask)
        rows_trip.append((x + 1, y + 1, z + 1))
        cols_to_rows[c_base].append(idx)
        cols_to_rows[c_cat].append(idx)
        cols_to_rows[c_ther].append(idx)

    ALL = (1 << (3 * k)) - 1
    dead = set()                     # masks proven unsolvable

    # -------------------------------------------------------------
    def dfs(used_mask: int, solution: list) -> list | None:
        if used_mask == ALL:
            return solution
        if used_mask in dead:
            return None

        # pick uncovered column with fewest compatible rows
        uncovered = (~used_mask) & ALL
        best_col = -1
        best_cands = None
        min_len = 10 ** 9

        u = uncovered
        while u:
            low = u & -u
            col = low.bit_length() - 1
            cand = []
            for rid in cols_to_rows[col]:
                if rows_mask[rid] & used_mask == 0:
                    cand.append(rid)
            if not cand:               # dead end
                dead.add(used_mask)
                return None
            if len(cand) < min_len:
                min_len = len(cand)
                best_col = col
                best_cands = cand
                if min_len == 1:
                    break
            u ^= low

        for rid in best_cands:
            new_used = used_mask | rows_mask[rid]
            solution.append(rid)
            res = dfs(new_used, solution)
            if res is not None:
                return res
            solution.pop()

        dead.add(used_mask)
        return None
    # -------------------------------------------------------------

    ans = dfs(0, [])
    out = []
    if ans is None:
        out.append("NO")
    else:
        out.append("YES")
        for rid in ans:
            out.append("{} {} {}".format(*rows_trip[rid]))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()