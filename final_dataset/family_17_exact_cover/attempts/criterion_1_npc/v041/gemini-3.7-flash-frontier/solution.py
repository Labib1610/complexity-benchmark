import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    
    num_cols = 3 * q
    
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]) - 1
        b = int(input_data[idx+1]) - 1
        c = int(input_data[idx+2]) - 1
        idx += 3
        triples.append((a, b, c))

    # DLX Implementation
    # Columns 0 to num_cols - 1 represent elements to cover
    # Node 0 is the root/header
    # Nodes 1 to num_cols are column headers
    
    MAX_NODES = num_cols + 1 + 3 * t + 5
    L = [0] * MAX_NODES
    R = [0] * MAX_NODES
    U = [0] * MAX_NODES
    D = [0] * MAX_NODES
    col_idx = [0] * MAX_NODES
    row_idx = [0] * MAX_NODES
    sz = [0] * (num_cols + 1)
    
    # Initialize column headers
    for i in range(num_cols + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = i
        D[i] = i
    L[0] = num_cols
    R[num_cols] = 0
    
    node_cnt = num_cols + 1
    
    for r_id, (c1, c2, c3) in enumerate(triples):
        cols = [c1 + 1, c2 + 1, c3 + 1]
        first = node_cnt
        for j, c in enumerate(cols):
            cur = node_cnt + j
            col_idx[cur] = c
            row_idx[cur] = r_id
            sz[c] += 1
            
            # Insert into column c list (at the bottom, above c)
            U[cur] = U[c]
            D[cur] = c
            D[U[c]] = cur
            U[c] = cur
            
            # Horizontal circular links
            L[cur] = cur - 1
            R[cur] = cur + 1
            
        L[first] = first + 2
        R[first + 2] = first
        node_cnt += 3

    def cover(c):
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                sz[col_idx[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                sz[col_idx[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    ans = []

    def search():
        if R[0] == 0:
            return True
        
        # Choose column with minimum size
        c = R[0]
        min_sz = sz[c]
        cur = R[c]
        while cur != 0:
            if sz[cur] < min_sz:
                min_sz = sz[cur]
                c = cur
            cur = R[cur]
            
        if min_sz == 0:
            return False
            
        cover(c)
        r = D[c]
        while r != c:
            ans.append(row_idx[r])
            j = R[r]
            while j != r:
                cover(col_idx[j])
                j = R[j]
                
            if search():
                return True
                
            ans.pop()
            j = L[r]
            while j != r:
                uncover(col_idx[j])
                j = L[j]
            r = D[r]
            
        uncover(c)
        return False

    if search():
        out = ["YES"]
        for r_id in ans:
            a, b, c = triples[r_id]
            out.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()