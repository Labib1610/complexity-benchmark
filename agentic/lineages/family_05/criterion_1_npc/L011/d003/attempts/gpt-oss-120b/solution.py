import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # column indices: 0..k-1 molds, k..2k-1 dyes, 2k..3k-1 packs
    ncol = 3 * k

    rows = []          # list of triples (x,y,z)
    row_nodes = []     # list of column indices for each row

    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        rows.append((x + 1, y + 1, z + 1))
        row_nodes.append([x, k + y, 2 * k + z])

    # ---------- DLX structures ----------
    max_nodes = 3 * t + ncol + 1
    up = [0] * max_nodes
    down = [0] * max_nodes
    left = [0] * max_nodes
    right = [0] * max_nodes
    col = [0] * max_nodes
    row_id = [0] * max_nodes
    size = [0] * (ncol + 1)          # size[0] unused, columns are 1..ncol

    header = 0
    # header linked list of column headers 1..ncol
    for i in range(ncol + 1):
        up[i] = down[i] = i
        left[i] = i - 1
        right[i] = i + 1
    left[0] = ncol
    right[ncol] = 0

    node_cnt = ncol + 1

    # add rows
    for r, cols in enumerate(row_nodes, start=1):
        first = -1
        for c in cols:
            c += 1                     # shift to 1‑based column header
            node = node_cnt
            node_cnt += 1

            col[node] = c
            row_id[node] = r

            # vertical links
            up[node] = up[c]
            down[node] = c
            down[up[c]] = node
            up[c] = node
            size[c] += 1

            # horizontal links
            if first == -1:
                left[node] = right[node] = node
                first = node
            else:
                left[node] = left[first]
                right[node] = first
                right[left[first]] = node
                left[first] = node

    solution = []
    answer = None

    def cover(c):
        # remove column header
        left[right[c]] = left[c]
        right[left[c]] = right[c]
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

    def search(kd):
        nonlocal answer
        if right[header] == header:          # all columns covered
            answer = solution.copy()
            return True
        # choose column with minimal size
        c = right[header]
        min_sz = size[c]
        cc = c
        while cc != header:
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
            solution.append(row_id[r])
            j = right[r]
            while j != r:
                cover(col[j])
                j = right[j]
            if search(kd + 1):
                return True
            # backtrack
            j = left[r]
            while j != r:
                uncover(col[j])
                j = left[j]
            solution.pop()
            r = down[r]
        uncover(c)
        return False

    if search(0):
        out = ["YES"]
        for idx in answer:
            out.append("{} {} {}".format(*rows[idx - 1]))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()