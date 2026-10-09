import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))

    # Exact cover with dancing links
    n_cols = 3 * k  # columns: bases 0..k-1, catalysts k..2k-1, essences 2k..3k-1

    # Build column headers
    size = [0] * n_cols
    col_nodes = [[] for _ in range(n_cols)]  # list of row indices containing the column

    for idx, (x, y, z) in enumerate(triples):
        cols = (x, k + y, 2 * k + z)
        for c in cols:
            col_nodes[c].append(idx)
            size[c] += 1

    # If any column has zero rows, impossible
    if any(s == 0 for s in size):
        print("NO")
        return

    # DLX structures
    # For each row we store its three columns
    row_cols = [ (x, k + y, 2 * k + z) for (x, y, z) in triples ]

    # Active columns set
    active_cols = [True] * n_cols
    # Rows that are still available
    active_rows = [True] * t

    solution_rows = []

    # Heuristic: choose column with minimal remaining rows
    def choose_column():
        min_sz = 10**9
        chosen = -1
        for c in range(n_cols):
            if active_cols[c]:
                # count only active rows
                cnt = 0
                for r in col_nodes[c]:
                    if active_rows[r]:
                        cnt += 1
                if cnt < min_sz:
                    min_sz = cnt
                    chosen = c
                    if cnt == 1:
                        break
        return chosen

    def cover(row):
        """remove row and its columns' other rows"""
        # mark row inactive
        active_rows[row] = False
        # for each column this row covers, deactivate column and rows that use it
        for c in row_cols[row]:
            if not active_cols[c]:
                continue
            active_cols[c] = False
            for r in col_nodes[c]:
                if active_rows[r]:
                    # deactivate row r
                    active_rows[r] = False
                    # for other columns of r, decrement counts implicitly via active_rows check
        # No need to store changes; we will undo manually

    # To undo, we need to record what we changed
    def cover_with_record(row):
        changed_cols = []
        removed_rows = []
        # deactivate row
        active_rows[row] = False
        removed_rows.append(row)
        for c in row_cols[row]:
            if not active_cols[c]:
                continue
            active_cols[c] = False
            changed_cols.append(c)
            for r in col_nodes[c]:
                if active_rows[r]:
                    active_rows[r] = False
                    removed_rows.append(r)
        return changed_cols, removed_rows

    def uncover(changed_cols, removed_rows):
        # restore rows
        for r in removed_rows:
            active_rows[r] = True
        # restore columns
        for c in changed_cols:
            active_cols[c] = True

    def search(depth=0):
        if all(not ac for ac in active_cols):
            return True
        c = choose_column()
        if c == -1:
            return False
        # try each row that covers column c
        for r in col_nodes[c]:
            if not active_rows[r]:
                continue
            changed_cols, removed_rows = cover_with_record(r)
            solution_rows.append(r)
            if search(depth + 1):
                return True
            solution_rows.pop()
            uncover(changed_cols, removed_rows)
        return False

    if search():
        print("YES")
        out = []
        for r in solution_rows:
            x, y, z = triples[r]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        print("NO")

if __name__ == "__main__":
    solve()