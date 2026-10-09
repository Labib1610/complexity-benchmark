import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    ncol = 3 * q

    # DLX arrays (1‑based indexing for nodes, 0 is the root header)
    max_nodes = 3 * t + ncol + 5
    left = [0] * max_nodes
    right = [0] * max_nodes
    up = [0] * max_nodes
    down = [0] * max_nodes
    col = [0] * max_nodes
    size = [0] * (ncol + 1)          # size per column header
    row_head = []                    # store one node id per row (for output)

    # initialise column headers and root
    root = 0
    for i in range(ncol + 1):
        left[i] = i - 1
        right[i] = i + 1
        up[i] = down[i] = i
    left[0] = ncol
    right[ncol] = 0

    node_cnt = ncol  # nodes 1..ncol are column headers

    # add rows
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        cols = (a, b, c)
        first = None
        for ccol in cols:
            node_cnt += 1
            nid = node_cnt
            col[nid] = ccol
            # vertical link (insert at bottom of column)
            up[nid] = up[ccol]
            down[nid] = ccol
            down[up[ccol]] = nid
            up[ccol] = nid
            size[ccol] += 1
            # horizontal link within the row
            if first is None:
                left[nid] = right[nid] = nid
                first = nid
            else:
                # insert to the right of first
                left[nid] = left[first]
                right[nid] = first
                right[left[first]] = nid
                left[first] = nid
        row_head.append(first)

    answer = [0] * (q + 1)   # store node id of chosen rows
    solved = False

    # ----- DLX core operations -----
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

    # ----- recursive search -----
    def search(k):
        nonlocal solved
        if right[root] == root:          # all columns covered
            solved = True
            return True
        # choose column with minimal size
        c = right[root]
        min_sz = size[c]
        cc = c
        j = right[c]
        while j != root:
            if size[j] < min_sz:
                min_sz = size[j]
                cc = j
                if min_sz == 0:
                    break
            j = right[j]
        if min_sz == 0:
            return False
        cover(cc)
        r = down[cc]
        while r != cc:
            answer[k] = r
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
            r = down[r]
        uncover(cc)
        return False

    if search(0):
        out = ["YES"]
        for i in range(q):
            node = answer[i]
            triple = []
            j = node
            while True:
                triple.append(col[j])
                j = right[j]
                if j == node:
                    break
            out.append(" ".join(map(str, triple)))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()