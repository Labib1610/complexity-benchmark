import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Bitmask for each tier tracking assigned workers
    tier_mask = [0, 0, 0]
    # Bitmask for each worker tracking incompatible workers
    incompatible = [0] * n
    
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        incompatible[u] |= (1 << v)
        incompatible[v] |= (1 << u)
    
    assignment = [0] * n
    
    def backtrack(worker):
        if worker == n:
            return True
        
        for tier in range(3):
            # Check if tier is valid (no conflict with incompatible workers)
            if tier_mask[tier] & incompatible[worker] == 0:
                assignment[worker] = tier + 1
                tier_mask[tier] |= (1 << worker)
                if backtrack(worker + 1):
                    return True
                tier_mask[tier] &= ~(1 << worker)
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()