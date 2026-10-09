import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    triplets = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        triplets.append((x, y, z))
    
    # Build adjacency lists
    adj_x = [[] for _ in range(k + 1)]  # x -> list of (y, z, triplet_idx)
    adj_y = [[] for _ in range(k + 1)]  # y -> list of (x, z, triplet_idx)
    adj_z = [[] for _ in range(k + 1)]  # z -> list of (x, y, triplet_idx)
    
    for idx, (x, y, z) in enumerate(triplets):
        adj_x[x].append((y, z, idx))
        adj_y[y].append((x, z, idx))
        adj_z[z].append((x, y, idx))
    
    # Check Hall's condition for each set
    def check_hall():
        # Check specialists
        for mask in range(1, 1 << k):
            count = bin(mask).count('1')
            neighbor_z = set()
            for i in range(k):
                if mask & (1 << i):
                    x = i + 1
                    for y, z, idx in adj_x[x]:
                        neighbor_z.add(z)
            if len(neighbor_z) < count:
                return False
        
        # Check machines
        for mask in range(1, 1 << k):
            count = bin(mask).count('1')
            neighbor_x = set()
            for i in range(k):
                if mask & (1 << i):
                    y = i + 1
                    for x, z, idx in adj_y[y]:
                        neighbor_x.add(x)
            if len(neighbor_x) < count:
                return False
        
        # Check time intervals
        for mask in range(1, 1 << k):
            count = bin(mask).count('1')
            neighbor_y = set()
            for i in range(k):
                if mask & (1 << i):
                    z = i + 1
                    for x, y, idx in adj_z[z]:
                        neighbor_y.add(y)
            if len(neighbor_y) < count:
                return False
        
        return True
    
    if not check_hall():
        print("NO")
        return
    
    # Try to find a valid assignment using backtracking
    used_x = [False] * (k + 1)
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    result = []
    
    def backtrack():
        if len(result) == k:
            return True
        
        # Find the first unassigned x
        for x in range(1, k + 1):
            if not used_x[x]:
                break
        
        used_x[x] = True
        for y, z, idx in adj_x[x]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                result.append(triplets[idx])
                if backtrack():
                    return True
                result.pop()
                used_y[y] = False
                used_z[z] = False
        used_x[x] = False
        return False
    
    if backtrack():
        print("YES")
        for triplet in result:
            print(triplet[0], triplet[1], triplet[2])
    else:
        print("NO")

solve()