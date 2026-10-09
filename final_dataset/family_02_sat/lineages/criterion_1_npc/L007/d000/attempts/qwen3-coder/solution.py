def solve():
    n, m = map(int, input().split())
    
    # If no criteria, any configuration works
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each criterion, we have a clause with 3 literals
    # This is a 3-SAT problem
    
    # We'll use brute force since n <= 90, but that's too large for brute force
    # Let's try to solve it as a 3-SAT problem using backtracking with pruning
    
    # Read clauses
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        clauses.append(clause)
    
    # Try all possible assignments
    # But n can be up to 90, so 2^90 is impossible
    # We need a smarter approach
    
    # Let's implement a simple backtracking solver
    def is_satisfied(assignment):
        # assignment is a list where assignment[i] is the value of variable i+1
        # assignment[0] is dummy, variables are 1-indexed
        for clause in clauses:
            satisfied = False
            for literal in clause:
                var = abs(literal)
                required = 1 if literal > 0 else 0
                if var < len(assignment) and assignment[var] == required:
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True
    
    # Check if a partial assignment can be extended
    def consistent(assignment):
        # Check if current partial assignment violates any clause
        for clause in clauses:
            unsatisfied = True
            unknown = False
            for literal in clause:
                var = abs(literal)
                required = 1 if literal > 0 else 0
                if var < len(assignment):
                    if assignment[var] == required:
                        unsatisfied = False
                        break
                else:
                    unknown = True
            if unsatisfied and not unknown:
                return False
        return True
    
    # Backtracking solver
    def solve_sat():
        assignment = [None] * (n + 1)  # index 0 unused, vars are 1-indexed
        
        def backtrack(var_index):
            if var_index > n:
                return is_satisfied(assignment)
            
            # Try setting variable to 0
            assignment[var_index] = 0
            if consistent(assignment):
                if backtrack(var_index + 1):
                    return True
            
            # Try setting variable to 1
            assignment[var_index] = 1
            if consistent(assignment):
                if backtrack(var_index + 1):
                    return True
            
            assignment[var_index] = None
            return False
        
        if backtrack(1):
            return [assignment[i] if assignment[i] is not None else 0 for i in range(n + 1)]
        else:
            return None
    
    # For large n, even this might be too slow
    # But given the constraints and that this is likely designed to be solvable...
    
    # Let's try a different approach - since each clause has 3 literals,
    # and n <= 90, m <= 400, we can try to solve with a more optimized backtracking
    
    def solve_3sat():
        # assignment[i] represents the value of variable i (1-indexed)
        assignment = [None] * (n + 1)
        
        def is_clause_satisfied(clause):
            for literal in clause:
                var = abs(literal)
                sign = literal > 0
                if assignment[var] is not None:
                    if (assignment[var] == 1 and sign) or (assignment[var] == 0 and not sign):
                        return True
            return False
        
        def all_clauses_satisfied():
            for clause in clauses:
                if not is_clause_satisfied(clause):
                    return False
            return True
        
        def some_clause_unsatisfiable():
            for clause in clauses:
                # If all literals are assigned and none are satisfied, clause is unsatisfied
                all_assigned = True
                satisfied = False
                for literal in clause:
                    var = abs(literal)
                    sign = literal > 0
                    if assignment[var] is None:
                        all_assigned = False
                        break
                    if (assignment[var] == 1 and sign) or (assignment[var] == 0 and not sign):
                        satisfied = True
                        break
                if all_assigned and not satisfied:
                    return True
            return False
        
        def backtrack(var_index):
            if some_clause_unsatisfiable():
                return False
                
            if var_index > n:
                return all_clauses_satisfied()
            
            # Try 0
            assignment[var_index] = 0
            if backtrack(var_index + 1):
                return True
                
            # Try 1
            assignment[var_index] = 1
            if backtrack(var_index + 1):
                return True
                
            assignment[var_index] = None
            return False
        
        if backtrack(1):
            # Return result
            result = []
            for i in range(1, n + 1):
                result.append(str(assignment[i]) if assignment[i] is not None else "0")
            return " ".join(result)
        else:
            return None
    
    result = solve_3sat()
    if result is None:
        print("NO")
    else:
        print("YES")
        print(result)

solve()