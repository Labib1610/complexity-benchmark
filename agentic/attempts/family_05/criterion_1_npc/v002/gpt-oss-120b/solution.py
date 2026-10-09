import sys

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

    if t < k:
        print("NO")
        return

    # DLX structures
    n_cols = 3 * k
    header = 0
    max_nodes = t * 3 + n_cols + 1

    left = [0] * max_nodes
    right = [0] * max_nodes
    up = [0] * max_nodes
    down = [0] * max_nodes
    col = [0] * max_nodes
    row_id = [0] * max_nodes
    size = [0] * (n_cols + 1)  # column sizes, 1-indexed for columns

    # init header and column headers (1..n_cols)
    for i in range(n_cols + 1):
        left[i] = i - 1
        right[i] = i + 1
        up[i] = down[i] = i
    left[0] = n_cols
    right[n_cols] = 0

    node_cnt = n_cols + 1  # next free node index

    # add rows
    for r_idx, (x, y, z) in enumerate(triples):
        cols = [x + 1, k + y + 1, 2 * k + z + 1]  # shift by 1 because column 0 is header
        first = None
        for c in cols:
            node = node_cnt
            node_cnt += 1
            col[node] = c
            row_id[node] = r_idx
            # vertical links
            up[node] = up[c]
            down[node] = c
            down[up[c]] = node
            up[c] = node
            size[c] += 1
            # horizontal links
            if first is None:
                left[node] = right[node] = node
                first = node
            else:
                left[node] = left[first]
                right[node] = first
                right[left[first]] = node
                left[first] = node

    solution_rows = []

    sys.setrecursionlimit(10000)

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

    def search(depth):
        if right[header] == header:
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
            if search(depth + 1):
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
        print("YES")
        used = set()
        for idx in solution_rows:
            x, y, z = triples[idx]
            print(x + 1, y + 1, z + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()