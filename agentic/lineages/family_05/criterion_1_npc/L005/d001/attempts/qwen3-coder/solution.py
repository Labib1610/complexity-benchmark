import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    triples = []
    index = 2
    for _ in range(t):
        x = int(data[index]) - 1  # Convert to 0-based indexing
        y = int(data[index+1]) - 1
        z = int(data[index+2]) - 1
        triples.append((x, y, z))
        index += 3
    
    # We need to find a perfect matching: each resource used exactly once
    # This is equivalent to finding a permutation of triples such that:
    # all x's are distinct, all y's are distinct, all z's are distinct
    # i.e., a Latin hypercube in 3D of size k, using the given triples
    
    # Backtracking approach with pruning
    # We'll try to assign each position 0..k-1 to one of the triples
    # But we need to ensure that across all assignments:
    # - each x in 0..k-1 is used exactly once
    # - each y in 0..k-1 is used exactly once  
    # - each z in 0..k-1 is used exactly once
    
    # Preprocess: for each resource, store which triples use it
    x_triples = [[] for _ in range(k)]
    y_triples = [[] for _ in range(k)]
    z_triples = [[] for _ in range(k)]
    
    for i, (x, y, z) in enumerate(triples):
        x_triples[x].append(i)
        y_triples[y].append(i)
        z_triples[z].append(i)
    
    # To speed up search, sort triples by how constrained they are
    # (i.e., how many options there are for x,y,z)
    # Actually, let's just do backtracking with bitmasks
    
    # Use bitmasks to track which x,y,z have been used
    used_x = 0
    used_y = 0
    used_z = 0
    selected = []
    
    def backtrack(pos):
        if pos == k:
            return True
            
        # Try each triple that hasn't been used yet and satisfies constraints
        for i, (x, y, z) in enumerate(triples):
            # Check if this triple conflicts with already selected ones
            if (used_x & (1 << x)) or (used_y & (1 << y)) or (used_z & (1 << z)):
                continue
                
            # Take this triple
            used_x |= 1 << x
            used_y |= 1 << y  
            used_z |= 1 << z
            selected.append((x, y, z))
            
            if backtrack(pos + 1):
                return True
                
            # Backtrack
            used_x ^= 1 << x
            used_y ^= 1 << y
            used_z ^= 1 << z
            selected.pop()
            
        return False
    
    # Optimization: start with the most constrained resources
    # Let's instead do a smarter backtracking by picking the next variable smartly
    # But for simplicity with k<=22, let's stick to basic backtracking with pruning
    
    # Actually, let's model this as a bipartite matching problem generalized to 3-partite 3-uniform hypergraph matching
    # Which is NP-hard in general but tractable for small k
    
    # Let's try a different approach: for each position, pick a triple that doesn't conflict
    # We can represent state as (used_x_mask, used_y_mask, used_z_mask) 
    # But state space is too large
    
    # Let's go back to the backtracking idea but implement it correctly
    
    selected_indices = []
    
    def solve(pos):
        if pos == k:
            return True
            
        # For current position, try to assign any valid triple
        for i in range(t):
            x, y, z = triples[i]
            # Check if this triple can be used (resources not already taken)
            if (used_x & (1 << x)) or (used_y & (1 << y)) or (used_z & (1 << z)):
                continue
                
            # Assign this triple
            used_x |= 1 << x
            used_y |= 1 << y
            used_z |= 1 << z
            selected_indices.append(i)
            
            if solve(pos + 1):
                return True
                
            # Backtrack
            used_x ^= 1 << x
            used_y ^= 1 << y
            used_z ^= 1 << z
            selected_indices.pop()
        
        return False
    
    if solve(0):
        print("YES")
        for idx in selected_indices:
            x, y, z = triples[idx]
            print(x+1, y+1, z+1)  # Convert back to 1-based
    else:
        print("NO")

if __name__ == "__main__":
    main()