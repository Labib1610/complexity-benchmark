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

    n = 3 * q                     # number of columns
    max_nodes = t * 3 + n + 1

    # dancing links arrays
    left = [0] * max_nodes
    right = [0] * max_nodes
    up = [0] * max_nodes
    down = [0] * max_nodes
    col = [0] * max_nodes          # column header of each node
    row_id = [0] * max_nodes       # which input row this node belongs to
    size = [0] * (n + 1)           # size of each column

    header = 0
    # initialise header and column headers
    for i in range(n + 1):
        left[i] = i - 1
        right[i] = i + 1
        up[i] = down[i] = i
    left[0] = n
    right[n] = 0

    node_cnt = n + 1  # next free index

    # add rows
    for rid, (a, b, c) in enumerate(triples, start=1):
        cols = (a, b, c)
        first = None
        for ccol in cols:
            nd = node_cnt
            node_cnt += 1
            col[nd] = ccol
            row_id[nd] = rid
            # vertical links
            up[nd] = up[ccol]
            down[nd] = ccol
            down[up[ccol]] = nd
            up[ccol] = nd
            size[ccol] += 1
            # horizontal links
            if first is None:
                left[nd] = right[nd] = nd
                first = nd
            else:
                left[nd] = left[first]
                right[nd] = first
                right[left[first]] = nd
                left[first] = nd

    solution_rows = []
    answer = []

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

    found = False

    def search():
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
            # cover other columns in this row
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
        uncover(c)
        return False

    if search():
        sys.stdout.write("YES\n")
        # map row ids back to triples
        id_to_trip = {i+1: triples[i] for i in range(len(triples))}
        for rid in solution_rows:
            a,b,c = id_to_trip[rid]
            sys.stdout.write(f"{a} {b} {c}\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()