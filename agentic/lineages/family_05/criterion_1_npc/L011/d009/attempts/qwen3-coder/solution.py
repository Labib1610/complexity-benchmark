import sys
from itertools import combinations

def is_non_singular(values):
    """Check if the Vandermonde-like matrix formed by values is non-singular."""
    n = len(values)
    # For a Vandermonde matrix, determinant is product of (values[i] - values[j]) for i < j
    # If any two values are equal, determinant is zero
    sorted_vals = sorted(values)
    for i in range(n - 1):
        if sorted_vals[i] == sorted_vals[i + 1]:
            return False
    return True

def solve():
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    configs = []
    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx + 1])
        z = int(data[idx + 2])
        configs.append((x, y, z))
        idx += 3
    
    # Try all combinations of k configurations
    for combo in combinations(configs, k):
        # Extract x, y, z values
        xs = [config[0] for config in combo]
        ys = [config[1] for config in combo]
        zs = [config[2] for config in combo]
        
        # Check if all three matrices are non-singular
        if is_non_singular(xs) and is_non_singular(ys) and is_non_singular(zs):
            print("YES")
            for config in combo:
                print(config[0], config[1], config[2])
            return
    
    print("NO")

solve()