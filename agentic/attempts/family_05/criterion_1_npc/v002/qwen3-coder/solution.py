from itertools import permutations

def solve():
    k, t = map(int, input().split())
    allowed = set()
    for _ in range(t):
        x, y, z = map(int, input().split())
        allowed.add((x, y, z))
    
    if t < k:
        print("NO")
        return
    
    # Try all possible permutations of desserts for each main course
    # We'll try to find a perfect matching
    # Let's model this as a bipartite matching between appetizers and (main, dessert) pairs
    # But it's actually a 3D matching problem
    
    # Try all k! permutations of main courses and desserts
    mains = list(range(1, k+1))
    desserts = list(range(1, k+1))
    
    for p_mains in permutations(mains):
        for p_desserts in permutations(desserts):
            # For each appetizer i, try pairing it with main p_mains[i-1] and dessert p_desserts[i-1]
            valid = True
            menus = []
            used_mains = set()
            used_desserts = set()
            
            for i in range(1, k+1):
                x = i
                y = p_mains[i-1]
                z = p_desserts[i-1]
                
                if (x, y, z) not in allowed:
                    valid = False
                    break
                    
                if y in used_mains or z in used_desserts:
                    valid = False
                    break
                    
                used_mains.add(y)
                used_desserts.add(z)
                menus.append((x, y, z))
            
            if valid:
                print("YES")
                for menu in menus:
                    print(menu[0], menu[1], menu[2])
                return
    
    print("NO")

solve()