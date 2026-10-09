from collections import defaultdict
import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each pin, we have a clause: at least one of the three prongs must be satisfied
    # This is a 3-SAT problem where each clause has exactly 3 literals
    # Literal x means variable x is True
    # Literal -x means variable x is False
    
    # We'll use the classic reduction to 2-SAT by introducing auxiliary variables
    # But actually, let's try a different approach: since each clause has 3 literals,
    # we can convert it to multiple 2-SAT clauses
    
    # However, let's think differently. We can try all 2^n possibilities for small n
    # But n can be up to 90, so that's not feasible.
    
    # Let's model this as a 3-SAT problem and use a SAT solver approach
    # Each tumbler i is a boolean variable: True means high (1), False means low (0)
    # For each pin with prongs l1, l2, l3:
    #   if li > 0: tumbler li must be True (1)
    #   if li < 0: tumbler |li| must be False (0)
    # So the clause is: (t[|l1|] == (l1>0)) OR (t[|l2|] == (l2>0)) OR (t[|l3|] == (l3>0))
    
    # This is exactly 3-SAT. But since we need to solve it efficiently, let's try to 
    # find a solution using backtracking with constraint propagation
    
    # Let's represent the problem as clauses
    clauses = []
    for _ in range(m):
        l1, l2, l3 = map(int, sys.stdin.readline().split())
        # Convert to 0-indexed variables
        # Positive literal means tumbler should be 1
        # Negative literal means tumbler should be 0
        clause = []
        for lit in [l1, l2, l3]:
            if lit > 0:
                clause.append((lit-1, 1))  # tumbler lit (1-indexed) should be 1
            else:
                clause.append((-lit-1, 0)) # tumbler |lit| (1-indexed) should be 0
        clauses.append(clause)
    
    # Now we need to find an assignment of 0/1 to variables 0..n-1
    # such that for each clause, at least one literal is satisfied
    
    # Try to solve with backtracking
    assignment = [None] * n
    
    def is_satisfied(clause, assignment):
        for var, val in clause:
            if assignment[var] is not None:
                if assignment[var] == val:
                    return True
        return False
    
    def all_clauses_satisfied(clauses, assignment):
        for clause in clauses:
            if not is_satisfied(clause, assignment):
                return False
        return True
    
    def find_unsatisfied_clause(clauses, assignment):
        for i, clause in enumerate(clauses):
            if not is_satisfied(clause, assignment):
                return i, clause
        return None, None
    
    def backtrack(index):
        if index == n:
            return all_clauses_satisfied(clauses, assignment)
        
        # Try setting variable index to 0
        assignment[index] = 0
        if backtrack(index + 1):
            return True
            
        # Try setting variable index to 1
        assignment[index] = 1
        if backtrack(index + 1):
            return True
            
        assignment[index] = None
        return False
    
    # Optimization: Unit propagation
    def unit_propagate():
        changed = True
        while changed:
            changed = False
            clause_idx, clause = find_unsatisfied_clause(clauses, assignment)
            while clause_idx is not None:
                unset_vars = [(var, val) for var, val in clause if assignment[var] is None]
                if len(unset_vars) == 0:
                    # All variables are set but clause is not satisfied
                    return False
                elif len(unset_vars) == 1:
                    # Unit clause
                    var, val = unset_vars[0]
                    if assignment[var] is None:
                        assignment[var] = val
                        changed = True
                    elif assignment[var] != val:
                        return False
                clause_idx, clause = find_unsatisfied_clause(clauses, assignment)
        return True
    
    # More sophisticated approach with better propagation
    def solve_with_propagation():
        # First, do unit propagation
        stack = []
        if not unit_propagate():
            return False
            
        # Find first unassigned variable
        for i in range(n):
            if assignment[i] is None:
                # Try 0
                assignment[i] = 0
                stack.append((i, 0))
                if solve_with_propagation():
                    return True
                    
                # Backtrack
                assignment[i] = None
                stack.pop()
                
                # Try 1
                assignment[i] = 1
                stack.append((i, 1))
                if solve_with_propagation():
                    return True
                    
                # Backtrack
                assignment[i] = None
                stack.pop()
                return False
                
        # All variables assigned
        return all_clauses_satisfied(clauses, assignment)
    
    # Even simpler: just do basic backtracking with unit propagation at each step
    def backtrack_improved(index):
        # Do unit propagation
        if not unit_propagate():
            return False
            
        # Check if done
        if all(assignment[i] is not None for i in range(n)):
            return all_clauses_satisfied(clauses, assignment)
            
        # Find next unassigned variable
        next_var = index
        while next_var < n and assignment[next_var] is not None:
            next_var += 1
            
        if next_var == n:
            return all_clauses_satisfied(clauses, assignment)
            
        # Save state for backtracking
        old_assignment = assignment[:]
        
        # Try 0
        assignment[next_var] = 0
        if backtrack_improved(next_var + 1):
            return True
            
        # Restore and try 1
        for i in range(n):
            assignment[i] = old_assignment[i]
        assignment[next_var] = 1
        if backtrack_improved(next_var + 1):
            return True
            
        # Restore
        for i in range(n):
            assignment[i] = old_assignment[i]
        return False
    
    # Actually, let's implement a cleaner version
    def solve_sat():
        def propagate():
            # Simple unit propagation
            changed = True
            while changed:
                changed = False
                _, clause = find_unsatisfied_clause(clauses, assignment)
                while clause is not None:
                    unset_count = 0
                    unset_var, unset_val = -1, -1
                    conflict = False
                    
                    for var, val in clause:
                        if assignment[var] is None:
                            unset_count += 1
                            unset_var, unset_val = var, val
                        elif assignment[var] == val:
                            # Clause already satisfied
                            break
                    else:
                        # Went through all literals in clause
                        if unset_count == 0:
                            # Conflict - all literals are false
                            return False
                        elif unset_count == 1:
                            # Unit propagation
                            if assignment[unset_var] is None:
                                assignment[unset_var] = unset_val
                                changed = True
                            elif assignment[unset_var] != unset_val:
                                return False
                                
                    _, clause = find_unsatisfied_clause(clauses, assignment)
            return True
        
        def backtrack(index):
            if not propagate():
                return False
                
            # Find next unassigned variable
            next_index = index
            while next_index < n and assignment[next_index] is not None:
                next_index += 1
                
            if next_index == n:
                # Check if all clauses satisfied
                return all_clauses_satisfied(clauses, assignment)
                
            # Try both values
            old_state = assignment[:]
            assignment[next_index] = 0
            if backtrack(next_index + 1):
                return True
                
            # Restore and try 1
            assignment[:] = old_state
            assignment[next_index] = 1
            if backtrack(next_index + 1):
                return True
                
            # Restore
            assignment[:] = old_state
            return False
            
        return backtrack(0)
    
    if solve_sat():
        print("YES")
        print(" ".join(str(x) for x in assignment))
    else:
        print("NO")

solve()