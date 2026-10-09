import sys

# Increase recursion depth for search
sys.setrecursionlimit(5000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    
    n = 3 * q
    
    # DLX arrays
    # Nodes: 0 is root, 1..n are column headers, then 3 nodes per row
    max_nodes = 1 + n + 3 * t + 10
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes
    row_idx = [0] * max_nodes
    sz = [0] * (n + 1)
    
    # Initialize column headers
    L[0] = n
    R[0] = 1
    for c in range(1, n + 1):
        L[c] = c - 1
        R[c] = (c + 1) if c < n else 0
        U[c] = c
        D[c] = c
        sz[c] = 0
        
    node_cnt = n
    
    triplets = []
    idx = 2
    for r in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        triplets.append((a, b, c))
        
        row_nodes = []
        for col in (a, b, c):
            node_cnt += 1
            node = node_cnt
            row_nodes.append(node)
            
            sz[col] += 1
            C[node] = col
            row_idx[node] = r
            
            # Vertical linking into column col
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            
        # Horizontal circular linking for the row of 3 nodes
        n1, n2, n3 = row_nodes
        L[n1], R[n1] = n3, n2
        L[n2], R[n2] = n1, n3
        L[n3], R[n3] = n2, n1

    def cover(col):
        R[L[col]] = R[col]
        L[R[col]] = L[col]
        i = D[col]
        while i != col:
            j = R[i]
            while j != i:
                D[U[j]] = D[j]
                U[D[j]] = U[j]
                sz[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                sz[C[j]] += 1
                D[U[j]] = j
                U[D[j]] = j
                j = L[j]
            i = U[i]
        R[L[col]] = col
        L[R[col]] = col

    solution = []

    def search():
        if R[0] == 0:
            return True
        
        # Choose column with minimum size (MRV heuristic)
        c = R[0]
        min_sz = sz[c]
        temp = R[c]
        while temp != 0:
            if sz[temp] < min_sz:
                min_sz = sz[temp]
                c = temp
            temp = R[temp]
            
        if min_sz == 0:
            return False
            
        cover(c)
        i = D[c]
        while i != c:
            solution.append(row_idx[i])
            j = R[i]
            while j != i:
                cover(C[j])
                j = R[j]
            if search():
                return True
            solution.pop()
            j = L[i]
            while j != i:
                uncover(C[j])
                j = L[j]
            i = D[i]
        uncover(c)
        return False

    if search():
        out = ["YES"]
        for r in solution:
            a, b, c = triplets[r]
            out.append(f"{a} {b} {c}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()