import sys
from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

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
    
    # Precompute which pairs (a, b) satisfy gcd(a, b) < lcm(a, b)
    # Values are from {1, 2, 3}
    valid_pair = {}
    for a in [1, 2, 3]:
        for b in [1, 2, 3]:
            valid_pair[(a, b)] = (gcd(a, b) < lcm(a, b))
    
    # Try all possible assignments
    best = None
    
    # Generate all possible sequences
    # Since n <= 40 and values are 1, 2, 3, we need to be smart
    # But 3^40 is too large, so we use backtracking with pruning
    
    def backtrack(idx, current):
        nonlocal best
        if best is not None:
            return
        if idx == n:
            # Check all constraints
            for u, v in constraints:
                if not valid_pair[(current[u], current[v])]:
                    return
            best = current[:]
            return
        
        for val in [1, 2, 3]:
            # Check constraints with already assigned positions
            valid = True
            for u, v in constraints:
                if u == idx:
                    if v < idx:
                        if not valid_pair[(val, current[v])]:
                            valid = False
                            break
                elif v == idx:
                    if u < idx:
                        if not valid_pair[(current[u], val)]:
                            valid = False
                            break
            if valid:
                current.append(val)
                backtrack(idx + 1, current)
                current.pop()
                if best is not None:
                    return
    
    backtrack(0, [])
    
    if best is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, best)))

solve()