import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    rows = []          # each row: list of column indices (size 3)
    for _ in range(t):
        d = int(next(it)) - 1
        f = int(next(it)) - 1
        m = int(next(it)) - 1
        rows.append([d, k + f, 2 * k + m])

    # ---------- DLX structures ----------
    # column header nodes: 0..m-1
    m = 3 * k
    size = [0] * m          # number of rows in each column
    col_head = list(range(m))

    # linked lists for rows
    # for each row we store its three column indices and the node ids
    # node ids are 0..(3*len(rows)-1)
    node_col = []   # column of each node
    up = []         # up link (node id)
    down = []       # down link
    left = []       # left link within row
    right = []      # right link within row
    row_of_node = []  # which row a node belongs to

    # column header links (circular)
    col_up = list(range(m))
    col_down = list(range(m))

    # build nodes
    for r_idx, cols in enumerate(rows):
        first = len(node_col)
        for i, c in enumerate(cols):
            node_id = len(node_col)
            node_col.append(c)
            row_of_node.append(r_idx)
            # vertical links: insert at bottom of column c
            up.append(col_up[c])
            down.append(c)          # temporary, will be fixed later
            # adjust column links
            col_down[col_up[c]] = node_id
            col_up[c] = node_id
            # horizontal links (circular within the row)
            left.append(node_id - 1 if i > 0 else first + 2)
            right.append(first if i == 2 else node_id + 1)
        # close the row circle (already set by left/right above)

    # close column circles (point to header)
    for c in range(m):
        down[col_up[c]] = c
        up[c] = col_up[c]

    # column header nodes are identified by numbers 0..m-1 (they act as nodes)
    # we keep a list of which columns are still present
    column_active = [True] * m

    solution_rows = []
    answer = None

    # ---------- DLX operations ----------
    def cover(col):
        # remove column header
        column_active[col] = False
        # unlink column from its neighbours (vertical)
        i = down[col]
        while i != col:
            j = right[i]
            while j != i:
                # unlink node j from its column
                up[down[j]] = up[j]
                down[up[j]] = down[j]
                size[node_col[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(col):
        i = up[col]
        while i != col:
            j = left[i]
            while j != i:
                size[node_col[j]] += 1
                up[down[j]] = j
                down[up[j]] = j
                j = left[j]
            i = up[i]
        column_active[col] = True

    # initialise column sizes
    for c in range(m):
        cnt = 0
        i = down[c]
        while i != c:
            cnt += 1
            i = down[i]
        size[c] = cnt

    # ---------- recursive search ----------
    def search():
        nonlocal answer
        # if all columns covered
        if all(not column_active[c] for c in range(m)):
            answer = solution_rows.copy()
            return True

        # choose column with minimal size
        c = -1
        min_sz = 10**9
        for col in range(m):
            if column_active[col] and size[col] < min_sz:
                min_sz = size[col]
                c = col
                if min_sz == 0:
                    break
        if min_sz == 0:
            return False

        cover(c)
        r = down[c]
        while r != c:
            solution_rows.append(row_of_node[r])
            # cover other columns of this row
            j = right[r]
            while j != r:
                cover(node_col[j])
                j = right[j]
            if search():
                return True
            # backtrack
            j = left[r]
            while j != r:
                uncover(node_col[j])
                j = left[j]
            solution_rows.pop()
            r = down[r]
        uncover(c)
        return False

    if search():
        out = ["YES"]
        for rid in answer:
            d, f, m_ = rows[rid]
            out.append(f"{d+1} {f - k + 1} {m_ - 2*k + 1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()