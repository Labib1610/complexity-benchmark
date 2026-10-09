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
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        triples.append((a, b, c))

    n_cols = 3 * q

    # ----- DLX structures -----
    # header nodes: 0..n_cols (0 is root)
    size = [0] * (n_cols + 1)
    col_head = list(range(n_cols + 1))

    # doubly linked list of column headers (horizontal)
    left = [i - 1 for i in range(n_cols + 1)]
    right = [i + 1 for i in range(n_cols + 1)]
    left[0] = n_cols
    right[n_cols] = 0

    # node links (vertical)
    up = [i for i in range(n_cols + 1)]
    down = [i for i in range(n_cols + 1)]

    # for each node: column it belongs to, row id
    node_col = []
    node_row = []

    row_head = []          # first node index of each row

    # add rows
    for rid, (a, b, c) in enumerate(triples):
        first = None
        for v in (a, b, c):
            col = v
            node_idx = len(node_col)
            node_col.append(col)
            node_row.append(rid)

            # vertical insertion at bottom of column
            up.append(up[col])
            down.append(col)
            down[up[col]] = node_idx
            up[col] = node_idx

            size[col] += 1

            # horizontal links within the row
            if first is None:
                left.append(node_idx)
                right.append(node_idx)
                first = node_idx
            else:
                # insert after previous node in row
                prev = right[first - 1] if first else None
                # simpler: maintain circular list per row
                left.append(left[first])
                right.append(first)
                right[left[first]] = node_idx
                left[first] = node_idx

        row_head.append(first)

    # ----- DLX operations -----
    def cover(c):
        # remove column header
        right[left[c]] = right[c]
        left[right[c]] = left[c]
        # remove rows
        i = down[c]
        while i != c:
            j = right[i]
            while j != i:
                down[up[j]] = down[j]
                up[down[j]] = up[j]
                size[node_col[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                size[node_col[j]] += 1
                down[up[j]] = j
                up[down[j]] = j
                j = left[j]
            i = up[i]
        right[left[c]] = c
        left[right[c]] = c

    solution_rows = []
    found = False

    # heuristic: choose column with minimal size
    def choose_column():
        c = right[0]
        min_sz = size[c]
        cur = right[c]
        while cur != 0:
            if size[cur] < min_sz:
                min_sz = size[cur]
                c = cur
                if min_sz == 0:
                    break
            cur = right[cur]
        return c

    def search(k):
        nonlocal found
        if right[0] == 0:
            # all columns covered
            found = True
            return True
        c = choose_column()
        if size[c] == 0:
            return False
        cover(c)
        r = down[c]
        while r != c:
            solution_rows.append(node_row[r])
            j = right[r]
            while j != r:
                cover(node_col[j])
                j = right[j]
            if search(k + 1):
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

    if search(0):
        sys.stdout.write("YES\n")
        # output triples in the order they were selected
        for rid in solution_rows:
            a, b, c = triples[rid]
            sys.stdout.write(f"{a} {b} {c}\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()