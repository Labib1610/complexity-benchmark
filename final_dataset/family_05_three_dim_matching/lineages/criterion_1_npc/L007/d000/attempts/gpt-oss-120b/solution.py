import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []
    for _ in range(t):
        e = int(next(it)) - 1          # 0‑based
        s = int(next(it)) - 1
        p = int(next(it)) - 1
        triples.append((e, s, p))

    # ----- build DLX structure -----
    # columns: 0..k-1 enzymes, k..2k-1 substrates, 2k..3k-1 profiles
    ncol = 3 * k
    max_nodes = t * 3 + ncol + 1

    # arrays (1‑based node indexing, 0 is header)
    up = [0] * max_nodes
    down = [0] * max_nodes
    left = [0] * max_nodes
    right = [0] * max_nodes
    col = [0] * max_nodes          # column of node
    row_id = [0] * max_nodes       # which triple (index) the node belongs to
    size = [0] * ncol              # number of nodes in each column

    # header links columns in a circular list
    for i in range(ncol):
        up[i] = down[i] = i
        left[i] = i - 1 if i > 0 else ncol - 1
        right[i] = i + 1 if i + 1 < ncol else 0
    left[0] = ncol - 1
    right[ncol - 1] = 0

    node_cnt = ncol  # next free index

    def add_node(r, c):
        nonlocal node_cnt
        node = node_cnt
        node_cnt += 1
        col[node] = c
        row_id[node] = r

        # insert into column c (at bottom)
        up[node] = up[c]
        down[node] = c
        down[up[c]] = node
        up[c] = node
        size[c] += 1

        return node

    # create rows
    for idx, (e, s, p) in enumerate(triples):
        nodes = []
        for c in (e, k + s, 2 * k + p):
            nodes.append(add_node(idx, c))
        # link the three nodes horizontally (circular)
        for i in range(3):
            left[nodes[i]] = nodes[i - 1]
            right[nodes[i]] = nodes[(i + 1) % 3]

    # ----- DLX operations -----
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

    solution = []
    answer_rows = None

    # heuristic: choose column with minimal size
    def choose_column():
        c = right[0]
        min_sz = size[c]
        best = c
        while c != 0:
            if size[c] < min_sz:
                min_sz = size[c]
                best = c
                if min_sz == 0:
                    break
            c = right[c]
        return best

    def search():
        nonlocal answer_rows
        if right[0] == 0:          # all columns covered
            answer_rows = solution.copy()
            return True
        c = choose_column()
        if size[c] == 0:
            return False
        cover(c)
        r = down[c]
        while r != c:
            solution.append(row_id[r])
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
            solution.pop()
            r = down[r]
        uncover(c)
        return False

    possible = search()

    out = []
    if possible:
        out.append("YES")
        for idx in answer_rows:
            e, s, p = triples[idx]
            out.append(f"{e+1} {s+1} {p+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()