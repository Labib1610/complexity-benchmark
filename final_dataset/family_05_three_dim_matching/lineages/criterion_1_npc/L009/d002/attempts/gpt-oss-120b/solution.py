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

    n_cols = 3 * k
    # DLX structures
    max_nodes = t * 3 + n_cols + 1
    left = [0] * max_nodes
    right = [0] * max_nodes
    up = [0] * max_nodes
    down = [0] * max_nodes
    col = [0] * max_nodes
    row_id = [0] * max_nodes
    size = [0] * (n_cols + 1)  # column sizes, header at 0

    # header node 0
    for i in range(n_cols + 1):
        left[i] = i - 1
        right[i] = i + 1
        up[i] = down[i] = i
    left[0] = n_cols
    right[n_cols] = 0

    node_cnt = n_cols + 1

    def add_row(rid, columns):
        nonlocal node_cnt
        first = None
        for c in columns:
            node = node_cnt
            node_cnt += 1
            col[node] = c + 1  # shift by 1 because column 0 is header
            row_id[node] = rid
            # vertical links
            up[node] = up[col[node]]
            down[node] = col[node]
            down[up[node]] = node
            up[down[node]] = node
            size[col[node]] += 1
            # horizontal links
            if first is None:
                left[node] = right[node] = node
                first = node
            else:
                left[node] = left[first]
                right[node] = first
                right[left[node]] = node
                left[first] = node

    for idx, (x, y, z) in enumerate(triples):
        add_row(idx, [x, k + y, 2 * k + z])

    solution = []

    def cover(c):
        # remove column header
        left[right[c]] = left[c]
        right[left[c]] = right[c]
        i = down[c]
        while i != c:
            j = right[i]
            while j != i:
                up[down[j]] = up[j]
                down[up[j]] = down[j]
                size[col[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                size[col[j]] += 1
                up[down[j]] = j
                down[up[j]] = j
                j = left[j]
            i = up[i]
        left[right[c]] = c
        right[left[c]] = c

    def search(depth):
        if right[0] == 0:  # all columns covered
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
            solution.append(row_id[r])
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
            solution.pop()
            r = down[r]
        uncover(c)
        return False

    if search(0):
        out = ["YES"]
        for rid in solution:
            x, y, z = triples[rid]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()