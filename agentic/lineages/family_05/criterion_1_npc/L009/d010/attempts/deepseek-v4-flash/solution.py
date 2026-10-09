import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    paths = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        paths.append((x, y, z))

    if t == 0:
        print("NO")
        return

    # columns: 0..3k-1
    # 0..k-1 for x, k..2k-1 for y, 2k..3k-1 for z
    ncols = 3 * k
    nrows = t

    # DLX arrays
    # We'll use 1-indexed nodes: 0 is header
    # Each column has a header node
    # We'll create column nodes first
    left = [0] * (1 + ncols + nrows * 3)
    right = [0] * (1 + ncols + nrows * 3)
    up = [0] * (1 + ncols + nrows * 3)
    down = [0] * (1 + ncols + nrows * 3)
    col = [0] * (1 + ncols + nrows * 3)
    row = [0] * (1 + ncols + nrows * 3)

    # column headers
    for i in range(ncols + 1):
        left[i] = i - 1
        right[i] = i +  ​1
        up[i] = i
        down[i] = i
        col[i] = i
        row[i] = -1
    left[0] = ncols
    right[ncols] = 0

    size = [0] * (ncols + 1)

    # We'll add rows
    node_idx = ncols +  ​1
    # For each column, keep last node index (initially column header)
    last = [i for i in range(ncols + 1)]

    for r in range(t):
        x, y, z = paths[r]
        cols = [x-1, k + (y-1), 2*k + (z-1)]
        # sort columns to keep order (not necessary but helps)
        cols.sort()
        first = -1
        prev = -1
        for c in cols:
            idx = node_idx
            node_idx += 1
            left[idx] = prev
            right[idx] = -1
            if prev != -1:
                right[prev] = idx
            else:
                first = idx
            # vertical links
            up[idx] = last[c]
            down[idx] = c
            down[last[c]] = idx
            up[c] = idx
            last[c] = idx
            col[idx] = c
            row[idx] = r
            size[c] += 1
            prev = idx
        # close row loop
        right[prev] = first
        left[first] = prev

    # Now DLX search
    answer = []

    def cover(c):
        # remove column c from header
        right[left[c]] = right[c]
        left[right[c]] = left[c]
        # for each row in this column
        i = down[c]
        while i != c:
            # cover all columns in this row
            j = right[i]
            while j != i:
                up[down[j]] = up[j]
                down[up[j]] = down[j]
                size[col[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                size[col[j]] += 1
                up[down[j]] = j
                down[up[j]] = j
                j = left[j]
            i = up[i]
        right[left[c]] = c
        left[right[c]] = c

    def search():
        if right[0] == 0:
            return True
        # choose column with min size
        c = right[0]
        min_size = size[c]
        j = right[c]
        while j != 0:
            if size[j] < min_size:
                min_size = size[j]
                c = j
            j = right[j]
        if min_size == 0:
            return False
        cover(c)
        r = down[c]
        while r != c:
            answer.append(row[r])
            # cover all columns in this row
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
            answer.pop()
            r = down[r]
        uncover(c)
        return False

    if search():
        print("YES")
        for idx in answer:
            x, y, z = paths[idx]
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()