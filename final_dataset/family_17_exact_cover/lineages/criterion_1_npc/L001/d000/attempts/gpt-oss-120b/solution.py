import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q                     # number of columns / persons

    # ---------- DLX structures ----------
    class Node:
        __slots__ = ('l','r','u','d','col','row')
        def __init__(self):
            self.l = self.r = self.u = self.d = self
            self.col = None
            self.row = None

    class Column(Node):
        __slots__ = ('size','name')
        def __init__(self, name):
            super().__init__()
            self.size = 0
            self.name = name

    header = Column(-1)           # root
    columns = [Column(i) for i in range(1, n+1)]

    # link column headers horizontally
    last = header
    for col in columns:
        col.l = last
        col.r = header
        last.r = col
        header.l = col
        last = col

    rows_nodes = []               # for output: list of (a,b,c) per row
    # ---------- insert rows ----------
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        triple = (a, b, c)
        # create three nodes
        nodes = [Node() for _ in range(3)]
        for node, val in zip(nodes, triple):
            col = columns[val-1]
            node.col = col
            node.row = len(rows_nodes)   # index of this row
            # vertical insertion (at bottom)
            node.u = col.u
            node.d = col
            col.u.d = node
            col.u = node
            col.size += 1
        # horizontal linking (circular)
        for i in range(3):
            nodes[i].r = nodes[(i+1)%3]
            nodes[i].l = nodes[(i-1)%3]
        rows_nodes.append(triple)

    # early impossibility check
    for col in columns:
        if col.size == 0:
            print("NO")
            return

    # ---------- DLX operations ----------
    def cover(col: Column):
        col.r.l = col.l
        col.l.r = col.r
        i = col.d
        while i != col:
            j = i.r
            while j != i:
                j.d.u = j.u
                j.u.d = j.d
                j.col.size -= 1
                j = j.r
            i = i.d

    def uncover(col: Column):
        i = col.u
        while i != col:
            j = i.l
            while j != i:
                j.col.size += 1
                j.d.u = j
                j.u.d = j
                j = j.l
            i = i.u
        col.r.l = col
        col.l.r = col

    solution = []

    def search(k: int) -> bool:
        if header.r == header:          # all columns covered
            return True
        # choose column with minimal size
        c = header.r
        min_sz = c.size
        col = c
        while c != header:
            if c.size < min_sz:
                min_sz = c.size
                col = c
                if min_sz == 0:
                    break
            c = c.r
        if min_sz == 0:
            return False
        cover(col)
        r = col.d
        while r != col:
            solution.append(r.row)
            j = r.r
            while j != r:
                cover(j.col)
                j = j.r
            if search(k+1):
                return True
            # backtrack
            solution.pop()
            j = r.l
            while j != r:
                uncover(j.col)
                j = j.l
            r = r.d
        uncover(col)
        return False

    if search(0):
        print("YES")
        for idx in solution:
            a,b,c = rows_nodes[idx]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()