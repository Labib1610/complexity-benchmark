import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # column indices: 0..k-1 for X, k..2k-1 for Y, 2k..3k-1 for Z
    ncol = 3 * k

    # dancing links structures
    # header node is 0
    size = 1  # next free node index
    # arrays
    left = [0]
    right = [0]
    up = [0]
    down = [0]
    col = [0]          # column of node
    row_id = [0]       # which input row (0‑based) the node belongs to

    # column header nodes 1..ncol
    for c in range(ncol):
        left.append(c)          # will be fixed later
        right.append(c + 1 if c + 1 <= ncol else 0)
        up.append(c)
        down.append(c)
        col.append(c)           # column header points to itself
        row_id.append(-1)
    left[0] = ncol
    right[ncol] = 0
    # fix left/right of column headers
    for c in range(1, ncol + 1):
        left[c] = c - 1
        right[c] = c + 1 if c + 1 <= ncol else 0

    # store the triples for output
    triples = []

    # add a row (three columns) for each triple
    for idx in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x + 1, y + 1, z + 1))
        cols = [x, k + y, 2 * k + z]          # column numbers (0‑based)
        first = None
        for c in cols:
            node = size
            size += 1
            # ensure arrays are long enough
            left.append(0)
            right.append(0)
            up.append(0)
            down.append(0)
            col.append(c)
            row_id.append(idx)

            # vertical links (insert above column header)
            up[node] = up[c + 1]
            down[node] = c + 1
            down[up[node]] = node
            up[down[node]] = node

            # horizontal links within the row
            if first is None:
                first = node
                left[node] = right[node] = node
            else:
                # insert to the right of first
                left[node] = left[first]
                right[node] = first
                right[left[node]] = node
                left[first] = node

    # column sizes for heuristic
    col_size = [0] * (ncol + 1)
    for c in range(1, ncol + 1):
        cnt = 0
        i = down[c]
        while i != c:
            cnt += 1
            i = down[i]
        col_size[c] = cnt

    solution = []
    found = False

    def cover(c):
        # remove column header
        left[right[c]] = left[c]
        right[left[c]] = right[c]
        # remove rows
        i = down[c]
        while i != c:
            j = right[i]
            while j != i:
                up[down[j]] = up[j]
                down[up[j]] = down[j]
                col_size[col[j] + 1] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                col_size[col[j] + 1] += 1
                up[down[j]] = j
                down[up[j]] = j
                j = left[j]
            i = up[i]
        left[right[c]] = c
        right[left[c]] = c

    def search():
        nonlocal found
        if right[0] == 0:          # all columns covered
            found = True
            return
        # choose column with minimal size
        c = right[0]
        min_sz = col_size[c]
        j = right[c]
        while j != 0:
            if col_size[j] < min_sz:
                c = j
                min_sz = col_size[j]
                if min_sz == 0:
                    break
            j = right[j]
        if min_sz == 0:
            return
        cover(c)
        r = down[c]
        while r != c:
            solution.append(row_id[r])
            j = right[r]
            while j != r:
                cover(col[j] + 1)
                j = right[j]
            search()
            if found:
                return
            # backtrack
            j = left[r]
            while j != r:
                uncover(col[j] + 1)
                j = left[j]
            solution.pop()
            r = down[r]
        uncover(c)

    search()

    out = []
    if found:
        out.append("YES")
        for idx in solution:
            x, y, z = triples[idx]
            out.append(f"{x} {y} {z}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()