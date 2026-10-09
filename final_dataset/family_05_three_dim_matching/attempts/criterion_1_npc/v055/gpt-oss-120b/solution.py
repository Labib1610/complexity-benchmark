import sys

sys.setrecursionlimit(1000000)

class Node:
    __slots__ = ('left', 'right', 'up', 'down', 'col', 'row_id')
    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.col = None          # Column header
        self.row_id = None       # Index of the original triple

class Column(Node):
    __slots__ = ('size', 'name')
    def __init__(self, name):
        super().__init__()
        self.size = 0
        self.name = name

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

    # ----- build DLX -----
    header = Column('header')
    columns = []

    # create column headers for surgeons, rooms, times
    for i in range(k):
        c = Column(('S', i))
        columns.append(c)
    for i in range(k):
        c = Column(('R', i))
        columns.append(c)
    for i in range(k):
        c = Column(('T', i))
        columns.append(c)

    # link column headers horizontally
    last = header
    for c in columns:
        c.left = last
        c.right = header
        last.right = c
        header.left = c
        last = c

    # add rows
    row_nodes = []          # list of one node per row (any node of that row)
    for idx, (x, y, z) in enumerate(triples):
        # three columns indices
        col_idxs = [x, k + y, 2 * k + z]
        first = None
        prev = None
        for ci in col_idxs:
            col = columns[ci]
            node = Node()
            node.col = col
            node.row_id = idx

            # vertical link (insert at bottom of column)
            node.up = col.up
            node.down = col
            col.up.down = node
            col.up = node
            col.size += 1

            # horizontal link within the row
            if first is None:
                first = node
            else:
                node.left = prev
                node.right = first
                prev.right = node
                first.left = node
            prev = node
        row_nodes.append(first)

    # ----- DLX operations -----
    solution_rows = []

    def cover(col: Column):
        col.right.left = col.left
        col.left.right = col.right
        i = col.down
        while i != col:
            j = i.right
            while j != i:
                j.down.up = j.up
                j.up.down = j.down
                j.col.size -= 1
                j = j.right
            i = i.down

    def uncover(col: Column):
        i = col.up
        while i != col:
            j = i.left
            while j != i:
                j.col.size += 1
                j.down.up = j
                j.up.down = j
                j = j.left
            i = i.up
        col.right.left = col
        col.left.right = col

    # choose column with minimal size
    def choose_column():
        c = header.right
        best = c
        min_sz = c.size
        while c != header:
            if c.size < min_sz:
                min_sz = c.size
                best = c
                if min_sz == 0:
                    break
            c = c.right
        return best

    found = False

    def search():
        nonlocal found
        if header.right == header:          # all columns covered
            found = True
            return
        col = choose_column()
        if col.size == 0:
            return
        cover(col)
        r = col.down
        while r != col and not found:
            solution_rows.append(r.row_id)
            j = r.right
            while j != r:
                cover(j.col)
                j = j.right
            search()
            if found:
                return
            # backtrack
            solution_rows.pop()
            j = r.left
            while j != r:
                uncover(j.col)
                j = j.left
            r = r.down
        uncover(col)

    search()

    out = []
    if found:
        out.append("YES")
        for idx in solution_rows:
            x, y, z = triples[idx]
            out.append(f"{x+1} {y+1} {z+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()