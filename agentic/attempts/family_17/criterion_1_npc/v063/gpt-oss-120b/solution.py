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

    ncol = 3 * q                     # columns 1..ncol
    # Dancing Links structures
    max_nodes = 3 * t + ncol + 1     # + header
    left = [0] * max_nodes
    right = [0] * max_nodes
    up = [0] * max_nodes
    down = [0] * max_nodes
    col = [0] * max_nodes            # column header of each node
    size = [0] * (ncol + 1)          # size of each column
    row_id = [0] * max_nodes         # which input row a node belongs to

    header = 0
    # initialise header list of columns
    for i in range(ncol + 1):
        left[i] = i - 1
        right[i] = i + 1
        up[i] = down[i] = i
    left[0] = ncol
    right[ncol] = 0

    node_cnt = ncol  # nodes 1..ncol are column headers

    # add rows
    for rid, (a, b, c) in enumerate(triples, 1):
        first = None
        for col_num in (a, b, c):
            node_cnt += 1
            col[node_cnt] = col_num
            row_id[node_cnt] = rid
            # vertical links
            up[node_cnt] = up[col_num]
            down[node_cnt] = col_num
            down[up[col_num]] = node_cnt
            up[col_num] = node_cnt
            size[col_num] += 1
            # horizontal links
            if first is None:
                left[node_cnt] = right[node_cnt] = node_cnt
                first = node_cnt
            else:
                left[node_cnt] = left[first]
                right[node_cnt] = first
                right[left[first]] = node_cnt
                left[first] = node_cnt

    solution_rows = []

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

    def search(k):
        if right[header] == header:   # all columns covered
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
        uncover(cc)
        return False

    if search(0):
        out = ["YES"]
        # retrieve triples by row id
        for rid in solution_rows:
            a, b, c = triples[rid - 1]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()