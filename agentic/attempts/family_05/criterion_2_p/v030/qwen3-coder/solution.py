from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    reactions = []
    catalyst_to_solvent = {}
    solvent_to_catalyst = {}
    
    # Read reactions and build mappings
    for _ in range(t):
        x, y, z = map(int, input().split())
        reactions.append((x, y, z))
        
        # Due to lab procedures, each catalyst is tied to exactly one solvent
        if x not in catalyst_to_solvent:
            catalyst_to_solvent[x] = y
        if y not in solvent_to_catalyst:
            solvent_to_catalyst[y] = x
    
    # Check if we have exactly k catalysts and k solvents
    if len(catalyst_to_solvent) != k or len(solvent_to_catalyst) != k:
        print("NO")
        return
    
    # Build a graph for matching temperatures to (catalyst, solvent) pairs
    # For each temperature, we can only use it with reactions that have that temp
    temp_to_reactions = defaultdict(list)
    for i, (x, y, z) in enumerate(reactions):
        temp_to_reactions[z].append(i)
    
    # Try to find a matching: for each catalyst (and its fixed solvent), 
    # we need to pick one reaction with a unique temperature
    # This is essentially a bipartite matching between catalysts and temperatures
    
    # For each catalyst, list possible temperatures
    catalyst_to_temps = defaultdict(list)
    for i, (x, y, z) in enumerate(reactions):
        catalyst_to_temps[x].append((z, i))  # (temperature, reaction_index)
    
    # Now try to match each catalyst to a unique temperature
    matched_temp = {}  # temp -> reaction_index
    matched_catalyst = {}  # catalyst -> reaction_index
    visited = set()
    
    def dfs(catalyst):
        for temp, reaction_idx in catalyst_to_temps[catalyst]:
            if temp in visited:
                continue
            visited.add(temp)
            
            # If temp is unmatched or we can find augmenting path
            if temp not in matched_temp or dfs(matched_temp[temp][0]):
                matched_temp[temp] = (catalyst, reaction_idx)
                matched_catalyst[catalyst] = reaction_idx
                return True
        return False
    
    # Try to match each catalyst
    for catalyst in range(1, k+1):
        visited.clear()
        if not dfs(catalyst):
            print("NO")
            return
    
    # Check if all catalysts are matched
    if len(matched_catalyst) != k:
        print("NO")
        return
        
    print("YES")
    for reaction_idx in matched_catalyst.values():
        x, y, z = reactions[reaction_idx]
        print(x, y, z)

solve()