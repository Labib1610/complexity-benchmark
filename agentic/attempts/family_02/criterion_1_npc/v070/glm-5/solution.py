import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Each clause is (p1, p2, p3) where p_k is non-zero.
    # +x means x is True (Alpha), -x means x is False (Beta).
    # We need to satisfy all clauses, each clause is an OR of 3 literals.
    
    # We use a backtracking search with unit propagation (DPLL style).
    # Assignment array: 0 = False (Beta), 1 = True (Alpha), -1 = Unassigned.
    assignment = [-1] * (n + 1)
    
    # Pre-process clauses into list of lists of integers
    clauses = []
    for _ in range(m):
        c = [int(next(it)) for _ in range(3)]
        clauses.append(c)
        
    # Optimization: Pre-calculate variable occurrences for faster unit propagation
    # pos_occurrence[v] stores indices of clauses where +v appears
    # neg_occurrence[v] stores indices of clauses where -v appears
    pos_occurrence = [[] for _ in range(n + 1)]
    neg_occurrence = [[] for _ in range(n + 1)]
    
    for i, c in enumerate(clauses):
        for lit in c:
            v = abs(lit)
            if lit > 0:
                pos_occurrence[v].append(i)
            else:
                neg_occurrence[v].append(i)
                
    # We maintain a state for each clause to track how many literals are satisfied
    # or if the clause is currently unsatisfied (all literals false).
    # However, with backtracking, we can just evaluate on the fly or use counters.
    # Given N=90, M=400, simple evaluation is fast enough.
    
    # Let's implement a recursive solver with basic unit propagation.
    
    # To speed up checking, we can maintain clause status.
    # status[i] = 1 if satisfied, 0 if unresolved, -1 if conflict (empty clause found)
    # But simpler: just check constraints.
    
    # Optimization: Pure Literal Elimination?
    # If a variable appears only positively in all unresolved clauses, it can be set True.
    # If only negatively, set False.
    # This can be done iteratively before branching.
    
    # Let's stick to a recursive function that:
    # 1. Propagates unit clauses.
    # 2. Checks for conflicts.
    # 3. Picks a variable and branches.
    
    # We need to track which variables are decided at which depth to backtrack properly.
    # Instead of complex trail management, we can use the fact that N is small (90).
    # We can pass a set of assigned variables or just rely on the `assignment` array
    # and use a `depth` parameter to undo changes.
    
    # Stack for backtracking: (variable_assigned, list_of_variables_set_in_propagation)
    # Actually, just a simple stack of variables assigned is enough to undo.
    assigned_stack = []
    
    def get_clause_status(clause_idx):
        # Returns 1 if satisfied, 0 if unresolved (at least one unassigned), -1 if conflict (all false)
        # Also returns the unit literal if it is a unit clause.
        unassigned_lit = 0
        for lit in clauses[clause_idx]:
            v = abs(lit)
            val = assignment[v]
            if val == -1:
                unassigned_lit = lit
            else:
                # Check if literal is true
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    return 1, 0 # Satisfied
        if unassigned_lit == 0:
            return -1, 0 # Conflict
        return 0, unassigned_lit # Unresolved, potential unit

    def propagate(start_var):
        # Propagate assignment of start_var.
        # Returns False if conflict detected, True otherwise.
        # Uses a queue for BFS-style propagation.
        queue = [start_var]
        head = 0
        while head < len(queue):
            curr_var = queue[head]
            head += 1
            curr_val = assignment[curr_var]
            
            # Determine which clauses to check
            # If curr_var is True, clauses with -curr_var lose a candidate.
            # If curr_var is False, clauses with +curr_var lose a candidate.
            # We only need to check clauses containing the negation of the assigned literal.
            
            # If assigned True (1), we check clauses where -curr_var appears.
            # If assigned False (0), we check clauses where +curr_var appears.
            
            if curr_val == 1:
                # Check clauses with -curr_var
                indices_to_check = neg_occurrence[curr_var]
            else:
                # Check clauses with +curr_var
                indices_to_check = pos_occurrence[curr_var]
                
            for idx in indices_to_check:
                status, unit_lit = get_clause_status(idx)
                if status == -1:
                    return False # Conflict
                if status == 0 and unit_lit != 0:
                    # Unit clause found
                    v_unit = abs(unit_lit)
                    if assignment[v_unit] != -1:
                        continue # Should not happen if logic is correct
                    
                    # Assign
                    new_val = 1 if unit_lit > 0 else 0
                    assignment[v_unit] = new_val
                    assigned_stack.append(v_unit)
                    queue.append(v_unit)
        return True

    def solve_recursive():
        # 1. Unit Propagation
        # We need to find all unit clauses. Since propagation can generate new units,
        # we iterate until no new units.
        # Note: The `propagate` function handles the chain reaction starting from
        # variables already assigned. But we need to scan for initial units or
        # units resulting from previous branches.
        # Actually, `propagate` is called after a branch assignment.
        # Here, we might enter `solve_recursive` without a new branch (initial call).
        # Let's scan all clauses once.
        
        # To avoid re-scanning, we can rely on the fact that `propagate` handles
        # everything if we trigger it. But we need a trigger.
        # If we just made a branch, the branch variable triggers propagate.
        # If we are at the start, we scan.
        
        # Let's refine: `propagate` assumes a variable was just assigned.
        # We can scan for any unit clause here.
        while True:
            unit_found = False
            for i, c in enumerate(clauses):
                status, unit_lit = get_clause_status(i)
                if status == -1:
                    return False
                if status == 0 and unit_lit != 0:
                    # Found a unit clause
                    v = abs(unit_lit)
                    if assignment[v] == -1:
                        val = 1 if unit_lit > 0 else 0
                        assignment[v] = val
                        assigned_stack.append(v)
                        if not propagate(v):
                            return False
                        unit_found = True
                        break # Restart scan after propagation
            if not unit_found:
                break
        
        # 2. Check if all satisfied
        # If no variables unassigned, we are done (since we checked conflicts)
        unassigned_var = -1
        for i in range(1, n + 1):
            if assignment[i] == -1:
                unassigned_var = i
                break
        
        if unassigned_var == -1:
            return True
            
        # 3. Branching
        # Heuristic: pick the variable appearing most often? Or just first one.
        # Given constraints, first one is fine.
        
        # Save state for backtracking
        # We only need to know how many variables were assigned in this step to undo.
        # The `assigned_stack` grows. We record its current length.
        stack_len = len(assigned_stack)
        
        # Try True
        assignment[unassigned_var] = 1
        assigned_stack.append(unassigned_var)
        if propagate(unassigned_var) and solve_recursive():
            return True
            
        # Backtrack
        while len(assigned_stack) > stack_len:
            v = assigned_stack.pop()
            assignment[v] = -1
        assignment[unassigned_var] = -1 # Should be covered by pop but safety
            
        # Try False
        assignment[unassigned_var] = 0
        assigned_stack.append(unassigned_var)
        if propagate(unassigned_var) and solve_recursive():
            return True
            
        # Backtrack
        while len(assigned_stack) > stack_len:
            v = assigned_stack.pop()
            assignment[v] = -1
            
        return False

    if solve_recursive():
        print("YES")
        res = []
        for i in range(1, n + 1):
            # Default to 0 if unassigned (though recursive should assign all or fail)
            val = assignment[i]
            if val == -1: val = 0 # Should not happen if logic is correct
            res.append(str(val))
        print(" ".join(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()