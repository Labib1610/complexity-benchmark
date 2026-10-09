import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    rows = []          # list of (m,c,f)
    col_rows = [[] for _ in range(3 * k)]   # column -> list of row indices

    for idx in range(t):
        m = int(next(it)) - 1
        c = int(next(it)) - 1
        f = int(next(it)) - 1
        rows.append((m, c, f))
        col_rows[m].append(idx)
        col_rows[k + c].append(idx)
        col_rows[2 * k + f].append(idx)

    # DLX structures
    n_cols = 3 * k
    # For each column, maintain a set of active rows
    active_rows = [set(col_rows[i]) for i in range(n_cols)]
    used_rows = [False] * t
    solution = []

    # heuristic: choose column with smallest active set
    def choose_column():
        min_sz = None
        chosen = -1
        for c in range(n_cols):
            sz = len(active_rows[c])
            if sz == 0:
                return -1  # dead end
            if min_sz is None or sz < min_sz:
                min_sz = sz
                chosen = c
        return chosen

    sys.setrecursionlimit(10000)
    found = False

    def search(depth: int):
        nonlocal found
        if found:
            return
        if depth == k:
            # all rows selected
            found = True
            return
        col = choose_column()
        if col == -1:
            return
        # copy list to avoid modification during iteration
        rows_list = list(active_rows[col])
        for r in rows_list:
            if used_rows[r]:
                continue
            # select row r
            used_rows[r] = True
            solution.append(r)
            # remove all columns covered by this row
            removed = []  # list of (col, rows_removed_set)
            m, c, f = rows[r]
            cols = (m, k + c, 2 * k + f)
            for cc in cols:
                # rows to be removed from other columns because they share this column
                to_remove = list(active_rows[cc])
                for rr in to_remove:
                    if rr == r:
                        continue
                    if used_rows[rr]:
                        continue
                    # remove rr from all its columns
                    mr, cr, fr = rows[rr]
                    for ccc in (mr, k + cr, 2 * k + fr):
                        if rr in active_rows[ccc]:
                            active_rows[ccc].remove(rr)
                    removed.append((rr, (mr, k + cr, 2 * k + fr)))
                # finally clear this column (row r will be removed later)
                active_rows[cc].clear()
            # recurse
            search(depth + 1)
            if found:
                return
            # backtrack
            # restore columns
            for rr, cols_rr in removed:
                mr, cr, fr = cols_rr
                for ccc in (mr, cr, fr):
                    active_rows[ccc].add(rr)
                used_rows[rr] = False
            # restore this row's columns (except the row itself)
            for cc in cols:
                active_rows[cc].add(r)
            used_rows[r] = False
            solution.pop()

    search(0)

    out = []
    if found:
        out.append("YES")
        for idx in solution:
            m, c, f = rows[idx]
            out.append(f"{m+1} {c+1} {f+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()