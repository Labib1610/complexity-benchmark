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
    # dancing links structures
    # column headers: 0..n (0 is dummy head)
    size = [0] * (n + 1)          # number of rows in each column
    up = [0] * (3 * t + n + 1)    # node links, will be resized later
    down = [0] * (3 * t + n + 1)
    left = [0] * (3 * t + n + 1)
    right = [0] * (3 * t + n + 1)
    col = [0] * (3 * t + n + 1)   # column of each node
    row_id = [0] * (3 * t + n + 1)

    # initialise column header circular list
    for i in range(n + 1):
        up[i] = down[i] = i
        left[i] = i - 1
        right[i] = i + 1
    left[0] = n
    right[n] = 0

    node_cnt = n
    # add rows
    for rid, (a, b, c) in enumerate(triples):
        cols = (a, b, c)
        first = None
        for ccol in cols:
            node_cnt += 1
            nid = node_cnt
            col[nid] = ccol
            row_id[nid] = rid
            # insert into column list (at bottom)
            up[nid] = up[ccol]
            down[nid] = ccol
            down[up[ccol]] = nid
            up[ccol] = nid
            size[ccol] += 1
            # horizontal links
            if first is None:
                left[nid] = right[nid] = nid
                first = nid
            else:
                # insert to the left of first
                left[nid] = left[first]
                right[nid] = first
                right[left[first]] = nid
                left[first] = nid

    solution_rows = []
    answer = []

    # cover / uncover operations
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

    # choose column with minimal size
    def choose_column():
        c = right[0]
        min_sz = size[c]
        cur = c
        while cur != 0:
            if size[cur] < min_sz:
                min_sz = size[cur]
                c = cur
                if min_sz == 0:
                    break
            cur = right[cur]
        return c

    found = False

    def search():
        nonlocal found
        if right[0] == 0:          # all columns covered
            # build answer from stored row ids
            for rid in solution_rows:
                answer.append(triples[rid])
            found = True
            return True
        c = choose_column()
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
        out = ["YES"]
        for a, b, c in answer:
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()