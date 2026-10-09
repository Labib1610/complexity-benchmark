from itertools import product

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        # No toxic pairs, just check water constraint
        if n > 45:
            print("NO")
            return
        else:
            print("YES")
            print(" ".join(["1"] * n))
            return
    
    # Read toxic pairs
    toxic_pairs = []
    for _ in range(m):
        u, v = map(int, input().split())
        toxic_pairs.append((u-1, v-1))  # Convert to 0-indexed
    
    # Try all possible assignments
    for assignment in product([1, 2, 3], repeat=n):
        # Check water constraint: each greenhouse can have at most 45 species
        count = [0, 0, 0]
        for greenhouse in assignment:
            count[greenhouse-1] += 1
        
        if any(c > 45 for c in count):
            continue
            
        # Check toxicity isolation constraint
        valid = True
        for u, v in toxic_pairs:
            if assignment[u] == assignment[v]:
                valid = False
                break
                
        if not valid:
            continue
            
        # Check filtration budget: count pairs assigned to different greenhouses
        filtration_units = 0
        for u, v in toxic_pairs:
            if assignment[u] != assignment[v]:
                filtration_units += 1
                
        if filtration_units > 800:
            continue
            
        # If we reach here, we found a valid assignment
        print("YES")
        print(" ".join(map(str, assignment)))
        return
    
    # If no valid assignment found
    print("NO")

solve()