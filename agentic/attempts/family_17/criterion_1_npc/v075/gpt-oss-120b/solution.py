import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q                     # number of columns (tasks)

    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    # ---------- DLX structures ----------
    # column headers: 0..n-1, plus a dummy header at index n
    size = n + 1                  # total column nodes
    up = list(range(size))
    down = list(range(size))
    left = list(range(size))
    right = list(range(size))
    col_size = [0] * size         # only meaningful for column headers
    col_head = list(range(size))  # column of each node (itself for headers)

    # row list: for each row we keep one representative node index
    row_rep = []

    node_cnt = size               # next free index

    # helper to link a node vertically into column c
    def link_vert(node, c):
        nonlocal up, down, col_head, col_size
        up[node] = up[c]
        down[node] = c
        down[up[c]] = node
        up[c] = node
        col_head[node] = c
        col_size[c] += 1

    # helper to link a node horizontally into its row (circular)
    def link_horiz(first, node):
        # insert node to the right of first
        right[node] = right[first]
        left[node] = first
        left[right[first]] = node
        right[first] = node

    # build rows
    for r_idx, (a, b, c) in enumerate(triples):
        # create first node of the row
        first = node_cnt
        node_cnt += 1
        link_vert(first, a)
        row_rep.append(first)

        # second node
        second = node_cnt
        node_cnt += 1
        link_vert(second, b)
        link_horiz(first, second)

        # third node
        third = node_cnt
        node_cnt += 1
        link_vert(third, c)
        link_horiz(first, third)

    # ---------- DLX operations ----------
    header = n  # dummy header node

    # initially link column headers left-right
    for i in range(n):
        left[i] = i - 1 if i > 0 else header
        right[i] = i + 1 if i < n - 1 else header
    left[header] = n - 1
    right[header] = 0

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
                col_size[col_head[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                col_size[col_head[j]] += 1
                down[up[j]] = j
                up[down[j]] = j
                j = left[j]
            i = up[i]
        right[left[c]] = c
        left[right[c]] = c

    solution = []

    # heuristic: choose column with minimal size
    def choose_column():
        c = right[header]
        min_sz = 10**9
        best = -1
        while c != header:
            if col_size[c] < min_sz:
                min_sz = col_size[c]
                best = c
                if min_sz == 0:
                    break
            c = right[c]
        return best

    def dfs():
        if right[header] == header:   # all columns covered
            return True
        c = choose_column()
        if c == -1 or col_size[c] == 0:
            return False
        cover(c)
        r = down[c]
        while r != c:
            solution.append(r)
            j = right[r]
            while j != r:
                cover(col_head[j])
                j = right[j]
            if dfs():
                return True
            # backtrack
            solution.pop()
            j = left[r]
            while j != r:
                uncover(col_head[j])
                j = left[j]
            r = down[r]
        uncover(c)
        return False

    if dfs():
        out = ["YES"]
        # translate node indices back to original triples
        for node in solution:
            # collect the three columns of this row
            cols = []
            j = node
            while True:
                cols.append(col_head[j] + 1)   # back to 1‑based
                j = right[j]
                if j == node:
                    break
            cols.sort()
            out.append(f"{cols[0]} {cols[1]} {cols[2]}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()