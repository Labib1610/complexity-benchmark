import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []
    for _ in range(t):
        a = int(next(it)) - 1          # 0‑based
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    cols = 3 * k
    full_mask = (1 << cols) - 1

    masks = []               # mask of each row
    col_rows = [[] for _ in range(cols)]   # rows that contain column j

    for idx, (a, b, c) in enumerate(triples):
        m = (1 << a) | (1 << (k + b)) | (1 << (2 * k + c))
        masks.append(m)
        col_rows[a].append(idx)
        col_rows[k + b].append(idx)
        col_rows[2 * k + c].append(idx)

    solution = []            # indices of chosen rows
    used = set()             # for quick test if a row already taken (optional)

    sys.setrecursionlimit(10000)

    def dfs(cur_mask: int) -> bool:
        if cur_mask == full_mask:
            return True

        # choose uncovered column with fewest compatible rows
        uncovered = (~cur_mask) & full_mask
        best_col = -1
        best_cand = None

        while uncovered:
            lsb = uncovered & -uncovered
            col = (lsb.bit_length() - 1)
            uncovered ^= lsb

            cand = []
            for r in col_rows[col]:
                if masks[r] & cur_mask == 0:
                    cand.append(r)
            if not cand:
                return False          # dead end
            if best_cand is None or len(cand) < len(best_cand):
                best_cand = cand
                best_col = col
                if len(best_cand) == 1:
                    break

        for r in best_cand:
            solution.append(r)
            if dfs(cur_mask | masks[r]):
                return True
            solution.pop()
        return False

    if dfs(0):
        out_lines = ["YES"]
        for idx in solution:
            a, b, c = triples[idx]
            out_lines.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()