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

    C = 3 * k                     # number of columns
    # ---------- DLX structures ----------
    # node 0 is the header, nodes 1..C are column headers
    left = [0] * (1 + C)
    right = [0] * (1 + C)
    up = [0] * (1 + C)
    down = [0] * (1 + C)
    column = [0] * (1 + C)        # column of a node (for row nodes)
    row_id = [0] * (1 + C)        # row id for a node (for row nodes)
    size = [0] * (C + 1)          # size of each column (only for headers)

    # initialise header list (circular)
    for i in range(C + 1):
        left[i] = i - 1 if i != 0 else C
        right[i] = i + 1 if i != C else 0
        up[i] = down[i] = i       # empty column

    # ---------- add rows ----------
    def add_row(rid, cols):
        first = None
        for c in cols:
            node = len(left)
            left.append(0)
            right.append(0)
            up.append(0)
            down.append(0)
            column.append(c)
            row_id.append(rid)

            # vertical link into column c
            up[node] = up[c]
            down[node] = c
            down[up[c]] = node
            up[c] = node
            size[c] += 1

            # horizontal link within the row
            if first is None:
                first = node
                left[node] = right[node] = node
            else:
                # insert node to the left of first
                left[node] = left[first]
                right[node] = first
                right[left[first]] = node
                left[first] = node

    for idx, (x, y, z) in enumerate(triples):
        cols = [x + 1, k + y + 1, 2 * k + z + 1]   # column headers are 1‑based
        add_row(idx, cols)

    # quick impossibility test
    for c in range(1, C + 1):
        if size[c] == 0:
            print("NO")
            return

    # ---------- DLX core ----------
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
                size[column[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                size[column[j]] += 1
                down[up[j]] = j
                up[down[j]] = j
                j = left[j]
            i = up[i]
        right[left[c]] = c
        left[right[c]] = c

    solution = []

    def search():
        if right[0] == 0:          # no columns left
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
            solution.append(row_id[r])
            j = right[r]
            while j != r:
                cover(column[j])
                j = right[j]
            if search():
                return True
            # backtrack
            j = left[r]
            while j != r:
                uncover(column[j])
                j = left[j]
            solution.pop()
            r = down[r]
        uncover(c)
        return False

    if search():
        print("YES")
        for rid in solution:
            x, y, z = triples[rid]
            print(x + 1, y + 1, z + 1)
    else:
        print("NO")


if __name__ == "__main__":
    solve()