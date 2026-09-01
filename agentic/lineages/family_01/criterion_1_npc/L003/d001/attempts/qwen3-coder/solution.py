def solve():
    import sys
    from collections import defaultdict
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list for conflicts
    conflicts = defaultdict(set)
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-indexed
        v = int(data[idx+1]) - 1
        conflicts[u].add(v)
        conflicts[v].add(u)
        idx += 2
    
    # Try all 3^n assignments, but prune using backtracking for efficiency
    # We'll generate assignments in lexicographical order and return the first valid one
    
    def is_valid_assignment(assignment):
        # Check if current partial assignment is valid
        for i in range(len(assignment)):
            for j in conflicts[i]:
                if j < len(assignment) and assignment[j] == assignment[i]:
                    return False
        return True
    
    # Backtracking search for the lexicographically smallest valid assignment
    def backtrack(assignment):
        if len(assignment) == n:
            return assignment[:]
        
        current_worker = len(assignment)
        for shift in [1, 2, 3]:
            assignment.append(shift)
            valid = True
            # Check conflicts with already assigned workers
            for neighbor in conflicts[current_worker]:
                if neighbor < current_worker:
                    if assignment[neighbor] == shift:
                        valid = False
                        break
            if valid:
                result = backtrack(assignment)
                if result:
                    return result
            assignment.pop()
        
        return None
    
    result = backtrack([])
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, result)))

solve()