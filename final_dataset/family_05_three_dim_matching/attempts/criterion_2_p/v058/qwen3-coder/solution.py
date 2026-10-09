from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    complexes = []
    protein_to_receptor = {}
    receptor_to_protein = {}
    
    # Read complexes and build mappings
    for _ in range(t):
        x, y, z = map(int, input().split())
        complexes.append((x, y, z))
        
        # Verify the constraint: each protein chain maps to exactly one receptor
        if x in protein_to_receptor:
            if protein_to_receptor[x] != y:
                print("NO")
                return
        else:
            protein_to_receptor[x] = y
            
        if y in receptor_to_protein:
            if receptor_to_protein[y] != x:
                print("NO")
                return
        else:
            receptor_to_protein[y] = x
    
    # Check if we have exactly k proteins and k receptors
    if len(protein_to_receptor) != k or len(receptor_to_protein) != k:
        print("NO")
        return
    
    # Build a bipartite graph: proteins <-> catalysts
    # Edge exists if there's a complex with that protein and catalyst
    protein_catalysts = defaultdict(set)
    for x, y, z in complexes:
        protein_catalysts[x].add(z)
    
    # Try to find a perfect matching using Hungarian algorithm approach
    # But since we just need to check if a perfect matching exists,
    # we can use a simpler approach: try all possible assignments
    
    # Since each protein must be matched to exactly one catalyst,
    # and all proteins are distinct and all receptors are determined,
    # this becomes a matching problem: proteins -> catalysts
    
    # We can model this as a maximum bipartite matching problem
    # where left side is proteins (1..k) and right side is catalysts (1..k)
    
    # Build adjacency list for the bipartite graph
    adj = defaultdict(list)
    for x, y, z in complexes:
        adj[x].append(z)
    
    # Maximum bipartite matching using DFS
    def dfs(u, match_right, match_left, visited):
        for v in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            
            if match_right[v] == -1 or dfs(match_right[v], match_right, match_left, visited):
                match_right[v] = u
                match_left[u] = v
                return True
        return False
    
    # Initialize matching arrays
    match_left = [-1] * (k + 1)   # match_left[protein] = catalyst
    match_right = [-1] * (k + 1)  # match_right[catalyst] = protein
    
    matching = 0
    for u in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(u, match_right, match_left, visited):
            matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    # Reconstruct the solution
    result = []
    for protein in range(1, k + 1):
        receptor = protein_to_receptor[protein]
        catalyst = match_left[protein]
        result.append(f"{protein} {receptor} {catalyst}")
    
    print("\n".join(result))

solve()