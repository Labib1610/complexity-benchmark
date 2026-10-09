import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # If t == 0 and k > 0, impossible
    if t == 0:
        print("NO")
        return
    
    # Map each element to a column index
    # specialists: 1..k -> columns 1..k
    # machines:   1..k -> columns k+1..2k
    # times:      1..k -> columns 2k+1..3k
    total_cols = 3 * k
    
    # Build DLX
    # Node 0 is head
    # Columns 1..total_cols
    # We'll use arrays for left, right, up, down, col, row
    # We'll dynamically add nodes
    
    # Initialize column headers
    left = [0] * (total_cols + 1)
    right = [0] * (total_cols + 1)
    up = [0] * (total_cols + 1)
    down = [0] * (total_cols + 1)
    col = [0] * (total_cols + 1)
    row = [0] * (total_cols + 1)
    size = [0] * (total_cols + 1)
    
    # Head node 0
    left[0] = total_cols
    right[0] = 1
    for i in range(1, total_cols + 1):
        left[i] = i - 1
        right[i] = i + 1 if i < total_cols else 0
        up[i] = i
        down[i] = i
        col[i] = i
        row[i] = 0
        size[i] = 0
    
    # We'll store rows for output
    row_triples = []  # each entry is (x, y, z) 1-indexed
    # For each row, we'll store its column nodes
    row_nodes = []  # list of node indices for each row
    
    node_cnt = total_cols  # next node index to use
    
    # Read allowed triples
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        # columns for this triple
        cols = [x, k + y, 2 * k + z]
        # Create nodes for this row
        first_node = None
        prev_node = None
        for c in cols:
            node_cnt += 1
            # Extend arrays
            left.append(0)
            right.append(0)
            up.append(0)
            down.append(0)
            col.append(c)
            row.append(len(row_triples))
            # Link vertically into column c
            # Insert before column header c (i.e., after up[c])
            up[node_cnt] = up[c]
            down[node_cnt] = c
            down[up[c]] = node_cnt
            up[c] = node_cnt
            size[c] += 1
            # Link horizontally
            if first_node is None:
                first_node = node_cnt
                left[node_cnt] = node_cnt
                right[node_cnt] = node_cnt
            else:
                left[node_cnt] = prev_node
                right[node_cnt] = first_node
                right[prev_node] = node_cnt
                left[first_node] = node_cnt
            prev_node = node_cnt
        row_triples.append((x, y, z))
        row_nodes.append(first_node)
    
    # Quick check: if any column has size 0, impossible
    for i in range(1, total_cols + 1):
        if size[i] == 0:
            print("NO")
            return
    
    # DLX search
    solution = []  # row indices
    
    def cover(c):
        right[left[c]] = right[c]
        left[right[c]] = left[c]
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
        right[left[c]] = c
        left[right[c]] = c
    
    def search():
        if right[0] == 0:
            return True
        # Choose column with minimum size
        c = right[0]
        min_size = size[c]
        j = right[c]
        while j != 0:
            if size[j] < min_size:
                min_size = size[j]
                c = j
                if min_size == 0:
                    return False
            j = right[j]
        cover(c)
        r = down[c]
        while r != c:
            solution.append(row[r])
            # Cover all columns in this row
            j = right[r]
            while j != r:
                cover(col[j])
                j = right[j]
            if search():
                return True
            # Backtrack
            j = left[r]
            while j != r:
                uncover(col[j])
                j = left[j]
            solution.pop()
            r = down[r]
        uncover(c)
        return False
    
    if search():
        print("YES")
        for idx in solution:
            x, y, z = row_triples[idx]
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()