from collections import defaultdict
import sys

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    index = 2
    squads = []
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        squads.append((a, b, c))
        index += 3
    
    # We need to find a perfect matching that covers all 3q nodes
    # This is essentially a exact cover problem, can be modeled as finding a maximum matching
    # Since each squad covers exactly 3 people, and we want to cover exactly 3q people with q squads
    # We can model this as a bipartite graph matching or use backtracking with pruning
    
    # Let's try a backtracking approach with bitmasks for efficiency
    # But since q can be up to 200, that's too large for backtracking unless the structure is sparse
    
    # Actually, let's think differently. This is a hypergraph matching problem.
    # Each squad is a hyperedge connecting 3 vertices.
    # We want to find a matching that covers all vertices exactly once.
    
    # For small q, we can try backtracking.
    # But given constraints, let's see if we can do better.
    
    # Let's try a greedy + backtracking hybrid approach.
    # First, build adjacency for each person
    adj = defaultdict(list)
    for i in range(t):
        a, b, c = squads[i]
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)
    
    # Try to find a matching of size q that covers all 3*q people
    # Use backtracking with pruning
    
    def backtrack(pos, selected, covered):
        if len(selected) == q:
            if len(covered) == 3 * q:
                return True, selected[:]
            return False, []
        
        if pos == t:
            return False, []
            
        # Pruning: if even selecting all remaining squads won't make up to q
        if len(selected) + (t - pos) < q:
            return False, []
            
        # Pruning: if current coverage already exceeds what we can cover
        needed = 3 * q - len(covered)
        remaining_squads = t - pos
        if needed > 3 * remaining_squads:
            return False, []
        
        # Try not taking current squad
        res, sel = backtrack(pos + 1, selected, covered)
        if res:
            return res, sel
            
        # Try taking current squad if none of its members are already covered
        a, b, c = squads[pos]
        if a not in covered and b not in covered and c not in covered:
            selected.append(pos)
            covered.add(a)
            covered.add(b)
            covered.add(c)
            res, sel = backtrack(pos + 1, selected, covered)
            if res:
                return res, sel
            selected.pop()
            covered.remove(a)
            covered.remove(b)
            covered.remove(c)
            
        return False, []
    
    # Optimization: sort squads by some heuristic to improve pruning
    # E.g., prioritize squads with members that have fewer options
    # For now, let's proceed with basic backtracking
    
    # Start backtracking
    result, selection = backtrack(0, [], set())
    
    if not result:
        print("NO")
    else:
        print("YES")
        for idx in selection:
            a, b, c = squads[idx]
            print(a, b, c)

# The above approach might be too slow for large inputs due to exponential complexity.
# However, given the constraints and that this is likely designed to be solvable,
# let's try a more optimized version using network flow or other techniques.

# Actually, this is known as the Exact Cover problem, and can be solved via Algorithm X (Dancing Links).
# But for simplicity and given time constraints, let's optimize our backtracking:

def solve_optimized():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    index = 2
    squads = []
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        squads.append((a, b, c))
        index += 3
        
    if t == 0 and q > 0:
        print("NO")
        return
        
    # Build a mapping from person to list of squads they're in
    person_to_squads = defaultdict(list)
    for i in range(t):
        a, b, c = squads[i]
        person_to_squads[a].append(i)
        person_to_squads[b].append(i)
        person_to_squads[c].append(i)
    
    # Sort squads based on how "rare" their members are (least frequent first)
    # This helps in pruning earlier
    def squad_priority(sq_idx):
        a, b, c = squads[sq_idx]
        return (len(person_to_squads[a]), len(person_to_squads[b]), len(person_to_squads[c]))
    
    # Precompute priorities
    squad_indices = list(range(t))
    # Not sorting for now to keep order consistent
    
    used_squad = [False] * t
    selected = []
    used_person = [False] * (3*q + 1)  # 1-indexed
    
    def backtrack_opt(pos):
        if len(selected) == q:
            return True
            
        if pos == t:
            return False
            
        # Pruning
        if len(selected) + (t - pos) < q:
            return False
            
        # Try including this squad
        a, b, c = squads[pos]
        if not used_person[a] and not used_person[b] and not used_person[c]:
            # Include this squad
            used_squad[pos] = True
            used_person[a] = True
            used_person[b] = True
            used_person[c] = True
            selected.append(pos)
            
            if backtrack_opt(pos + 1):
                return True
                
            # Backtrack
            selected.pop()
            used_person[a] = False
            used_person[b] = False
            used_person[c] = False
            used_squad[pos] = False
            
        # Try not including this squad
        if backtrack_opt(pos + 1):
            return True
            
        return False
    
    if backtrack_opt(0):
        print("YES")
        for idx in selected:
            a, b, c = squads[idx]
            print(a, b, c)
    else:
        print("NO")

solve_optimized()