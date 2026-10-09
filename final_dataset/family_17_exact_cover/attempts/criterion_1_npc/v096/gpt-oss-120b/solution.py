import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q                     # number of columns
    rows = []                     # each row: list of column indices (0‑based)
    triples = []                 # original triples for output
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append([a, b, c])
        triples.append((a + 1, b + 1, c + 1))

    # ---------- DLX structures ----------
    # column header nodes: 0..n-1
    size = [0] * n               # number of rows covering column
    col_head = list(range(n))    # self link for column headers
    up = list(range(n))
    down = list(range(n))
    left = list(range(n))
    right = list(range(n))

    # row nodes start after column headers
    # we will store for each node: col, row_id, up, down, left, right
    col = []
    row_id = []
    up_node = []
    down_node = []
    left_node = []
    right_node = []

    # helper to add a node
    def add_node(c, r):
        idx = len(col)
        col.append(c)
        row_id.append(r)
        up_node.append(0)
        down_node.append(0)
        left_node.append(0)
        right_node.append(0)
        return idx

    # build rows
    row_nodes = []   # list of one node index per row (any node of that row)
    for r, cols in enumerate(rows):
        first = -1
        prev = -1
        for c in cols:
            node = add_node(c, r)
            # vertical links
            up_node[node] = up[c]
            down_node[node] = c
            down[up[c]] = node
            up[c] = node
            size[c] += 1
            # horizontal links within the row
            if first == -1:
                first = node
            else:
                left_node[node] = prev
                right_node[prev] = node
            prev = node
        # close the row circle
        left_node[first] = prev
        right_node[prev] = first
        row_nodes.append(first)

    # column header circular list (only columns with size>0 are kept)
    # we keep all columns, but skip empty ones during search
    # link column headers together
    head = n  # dummy header index
    col.append(head)  # dummy column for header
    row_id.append(-1)
    up_node.append(head)
    down_node.append(head)
    left_node.append(head)
    right_node.append(head)

    # link columns
    last = head
    for c in range(n):
        left_node[c] = last
        right_node[last] = c
        last = c
    right_node[last] = head
    left_node[head] = last

    solution_rows = []

    # ---------- DLX operations ----------
    def cover(c):
        # remove column header
        right_node[left_node[c]] = right_node[c]
        left_node[right_node[c]] = left_node[c]
        # for each row i in column c
        i = down_node[c]
        while i != c:
            j = right_node[i]
            while j != i:
                down_node[up_node[j]] = down_node[j]
                up_node[down_node[j]] = up_node[j]
                size[col[j]] -= 1
                j = right_node[j]
            i = down_node[i]

    def uncover(c):
        i = up_node[c]
        while i != c:
            j = left_node[i]
            while j != i:
                size[col[j]] += 1
                down_node[up_node[j]] = j
                up_node[down_node[j]] = j
                j = left_node[j]
            i = up_node[i]
        right_node[left_node[c]] = c
        left_node[right_node[c]] = c

    # ---------- recursive search ----------
    def search(k):
        if right_node[head] == head:   # all columns covered
            return True
        # choose column with minimal size
        c = right_node[head]
        min_sz = size[c]
        cc = c
        j = right_node[c]
        while j != head:
            if size[j] < min_sz:
                min_sz = size[j]
                cc = j
                if min_sz == 0:
                    break
            j = right_node[j]
        if min_sz == 0:
            return False
        cover(cc)
        r = down_node[cc]
        while r != cc:
            solution_rows.append(row_id[r])
            j = right_node[r]
            while j != r:
                cover(col[j])
                j = right_node[j]
            if search(k + 1):
                return True
            # backtrack
            j = left_node[r]
            while j != r:
                uncover(col[j])
                j = left_node[j]
            solution_rows.pop()
            r = down_node[r]
        uncover(cc)
        return False

    possible = search(0)

    out = []
    if possible:
        out.append("YES")
        for rid in solution_rows:
            a, b, c = triples[rid]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()