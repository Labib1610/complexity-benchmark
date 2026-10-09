import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q  # number of items
    rows = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append((a, b, c))

    # ---------- DLX structures ----------
    # column header nodes: 0..n-1
    # each node: left, right, up, down, col, row_id
    size = n + 1  # header at index n
    left = list(range(size))
    right = list(range(size))
    up = list(range(size))
    down = list(range(size))
    col = [i for i in range(size)]
    row_id = [-1] * size
    col_size = [0] * n

    # link column headers in a circular list, header is n
    for i in range(n):
        left[i] = i - 1 if i else n
        right[i] = i + 1 if i + 1 < n else n
    left[n] = n - 1 if n else n
    right[n] = 0

    node_cnt = n + 1  # next free index

    # add rows
    for rid, (a, b, c) in enumerate(rows):
        for item in (a, b, c):
            # create node
            idx = node_cnt
            node_cnt += 1
            col.append(item)
            row_id.append(rid)
            # vertical links
            up.append(up[item])
            down.append(item)
            up[item] = idx
            down[up[idx]] = idx
            col_size[item] += 1
            # horizontal links (temporarily self-loop)
            left.append(idx)
            right.append(idx)

        # now link the three nodes horizontally
        base = node_cnt - 3
        # nodes: base, base+1, base+2
        left[base] = base + 2
        right[base] = base + 1
        left[base + 1] = base
        right[base + 1] = base + 2
        left[base + 2] = base + 1
        right[base + 2] = base

    solution_rows = []

    def cover(c):
        # remove column header
        left[right[c]] = left[c]
        right[left[c]] = right[c]
        # remove rows
        i = down[c]
        while i != c:
            j = right[i]
            while j != i:
                up[down[j]] = up[j]
                down[up[j]] = down[j]
                col_size[col[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                col_size[col[j]] += 1
                up[down[j]] = j
                down[up[j]] = j
                j = left[j]
            i = up[i]
        left[right[c]] = c
        right[left[c]] = c

    def search(k):
        if right[n] == n:  # all columns covered
            return True
        # choose column with minimal size
        c = right[n]
        min_sz = col_size[c]
        j = right[c]
        while j != n:
            if col_size[j] < min_sz:
                c = j
                min_sz = col_size[j]
                if min_sz == 0:
                    break
            j = right[j]
        if min_sz == 0:
            return False
        cover(c)
        r = down[c]
        while r != c:
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
        uncover(c)
        return False

    possible = search(0)

    out = []
    if possible:
        out.append("YES")
        used = set()
        for rid in solution_rows:
            a, b, c = rows[rid]
            out.append(f"{a+1} {b+1} {c+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()