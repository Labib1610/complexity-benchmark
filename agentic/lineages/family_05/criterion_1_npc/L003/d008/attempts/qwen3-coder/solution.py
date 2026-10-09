from itertools import combinations

def is_stable(selection):
    k = len(selection)
    # Check each parameter: frequency (x), amplitude (y), phase (z)
    for param_index in range(3):
        values = [module[param_index] for module in selection]
        # Create the characteristic matrix
        matrix = []
        for r in range(k):
            row = []
            for c in range(k):
                row.append(values[c] ** r)
            matrix.append(row)
        
        # Compute determinant using Gaussian elimination
        det = determinant(matrix)
        if det == 0:
            return False
    return True

def determinant(matrix):
    n = len(matrix)
    # Copy matrix to avoid modifying original
    m = [row[:] for row in matrix]
    
    det = 1
    for i in range(n):
        # Find pivot
        pivot_row = i
        for row in range(i+1, n):
            if abs(m[row][i]) > abs(m[pivot_row][i]):
                pivot_row = row
        
        # Swap rows if needed
        if pivot_row != i:
            m[i], m[pivot_row] = m[pivot_row], m[i]
            det *= -1
        
        # Check for zero pivot
        if m[i][i] == 0:
            return 0
            
        # Eliminate column
        for row in range(i+1, n):
            factor = m[row][i] / m[i][i]
            for col in range(i, n):
                m[row][col] -= factor * m[i][col]
    
    # Multiply diagonal elements
    for i in range(n):
        det *= m[i][i]
        
    return round(det)

def solve():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    
    k, t = map(int, input_lines[0].split())
    
    if t < k:
        print("NO")
        return
    
    modules = []
    for i in range(1, t+1):
        x, y, z = map(int, input_lines[i].split())
        modules.append((x, y, z))
    
    # Try all combinations of k modules
    for combo in combinations(modules, k):
        if is_stable(combo):
            print("YES")
            for module in combo:
                print(module[0], module[1], module[2])
            return
    
    print("NO")

solve()