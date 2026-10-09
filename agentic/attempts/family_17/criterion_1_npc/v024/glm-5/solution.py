import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    n = 3 * q
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    triples = []
    for _ in range(t):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        triples.append((a, b, c))
    
    # Build column -> list of row indices
    col_to_rows = defaultdict(list)
    for i, (a, b, c) in enumerate(triples):
        col_to_rows[a].append(i)
        col_to_rows[b].append(i)
        col_to_rows[c].append(i)
    
    # Check all servers have at least one option
    for s in range(1, n + 1):
        if s not in col_to_rows or len(col_to_rows[s]) == 0:
            print("NO")
            return
    
    # DLX implementation
    # Each node: [left, right, up, down, col_header, row_id]
    # Header nodes: [left, right, up, down, col_id, size]
    
    # Create headers
    headers = [None] * (n + 1)  # headers[col] = header node
    # Circular doubly linked list of headers
    # header[0] is root
    
    root = [None, None, None, None, 0, 0]
    root[0] = root
    root[1] = root
    
    prev = root
    for col in range(1, n + 1):
        h = [prev, root, None, None, col, 0]
        h[2] = h  # up
        h[3] = h  # down
        prev[1] = h
        root[0] = h
        headers[col] = h
        prev = h
    
    # Create nodes for each triple
    # For each row, link nodes horizontally
    row_first_node = [None] * t
    
    for i, (a, b, c) in enumerate(triples):
        cols = [a, b, c]
        nodes = []
        for col in cols:
            h = headers[col]
            node = [None, None, None, None, h, i]
            # Insert below header (at bottom)
            up_node = h[2]  # current last (up of header)
            down_node = h   # header itself
            node[2] = up_node
            node[3] = down_node
            up_node[3] = node
            down_node[2] = node
            h[5] += 1
            nodes.append(node)
        
        # Link horizontally (circular)
        for j in range(3):
            nodes[j][0] = nodes[(j - 1) % 3]
            nodes[j][1] = nodes[(j + 1) % 3]
        
        row_first_node[i] = nodes[0]
    
    solution = []
    
    def cover(col_header):
        # Remove header from header list
        col_header[0][1] = col_header[1]
        col_header[1][0] = col_header[0]
        # For each row in this column
        node = col_header[3]
        while node != col_header:
            # Cover all other columns in this row
            rnode = node[1]
            while rnode != node:
                h = rnode[4]
                rnode[2][3] = rnode[3]
                rnode[3][2] = rnode[2]
                h[5] -= 1
                rnode = rnode[1]
            node = node[3]
    
    def uncover(col_header):
        # For each row in this column (reverse order)
        node = col_header[2]
        while node != col_header:
            rnode = node[0]
            while rnode != node:
                h = rnode[4]
                h[5] += 1
                rnode[2][3] = rnode
                rnode[3][2] = rnode
                rnode = rnode[0]
            node = node[2]
        # Restore header
        col_header[0][1] = col_header
        col_header[1][0] = col_header
    
    def search():
        if root[1] == root:
            return True  # All columns covered
        
        # Choose column with minimum size (S heuristic)
        best_col = None
        best_size = float('inf')
        h = root[1]
        while h != root:
            if h[5] < best_size:
                best_size = h[5]
                best_col = h
                if best_size <= 1:
                    break
            h = h[1]
        
        if best_size == 0:
            return False
        
        cover(best_col)
        
        node = best_col[3]
        while node != best_col:
            solution.append(node[5])
            rnode = node[1]
            while rnode != node:
                cover(rnode[4])
                rnode = rnode[1]
            
            if search():
                return True
            
            # Backtrack
            solution.pop()
            rnode = node[0]
            while rnode != node:
                uncover(rnode[4])
                rnode = rnode[0]
            
            node = node[3]
        
        uncover(best_col)
        return False
    
    if search():
        print("YES")
        for row_id in solution:
            a, b, c = triples[row_id]
            print(f"{a} {b} {c}")
    else:
        print("NO")

solve()