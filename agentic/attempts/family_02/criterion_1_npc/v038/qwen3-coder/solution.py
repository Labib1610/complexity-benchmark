from collections import defaultdict
import sys

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each check, we have a clause: at least one of the three literals must be true
    # This is a 3-SAT problem where each clause has exactly 3 literals
    
    # We'll use a SAT solver approach
    # Variable i represents toggle i being in position 1
    # Literal i means variable i is true (toggle i = 1)
    # Literal -i means variable i is false (toggle i = 0)
    
    clauses = []
    for _ in range(m):
        l1, l2, l3 = map(int, input().split())
        clauses.append([l1, l2, l3])
    
    # Try to solve using brute force since n <= 90 but let's think of a better approach
    # Since each clause must have at least one literal satisfied, 
    # we can try to model this more efficiently
    
    # Let's implement a simple randomized local search or backtracking
    # But given constraints, let's try a systematic approach
    
    # We'll encode this as a 3-SAT problem and solve it with a simple backtracking algorithm
    
    def is_satisfied(assignment, clause):
        """Check if a clause is satisfied by the assignment"""
        for lit in clause:
            var = abs(lit)
            required_val = 1 if lit > 0 else 0
            if var in assignment and assignment[var] == required_val:
                return True
            elif var not in assignment:  # Variable not assigned yet
                return True  # Could still be satisfied
        return False
    
    def is_fully_satisfied(assignment, clauses):
        """Check if all clauses are satisfied by the assignment"""
        for clause in clauses:
            if not is_satisfied(assignment, clause):
                return False
        return True
    
    def backtrack(assignment, variables, clauses):
        """Backtracking solver"""
        # Check if current assignment violates any clause
        for clause in clauses:
            satisfied = False
            unknown = False
            for lit in clause:
                var = abs(lit)
                required_val = 1 if lit > 0 else 0
                if var in assignment:
                    if assignment[var] == required_val:
                        satisfied = True
                        break
                else:
                    unknown = True
            
            if not satisfied and not unknown:
                return None  # Current assignment violates this clause
        
        # If all variables are assigned, we have a solution
        if len(assignment) == len(variables):
            return assignment.copy()
        
        # Pick next unassigned variable
        for var in variables:
            if var not in assignment:
                # Try value 0
                assignment[var] = 0
                result = backtrack(assignment, variables, clauses)
                if result is not None:
                    return result
                
                # Try value 1
                assignment[var] = 1
                result = backtrack(assignment, variables, clauses)
                if result is not None:
                    return result
                
                # Backtrack
                del assignment[var]
                return None
        
        return None
    
    # Optimization: Pure literal elimination and unit propagation would help,
    # but let's first just try a simple approach with variable ordering heuristics
    
    def improved_backtrack(assignment, clauses, unassigned_vars):
        # Unit propagation
        changed = True
        while changed:
            changed = False
            new_clauses = []
            for clause in clauses:
                satisfied = False
                num_unassigned = 0
                unassigned_literal = None
                
                for lit in clause:
                    var = abs(lit)
                    required_val = 1 if lit > 0 else 0
                    
                    if var in assignment:
                        if assignment[var] == required_val:
                            satisfied = True
                            break
                    else:
                        num_unassigned += 1
                        unassigned_literal = lit
                
                if satisfied:
                    continue  # Clause already satisfied, remove it
                
                if num_unassigned == 0:
                    return None  # Unsatisfiable
                
                if num_unassigned == 1:
                    # Unit clause - force the unassigned literal
                    var = abs(unassigned_literal)
                    required_val = 1 if unassigned_literal > 0 else 0
                    if var in assignment and assignment[var] != required_val:
                        return None  # Conflict
                    assignment[var] = required_val
                    if var in unassigned_vars:
                        unassigned_vars.remove(var)
                    changed = True
                else:
                    new_clauses.append(clause)
            
            clauses = new_clauses
        
        # Check if solved
        if not unassigned_vars:
            return assignment.copy()
        
        # Choose variable with most occurrences (MOM heuristic)
        var_count = defaultdict(int)
        for clause in clauses:
            for lit in clause:
                var = abs(lit)
                if var in unassigned_vars:
                    var_count[var] += 1
        
        if var_count:
            var = max(var_count.keys(), key=lambda v: var_count[v])
        else:
            var = next(iter(unassigned_vars))
        
        unassigned_vars.remove(var)
        
        # Try value 1 first
        assignment[var] = 1
        result = improved_backtrack(assignment.copy(), [c[:] for c in clauses], unassigned_vars.copy())
        if result is not None:
            return result
        
        # Try value 0
        assignment[var] = 0
        result = improved_backtrack(assignment.copy(), [c[:] for c in clauses], unassigned_vars.copy())
        if result is not None:
            return result
        
        return None
    
    # Collect all variables
    variables = set()
    for clause in clauses:
        for lit in clause:
            variables.add(abs(lit))
    
    # Ensure all variables from 1 to n are considered
    all_variables = set(range(1, n+1))
    
    solution = improved_backtrack({}, clauses, all_variables)
    
    if solution is None:
        print("NO")
    else:
        print("YES")
        result = []
        for i in range(1, n+1):
            result.append(str(solution.get(i, 0)))  # Default to 0 if not in solution
        print(" ".join(result))

solve()