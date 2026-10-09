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
    class Node:
        __slots__ = ('up', 'down', 'left', 'right', 'col', 'row_id')
        def __init__(self):
            self.up = self.down = self.left = self.right = self
            self.col = None
            self.row_id = -1

    # column headers: 0..n-1, plus a root header at index n
    size = [0] * (n + 1)
    col_head = [Node() for _ in range(n + 1)]
    root = col_head[n]
    # link column headers horizontally
    for i in range(n + 1):
        col_head[i].col = i
        col_head[i].up = col_head[i].down = col_head[i]
        col_head[i].left = col_head[i - 1] if i > 0 else root
        col_head[i].right = col_head[i + 1] if i < n else root
    root.left = col_head[n - 1]
    root.right = col_head[0]

    # add rows
    row_nodes = []   # one node per row (any of its three nodes) to retrieve row_id
    for rid, (a, b, c) in enumerate(triples):
        cols = (a - 1, b - 1, c - 1)   # zero‑based
        first = None
        prev = None
        for col in cols:
            node = Node()
            node.col = col
            node.row_id = rid
            # vertical link
            header = col_head[col]
            node.down = header
            node.up = header.up
            header.up.down = node
            header.up = node
            size[col] += 1
            # horizontal link
            if first is None:
                first = node
            else:
                node.left = prev
                prev.right = node
            prev = node
        # close the row circle
        first.left = prev
        prev.right = first
        row_nodes.append(first)

    # ---------- DLX operations ----------
    def cover(col):
        # remove column header
        col_head[col].right.left = col_head[col].left
        col_head[col].left.right = col_head[col].right
        # remove rows
        i = col_head[col].down
        while i != col_head[col]:
            j = i.right
            while j != i:
                j.down.up = j.up
                j.up.down = j.down
                size[j.col] -= 1
                j = j.right
            i = i.down

    def uncover(col):
        i = col_head[col].up
        while i != col_head[col]:
            j = i.left
            while j != i:
                size[j.col] += 1
                j.down.up = j
                j.up.down = j
                j = j.left
            i = i.up
        col_head[col].right.left = col_head[col]
        col_head[col].left.right = col_head[col]

    solution_rows = []

    # ---------- recursive search ----------
    def search():
        # if no columns left -> success
        if root.right == root:
            return True
        # choose column with minimal size
        c = root.right
        min_sz = size[c.col]
        col = c
        while c != root:
            if size[c.col] < min_sz:
                min_sz = size[c.col]
                col = c
                if min_sz == 0:
                    break
            c = c.right
        if min_sz == 0:
            return False
        col_idx = col.col
        cover(col_idx)
        r = col.down
        while r != col:
            solution_rows.append(r.row_id)
            # cover other columns of this row
            j = r.right
            while j != r:
                cover(j.col)
                j = j.right
            if search():
                return True
            # backtrack
            j = r.left
            while j != r:
                uncover(j.col)
                j = j.left
            solution_rows.pop()
            r = r.down
        uncover(col_idx)
        return False

    possible = search()
    out = []
    if possible:
        out.append("YES")
        for rid in solution_rows:
            a, b, c = triples[rid]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()