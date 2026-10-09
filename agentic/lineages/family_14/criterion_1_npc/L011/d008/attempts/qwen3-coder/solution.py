import sys
from itertools import combinations

def find_min_cost(n, m, t, T, vectors):
    # T is the target set (1-indexed)
    # vectors is list of (u, v, w) where vector is b_u - b_v with cost w
    
    # We need to find a subset C of vectors such that:
    # 1. The vectors in C span a subspace of dimension |S| - 1
    # 2. |C| = |S| - 1
    # 3. For every k in S \ T, b_k appears in at least 2 vectors in C
    # Where S = T union {indices that appear in vectors in C}
    
    # This is essentially finding a minimum weight spanning tree in a graph
    # where nodes are the active indices and edges are the vectors
    # But with additional constraints
    
    # Let's try all possible subsets of vectors and check if they satisfy the conditions
    min_cost = float('inf')
    
    # Try all possible non-empty subsets of vectors
    for r in range(0, m + 1):
        for subset_indices in combinations(range(m), r):
            C = [vectors[i] for i in subset_indices]
            cost = sum(v[2] for v in C)
            
            if cost >= min_cost:
                continue
                
            # Determine the active index set S
            S = set(T)
            for u, v, w in C:
                S.add(u)
                S.add(v)
            
            # Check cardinality requirement: |C| = |S| - 1
            if len(C) != len(S) - 1:
                continue
                
            # Check non-target participation
            valid = True
            for k in S:
                if k not in T:
                    count = 0
                    for u, v, w in C:
                        if u == k or v == k:
                            count += 1
                    if count < 2:
                        valid = False
                        break
            if not valid:
                continue
                
            # Check dimension requirement
            # We need to check if the vectors are linearly independent
            # and span a space of dimension |S| - 1
            
            # Create a mapping from indices in S to 0-based indices
            index_map = {idx: i for i, idx in enumerate(sorted(S))}
            dim = len(S)
            
            # Represent each vector as a coordinate vector in R^|S|
            # But since each vector is b_u - b_v, it has +1 at position u and -1 at position v
            # The dimension of the space they span is |S| - 1 because they're all in the subspace
            # where sum of coordinates is 0
            
            # To check linear independence, we can build a matrix and compute its rank
            # But since we already have |C| = |S| - 1, we just need to check if they're independent
            
            if len(C) == 0:
                if len(S) == 1:  # |S| - 1 = 0
                    min_cost = min(min_cost, cost)
                continue
                
            # Build matrix for rank computation
            matrix = []
            for u, v, w in C:
                row = [0] * dim
                row[index_map[u]] = 1
                row[index_map[v]] = -1
                matrix.append(row)
            
            # Compute rank of matrix
            rank = compute_rank(matrix)
            
            if rank == len(C):
                min_cost = min(min_cost, cost)
    
    return min_cost

def compute_rank(matrix):
    if not matrix:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Gaussian elimination to row echelon form
    mat = [row[:] for row in matrix]  # Copy matrix
    rank = 0
    col = 0
    
    for row in range(rows):
        if col >= cols:
            break
        pivot_row = row
        while pivot_row < rows and mat[pivot_row][col] == 0:
            pivot_row += 1
            
        if pivot_row == rows:
            col += 1
            continue
            
        # Swap rows
        mat[row], mat[pivot_row] = mat[pivot_row], mat[row]
        
        # Eliminate column
        for i in range(row + 1, rows):
            if mat[i][col] != 0:
                # In real numbers, we would use division, but for integer matrices
                # we need to be careful. However, since our vectors have only +1, -1, 0
                # we can work with integers
                factor1 = mat[row][col]
                factor2 = mat[i][col]
                for j in range(cols):
                    mat[i][j] = mat[i][j] * factor1 - mat[row][j] * factor2
                    
        rank += 1
        col += 1
        
    return rank

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    T = []
    for _ in range(t):
        T.append(int(data[idx]))
        idx += 1
        
    vectors = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        vectors.append((u, v, w))
    
    result = find_min_cost(n, m, t, T, vectors)
    print(result)

if __name__ == "__main__":
    main()