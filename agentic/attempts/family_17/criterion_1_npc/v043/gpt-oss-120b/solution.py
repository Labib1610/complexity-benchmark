import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    ncol = 3 * q          # columns 0 .. ncol-1
    # DLX structures
    max_nodes = 3 * t + ncol + 1
    left = [0] * max_nodes
    right = [0] * max_nodes
    up = [0] * max_nodes
    down = [0] * max_nodes
    col = [0] * max_nodes
    size = [0] * (ncol + 1)   # size for column headers (1..ncol)
    row_id = [0] * max_nodes  # which input row a node belongs to

    header = 0
    # initialise header list of column headers
    for i in range(ncol + 1):
        left[i] = i - 1
        right[i] = i + 1
        up[i] = down[i] = i
    left[0] = ncol
    right[ncol] = 0

    node_cnt = ncol + 1  # next free index

    # add rows
    for r_idx, (a, b, c) in enumerate(triples, start=1):
        for v in (a, b, c):
            col_id = v + 1          # columns are 1..ncol
            node = node_cnt
            node_cnt += 1
            col[node] = col_id
            row_id[node] = r_idx

            # vertical links
            up[node] = up[col_id]
            down[node] = col_id
            down[up[col_id]] = node
            up[col_id] = node
            size[col_id] += 1

            # horizontal links (temporarily)
            left[node] = node
            right[node] = node

        # now link the three nodes horizontally
        first = node_cnt - 3
        for i in range(3):
            cur = first + i
            nxt = first + (i + 1) % 3
            prv = first + (i - 1) % 3
            right[cur] = nxt
            left[cur] = prv

    solution_rows = []

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
                size[col[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                size[col[j]] += 1
                down[up[j]] = j
                up[down[j]] = j
                j = left[j]
            i = up[i]
        left[right[c]] = c
        right[left[c]] = c

    found = False

    def search(k):
        nonlocal found
        if right[header] == header:
            # all columns covered
            found = True
            return True
        # choose column with minimal size
        c = right[header]
        min_sz = size[c]
        cc = c
        j = right[c]
        while j != header:
            if size[j] < min_sz:
                min_sz = size[j]
                cc = j
                if min_sz == 0:
                    break
            j = right[j]
        c = cc
        if size[c] == 0:
            return False
        cover(c)
        r = down[c]
        while r != c:
            solution_rows.append(row_id[r])
            j = right[r]
            while j != r:
                cover(col[j])
                j = right[j]
            if search(k + 1):
                return True
            # backtrack
            j = left[r]
            while j != r:
                uncover(col[j])
                j = left[j]
            solution_rows.pop()
            r = down[r]
        uncover(c)
        return False

    if search(0):
        out = ["YES"]
        # solution_rows contains row indices (1‑based) in order of selection
        for idx in solution_rows:
            a, b, c = triples[idx - 1]
            out.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()