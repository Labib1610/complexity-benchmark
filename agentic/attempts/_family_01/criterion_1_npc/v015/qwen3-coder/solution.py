def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Create adjacency list for conflicts
    conflicts = defaultdict(set)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        conflicts[u].add(v)
        conflicts[v].add(u)
    
    # Try to color the graph with 3 colors (blocks 1, 2, 3)
    # Using backtracking
    assignment = [0] * (n + 1)  # assignment[i] = block for technician i
    
    def is_valid(tech, block):
        # Check if assigning tech to block conflicts with neighbors
        for neighbor in conflicts[tech]:
            if assignment[neighbor] == block:
                return False
        return True
    
    def backtrack(tech):
        if tech > n:
            return True
            
        for block in range(1, 4):
            if is_valid(tech, block):
                assignment[tech] = block
                if backtrack(tech + 1):
                    return True
                assignment[tech] = 0
        
        return False
    
    if backtrack(1):
        print("YES")
        print(*assignment[1:])
    else:
        print("NO")

solve()