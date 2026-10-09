import sys

sys.setrecursionlimit(1000000)

class DLXNode:
    __slots__ = ('left', 'right', 'up', 'down', 'col', 'row_id')
    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.col = None          # Column header
        self.row_id = -1         # index of the original row (triple)

class ColumnNode(DLXNode):
    __slots__ = ('size', 'name')
    def __init__(self, name):
        super().__init__()
        self.size = 0
        self.name = name

class DLX:
    def __init__(self, n_cols):
        self.header = ColumnNode('header')
        self.cols = [ColumnNode(i) for i in range(n_cols)]
        # link column headers horizontally
        last = self.header
        for c in self.cols:
            c.left = last
            c.right = self.header
            last.right = c
            self.header.left = c
            last = c
        self.solution = []          # list of chosen row nodes
        self.row_nodes = []         # keep reference to any node of each row

    def add_row(self, row_id, columns):
        first = None
        for col_idx in columns:
            col = self.cols[col_idx]
            node = DLXNode()
            node.col = col
            node.row_id = row_id
            # vertical links
            node.up = col.up
            node.down = col
            col.up.down = node
            col.up = node
            col.size += 1
            # horizontal links
            if first is None:
                first = node
                node.left = node.right = node
            else:
                node.left = first.left
                node.right = first
                first.left.right = node
                first.left = node
        self.row_nodes.append(first)

    # cover a column
    def cover(self, col):
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

    # uncover a column (reverse of cover)
    def uncover(self, col):
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

    def search(self, k):
        if self.header.right == self.header:   # all columns covered
            return True
        # choose column with minimal size
        c = self.header.right
        min_sz = c.size
        col = c
        while c != self.header:
            if c.size < min_sz:
                min_sz = c.size
                col = c
                if min_sz == 0:
                    break
            c = c.right
        if min_sz == 0:
            return False
        self.cover(col)
        r = col.down
        while r != col:
            self.solution.append(r)
            j = r.right
            while j != r:
                self.cover(j.col)
                j = j.right
            if self.search(k + 1):
                return True
            # backtrack
            self.solution.pop()
            j = r.left
            while j != r:
                self.uncover(j.col)
                j = j.left
            r = r.down
        self.uncover(col)
        return False

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
    dlx = DLX(n_cols)
    for idx, (x, y, z) in enumerate(triples):
        dlx.add_row(idx, [x, k + y, 2 * k + z])

    if dlx.search(0):
        out = ['YES']
        for node in dlx.solution:
            rid = node.row_id
            x, y, z = triples[rid]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()