from itertools import combinations

def read_input():
    k, t = map(int, input().split())
    pockets = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        pockets.append((x, y, z))
    return k, t, pockets

def manhattan_3d(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

def projection_distances(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    dz = abs(p1[2] - p2[2])
    return dx + dy, dx + dz, dy + dz  # depth-lat, depth-long, lat-long

def is_valid_subset(subset):
    for p1, p2 in combinations(subset, 2):
        dist_3d = manhattan_3d(p1, p2)
        proj_dl, proj_dlo, proj_llo = projection_distances(p1, p2)
        if dist_3d <= proj_dl or dist_3d <= proj_dlo or dist_3d <= proj_llo:
            return False
    return True

def solve():
    k, t, pockets = read_input()
    
    if k > t:
        print("NO")
        return
    
    # Try all combinations of k pockets from the t available
    from itertools import combinations as iter_combinations
    
    for combo in iter_combinations(pockets, k):
        if is_valid_subset(combo):
            print("YES")
            for pocket in combo:
                print(pocket[0], pocket[1], pocket[2])
            return
    
    print("NO")

solve()