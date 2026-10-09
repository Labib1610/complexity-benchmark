from itertools import permutations

def solve():
    k, t = map(int, input().split())
    triplets = []
    for _ in range(t):
        m, p, s = map(int, input().split())
        triplets.append((m, p, s))
    
    # We need to select exactly k triplets such that each membrane, pathway, and sequence
    # appears exactly once.
    
    # This is essentially finding a perfect matching in a 3-dimensional matching problem.
    # Since k <= 22, we can try all possible combinations of k triplets from the t triplets.
    # But that's C(t, k) which can be too large.
    # A better approach is to model this as a bipartite matching or use backtracking.
    
    # Let's use backtracking with pruning.
    
    # For each membrane type, we need exactly one triplet that uses it.
    # For each metabolic pathway, we need exactly one triplet that uses it.
    # For each replication sequence, we need exactly one triplet that uses it.
    
    # Create mappings for easier access
    membranes = [[] for _ in range(k + 1)]
    pathways = [[] for _ in range(k + 1)]
    sequences = [[] for _ in range(k + 1)]
    
    for i, (m, p, s) in enumerate(triplets):
        membranes[m].append(i)
        pathways[p].append(i)
        sequences[s].append(i)
    
    # Check if any membrane, pathway, or sequence is not present in any triplet
    for i in range(1, k + 1):
        if not membranes[i] or not pathways[i] or not sequences[i]:
            print("NO")
            return
    
    # Use backtracking to find a valid selection
    selected = [False] * t  # To track which triplets are selected
    used_membrane = [False] * (k + 1)
    used_pathway = [False] * (k + 1)
    used_sequence = [False] * (k + 1)
    result = []
    
    def backtrack(index):
        if index == k:
            return True
        
        # Try to assign a triplet for the next membrane (index+1)
        # But we need to be careful - we're not just assigning by membrane order
        # We need to ensure all are used exactly once
        
        # Let's try a different approach: try all triplets that can be added
        # without violating the constraints
        
        for i in range(t):
            if selected[i]:
                continue
            m, p, s = triplets[i]
            if not used_membrane[m] and not used_pathway[p] and not used_sequence[s]:
                selected[i] = True
                used_membrane[m] = True
                used_pathway[p] = True
                used_sequence[s] = True
                result.append((m, p, s))
                
                if backtrack(index + 1):
                    return True
                
                # Backtrack
                selected[i] = False
                used_membrane[m] = False
                used_pathway[p] = False
                used_sequence[s] = False
                result.pop()
        
        return False
    
    # Optimization: start with membranes
    if backtrack(0):
        print("YES")
        for m, p, s in result:
            print(m, p, s)
    else:
        print("NO")

solve()