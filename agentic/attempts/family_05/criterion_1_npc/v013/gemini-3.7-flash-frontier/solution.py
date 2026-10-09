import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

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
        y = int(input_data[idx+1]) - 1
        z = int(input_data[idx+2]) - 1
        idx += 3
        triples.append((x, y, z))
        
    num_cols = 3 * k
    num_nodes = num_cols + 1 + 3 * t
    
    L = [0] * num_nodes
    R = [0] * num_nodes
    U = [0] * num_nodes
    D = [0] * num_nodes
    col = [0] * num_nodes
    row = [0] * num_nodes
    size = [0] * (num_cols + 1)
    
    head = 0
    L[0] = num_cols
    R[0] = 1
    for i in range(1, num_cols + 1):
        L[i] = i - 1
        R[i] = (i + 1) if i < num_cols else 0
        U[i] = i
        D[i] = i
        col[i] = i
        size[i] = 0
        
    node_idx = num_cols + 1
    for r, (x, y, z) in enumerate(triples):
        c1 = x + 1
        c2 = k + y + 1
        c3 = 2 * k + z + 1
        
        cols = [c1, c2, c3]
        first_node = node_idx
        
        for i, c in enumerate(cols):
            curr = node_idx + i
            col[curr] = c
            row[curr] = r
            size[c] += 1
            
            U[curr] = U[c]
            D[curr] = c
            D[U[c]] = curr
            U[c] = curr
            
        L[first_node] = first_node + 2
        R[first_node] = first_node + 1
        L[first_node + 1] = first_node
        R[first_node + 1] = first_node + 2
        L[first_node + 2] = first_node + 1
        R[first_node + 2] = first_node
        
        node_idx += 3

    def cover(c):
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                size[col[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[col[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    solution = []

    def search():
        if R[head] == head:
            return True
        
        # Choose column with minimum size
        c = R[head]
        min_size = size[c]
        curr = R[c]
        while curr != head:
            if size[curr] < min_size:
                min_size = size[curr]
                c = curr
            curr = R[curr]
            
        if min_size == 0:
            return False
        
        cover(c)
        r = D[c]
        while r != c:
            solution.append(row[r])
            j = R[r]
            while j != r:
                cover(col[j])
                j = R[j]
            
            if search():
                return True
            
            solution.pop()
            j = L[r]
            while j != r:
                uncover(col[j])
                j = L[j]
            r = D[r]
            
        uncover(c)
        return False

    if search():
        print("YES")
        out = []
        for r_idx in solution:
            x, y, z = triples[r_idx]
            out.append(f"{x + 1} {y + 1} {z + 1}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()