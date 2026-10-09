from itertools import combinations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    voxels = []
    index = 2
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        voxels.append((x, y, z))
        index += 3
    
    # Try all combinations of k voxels
    for combo in combinations(voxels, k):
        # Calculate unique x, y, z coordinates
        xs = set(v[0] for v in combo)
        ys = set(v[1] for v in combo)
        zs = set(v[2] for v in combo)
        
        # Check if dispersion metric equals 3k
        if len(xs) + len(ys) + len(zs) == 3 * k:
            print("YES")
            for voxel in combo:
                print(voxel[0], voxel[1], voxel[2])
            return
    
    print("NO")

solve()