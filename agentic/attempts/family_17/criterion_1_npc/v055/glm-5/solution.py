import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    n = 3 * q
    rows = []
    for _ in range(t):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        rows.append((a, b, c))
    
    if t < q:
        print("NO")
        return
    
    # DLX implementation
    # Node structure: we use arrays for speed
    # Each node: [L, R, U, D, col, row]
    # Header nodes: one per column + root
    
    # Count nodes: 3*t + n + 1
    max_nodes = 3 * t + n + 10
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    col = [0] * max_nodes
    row = [0] * max_nodes
    size = [0] * (n + 1)  # column sizes, index 0 is root (unused for size)
    
    # Root is node 0
    # Column headers are nodes 1..n
    # Data nodes start at n+1
    
    # Set up circular doubly linked list for headers
    for i in range(n + 1):
        L[i] = (i - 1) if i > 0 else n
        R[i] = (i + 1) if i < n else 0
        U[i] = i
        D[i] = i
        col[i] = i
        row[i] = -1  # header
    
    next_node = n + 1
    
    for r_idx, (a, b, c) in enumerate(rows):
        # a, b, c are 1-indexed frequencies, which map to column headers a, b, c
        nodes_in_row = []
        for freq in (a, b, c):
            node = next_node
            next_node += 1
            
            # Insert into column freq
            U[node] = U[freq]
            D[node] = freq
            D[U[freq]] = node
            U[freq] = node
            
            col[node] = freq
            row[node] = r_idx
            size[freq] += 1
            nodes_in_row.append(node)
        
        # Link nodes in row horizontally
        for i in range(3):
            L[nodes_in_row[i]] = nodes_in_row[(i - 1) % 3]
            R[nodes_in_row[i]] = nodes_in_row[(i + 1) % 3]
    
    # Algorithm X
    solution = []
    found = [False]
    
    setrecursionlimit(10000)
    
    def cover(c_col):
        L[R[c_col]] = L[c_col]
        R[L[c_col]] = R[c_col]
        i = D[c_col]
        while i != c_col:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                size[col[j]] -= 1
                j = R[j]
            i = D[i]
    
    def uncover(c_col):
        i = U[c_col]
        while i != c_col:
            j = L[i]
            while j != i:
                size[col[j]] += 1
                D[U[j]] = j
                U[D[j]] = j
                j = L[j]
            i = U[i]
        L[R[c_col]] = c_col
        R[L[c_col]] = c_col
    
    def search(k):
        if R[0] == 0:
            if k == q:
                found[0] = True
            return
        
        # Pruning: if remaining columns can't be covered by remaining rows needed
        # Each row covers 3 columns, so we need at least (remaining_cols + 2) // 3 more rows
        # But we can't easily count remaining rows, so skip this optimization
        
        # Choose column with minimum size (S heuristic)
        best_col = R[0]
        best_size = size[best_col]
        if best_size == 0:
            return  # Can't cover this column
        
        c_col = R[0]
        while c_col != 0:
            s = size[c_col]
            if s < best_size:
                best_size = s
                best_col = c_col
                if s == 1:
                    break
            c_col = R[c_col]
        
        c_col = best_col
        cover(c_col)
        
        r = D[c_col]
        while r != c_col and not found[0]:
            solution.append(row[r])
            j = R[r]
            while j != r:
                cover(col[j])
                j = R[j]
            
            search(k + 1)
            
            if found[0]:
                return
            
            # Backtrack
            j = L[r]
            while j != r:
                uncover(col[j])
                j = L[j]
            solution.pop()
            r = D[r]
        
        uncover(c_col)
    
    search(0)
    
    if found[0]:
        print("YES")
        for r_idx in solution:
            a, b, c = rows[r_idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

solve()