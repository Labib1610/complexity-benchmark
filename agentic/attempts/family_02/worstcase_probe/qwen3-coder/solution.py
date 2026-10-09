from collections import defaultdict
import sys

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each rule, we have a clause (at least one literal must be true)
    # This is a 3-SAT problem
    
    # We'll use a brute force approach since n <= 90, but we can check all 2^n assignments
    # However, 2^90 is too large. Let's think differently.
    
    # Actually, let's try a more systematic approach using 2-SAT reduction or brute force with pruning
    # But given the constraints, let's implement a solution that works for small cases and 
    # uses some optimization for larger ones.
    
    # Let's parse the clauses
    clauses = []
    for _ in range(m):
        line = list(map(int, input().split()))
        clauses.append(line)
    
    # Try all possible assignments
    # Since n can be up to 90, trying all 2^n is impossible
    # But we can do a randomized local search or use a SAT solver approach
    
    # Let's try a simple backtracking with unit propagation
    
    def is_satisfied(assignment):
        # Check if all clauses are satisfied
        for clause in clauses:
            satisfied = False
            for lit in clause:
                var = abs(lit)
                sign = lit > 0
                if var in assignment:
                    if assignment[var] == sign:
                        satisfied = True
                        break
            if not satisfied:
                return False
        return True
    
    # Unit propagation function
    def unit_propagate(clauses, assignment):
        changed = True
        while changed:
            changed = False
            new_clauses = []
            for clause in clauses:
                new_clause = []
                unknown_count = 0
                last_unknown = None
                satisfied = False
                
                for lit in clause:
                    var = abs(lit)
                    sign = lit > 0
                    
                    if var in assignment:
                        if assignment[var] == sign:
                            satisfied = True
                            break
                    else:
                        new_clause.append(lit)
                        unknown_count += 1
                        last_unknown = lit
                
                if satisfied:
                    continue  # Clause is already satisfied
                    
                if unknown_count == 0:
                    return False, [], assignment  # Contradiction
                    
                if unknown_count == 1:
                    # Unit clause
                    lit = last_unknown
                    var = abs(lit)
                    sign = lit > 0
                    if var not in assignment:
                        assignment[var] = sign
                        changed = True
                        # Don't add this clause, it's satisfied now
                        
                if unknown_count >= 1:
                    new_clauses.append(new_clause)
                    
            clauses = new_clauses
            
        return True, clauses, assignment
    
    def backtrack(clauses, assignment):
        # Unit propagation
        sat, new_clauses, new_assignment = unit_propagate(clauses, assignment)
        if not sat:
            return None
            
        # Check if done
        if not new_clauses:
            return new_assignment
            
        # Choose variable to branch on (simple heuristic: pick first unassigned)
        var_to_branch = None
        for clause in new_clauses:
            for lit in clause:
                var = abs(lit)
                if var not in new_assignment:
                    var_to_branch = var
                    break
            if var_to_branch:
                break
                
        if var_to_branch is None:
            return new_assignment
            
        # Try True
        assignment_true = new_assignment.copy()
        assignment_true[var_to_branch] = True
        result = backtrack(new_clauses, assignment_true)
        if result is not None:
            return result
            
        # Try False
        assignment_false = new_assignment.copy()
        assignment_false[var_to_branch] = False
        result = backtrack(new_clauses, assignment_false)
        if result is not None:
            return result
            
        return None
    
    # Start with empty assignment
    initial_assignment = {}
    result = backtrack(clauses, initial_assignment)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        # Fill in unassigned variables with default value (e.g., False)
        final_result = []
        for i in range(1, n+1):
            if i in result:
                final_result.append("1" if result[i] else "0")
            else:
                final_result.append("0")
        print(" ".join(final_result))

solve()