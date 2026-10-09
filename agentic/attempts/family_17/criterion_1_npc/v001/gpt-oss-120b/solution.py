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

    n = 3 * q                     # number of columns (elements)
    # DLX arrays
    max_nodes = 1 + n + 3 * t + 5   # header + column headers + all nodes
    left = [0] * max_nodes
    right = [0] * max_nodes
    up = [0] * max_nodes
    down = [0] * max_nodes
    col = [0] * max_nodes          # column header of each node
    row_id = [0] * max_nodes       # which input triple this node belongs to
    size = [0] * (n + 1)           # column sizes, index 1..n

    header = 0
    # initialise header list (circular)
    for i in range(n + 1):
        left[i] = i - 1
        right[i] = i + 1
        up[i] = down[i] = i
    left[0] = n
    right[n] = 0

    node_cnt = n + 1               # next free index
    # insert rows
    for rid, (a, b, c) in enumerate(triples):
        # create three nodes
        first = node_cnt
        nodes = []
        for elem in (a, b, c):
            nd = node_cnt
            node_cnt += 1
            col[nd] = elem
            row_id[nd] = rid
            # vertical link: insert at bottom of column
            up[nd] = up[elem]
            down[nd] = elem
            down[up[elem]] = nd
            up[elem] = nd
            size[elem] += 1
            nodes.append(nd)
        # horizontal links (circular)
        for i in range(3):
            left[nodes[i]] = nodes[(i - 1) % 3]
            right[nodes[i]] = nodes[(i + 1) % 3]

    answer_rows = [0] * q
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

    def search(k):
        nonlocal found
        if right[header] == header:   # all columns covered
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
        if min_sz == 0:
            return False
        cover(cc)
        r = down[cc]
        while r != cc:
            answer_rows[k] = row_id[r]
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
        for rid in answer_rows:
            a, b, c = triples[rid]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()