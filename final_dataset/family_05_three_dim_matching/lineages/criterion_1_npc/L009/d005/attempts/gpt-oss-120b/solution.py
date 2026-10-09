import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # columns: 0..k-1 for x, k..2k-1 for y, 2k..3k-1 for z
    ncol = 3 * k
    col_nodes = [[] for _ in range(ncol)]   # rows indices covering each column
    rows = []                               # each row = (x,y,z, [col indices])
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        cols = [x, k + y, 2 * k + z]
        row_id = len(rows)
        rows.append((x, y, z, cols))
        for c in cols:
            col_nodes[c].append(row_id)

    # If any column has zero rows, impossible
    for c in range(ncol):
        if not col_nodes[c]:
            print("NO")
            return

    # DLX structures
    # For each row we keep a flag whether it's still usable
    row_active = [True] * len(rows)
    # For each column we keep count of active rows covering it
    col_count = [len(col_nodes[c]) for c in range(ncol)]

    solution = []

    # Choose column with minimal count (heuristic)
    def choose_column():
        min_c = -1
        min_sz = 10**9
        for c in range(ncol):
            if col_count[c] and col_count[c] < min_sz:
                min_sz = col_count[c]
                min_c = c
        return min_c

    def cover(row_id):
        """remove row and all columns it covers, updating counts"""
        x, y, z, cols = rows[row_id]
        row_active[row_id] = False
        for c in cols:
            col_count[c] = 0
            for r in col_nodes[c]:
                if row_active[r]:
                    row_active[r] = False
                    # decrement counts of other columns of this row
                    for cc in rows[r][3]:
                        if cc != c:
                            col_count[cc] -= 1

    def uncover(row_id):
        """restore row and columns (simple re-evaluation)"""
        # recompute from scratch (k ≤ 22, rows ≤ 10648, recursion depth ≤ k)
        for i in range(len(row_active)):
            row_active[i] = True
        for c in range(ncol):
            col_count[c] = len(col_nodes[c])

        # reapply all rows currently in solution as covered
        for rid in solution:
            row_active[rid] = False
            for c in rows[rid][3]:
                col_count[c] = 0
                for r in col_nodes[c]:
                    if row_active[r]:
                        row_active[r] = False
                        for cc in rows[r][3]:
                            if cc != c:
                                col_count[cc] -= 1

    def dfs():
        if len(solution) == k:
            # all columns must be covered
            if all(col_count[c] == 0 for c in range(ncol)):
                return True
            return False
        c = choose_column()
        if c == -1:
            return False
        # try each active row covering column c
        for r in list(col_nodes[c]):  # copy to avoid modification issues
            if not row_active[r]:
                continue
            solution.append(r)
            # backup state
            saved_active = row_active[:]
            saved_count = col_count[:]
            # cover this row
            for cc in rows[r][3]:
                # remove column cc
                for rr in col_nodes[cc]:
                    if row_active[rr]:
                        row_active[rr] = False
                        for ccc in rows[rr][3]:
                            if ccc != cc:
                                col_count[ccc] -= 1
                col_count[cc] = 0
            if dfs():
                return True
            # restore
            solution.pop()
            row_active[:] = saved_active
            col_count[:] = saved_count
        return False

    if dfs():
        print("YES")
        for rid in solution:
            x, y, z, _ = rows[rid]
            print(x + 1, y + 1, z + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()