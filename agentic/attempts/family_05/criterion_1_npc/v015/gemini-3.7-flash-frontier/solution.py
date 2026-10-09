import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    triples = []
    idx = 2
    for _ in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx + 1]) - 1
        z = int(input_data[idx + 2]) - 1
        idx += 3
        triples.append((x, y, z))
    
    # Total columns = 3 * k
    # col 0..k-1: x
    # col k..2k-1: y
    # col 2k..3k-1: z
    num_cols = 3 * k
    
    # Pre-check: if any element is not present at all, return NO
    has_x = [False] * k
    has_y = [False] * k
    has_z = [False] * k
    for x, y, z in triples:
        has_x[x] = True
        has_y[y] = True
        has_z[z] = True
    if not (all(has_x) and all(has_y) and all(has_z)):
        print("NO")
        return

    # DLX / Dancing Links implementation
    # Items: 0 to num_cols - 1
    # We create DLX nodes
    class Node:
        __slots__ = ('left', 'right', 'up', 'down', 'col', 'row_id')
        def __init__(self, col=None, row_id=-1):
            self.left = self
            self.right = self
            self.up = self
            self.down = self
            self.col = col
            self.row_id = row_id

    class Column(Node):
        __slots__ = ('size', 'name')
        def __init__(self, name):
            super().__init__()
            self.size = 0
            self.name = name
            self.col = self

    root = Column(-1)
    columns = [Column(i) for i in range(num_cols)]
    
    # Link columns into root
    last = root
    for c in columns:
        c.left = last
        c.right = root
        last.right = c
        root.left = c
        last = c

    def cover(c):
        c.right.left = c.left
        c.left.right = c.right
        i = c.down
        while i != c:
            j = i.right
            while j != i:
                j.down.up = j.up
                j.up.down = j.down
                j.col.size -= 1
                j = j.right
            i = i.down

    def uncover(c):
        i = c.up
        while i != c:
            j = i.left
            while j != i:
                j.col.size += 1
                j.down.up = j
                j.up.down = j
                j = j.left
            i = i.up
        c.right.left = c
        c.left.right = c

    for r_id, (x, y, z) in enumerate(triples):
        cols_for_row = [columns[x], columns[k + y], columns[2 * k + z]]
        first_node = None
        for col in cols_for_row:
            node = Node(col=col, row_id=r_id)
            node.up = col.up
            node.down = col
            col.up.down = node
            col.up = node
            col.size += 1
            if first_node is None:
                first_node = node
            else:
                node.left = first_node.left
                node.right = first_node
                first_node.left.right = node
                first_node.left = node

    solution = []

    def search():
        if root.right == root:
            return True
        
        # MRV: pick column with smallest size
        c = root.right
        min_c = c
        min_size = c.size
        curr = c.right
        while curr != root:
            if curr.size < min_size:
                min_size = curr.size
                min_c = curr
                if min_size == 0:
                    break
            curr = curr.right
        
        if min_size == 0:
            return False
        
        c = min_c
        cover(c)
        r = c.down
        while r != c:
            solution.append(r.row_id)
            j = r.right
            while j != r:
                cover(j.col)
                j = j.right
            
            if search():
                return True
            
            solution.pop()
            j = r.left
            while j != r:
                uncover(j.col)
                j = j.left
            r = r.down
        
        uncover(c)
        return False

    if search():
        print("YES")
        for r_id in solution:
            x, y, z = triples[r_id]
            print(f"{x + 1} {y + 1} {z + 1}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()