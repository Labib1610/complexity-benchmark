import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    rows = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        rows.append((x, y, z))

    # DLX structures
    n_cols = 3 * k  # processors 0..k-1, sensors k..2k-1, transmitters 2k..3k-1

    # header node 0
    size = 1
    left = [0]
    right = [0]
    up = [0]
    down = [0]
    col = [0]
    row_id = [ -1 ]  # row index for each node, -1 for header

    col_size = [0] * (n_cols + 1)  # 1..n_cols
    col_head = [0] * (n_cols + 1)

    # create column header nodes 1..n_cols
    for c in range(1, n_cols + 1):
        left.append(c - 1)
        right.append(c + 1 if c < n_cols else 0)
        up.append(c)
        down.append(c)
        col.append(c)
        row_id.append(-1)
        col_size[c] = 0
        col_head[c] = c
    left[0] = n_cols
    right[n_cols] = 0

    # add rows
    for r_idx, (x, y, z) in enumerate(rows):
        cols = [x + 1, k + y + 1, 2 * k + z + 1]  # convert to 1‑based column ids
        first = None
        for c in cols:
            node = size
            size += 1
            left.append(0)
            right.append(0)
            up.append(0)
            down.append(0)
            col.append(c)
            row_id.append(r_idx)

            # vertical links
            up[node] = up[c]
            down[node] = c
            down[up[c]] = node
            up[c] = node
            col_size[c] += 1

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

    sys.setrecursionlimit(10000)

    def cover(c):
        # remove column header
        left[right[c]] = left[c]
        right[left[c]] = right[c]
        # remove rows
        i = down[c]
        while i != c:
            j = right[i]
            while j != i:
                down[up[j]] = down[j]
                up[down[j]] = up[j]
                col_size[col[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                col_size[col[j]] += 1
                down[up[j]] = j
                up[down[j]] = j
                j = left[j]
            i = up[i]
        left[right[c]] = c
        right[left[c]] = c

    def search():
        if right[0] == 0:  # all columns covered
            return True
        # choose column with minimal size
        c = right[0]
        min_sz = col_size[c]
        cc = c
        j = right[c]
        while j != 0:
            if col_size[j] < min_sz:
                min_sz = col_size[j]
                cc = j
                if min_sz == 0:
                    break
            j = right[j]
        if min_sz == 0:
            return False
        cover(cc)
        r = down[cc]
        while r != cc:
            solution_rows.append(row_id[r])
            j = right[r]
            while j != r:
                cover(col[j])
                j = right[j]
            if search():
                return True
            # backtrack
            j = left[r]
            while j != r:
                uncover(col[j])
                j = left[j]
            solution_rows.pop()
            r = down[r]
        uncover(cc)
        return False

    possible = search()
    out = []
    if possible:
        out.append("YES")
        for rid in solution_rows:
            x, y, z = rows[rid]
            out.append(f"{x+1} {y+1} {z+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()