import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    paths = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        paths.append((x, y, z))
    
    # Calculate capacities
    # C_1 = 2
    # C_i = 2 + sum_{j=1}^{i-1} C_j for i > 1
    # This gives C_i = 2^i
    # Total capacity = sum_{i=1}^{3k} 2^i = 2^{3k+1} - 2
    
    # Each path (x, y, z) uses levels x, k+y, 2k+z
    # Energy = C_x + C_{k+y} + C_{2k+z} = 2^x + 2^{k+y} + 2^{2k+z}
    
    # For stability: sum of k paths' energies = total capacity
    # Each level must be used exactly once across all k paths
    
    # Group paths by x (frequency band)
    paths_by_x = defaultdict(list)
    for p in paths:
        paths_by_x[p[0]].append(p)
    
    # Check if we have at least one path for each x from 1 to k
    for x in range(1, k + 1):
        if x not in paths_by_x:
            print("NO")
            return
    
    # For each x, we need to choose exactly one path
    # The y values must form a permutation of 1..k
    # The z values must form a permutation of 1..k
    
    # Use backtracking with pruning
    result = [None] * k
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    
    def backtrack(idx):
        if idx == k:
            return True
        x = idx + 1
        for p in paths_by_x[x]:
            _, y, z = p
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                result[idx] = p
                if backtrack(idx + 1):
                    return True
                used_y[y] = False
                used_z[z] = False
        return False
    
    if backtrack(0):
        print("YES")
        for p in result:
            print(f"{p[0]} {p[1]} {p[2]}")
    else:
        print("NO")

if __name__ == "__main__":
    solve()