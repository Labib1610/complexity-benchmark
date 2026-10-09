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
    # ---------- DLX structures ----------
    # header node is 0
    # column headers are 1..n
    size = [0] * (n + 1)          # size of each column
    col = [0]                     # column of each node (node 0 dummy)
    up = [0]; down = [0]; left = [0]; right = [0]

    # link column headers in a circular list (left/right)
    for i in range(n + 1):
        left.append(i - 1)
        right.append(i + 1)
    left[0] = n
    right[n] = 0
    for i in range(1, n + 1):
        up.append(i)
        down.append(i)

    row_of_node = []              # which input row a node belongs to
    row_head = []                 # one node index per row (first node)

    # ---------- add rows ----------
    for idx, (a, b, c) in enumerate(triples):
        nodes = []
        for col_id in (a, b, c):
            node = len(col)
            col.append(col_id)
            row_of_node.append(idx)
            # vertical links
            up.append(up[col_id])
            down.append(col_id)
            down[up[col_id]] = node
            up[col_id] = node
            size[col_id] += 1
            nodes.append(node)
        # horizontal links (circular)
        k = len(nodes)
        for i in range(k):
            left.append(nodes[(i - 1) % k])
            right.append(nodes[(i + 1) % k])
        row_head.append(nodes[0])

    # quick impossibility test
    for c in range(1, n + 1):
        if size[c] == 0:
            print("NO")
            return

    solution_rows = []

    # ---------- DLX core operations ----------
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

    # ---------- recursive search ----------
    def search():
        if right[0] == 0:          # no columns left
            return True
        # choose column with minimal size
        c = right[0]
        min_sz = size[c]
        j = right[c]
        while j != 0:
            if size[j] < min_sz:
                c = j
                min_sz = size[j]
                if min_sz == 0:
                    break
            j = right[j]
        if min_sz == 0:
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
        print("YES")
        # output triples in the order they were selected
        for idx in solution_rows:
            a, b, c = triples[idx]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()