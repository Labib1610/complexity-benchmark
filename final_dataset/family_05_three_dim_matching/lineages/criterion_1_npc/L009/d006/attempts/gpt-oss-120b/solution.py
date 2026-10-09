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

    # Exact cover columns: 0..k-1 for X, k..2k-1 for Y, 2k..3k-1 for Z
    ncol = 3 * k
    col_size = [0] * ncol
    rows_in_col = [[] for _ in range(ncol)]

    # Build rows
    rows = []          # each row: list of column indices it covers
    for idx, (x, y, z) in enumerate(triples):
        cols = [x, k + y, 2 * k + z]
        rows.append(cols)
        for c in cols:
            rows_in_col[c].append(idx)
            col_size[c] += 1

    # If any column has zero rows, impossible
    if any(col_size[c] == 0 for c in range(ncol)):
        print("NO")
        return

    used_row = [False] * len(rows)
    used_col = [False] * ncol
    solution = []

    # heuristic: choose column with minimal remaining rows
    def choose_column():
        best = -1
        best_sz = 10**9
        for c in range(ncol):
            if not used_col[c]:
                sz = 0
                for r in rows_in_col[c]:
                    if not used_row[r]:
                        sz += 1
                if sz < best_sz:
                    best_sz = sz
                    best = c
                    if sz == 1:
                        break
        return best

    def cover(row_idx):
        # mark row and its columns
        used_row[row_idx] = True
        for c in rows[row_idx]:
            used_col[c] = True

    def uncover(row_idx):
        used_row[row_idx] = False
        for c in rows[row_idx]:
            used_col[c] = False

    def dfs(depth):
        if depth == k:
            return True
        c = choose_column()
        if c == -1:
            return False
        # try each row that covers column c
        for r in rows_in_col[c]:
            if used_row[r]:
                continue
            # check if row conflicts with already used columns
            conflict = False
            for cc in rows[r]:
                if used_col[cc]:
                    conflict = True
                    break
            if conflict:
                continue
            cover(r)
            solution.append(r)
            if dfs(depth + 1):
                return True
            solution.pop()
            uncover(r)
        return False

    if dfs(0):
        print("YES")
        for r in solution:
            x, y, z = triples[r]
            print(x + 1, y + 1, z + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()