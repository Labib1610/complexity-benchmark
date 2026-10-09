from itertools import permutations

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    blueprints = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        blueprints.append((x, y, z))
    
    # Try all permutations of k blueprints
    for perm in permutations(blueprints, k):
        specialists = set()
        machineries = set()
        time_windows = set()
        
        valid = True
        for x, y, z in perm:
            if x in specialists or y in machineries or z in time_windows:
                valid = False
                break
            specialists.add(x)
            machineries.add(y)
            time_windows.add(z)
        
        if valid and len(specialists) == k and len(machineries) == k and len(time_windows) == k:
            print("YES")
            for x, y, z in perm:
                print(x, y, z)
            return
    
    print("NO")

solve()