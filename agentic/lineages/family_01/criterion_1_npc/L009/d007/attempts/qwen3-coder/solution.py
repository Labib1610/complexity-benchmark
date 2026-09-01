from itertools import product

def are_collinear(a, b):
    # Points P = (a, a^2, a^3), Q = (b, b^2, b^3), R = (0, 0, 0)
    # They are collinear if vectors RP and RQ are linearly dependent
    # RP = (a, a^2, a^3), RQ = (b, b^2, b^3)
    # Cross product RP × RQ = (a^2*b^3 - a^3*b^2, a^3*b - a*b^3, a*b^2 - a^2*b)
    # If all components are zero, they are collinear
    if a == 0 or b == 0:
        return True
    # Simplify: (a^2*b^2*(b - a), a*b*(a^2 - b^2), a*b*(b - a))
    # This is zero only if a = b
    return a == b

def is_valid_for_constraint(cu, cv):
    # Check if points (cu, cu^2, cu^3), (cv, cv^2, cv^3), (0,0,0) are non-collinear
    return not are_collinear(cu, cv)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    constraints = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-indexed
        v = int(data[idx+1]) - 1
        constraints.append((u, v))
        idx += 2
    
    # Try all possible sequences in lexicographical order
    for seq in product([1, 2, 3], repeat=n):
        valid = True
        for u, v in constraints:
            if not is_valid_for_constraint(seq[u], seq[v]):
                valid = False
                break
        if valid:
            print("YES")
            print(' '.join(map(str, seq)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()