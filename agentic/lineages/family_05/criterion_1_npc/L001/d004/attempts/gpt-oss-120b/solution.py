import sys

sys.setrecursionlimit(1000000)

class DLXNode:
    __slots__ = ('left', 'right', 'up', 'down', 'col', 'row_id')
    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.col = None
        self.row_id = -1

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
        # link columns horizontally
        last = self.header
        for c in self.cols:
            last.right = c
            c.left = last
            last = c
        last.right = self.header
        self.header.left = last
        self.solution = []
        self.row_nodes = []   # keep a reference to any node of each row

    def add_row(self, row_id, col_indices):
        first = None
        for ci in col_indices:
            col = self.cols[ci]
            node = DLXNode()
            node.col = col
            node.row_id = row_id
            # vertical links
            node.down = col
            node.up = col.up
            col.up.down = node
            col.up = node
            col.size += 1
            # horizontal links
            if first is None:
                first = node
                node.right = node.left = node
            else:
                node.right = first
                node.left = first.left
                first.left.right = node
                first.left = node
        self.row_nodes.append(first)

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
            self.solution.append(r.row_id)
            j = r.right
            while j != r:
                self.cover(j.col)
                j = j.right
            if self.search(k+1):
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
    points = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        points.append((x, y, z))
    n_cols = 3 * k
    dlx = DLX(n_cols)
    for idx, (x, y, z) in enumerate(points):
        dlx.add_row(idx, [x, k + y, 2 * k + z])
    if dlx.search(0):
        print("YES")
        for row_id in dlx.solution:
            x, y, z = points[row_id]
            print(x + 1, y + 1, z + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()