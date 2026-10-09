from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    # Read complexes
    complexes = []
    protein_to_receptor = {}
    receptor_to_protein = {}
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        complexes.append((x, y, z))
        
        # Verify the constraint: each protein chain only interacts with one receptor site
        if x in protein_to_receptor:
            if protein_to_receptor[x] != y:
                # This shouldn't happen according to problem constraints
                print("NO")
                return
        else:
            protein_to_receptor[x] = y
            
        if y in receptor_to_protein:
            if receptor_to_protein[y] != x:
                # This shouldn't happen according to problem constraints
                print("NO")
                return
        else:
            receptor_to_protein[y] = x
    
    # Build a bipartite graph between proteins and catalysts
    # We need to find a perfect matching that covers all k proteins
    
    # Create adjacency list for protein -> possible catalysts
    protein_to_catalysts = defaultdict(set)
    catalyst_to_proteins = defaultdict(set)
    
    for x, y, z in complexes:
        protein_to_catalysts[x].add(z)
        catalyst_to_proteins[z].add(x)
    
    # Check if we have all k proteins and all k receptors
    if len(protein_to_receptor) != k or len(receptor_to_protein) != k:
        print("NO")
        return
    
    # For each protein, we need to pick one catalyst such that:
    # 1. All k proteins are matched
    # 2. All k catalysts are distinct
    
    # This is a maximum bipartite matching problem
    # We can use Hopcroft-Karp or a simpler approach since k <= 1200
    
    # Try to find a maximum matching using DFS-based algorithm
    match_catalyst_to_protein = {}
    match_protein_to_catalyst = {}
    
    def dfs(protein, visited):
        for catalyst in protein_to_catalysts[protein]:
            if catalyst in visited:
                continue
            visited.add(catalyst)
            
            # If catalyst is unmatched or we can find an augmenting path
            if catalyst not in match_catalyst_to_protein or dfs(match_catalyst_to_protein[catalyst], visited):
                match_catalyst_to_protein[catalyst] = protein
                match_protein_to_catalyst[protein] = catalyst
                return True
        return False
    
    # Find maximum matching
    matching = 0
    for protein in range(1, k + 1):
        if protein in protein_to_catalysts:  # This protein appears in some complex
            visited = set()
            if dfs(protein, visited):
                matching += 1
    
    # Check if we have a perfect matching
    if matching != k:
        print("NO")
        return
    
    # Output the solution
    print("YES")
    for protein in range(1, k + 1):
        receptor = protein_to_receptor[protein]
        catalyst = match_protein_to_catalyst[protein]
        print(protein, receptor, catalyst)

solve()