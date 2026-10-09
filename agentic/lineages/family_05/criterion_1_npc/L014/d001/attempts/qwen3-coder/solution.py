from itertools import combinations

def solve():
    k, t = map(int, input().split())
    reactions = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        reactions.append((x, y, z))
    
    if k == 0:
        print("YES")
        return
    
    # Try all combinations of k reactions
    for combo in combinations(reactions, k):
        # Check if this combination satisfies the exact-incidence requirement
        fluids = set()
        catalysts = set()
        profiles = set()
        
        valid = True
        for x, y, z in combo:
            fluids.add(x)
            catalysts.add(y)
            profiles.add(z)
            
        if len(fluids) == k and len(catalysts) == k and len(profiles) == k:
            # Check if we have exactly the fluids, catalysts, and profiles 1 to k
            if fluids == set(range(1, k+1)) and catalysts == set(range(1, k+1)) and profiles == set(range(1, k+1)):
                print("YES")
                for x, y, z in combo:
                    print(x, y, z)
                return
    
    print("NO")

solve()