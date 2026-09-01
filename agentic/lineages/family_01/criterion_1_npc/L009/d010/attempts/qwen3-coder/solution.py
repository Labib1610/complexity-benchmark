from itertools import combinations

def harmonic_mean_is_integer(c1, c2):
    # H = 2*c1*c2 / (c1 + c2)
    # Check if this is an integer
    numerator = 2 * c1 * c2
    denominator = c1 + c2
    return numerator % denominator == 0

def is_valid_pair(c1, c2):
    # Valid if harmonic mean is NOT an integer
    return not harmonic_mean_is_integer(c1, c2)

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    constraints = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        constraints.append((u, v))
        index += 2
    
    # Precompute which pairs of concentrations are valid
    # valid_pairs[c1][c2] is True if concentrations c1 and c2 are compatible
    valid_pairs = [[False]*4 for _ in range(4)]
    for c1 in [1, 2, 3]:
        for c2 in [1, 2, 3]:
            valid_pairs[c1][c2] = is_valid_pair(c1, c2)
    
    # Try all 3^n combinations in lexicographical order
    # We can do this by trying 1,2,3 for each position in order
    # But we need to prune early when constraints are violated
    
    # Use backtracking
    def backtrack(pos, current):
        if pos == n:
            return current[:]
        
        for c in [1, 2, 3]:
            # Check if this choice violates any constraint with previous positions
            valid = True
            for u, v in constraints:
                if (u == pos and v < pos):
                    if not valid_pairs[c][current[v]]:
                        valid = False
                        break
                elif (v == pos and u < pos):
                    if not valid_pairs[current[u]][c]:
                        valid = False
                        break
            
            if valid:
                current[pos] = c
                result = backtrack(pos + 1, current)
                if result is not None:
                    return result
        return None
    
    solution = backtrack(0, [0]*n)
    
    if solution is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, solution)))

solve()