import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # column indices: 0..k-1 satellites, k..2k-1 frequencies, 2k..3k-1 keys
    rows = []          # list of (col1, col2, col3, original triple)
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        rows.append((x, k + y, 2 * k + z, (x + 1, y + 1, z + 1)))

    # ---------- DLX structures ----------
    n_cols = 3 * k
    # header node 0, column headers 1..n_cols
    size = [0] * (n_cols + 1)          # number of nodes in column
    col = [0] * (3 * t + n_cols + 1)   # column of each node
    up = [0] * (3 * t + n_cols + 1)
    down = [0] * (3 * t + n_cols + 1)
    left = [0] * (3 * t + n_cols + 1)
    right = [0] * (3 * t + n_cols + 1)

    # initialise column headers linked list
    for i in range(n_cols + 1):
        up[i] = down[i] = i
        left[i] = i - 1
        right[i] = i + 1
    left[0] = n_cols
    right[n_cols] = 0

    node_id = n_cols + 1
    row_head = []          # first node id of each row
    for r_idx, (c1, c2, c3, triple) in enumerate(rows):
        first = None
        for c in (c1, c2, c3):
            nid = node_id
            node_id += 1
            col[nid] = c + 1          # shift by 1 because header is 0
            # vertical links
            up[nid] = up[col[nid]]
            down[nid] = col[nid]
            down[up[nid]] = nid
            up[col[nid]] = nid
            size[col[nid]] += 1
            # horizontal links
            if first is None:
                left[nid] = right[nid] = nid
                first = nid
            else:
                left[nid] = left[first]
                right[nid] = first
                right[left[first]] = nid
                left[first] = nid
        row_head.append(first)

    solution_rows = []

    def cover(c):
        # remove column header
        right[left[c]] = right[c]
        left[right[c]] = left[c]
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
        right[left[c]] = c
        left[right[c]] = c

    def search():
        if right[0] == 0:          # all columns covered
            return True
        # choose column with minimal size
        c = right[0]
        min_sz = size[c]
        cc = c
        while cc != 0:
            if size[cc] < min_sz:
                min_sz = size[cc]
                c = cc
                if min_sz == 0:
                    break
            cc = right[cc]
        if min_sz == 0:
            return False

        cover(c)
        r = down[c]
        while r != c:
            solution_rows.append(r)
            j = right[r]
            while j != r:
                cover(col[j])
                j = right[j]
            if search():
                return True
            # backtrack
            solution_rows.pop()
            j = left[r]
            while j != r:
                uncover(col[j])
                j = left[j]
            r = down[r]
        uncover(c)
        return False

    found = search()
    out = []
    if found:
        out.append("YES")
        # translate node ids back to original triples
        used = set()
        for node in solution_rows:
            # any node of the row gives the row index
            # we can find the row by walking left until header column changes
            # easier: store mapping from first node id to row index
            # we stored row_head list, so find which row contains this node
            # Build a dict once
            pass
    else:
        out.append("NO")
        sys.stdout.write("\n".join(out))
        return

    # Build mapping node->row index
    node_to_row = {}
    for idx, head in enumerate(row_head):
        nid = head
        while True:
            node_to_row[nid] = idx
            nid = right[nid]
            if nid == head:
                break

    for node in solution_rows:
        rid = node_to_row[node]
        triple = rows[rid][3]
        out.append(f"{triple[0]} {triple[1]} {triple[2]}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()