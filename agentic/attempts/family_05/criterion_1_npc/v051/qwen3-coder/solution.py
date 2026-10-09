from itertools import permutations

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    trios = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        trios.append((x-1, y-1, z-1))  # Convert to 0-indexed
    
    # Create a mapping from linguist to possible trios
    linguist_trios = [[] for _ in range(k)]
    for i, (x, y, z) in enumerate(trios):
        linguist_trios[x].append(i)
    
    # Try all permutations of manuscripts
    manuscripts = list(range(k))
    
    for perm in permutations(manuscripts):
        # For this permutation, manuscript i is assigned to position perm[i]
        # We need to check if there's a matching for algorithms
        
        # Create a bipartite graph for linguists and algorithms
        # For each linguist, find which algorithms can be used with the assigned manuscript
        valid = True
        possible_assignments = []
        
        for linguist in range(k):
            assigned_manuscript = perm[linguist]
            valid_algorithms = []
            
            # Check which trios are valid for this linguist and assigned manuscript
            for trio_idx in linguist_trios[linguist]:
                x, y, z = trios[trio_idx]
                if y == assigned_manuscript:
                    valid_algorithms.append((z, trio_idx))
            
            if not valid_algorithms:
                valid = False
                break
                
            possible_assignments.append(valid_algorithms)
        
        if not valid:
            continue
            
        # Now we need to match algorithms uniquely to linguists
        # This is a bipartite matching problem
        used_algorithms = [-1] * k  # algorithm -> linguist assigned to it
        assignment_result = [-1] * k  # linguist -> trio index assigned
        
        def can_match(linguist_idx, visited):
            for algorithm, trio_idx in possible_assignments[linguist_idx]:
                if visited[algorithm]:
                    continue
                visited[algorithm] = True
                
                # If algorithm is free or the linguist using it can find another algorithm
                if used_algorithms[algorithm] == -1 or can_match(used_algorithms[algorithm], visited):
                    used_algorithms[algorithm] = linguist_idx
                    assignment_result[linguist_idx] = trio_idx
                    return True
            return False
        
        # Try to find a matching for all linguists
        matching_found = True
        for linguist_idx in range(k):
            visited = [False] * k
            if not can_match(linguist_idx, visited):
                matching_found = False
                break
                
        if matching_found:
            print("YES")
            for i in range(k):
                x, y, z = trios[assignment_result[i]]
                print(x+1, y+1, z+1)  # Convert back to 1-indexed
            return
    
    print("NO")

solve()