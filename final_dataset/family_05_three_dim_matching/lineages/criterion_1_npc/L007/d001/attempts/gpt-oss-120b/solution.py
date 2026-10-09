import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        c = int(next(it)) - 1
        n = int(next(it)) - 1
        s = int(next(it)) - 1
        triples.append((c, n, s))

    # Exact cover with DLX
    n_cols = 3 * k
    # header node 0
    size = 1  # next free node index
    # column headers 1..n_cols
    col_head = [0] * (n_cols + 1)
    col_size = [0] * (n_cols + 1)
    up = [0] * (t * 3 + n_cols + 1)
    down = [0] * (t * 3 + n_cols + 1)
    left = [0] * (t * 3 + n_cols + 1)
    right = [0] * (t * 3 + n_cols + 1)
    row_id = [0] * (t * 3 + n_cols + 1)

    # init column headers linked in a circular list
    for i in range(n_cols + 1):
        up[i] = down[i] = i
        left[i] = i - 1
        right[i] = i + 1
    left[0] = n_cols
    right[n_cols] = 0

    # add rows
    for r_idx, (c, n, s) in enumerate(triples):
        cols = [c + 1, n + 1 + k, s + 1 + 2 * k]  # shift to 1‑based column ids
        first = None
        for col in cols:
            node = size
            size += 1
            row_id[node] = r_idx
            # vertical links
            up[node] = up[col]
            down[node] = col
            down[up[col]] = node
            up[col] = node
            col_size[col] += 1
            # horizontal links
            if first is None:
                first = node
                left[node] = right[node] = node
            else:
                # insert to the left of first
                left[node] = left[first]
                right[node] = first
                right[left[first]] = node
                left[first] = node

    solution_rows = []

    def cover(col):
        # remove column header
        right[left[col]] = right[col]
        left[right[col]] = left[col]
        # remove rows
        i = down[col]
        while i != col:
            j = right[i]
            while j != i:
                down[up[j]] = down[j]
                up[down[j]] = up[j]
                col_size[col_id[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(col):
        i = up[col]
        while i != col:
            j = left[i]
            while j != i:
                col_size[col_id[j]] += 1
                down[up[j]] = j
                up[down[j]] = j
                j = left[j]
            i = up[i]
        right[left[col]] = col
        left[right[col]] = col

    # map node -> column id for vertical removal
    col_id = [0] * (t * 3 + n_cols + 1)
    for col in range(1, n_cols + 1):
        node = down[col]
        while node != col:
            col_id[node] = col
            node = down[node]

    def search():
        if right[0] == 0:  # all columns covered
            return True
        # choose column with minimal size
        c = right[0]
        min_sz = col_size[c]
        col = c
        j = right[c]
        while j != 0:
            if col_size[j] < min_sz:
                min_sz = col_size[j]
                col = j
                if min_sz == 0:
                    break
            j = right[j]
        if min_sz == 0:
            return False
        cover(col)
        r = down[col]
        while r != col:
            solution_rows.append(row_id[r])
            j = right[r]
            while j != r:
                cover(col_id[j])
                j = right[j]
            if search():
                return True
            # backtrack
            j = left[r]
            while j != r:
                uncover(col_id[j])
                j = left[j]
            solution_rows.pop()
            r = down[r]
        uncover(col)
        return False

    if search():
        out = ["YES"]
        for idx in solution_rows:
            c, n, s = triples[idx]
            out.append(f"{c+1} {n+1} {s+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()