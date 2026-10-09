from collections import defaultdict
import sys

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each cross-bar, we need at least one of its three linkages to be satisfied
    # This creates a 3-CNF clause for each cross-bar
    clauses = []
    
    for _ in range(m):
        l1, l2, l3 = map(int, input().split())
        # Convert to variables: positive means actuator should be 1, negative means 0
        clause = []
        # For each linkage, what assignment would satisfy it?
        # If l > 0, then actuator |l| should be 1
        # If l < 0, then actuator |l| should be 0
        for l in [l1, l2, l3]:
            clause.append(l)
        clauses.append(clause)
    
    # We'll try all possible assignments for small n
    # But since n can be up to 90, we need a better approach
    # This is essentially 3-SAT, but we can encode it as 2-SAT if we transform properly
    
    # Actually, let's think differently. Each clause needs at least one literal to be true.
    # We can use the fact that this is a constraint satisfaction problem.
    
    # Let's try a backtracking approach with pruning
    
    # For each actuator, we have two choices: 0 or 1
    assignment = [-1] * (n + 1)  # 1-indexed
    
    def is_clause_satisfied(clause):
        for lit in clause:
            var = abs(lit)
            if lit > 0:
                if assignment[var] == 1:
                    return True
            else:  # lit < 0
                if assignment[var] == 0:
                    return True
        return False
    
    def check_all_assigned_clauses():
        for clause in clauses:
            all_vars_assigned = True
            for lit in clause:
                var = abs(lit)
                if assignment[var] == -1:
                    all_vars_assigned = False
                    break
            
            if all_vars_assigned and not is_clause_satisfied(clause):
                return False
        return True
    
    def backtrack(var_index):
        if var_index > n:
            # Check if all clauses are satisfied
            for clause in clauses:
                if not is_clause_satisfied(clause):
                    return False
            return True
            # All variables assigned
            return True
        
        # Try assigning 0
        assignment[var_index] = 0
        if check_all_assigned_clauses() and backtrack(var_index + 1):
            return True
            
        # Try assigning 1
        assignment[var_index] = 1
        if check_all_assigned_clauses() and backtrack(var_index + 1):
            return True
            
        # Backtrack
        assignment[var_index] = -1
        return False
    
    # Optimization: Unit propagation
    # If a clause has only one unassigned variable, we might be able to force its value
    
    def unit_propagate():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unassigned_count = 0
                unassigned_literal = None
                satisfied = False
                
                # Check if clause is already satisfied
                for lit in clause:
                    var = abs(lit)
                    if assignment[var] != -1:  # Variable is assigned
                        if (lit > 0 and assignment[var] == 1) or (lit < 0 and assignment[var] == 0):
                            satisfied = True
                            break
                    else:  # Variable is unassigned
                        unassigned_count += 1
                        unassigned_literal = lit
                
                if satisfied:
                    continue
                    
                if unassigned_count == 0:
                    # All variables assigned but clause not satisfied
                    return False  # UNSAT
                    
                if unassigned_count == 1:
                    # Unit clause - force the unassigned variable
                    var = abs(unassigned_literal)
                    required_value = 1 if unassigned_literal > 0 else 0
                    if assignment[var] == -1:
                        assignment[var] = required_value
                        changed = True
                    elif assignment[var] != required_value:
                        return False  # Conflict
                        
        return True  # No conflict
    
    # Initial unit propagation
    if not unit_propagate():
        print("NO")
        return
    
    # Now do backtracking on remaining unassigned variables
    if backtrack(1):
        print("YES")
        result = []
        for i in range(1, n + 1):
            if assignment[i] == -1:  # If still unassigned, default to 0
                result.append("0")
            else:
                result.append(str(assignment[i]))
        print(" ".join(result))
    else:
        print("NO")

solve()