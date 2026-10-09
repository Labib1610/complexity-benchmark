import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    C = 3 * k                     # number of columns
    row_masks = []                # mask for each row
    rows = []                     # original triples for output
    col_rows = [[] for _ in range(C)]

    for idx in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        mask = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))
        row_masks.append(mask)
        rows.append((x + 1, y + 1, z + 1))
        # store index in each column list
        col_rows[x].append(idx)
        col_rows[k + y].append(idx)
        col_rows[2 * k + z].append(idx)

    full_mask = (1 << C) - 1
    solution = []
    found = False

    # pre‑compute column sizes for heuristic
    col_sizes = [len(col_rows[i]) for i in range(C)]

    def choose_column(used_mask: int) -> int:
        """return an uncovered column with minimal remaining rows"""
        best = -1
        best_sz = 10**9
        m = ~used_mask & full_mask
        while m:
            c = (m & -m).bit_length() - 1
            sz = col_sizes[c]
            if sz < best_sz:
                best_sz = sz
                best = c
                if sz == 0:
                    break
            m &= m - 1
        return best

    def dfs(used_mask: int):
        nonlocal found
        if found:
            return
        if used_mask == full_mask:
            # all columns covered
            found = True
            return
        c = choose_column(used_mask)
        for r in col_rows[c]:
            rm = row_masks[r]
            if rm & used_mask:
                continue
            solution.append(r)
            dfs(used_mask | rm)
            if found:
                return
            solution.pop()

    dfs(0)

    out = []
    if found:
        out.append("YES")
        for idx in solution:
            out.append(f"{rows[idx][0]} {rows[idx][1]} {rows[idx][2]}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()