from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    
    # Read interactions
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    # Try all possible combinations of k members for the focus panel
    members = list(range(1, n + 1))
    
    for panel in combinations(members, k):
        panel_set = set(panel)
        valid = True
        
        # Check if this panel assignment is valid
        # For each interaction, at least one member must be in control group
        for u, v in edges:
            # If both u and v are in the panel (focus group), this is invalid
            if u in panel_set and v in panel_set:
                valid = False
                break
        
        if valid:
            print("YES")
            print(*panel)
            return
    
    print("NO")

solve()