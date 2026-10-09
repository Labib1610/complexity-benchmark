def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    clauses = []
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        l3 = int(data[index+2])
        index += 3
        clauses.append((l1, l2, l3))
    
    # For each variable, try both values 0 and 1
    # We'll use brute force since n <= 90, but with small m this might be okay
    # Actually, let's think differently - this is a 3-SAT variant
    
    # Let's encode this as a 3-SAT problem and solve it
    # Variable i (1-indexed) corresponds to facility i
    # Positive literal i means facility i is set to 1
    # Negative literal -i means facility i is set to 0
    
    # Each clause is a disjunction of 3 literals
    # We need to find a truth assignment that satisfies all clauses
    
    # Since n can be up to 90, brute force won't work
    # But we can use a SAT solver approach or backtracking with pruning
    
    # Let's implement a simple backtracking solution
    
    def var_to_index(v):
        # Convert variable (1-indexed) to 0-indexed
        return abs(v) - 1
    
    def is_satisfied(clause, assignment):
        # Check if clause is satisfied by current assignment
        for lit in clause:
            var_idx = var_to_index(lit)
            if var_idx >= len(assignment):
                # Variable not assigned yet
                return True
            var_value = assignment[var_idx]
            if lit > 0 and var_value == 1:
                return True
            if lit < 0 and var_value == 0:
                return True
        return False
    
    def backtrack(assignment):
        # Check if all clauses are satisfied so far
        for clause in clauses:
            if not is_satisfied(clause, assignment):
                return None
        
        # If we've assigned all variables, we have a solution
        if len(assignment) == n:
            return assignment[:]
        
        # Try assigning next variable to 0 or 1
        next_var = len(assignment)
        for val in [0, 1]:
            assignment.append(val)
            result = backtrack(assignment)
            if result is not None:
                return result
            assignment.pop()
        
        return None
    
    solution = backtrack([])
    if solution is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, solution)))

solve()