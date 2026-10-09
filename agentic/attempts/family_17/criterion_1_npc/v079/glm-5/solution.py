import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    n = 3 * q
    
    triads = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]); b = int(input_data[idx+1]); c = int(input_data[idx+2])
        idx += 3
        triads.append((a, b, c))
    
    # Build adjacency list: for each vertex, list of triad indices containing it
    adj = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triads):
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)
    
    # DLX (Dancing Links) for exact cover
    # We have n items (1..n) and t rows (triads)
    # Each row covers exactly 3 items
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    # Build sparse matrix
    # For each item, store list of rows containing it
    # We'll use the standard DLX approach with linked lists
    
    # Number of columns = n, number of rows = t
    # Build the DLX structure
    
    # Node structure: we'll use arrays
    # L, R, U, D, row, col
    
    # Header nodes for each column (1-indexed, 0 is the root)
    # We'll create nodes for each 1 in the matrix
    
    # Total nodes: 1 (root) + n (column headers) + 3*t (matrix entries)
    max_nodes = 1 + n + 3 * t + 10
    
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    row = [0] * max_nodes
    col = [0] * max_nodes
    size = [0] * max_nodes  # column sizes
    
    # Root node at index 0
    root = 0
    L[root] = n
    R[root] = 1
    
    # Column headers at indices 1..n
    for j in range(1, n + 1):
        col[j] = j
        row[j] = 0
        U[j] = j
        D[j] = j
        L[j] = j - 1
        R[j] = j + 1
        size[j] = 0
    
    R[n] = root
    L[1] = root
    
    # Matrix entries
    node_idx = n + 1
    
    for i, (a, b, c) in enumerate(triads):
        cols = [a, b, c]
        first = node_idx
        for j_pos in range(3):
            j = cols[j_pos]
            col[node_idx] = j
            row[node_idx] = i + 1
            
            # Vertical links
            U[node_idx] = U[j]
            D[node_idx] = j
            D[U[j]] = node_idx
            U[j] = node_idx
            size[j] += 1
            
            # Horizontal links
            if j_pos == 0:
                L[node_idx] = node_idx + 2  # will fix later
                R[node_idx] = node_idx + 1
            elif j_pos == 1:
                L[node_idx] = node_idx - 1
                R[node_idx] = node_idx + 1
            else:
                L[node_idx] = node_idx - 1
                R[node_idx] = first
                L[first] = node_idx
            
            node_idx += 1
    
    solution = []
    
    def cover(c):
        nonlocal L, R, U, D
        R[L[c]] = R[c]
        L[R[c]] = L[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                D[U[j]] = D[j]
                U[D[j]] = U[j]
                size[col[j]] -= 1
                j = R[j]
            i = D[i]
    
    def uncover(c):
        nonlocal L, R, U, D
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[col[j]] += 1
                D[U[j]] = j
                U[D[j]] = j
                j = L[j]
            i = U[i]
        R[L[c]] = c
        L[R[c]] = c
    
    def search():
        if R[root] == root:
            return True
        
        # Choose column with minimum size
        c = R[root]
        best = size[c]
        j = R[c]
        while j != root:
            if size[j] < best:
                best = size[j]
                c = j
            j = R[j]
        
        if best == 0:
            return False
        
        cover(c)
        i = D[c]
        while i != c:
            solution.append(row[i] - 1)
            j = R[i]
            while j != i:
                cover(col[j])
                j = R[j]
            
            if search():
                return True
            
            j = L[i]
            while j != i:
                uncover(col[j])
                j = L[j]
            solution.pop()
            
            i = D[i]
        uncover(c)
        return False
    
    if search():
        print("YES")
        for idx in solution:
            a, b, c = triads[idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

solve()