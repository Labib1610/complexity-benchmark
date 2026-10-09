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

    # DLX structures
    n_cols = 3 * k  # columns: 0..k-1 for x, k..2k-1 for y, 2k..3k-1 for z
    col_size = [0] * n_cols
    rows_of_col = [[] for _ in range(n_cols)]
    row_nodes = []  # list of column indices for each row

    for idx, (x, y, z) in enumerate(triples):
        cols = [x, k + y, 2 * k + z]
        row_nodes.append(cols)
        for c in cols:
            rows_of_col[c].append(idx)
            col_size[c] += 1

    # If any column has zero rows, impossible
    if any(col_size[c] == 0 for c in range(n_cols)):
        print("NO")
        return

    used_row = [False] * len(triples)
    used_col = [False] * n_cols
    solution = []

    # heuristic: choose column with minimal remaining rows
    def choose_column():
        min_c = -1
        min_sz = 10**9
        for c in range(n_cols):
            if not used_col[c]:
                sz = 0
                for r in rows_of_col[c]:
                    if not used_row[r]:
                        sz += 1
                if sz < min_sz:
                    min_sz = sz
                    min_c = c
                    if sz == 0:
                        break
        return min_c, min_sz

    def cover(row_idx):
        # mark row and its columns
        used_row[row_idx] = True
        for c in row_nodes[row_idx]:
            used_col[c] = True

    def uncover(row_idx):
        used_row[row_idx] = False
        for c in row_nodes[row_idx]:
            used_col[c] = False

    def search(depth):
        if depth == k:
            return True
        c, sz = choose_column()
        if sz == 0:
            return False
        # try each row that covers column c
        for r in rows_of_col[c]:
            if used_row[r]:
                continue
            # check if row's other columns are free
            conflict = False
            for cc in row_nodes[r]:
                if used_col[cc]:
                    conflict = True
                    break
            if conflict:
                continue
            cover(r)
            solution.append(r)
            if search(depth + 1):
                return True
            solution.pop()
            uncover(r)
        return False

    if search(0):
        print("YES")
        for idx in solution:
            x, y, z = triples[idx]
            print(x + 1, y + 1, z + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()