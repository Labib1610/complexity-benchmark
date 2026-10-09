from itertools import permutations

def solve():
    k, t = map(int, input().split())
    
    reactions = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        reactions.append((x, y, z))
    
    # If k is 1, just check if there's at least one reaction
    if k == 1:
        if t >= 1:
            print("YES")
            print(reactions[0][0], reactions[0][1], reactions[0][2])
        else:
            print("NO")
        return
    
    # For each possible permutation of thermal profiles
    for perm in permutations(range(1, k + 1)):
        # Create a mapping: catalyst -> thermal profile
        thermal_for_catalyst = {}
        fluid_for_catalyst = {}
        used = set()
        valid = True
        result = []
        
        # Try to assign reactions
        for catalyst in range(1, k + 1):
            thermal = perm[catalyst - 1]
            found = False
            for fluid in range(1, k + 1):
                if (fluid, catalyst, thermal) in reactions and fluid not in used:
                    thermal_for_catalyst[catalyst] = thermal
                    fluid_for_catalyst[catalyst] = fluid
                    used.add(fluid)
                    result.append((fluid, catalyst, thermal))
                    found = True
                    break
            if not found:
                valid = False
                break
        
        if valid:
            print("YES")
            for r in result:
                print(r[0], r[1], r[2])
            return
    
    print("NO")

solve()