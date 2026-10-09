from itertools import permutations

def solve():
    k, t = map(int, input().split())
    
    # Read all approved combinations
    approved = set()
    for _ in range(t):
        x, y, z = map(int, input().split())
        approved.add((x, y, z))
    
    # Generate all possible permutations of desserts for each main course
    # We'll try all possible mappings from appetizers to main courses to desserts
    # This is essentially trying all possible perfect matchings in a 3D matching problem
    
    # Since k <= 22, and we need to find a perfect matching, we can try all permutations
    # of main courses and desserts for the k appetizers
    
    # But a better approach: try all possible assignments
    # We can model this as finding a tripartite matching
    # Let's use a backtracking approach or try all permutations
    
    # Try all possible permutations of main courses and desserts
    # For each appetizer 1..k, assign a unique main course and a unique dessert
    # This is equivalent to finding a Latin square or a 3D matching
    
    main_courses = list(range(1, k + 1))
    desserts = list(range(1, k + 1))
    
    # Try all permutations of main courses and desserts
    for p_main in permutations(main_courses):
        for p_dessert in permutations(desserts):
            # Check if this combination works
            valid = True
            meal_deals = []
            
            for i in range(k):
                x = i + 1  # appetizer
                y = p_main[i]  # main course
                z = p_dessert[i]  # dessert
                
                if (x, y, z) not in approved:
                    valid = False
                    break
                meal_deals.append((x, y, z))
            
            if valid:
                print("YES")
                for deal in meal_deals:
                    print(deal[0], deal[1], deal[2])
                return
    
    print("NO")

solve()