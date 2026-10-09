import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    n = 3 * q
    triples = []
    for _ in range(t):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        triples.append((a, b, c))
    
    if t < q:
        print("NO")
        return
    
    # DLX implementation
    # Columns: 1..n (elements to cover)
    # Rows: triples
    
    size = n + t + 1
    L = [0] * size
    R = [0] * size
    U = [0] * size
    D = [0] * size
    col = [0] * size
    row = [0] * size
    
    # Header nodes: 1..n
    # Row nodes: n+1 .. n+t (one per triple, used as row headers)
    # Element nodes: created dynamically
    
    # Initialize column headers (circular doubly linked)
    for i in range(1, n + 1):
        L[i] = i - 1 if i > 1 else n
        R[i] = i + 1 if i < n else 1
        U[i] = i
        D[i] = i
        col[i] = i
        row[i] = 0
    
    # We'll store element nodes in lists
    # For each triple, create 3 element nodes
    # Node IDs start from n + t + 1
    
    node_id = n + t + 1
    # We need to track row header nodes: n+1 .. n+t
    # Row header for triple i (0-indexed) is n + 1 + i
    
    # Build element nodes
    # For column c, we need to insert nodes in that column's vertical list
    
    # First, collect nodes per column
    col_nodes = [[] for _ in range(n + 1)]  # 1-indexed
    row_nodes = [[] for _ in range(t)]  # 0-indexed
    
    for i, (a, b, c) in enumerate(triples):
        row_header = n + 1 + i
        for v in (a, b, c):
            col_nodes[v].append(node_id)
            row_nodes[i].append(node_id)
            node_id += 1
    
    total_nodes = node_id
    # Extend arrays
    L.extend([0] * (total_nodes - size))
    R.extend([0] * (total_nodes - size))
    U.extend([0] * (total_nodes - size))
    D.extend([0] * (total_nodes - size))
    col.extend([0] * (total_nodes - size))
    row.extend([0] * (total_nodes - size))
    
    # Set up row headers
    for i in range(t):
        rh = n + 1 + i
        col[rh] = 0
        row[rh] = i + 1  # 1-indexed row
        # Row header points to itself if empty, but we'll link element nodes
        nodes = row_nodes[i]
        if not nodes:
            L[rh] = rh
            R[rh] = rh
        else:
            # Circular doubly linked list within row
            for j in range(len(nodes)):
                node = nodes[j]
                L[node] = nodes[j - 1] if j > 0 else rh
                R[node] = nodes[j + 1] if j < len(nodes) - 1 else rh
                col[node] = triples[i][j]
                row[node] = i + 1
            L[rh] = nodes[-1]
            R[rh] = nodes[0]
            # Also set L/R for first/last nodes properly
            L[nodes[0]] = rh
            R[nodes[-1]] = rh
    
    # Set up column vertical links
    for c in range(1, n + 1):
        nodes = col_nodes[c]
        if not nodes:
            # Column has no nodes - can't cover it
            print("NO")
            return
        # Link header -> nodes -> header
        prev = c  # header
        for node in nodes:
            D[prev] = node
            U[node] = prev
            prev = node
        D[prev] = c
        U[c] = prev
    
    # Count function - we'll track column sizes differently
    # Actually, let's use a simpler approach with size tracking
    # Let me just implement standard DLX
    
    # Rebuild with proper size tracking
    # Let me use a cleaner implementation
    
    pass

# Let me rewrite with a cleaner DLX
def solve_clean():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    n = 3 * q
    triples = []
    for _ in range(t):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        triples.append((a, b, c))
    
    if t < q:
        print("NO")
        return
    
    # Check all elements 1..n appear in at least one triple
    has_element = [False] * (n + 1)
    for a, b, c in triples:
        has_element[a] = True
        has_element[b] = True
        has_element[c] = True
    for i in range(1, n + 1):
        if not has_element[i]:
            print("NO")
            return
    
    # DLX
    # Node structure: L, R, U, D, col, row
    # Header nodes: 0 (root), 1..n (columns)
    
    # Count nodes needed
    num_nodes = 1 + n + 3 * t  # root + columns + element nodes
    
    L = [0] * num_nodes
    R = [0] * num_nodes
    U = [0] * num_nodes
    D = [0] * num_nodes
    col = [0] * num_nodes
    row = [0] * num_nodes
    size = [0] * num_nodes  # column sizes
    
    ROOT = 0
    
    # Initialize root and column headers
    # Root: 0, Columns: 1..n
    # Horizontal: 0 <-> 1 <-> 2 <-> ... <-> n <-> 0
    for i in range(n + 1):
        L[i] = (i - 1) if i > 0 else n
        R[i] = (i + 1) if i < n else 0
    
    for i in range(1, n + 1):
        U[i] = i
        D[i] = i
        col[i] = i
        row[i] = 0
        size[i] = 0
    
    # Create element nodes
    node_id = n + 1
    for r_idx, (a, b, c) in enumerate(triples):
        vals = [a, b, c]
        first_node = node_id
        for j, v in enumerate(vals):
            nid = node_id
            col[nid] = v
            row[nid] = r_idx
            size[v] += 1
            # Vertical: insert below header
            U[nid] = U[v]  # U[v] is currently the last node in column v
            D[nid] = v
            D[U[v]] = nid
            U[v] = nid
            # Horizontal: link within row
            if j == 0:
                L[nid] = nid
                R[nid] = nid
            else:
                L[nid] = node_id - 1
                R[nid] = first_node
                R[node_id - 1] = nid
                L[first_node] = nid
            node_id += 1
    
    solution = []
    
    def cover(c):
        L[R[c]] = L[c]
        R[L[c]] = R[c]
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
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[col[j]] += 1
                D[U[j]] = j
                U[D[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c
    
    def search():
        if R[ROOT] == ROOT:
            return True
        # Find column with minimum size
        c = R[ROOT]
        best = c
        best_size = size[c]
        while c != ROOT:
            if size[c] < best_size:
                best = c
                best_size = size[c]
                if best_size <= 1:
                    break
            c = R[c]
        
        if best_size == 0:
            return False
        
        cover(best)
        r = D[best]
        while r != best:
            solution.append(row[r])
            j = R[r]
            while j != r:
                cover(col[j])
                j = R[j]
            
            if search():
                return True
            
            # Undo
            solution.pop()
            j = L[r]
            while j != r:
                uncover(col[j])
                j = L[j]
            r = D[r]
        
        uncover(best)
        return False
    
    if search():
        print("YES")
        for r_idx in solution:
            a, b, c = triples[r_idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

solve_clean()