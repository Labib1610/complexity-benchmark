import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    rows = []
    for _ in range(t):
        s = int(next(it)) - 1
        c = int(next(it)) - 1
        f = int(next(it)) - 1
        rows.append((s, c, f))

    # DLX implementation for exact cover with 3k columns
    n_cols = 3 * k

    # Node structure
    class Node:
        __slots__ = ('l', 'r', 'u', 'd', 'col', 'row')
        def __init__(self):
            self.l = self.r = self.u = self.d = self
            self.col = None
            self.row = -1

    header = Node()
    cols = [Node() for _ in range(n_cols)]
    for i, col in enumerate(cols):
        col.col = i
        col.u = col.d = col
        # link into header list
        col.l = header.l
        col.r = header
        header.l.r = col
        header.l = col

    # add rows
    row_nodes = []
    for idx, (s, c, f) in enumerate(rows):
        first = None
        for col_idx in (s, k + c, 2 * k + f):
            col = cols[col_idx]
            node = Node()
            node.col = col_idx
            node.row = idx
            # vertical links
            node.u = col.u
            node.d = col
            col.u.d = node
            col.u = node
            # horizontal links
            if first is None:
                first = node
                node.l = node.r = node
            else:
                node.l = first.l
                node.r = first
                first.l.r = node
                first.l = node
        row_nodes.append(first)

    solution = []
    found = False

    def cover(col_node: Node):
        # remove column header
        col_node.r.l = col_node.l
        col_node.l.r = col_node.r
        # remove rows
        i = col_node.d
        while i != col_node:
            j = i.r
            while j != i:
                j.d.u = j.u
                j.u.d = j.d
                j = j.r
            i = i.d

    def uncover(col_node: Node):
        i = col_node.u
        while i != col_node:
            j = i.l
            while j != i:
                j.d.u = j
                j.u.d = j
                j = j.l
            i = i.u
        col_node.r.l = col_node
        col_node.l.r = col_node

    def search():
        nonlocal found
        if header.r == header:
            # all columns covered
            found = True
            return
        # choose column with minimal size
        c = header.r
        min_sz = float('inf')
        col = None
        while c != header:
            sz = 0
            node = c.d
            while node != c:
                sz += 1
                node = node.d
            if sz < min_sz:
                min_sz = sz
                col = c
                if sz == 0:
                    break
            c = c.r
        if min_sz == 0:
            return
        cover(col)
        r = col.d
        while r != col and not found:
            solution.append(r.row)
            j = r.r
            while j != r:
                cover(cols[j.col])
                j = j.r
            search()
            if found:
                return
            # backtrack
            solution.pop()
            j = r.l
            while j != r:
                uncover(cols[j.col])
                j = j.l
            r = r.d
        uncover(col)

    search()
    out = []
    if found:
        out.append("YES")
        for idx in solution:
            s, c, f = rows[idx]
            out.append(f"{s+1} {c+1} {f+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()