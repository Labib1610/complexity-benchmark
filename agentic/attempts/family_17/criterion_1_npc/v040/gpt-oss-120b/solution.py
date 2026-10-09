import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q                     # number of columns / persons
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    # ---------- DLX structures ----------
    # column headers: 0..n-1, plus a special header at index n
    size = [0] * n                # number of nodes in each column
    up = []                       # node lists
    down = []
    left = []
    right = []
    col = []                      # column of each node
    row_id = []                   # which triple this node belongs to

    header = n                    # index of master header
    # initialise header links (circular)
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    for i in range(n + 1):
        left[i] = i - 1
        right[i] = i + 1
    left[0] = header
    right[header] = 0
    left[header] = n
    right[n] = header

    # for each column, a dummy node that points to itself (acts as column header)
    up = list(range(n + 1))
    down = list(range(n + 1))

    # add rows
    for idx, (a, b, c) in enumerate(triples):
        cols = (a, b, c)
        first = None
        prev = None
        for cc in cols:
            node = len(col)
            col.append(cc)
            row_id.append(idx)
            # vertical links
            up.append(up[cc])
            down.append(cc)
            down[up[cc]] = node
            up[cc] = node
            size[cc] += 1
            # horizontal links
            if first is None:
                first = node
                left.append(node)   # temporary, will fix later
                right.append(node)
            else:
                left.append(prev)
                right.append(first)
                right[prev] = node
                left[first] = node
            prev = node
        # close the row circularly (already done by linking to first)

    # ---------- DLX operations ----------
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

    solution = []

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
            solution.append(row_id[r])
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
            solution.pop()
            r = down[r]
        uncover(cc)
        return False

    ok = search(0)
    out = []
    if ok:
        out.append("YES")
        for idx in solution:
            a, b, c = triples[idx]
            out.append(f"{a+1} {b+1} {c+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()