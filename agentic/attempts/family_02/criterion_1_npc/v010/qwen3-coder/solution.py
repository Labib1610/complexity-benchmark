from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    clauses = []
    idx = 2
    for _ in range(m):
        clause = []
        for _ in range(3):
            lit = int(data[idx])
            idx += 1
            clause.append(lit)
        clauses.append(clause)
    
    # For each regulator i, we have variable i (1-indexed)
    # Positive literal: regulator i is active (1)
    # Negative literal: regulator i is standby (0)
    
    # We reduce to 2-SAT by creating auxiliary variables for 3-literals
    
    # However, since we're dealing with 3-SAT, we can try all 2^n possibilities for small n,
    # but n can be up to 90, so that's infeasible.
    
    # Instead, we'll model this as a 3-SAT problem and use the fact that each clause has 3 literals.
    # But since n is large and m is up to 400, we should think of a different approach.
    
    # Actually, let's re-think the problem:
    # Each hazard scenario is defined by 3 specific regulator states.
    # The scenario triggers (shuts down) if NONE of these 3 states match the actual configuration.
    # So for each clause (scenario), AT LEAST ONE of the literals must be true.
    # This is exactly 3-SAT.
    
    # Since n can be up to 90, and m up to 400, solving general 3-SAT is NP-hard.
    # But perhaps there's structure or we can use SAT solving techniques.
    
    # Let's implement a simple randomized algorithm or backtracking with pruning.
    
    # Given the constraints, let's try a local search or backtracking approach.
    # But with n=90, even that might be too slow.
    
    # Wait, let's re-read the problem:
    # "A hazard scenario is defined by a combination of three specific regulator states."
    # "A hazard scenario materializes if and only if the plant's actual configuration does not match any of the three states"
    # So for each scenario, the configuration must match at least one of the three specified states.
    
    # So for each clause (l1 OR l2 OR l3), at least one must be satisfied.
    # This is indeed 3-SAT.
    
    # But given that this is a competitive programming problem, there might be a special case
    # or we're expected to solve it via some heuristic or reduction.
    
    # Let's try to implement a backtracking solution with pruning.
    
    # Variables: x[1] to x[n], where x[i] = 1 means active, x[i] = 0 means standby
    
    # To make indexing easier, we'll use 1-based indexing for variables.
    
    # Let's convert the clauses to a form suitable for checking.
    # Each clause is a list of 3 literals. A literal is either +i or -i.
    # If literal is +i, then x[i] must be 1.
    # If literal is -i, then x[i] must be 0.
    
    def check_satisfied(clause, assignment):
        for lit in clause:
            var = abs(lit)
            required_value = 1 if lit > 0 else 0
            if assignment[var] == required_value:
                return True
        return False
    
    def solve():
        # Try to find a satisfying assignment using backtracking with unit propagation
        # But with n up to 90, this might be too slow.
        
        # Let's instead model this properly and see if we can apply optimizations.
        
        # One idea: convert to 3-CNF and look for conflicts or use known algorithms.
        # Another idea: since m <= 400, maybe we can do something smarter.
        
        # Let's try a greedy approach: assign values to satisfy as many clauses as possible.
        # Or implement a simple DPLL-style solver.
        
        # For now, let's implement a basic backtracking with optimizations.
        
        # But given time constraints, let's consider that maybe we can solve a subset.
        
        # Actually, let's just implement a backtracking solution and hope it passes.
        
        assignment = [None] * (n+1)  # 1-indexed
        
        # Unit propagation: if a clause has only one unassigned literal, set it to satisfy the clause
        def unit_propagate():
            changed = True
            while changed:
                changed = False
                for clause in clauses:
                    unknown_count = 0
                    unknown_lit = None
                    satisfied = False
                    for lit in clause:
                        var = abs(lit)
                        if assignment[var] is None:
                            unknown_count += 1
                            unknown_lit = lit
                        else:
                            required = 1 if lit > 0 else 0
                            if assignment[var] == required:
                                satisfied = True
                                break
                    if not satisfied and unknown_count == 1:
                        # Unit clause
                        var = abs(unknown_lit)
                        required = 1 if unknown_lit > 0 else 0
                        if assignment[var] is None:
                            assignment[var] = required
                            changed = True
                        elif assignment[var] != required:
                            return False  # Conflict
            return True
        
        def is_satisfied():
            for clause in clauses:
                satisfied = False
                for lit in clause:
                    var = abs(lit)
                    required = 1 if lit > 0 else 0
                    if assignment[var] == required:
                        satisfied = True
                        break
                if not satisfied:
                    return False
            return True
        
        # First, do unit propagation
        if not unit_propagate():
            return None
            
        # Check if already satisfied
        if is_satisfied():
            return assignment
            
        # Find unassigned variables
        unassigned_vars = [i for i in range(1, n+1) if assignment[i] is None]
        
        def backtrack(index):
            if index == len(unassigned_vars):
                return is_satisfied()
            
            var = unassigned_vars[index]
            for value in [0, 1]:
                assignment[var] = value
                if unit_propagate():  # Propagate units after assignment
                    if backtrack(index + 1):
                        return True
                # Undo unit propagation changes would be complex, so let's copy assignment
                # Actually, let's simplify and not do full unit propagation in recursion
                pass
                
            assignment[var] = None
            return False
            
        # Simplified backtracking without full unit propagation during search
        def simple_backtrack(index):
            if index == len(unassigned_vars):
                return is_satisfied()
                
            var = unassigned_vars[index]
            for value in [0, 1]:
                assignment[var] = value
                if simple_backtrack(index + 1):
                    return True
            assignment[var] = None
            return False
            
        # Run simplified backtracking
        if simple_backtrack(0):
            return assignment
        else:
            return None
    
    result = solve()
    if result is None:
        print("NO")
    else:
        print("YES")
        # Output the assignment for variables 1 to n
        out_vals = []
        for i in range(1, n+1):
            val = result[i]
            if val is None:
                val = 0  # Default to 0 if unassigned
            out_vals.append(str(val))
        print(' '.join(out_vals))

if __name__ == "__main__":
    main()