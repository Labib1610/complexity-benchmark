import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    constraints = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        constraints.append((u - 1, v - 1))  # 0-indexed
    
    # Precompute which pairs (a, b) are valid (form non-degenerate triangle)
    # Points: P=(a, a^2), Q=(b, b^2), R=(4, 16)
    # Collinear if (b^2 - a^2)(4 - a) = (16 - a^2)(b - a)
    valid_pair = [[False] * 4 for _ in range(4)]
    for a in range(1, 4):
        for b in range(1, 4):
            lhs = (b * b - a * a) * (4 - a)
            rhs = (16 - a * a) * (b - a)
            valid_pair[a][b] = (lhs != rhs)
    
    # Try all 3^n combinations
    best = None
    total = 3 ** n
    
    for mask in range(total):
        # Build sequence from mask (base-3 representation)
        seq = []
        temp = mask
        valid = True
        for _ in range(n):
            seq.append((temp % 3) + 1)
            temp //= 3
        
        # Check all constraints
        for u, v in constraints:
            if not valid_pair[seq[u]][seq[v]]:
                valid = False
                break
        
        if valid:
            # Convert to tuple for comparison (lexicographically)
            seq_tuple = tuple(seq)
            if best is None or seq_tuple < best:
                best = seq_tuple
    
    if best is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, best)))

solve()