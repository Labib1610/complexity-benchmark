from itertools import combinations

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
        
    pathways = []
    for _ in range(t):
        m, c, f = map(int, input().split())
        pathways.append((m, c, f))
    
    # Try all combinations of k pathways
    for combo in combinations(range(t), k):
        selected = [pathways[i] for i in combo]
        
        # Check if all compounds, reagents, and profiles are used exactly once
        compounds = [p[0] for p in selected]
        reagents = [p[1] for p in selected]
        profiles = [p[2] for p in selected]
        
        if (len(set(compounds)) == k and 
            len(set(reagents)) == k and 
            len(set(profiles)) == k):
            print("YES")
            for pathway in selected:
                print(pathway[0], pathway[1], pathway[2])
            return
    
    print("NO")

solve()