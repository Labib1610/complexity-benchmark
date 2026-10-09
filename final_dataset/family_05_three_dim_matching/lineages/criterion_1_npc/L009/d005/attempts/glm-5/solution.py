import sys
from sys import setrecursionlimit
setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    paths = []
    for i in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        paths.append((x, y, z))
    
    if t < k:
        print("NO")
        return
    
    # Bits to cover: 1 through 3k (0-indexed as 0 through 3k-1)
    # Path (x,y,z) covers bits: x-1, k+y-1, 2k+z-1
    n_cols = 3 * k
    n_rows = t
    
    # Build sparse representation
    row_cols = []
    for (x, y, z) in paths:
        cols = [x-1, k+y-1, 2*k+z-1]
        row_cols.append(cols)
    
    # DLX
    # Use arrays
    size = n_cols + 1  # headers 0..n_cols-1, root = n_cols
    ROOT = n_cols
    
    L = [0] * (size + n_rows * 3 + 10)
    R = [0] * (size + n_rows * 3 + 10)
    U = [0] * (size + n_rows * 3 + 10)
    D = [0] * (size + n_rows * 3 + 10)
    col = [0] * (size + n_rows * 3 + 10)
    row_id = [0] * (size + n_rows * 3 + 10)
    cnt = [0] * size  # count for each column header
    
    # Initialize circular linked list for headers
    for i in range(n_cols + 1):
        L[i] = (i - 1) if i > 0 else n_cols
        R[i] = (i + 1) if i < n_cols else 0
        U[i] = i
        D[i] = i
        col[i] = i
        row_id[i] = -1
    
    R[ROOT] = 0 if n_cols > 0 else ROOT
    L[ROOT] = n_cols - 1 if n_cols > 0 else ROOT
    L[0] = ROOT
    R[n_cols - 1] = ROOT if n_cols > 0 else ROOT
    
    node_count = n_cols + 1  # next available node index
    
    for r in range(n_rows):
        prev = -1
        first = -1
        for c in row_cols[r]:
            nid = node_count
            node_count += 1
            # Insert into column c
            up_node = U[c]
            D[nid] = c
            U[nid] = up_node
            D[up_node] = nid
            U[c] = nid
            col[nid] = c
            row_id[nid] = r
            cnt[c] += 1
            
            if prev == -1:
                first = nid
                L[nid] = nid
                R[nid] = nid
            else:
                L[nid] = prev
                R[nid] = first
                R[prev] = nid
                L[first] = nid
            prev = nid
    
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
                cnt[col[j]] -= 1
                j = R[j]
            i = D[i]
    
    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                cnt[col[j]] += 1
                D[U[j]] = j
                U[D[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c
    
    def search():
        if R[ROOT] == ROOT:
            return True
        # Choose column with fewest options
        c = R[ROOT]
        best = c
        s = cnt[c]
        c = R[c]
        while c != ROOT:
            if cnt[c] < s:
                s = cnt[c]
                best = c
            c = R[c]
        c = best
        if s == 0:
            return False
        cover(c)
        i = D[c]
        while i != c:
            solution.append(row_id[i])
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
        for r in solution:
            x, y, z = paths[r]
            print(x, y, z)
    else:
        print("NO")

solve()