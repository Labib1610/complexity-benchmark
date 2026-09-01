def solve():
    n, m = map(int, input().split())
    
    # Create adjacency list to represent conflicts
    conflicts = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts[u].append(v)
        conflicts[v].append(u)
    
    # Try all possible assignments with backtracking
    assignment = [0] * (n + 1)  # assignment[i] represents the storage unit for specimen i
    
    def is_valid(specimen, unit):
        # Check if assigning 'unit' to 'specimen' conflicts with any already assigned neighbors
        for neighbor in conflicts[specimen]:
            if assignment[neighbor] == unit:
                return False
        return True
    
    def backtrack(specimen):
        if specimen > n:
            return True
            
        # Try units in order 1, 2, 3 to satisfy tie-breaking rule
        for unit in [1, 2, 3]:
            if is_valid(specimen, unit):
                assignment[specimen] = unit
                if backtrack(specimen + 1):
                    return True
                assignment[specimen] = 0  # Backtrack
        
        return False
    
    # Start backtracking from specimen 1
    if backtrack(1):
        print("YES")
        print(*assignment[1:])
    else:
        print("NO")

solve()