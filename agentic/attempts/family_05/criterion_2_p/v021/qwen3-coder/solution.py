from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    configs = []
    catalyst_to_reagent = {}
    catalyst_reagent_to_solvents = defaultdict(list)
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        configs.append((x, y, z))
        
        # Verify the constraint: each catalyst always uses the same reagent
        if x in catalyst_to_reagent:
            if catalyst_to_reagent[x] != y:
                # This shouldn't happen according to problem statement
                print("NO")
                return
        else:
            catalyst_to_reagent[x] = y
            
        catalyst_reagent_to_solvents[(x, y)].append(z)
    
    # Check if we have all catalysts from 1 to k
    if len(catalyst_to_reagent) != k:
        print("NO")
        return
        
    # Check if we have all reagents from 1 to k (and they're distinct)
    reagents = set(catalyst_to_reagent.values())
    if len(reagents) != k or min(reagents) < 1 or max(reagents) > k:
        print("NO")
        return
    
    # Create a mapping from reagent to catalyst
    reagent_to_catalyst = {v: u for u, v in catalyst_to_reagent.items()}
    
    # For each catalyst, we need to pick one solvent
    # This is essentially a bipartite matching problem where:
    # Left side: catalysts (1 to k) 
    # Right side: solvents (1 to k)
    # Edge exists if there's a configuration with that catalyst and solvent
    
    # But since catalyst x is always paired with reagent catalyst_to_reagent[x],
    # we're really looking for a perfect matching between catalysts and solvents
    # where edge (x,z) exists if there's a config (x, catalyst_to_reagent[x], z)
    
    # Build adjacency for matching: which solvents can each catalyst use
    adj = defaultdict(list)
    for (x, y), solvents in catalyst_reagent_to_solvents.items():
        for z in solvents:
            adj[x].append(z)
    
    # Try to find a perfect matching using Hungarian algorithm approach
    # or simpler DFS matching
    
    match_solvent_to_catalyst = [-1] * (k + 1)  # 1-indexed
    match_catalyst_to_solvent = [-1] * (k + 1)  # 1-indexed
    
    def dfs(catalyst, visited):
        for solvent in adj[catalyst]:
            if visited[solvent]:
                continue
            visited[solvent] = True
            
            # If solvent is unmatched or we can find augmenting path
            if match_solvent_to_catalyst[solvent] == -1 or dfs(match_solvent_to_catalyst[solvent], visited):
                match_solvent_to_catalyst[solvent] = catalyst
                match_catalyst_to_solvent[catalyst] = solvent
                return True
        return False
    
    matched = 0
    for catalyst in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(catalyst, visited):
            matched += 1
    
    if matched != k:
        print("NO")
        return
    
    print("YES")
    for catalyst in range(1, k + 1):
        solvent = match_catalyst_to_solvent[catalyst]
        reagent = catalyst_to_reagent[catalyst]
        print(catalyst, reagent, solvent)

solve()