import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    rows = []                     # (mask, (x,y,z))   1‑based values kept for output
    col_rows = [[] for _ in range(3 * k)]

    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        mask = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))
        idx = len(rows)
        rows.append((mask, (x + 1, y + 1, z + 1)))   # store 1‑based for output
        col_rows[x].append(idx)
        col_rows[k + y].append(idx)
        col_rows[2 * k + z].append(idx)

    FULL = (1 << (3 * k)) - 1
    solution = []

    # -----------------------------------------------------------------
    def search(used_mask: int, chosen):
        """return True and fill solution when a full cover is found"""
        if used_mask == FULL:
            solution.extend(chosen)
            return True

        # find uncovered column with fewest admissible rows
        missing = (~used_mask) & FULL
        best_col = -1
        best_candidates = None

        while missing:
            # lowest set bit
            lsb = missing & -missing
            col = (lsb.bit_length() - 1)

            cand = []
            for r in col_rows[col]:
                row_mask, _ = rows[r]
                if row_mask & used_mask == 0:
                    cand.append(r)

            if not cand:               # dead end
                return False

            if best_col == -1 or len(cand) < len(best_candidates):
                best_col = col
                best_candidates = cand
                if len(best_candidates) == 1:
                    break

            missing ^= lsb

        # try each candidate row
        for r in best_candidates:
            row_mask, triple = rows[r]
            if search(used_mask | row_mask, chosen + [triple]):
                return True
        return False
    # -----------------------------------------------------------------

    if search(0, []):
        out_lines = ["YES"]
        out_lines += ["{} {} {}".format(*tr) for tr in solution]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()