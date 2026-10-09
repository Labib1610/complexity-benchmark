import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    rows = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append((a, b, c))

    # columns: 0..k-1 for first coord, k..2k-1 for second, 2k..3k-1 for third
    ncol = 3 * k
    col_size = [0] * ncol
    # for each column keep list of row indices covering it
    col_rows = [[] for _ in range(ncol)]

    for idx, (a, b, c) in enumerate(rows):
        cols = (a, k + b, 2 * k + c)
        for col in cols:
            col_rows[col].append(idx)
            col_size[col] += 1

    # DLX structures
    # For each row store its three columns
    row_cols = [None] * t
    for idx, (a, b, c) in enumerate(rows):
        row_cols[idx] = (a, k + b, 2 * k + c)

    used_row = [False] * t
    used_col = [False] * ncol
    solution = []

    # heuristic: choose uncovered column with minimal remaining rows
    def choose_column():
        best = -1
        best_sz = 10**9
        for c in range(ncol):
            if not used_col[c]:
                sz = 0
                for r in col_rows[c]:
                    if not used_row[r]:
                        sz += 1
                if sz == 0:
                    return -1  # dead end
                if sz < best_sz:
                    best_sz = sz
                    best = c
        return best

    def cover(row):
        # mark row and its columns
        used_row[row] = True
        for c in row_cols[row]:
            used_col[c] = True

    def uncover(row):
        used_row[row] = False
        for c in row_cols[row]:
            used_col[c] = False

    def dfs():
        if len(solution) == k:
            return True
        col = choose_column()
        if col == -1:
            return False
        # try each row that covers col
        for r in col_rows[col]:
            if used_row[r]:
                continue
            # check if row's other columns are free
            ok = True
            for c2 in row_cols[r]:
                if used_col[c2]:
                    ok = False
                    break
            if not ok:
                continue
            cover(r)
            solution.append(r)
            if dfs():
                return True
            solution.pop()
            uncover(r)
        return False

    if dfs():
        out = ["YES"]
        for idx in solution:
            a, b, c = rows[idx]
            out.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()