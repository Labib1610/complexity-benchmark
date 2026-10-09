from collections import defaultdict
import sys

def main():
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
        clause = []
        for _ in range(3):
            lit = int(data[index])
            index += 1
            clause.append(lit)
        clauses.append(clause)
    
    # We need to solve 3-SAT with n variables
    # We'll use brute-force since n <= 90 but that's too large
    # Actually, let's try a more efficient approach like 2-SAT doesn't work here
    # Let's implement a simple backtracking with unit propagation
    
    # But even that might be slow. Let's think...
    # Since this is a competition problem, maybe intended solution is 
    # to recognize it as 3-SAT and use some heuristic or special property.
    
    # For small enough n, we could try all 2^n assignments, but 2^90 is impossible.
    # However, given the constraints and that this is a competition problem,
    # perhaps there's a pattern or we're expected to implement a SAT solver technique.
    
    # Let's model this as a 3-SAT problem and attempt to solve with a simple DPLL-style algorithm
    
    # Map variable indices: 1 to n => 1 to n (positive = active, negative = inactive)
    # So variable x (1-based) is True if switch x is ACTIVE, False if INACTIVE
    
    def dpll(clauses, assignment):
        # Unit propagation
        changed = True
        while changed:
            changed = False
            new_clauses = []
            unit_clause_found = False
            for clause in clauses:
                # Evaluate clause under current assignment
                eval_clause = None  # None=unknown, True=satisfied, False=unsatisfied
                unknown_literals = []
                for lit in clause:
                    var = abs(lit)
                    if var in assignment:
                        val = assignment[var]
                        if (lit > 0 and val) or (lit < 0 and not val):
                            eval_clause = True
                            break
                        # else literal is false, continue
                    else:
                        unknown_literals.append(lit)
                
                if eval_clause is None:  # Clause not yet satisfied
                    if len(unknown_literals) == 0:
                        # All literals are false -> unsat
                        return None
                    elif len(unknown_literals) == 1:
                        # Unit clause
                        unit_lit = unknown_literals[0]
                        var = abs(unit_lit)
                        val = (unit_lit > 0)
                        if var in assignment:
                            # Conflict
                            if assignment[var] != val:
                                return None
                        else:
                            assignment[var] = val
                            changed = True
                            unit_clause_found = True
                            new_clauses.append(clause) # Will be satisfied next iteration
                    else:
                        new_clauses.append(unknown_literals)
                # else clause is satisfied, remove it
            
            clauses = new_clauses
            if not unit_clause_found:
                break
        
        # Check for pure literals? Maybe later.
        
        # Check if all clauses satisfied
        if not clauses:
            return assignment
        
        # Choose a variable to branch on
        # Pick first unassigned variable from remaining clauses
        var_to_branch = None
        for clause in clauses:
            for lit in clause:
                var = abs(lit)
                if var not in assignment:
                    var_to_branch = var
                    break
            if var_to_branch is not None:
                break
        
        if var_to_branch is None:
            # All variables assigned, but clauses remain -> contradiction
            return None
            
        # Try True
        assignment_copy = assignment.copy()
        assignment_copy[var_to_branch] = True
        result = dpll(clauses, assignment_copy)
        if result is not None:
            return result
            
        # Try False
        assignment[var_to_branch] = False
        return dpll(clauses, assignment)
    
    # Convert clauses to list of lists
    sat_clauses = []
    for clause in clauses:
        sat_clauses.append(list(clause))
    
    solution = dpll(sat_clauses, {})
    
    if solution is None:
        print("NO")
    else:
        print("YES")
        result = []
        for i in range(1, n+1):
            if i in solution:
                result.append("1" if solution[i] else "0")
            else:
                # Variable not constrained, choose default (False = INACTIVE)
                result.append("0")
        print(" ".join(result))

if __name__ == "__main__":
    main()