from itertools import permutations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    points = []
    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        z = int(data[idx+2])
        points.append((x, y, z))
        idx += 3
    
    # We need to choose exactly k points such that no two share x, y, or z coordinate
    # This is equivalent to finding a permutation of k elements where each element has a unique x, y, z
    
    # First, let's see if we have at least k points
    if t < k:
        print("NO")
        return
    
    # Try all combinations of k points from the t points
    from itertools import combinations
    
    for combo in combinations(points, k):
        # For each combination, check if we can assign each point to a unique x, y, z coordinate
        # This is essentially checking if there exists a permutation matching all three dimensions
        
        xs = [p[0] for p in combo]
        ys = [p[1] for p in combo]
        zs = [p[2] for p in combo]
        
        # Check if all x, y, z coordinates are unique
        if len(set(xs)) == k and len(set(ys)) == k and len(set(zs)) == k:
            print("YES")
            for p in combo:
                print(p[0], p[1], p[2])
            return
    
    print("NO")

solve()