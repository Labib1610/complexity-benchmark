import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))

    # columns: 0..k-1 hardness, k..2k-1 malleability, 2k..3k-1 conductivity
    ncol = 3 * k

    # DLX structures
    size = ncol + 1                     # column headers 0..ncol-1, root=ncol
    up = list(range(size))
    down = list(range(size))
    left = list(range(size))
    right = list(range(size))
    col = [i for i in range(size)]      # column of each node (header points to itself)
    cnt = [0] * ncol                    # number of nodes in each column
    row_of_node = []                    # for solution reconstruction

    # link column headers horizontally (circular)
    for i in range(ncol):
        left[i] = i - 1 if i else ncol
        right[i] = i + 1 if i + 1 < ncol else ncol
    left[ncol] = ncol - 1
    right[ncol] = 0

    node_id = ncol  # next free node index

    # add a row for each triple
    for idx, (x, y, z) in enumerate(triples):
        cols = [x, k + y, 2 * k + z]
        first = None
        for c in cols:
            node = node_id
            node_id += 1
            # vertical links
            up[node] = up[c]
            down[node] = c
            down[up[c]] = node
            up[c] = node
            col.append(c)
            cnt[c] += 1
            row_of_node.append(idx)   # store original triple index
            # horizontal links within the row
            if first is None:
                left[node] = right[node] = node
                first = node
            else:
                # insert to the left of first
                left[node] = left[first]
                right[node] = first
                right[left[first]] = node
                left[first] = node

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
                cnt[col[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                cnt[col[j]] += 1
                down[up[j]] = j
                up[down[j]] = j
                j = left[j]
            i = up[i]
        right[left[c]] = c
        left[right[c]] = c

    def search():
        if right[ncol] == ncol:          # all columns covered
            return True
        # choose column with minimal cnt
        c = right[ncol]
        min_cnt = cnt[c]
        cc = c
        while cc != ncol:
            if cnt[cc] < min_cnt:
                min_cnt = cnt[cc]
                c = cc
                if min_cnt == 0:
                    break
            cc = right[cc]
        if min_cnt == 0:
            return False
        cover(c)
        r = down[c]
        while r != c:
            solution_rows.append(row_of_node[r])
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
        for idx in solution_rows:
            x, y, z = triples[idx]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()