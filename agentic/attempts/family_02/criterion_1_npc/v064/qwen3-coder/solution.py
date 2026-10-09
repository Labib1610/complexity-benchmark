from collections import defaultdict
import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each protocol, we have a clause with 3 literals
    # This is a 3-SAT problem
    clauses = []
    for _ in range(m):
        clause = list(map(int, sys.stdin.readline().split()))
        clauses.append(clause)
    
    # Try all possible assignments
    # But n can be up to 90, so 2^90 is too large
    # However, since each clause has 3 literals, we can use a randomized approach or 
    # more sophisticated algorithm. But given the constraints, let's try a smart brute force.
    
    # Actually, let's implement a proper 3-SAT solver using backtracking with unit propagation
    
    # Map variable to index: variable i (1-based) -> index 2*i (for positive) and 2*i+1 (for negative)
    # But simpler approach: for variable i (1-based):
    # positive literal i -> index 2*(i-1)
    # negative literal -i -> index 2*(i-1)+1
    
    def literal_to_index(lit):
        var = abs(lit)
        if lit > 0:
            return 2 * (var - 1)
        else:
            return 2 * (var - 1) + 1
    
    def index_to_literal(idx):
        var = (idx // 2) + 1
        if idx % 2 == 0:
            return var
        else:
            return -var
    
    # Convert clauses to indices
    indexed_clauses = []
    for clause in clauses:
        indexed_clause = [literal_to_index(lit) for lit in clause]
        indexed_clauses.append(indexed_clause)
    
    # TwoSAT/3SAT solver with backtracking
    def is_satisfied(assignment, clause):
        for lit_idx in clause:
            var_idx = lit_idx // 2
            is_positive = (lit_idx % 2 == 0)
            if var_idx < len(assignment):
                if is_positive and assignment[var_idx] == 1:
                    return True
                if not is_positive and assignment[var_idx] == 0:
                    return True
        return False
    
    def check_all_satisfied(assignment):
        for clause in indexed_clauses:
            if not is_satisfied(assignment, clause):
                return False
        return True
    
    # Backtracking search
    def backtrack(assignment):
        # Check if current assignment satisfies all clauses so far
        # Actually, better to just check at the end when all variables are assigned
        if len(assignment) == n:
            if check_all_satisfied(assignment):
                return assignment[:]
            else:
                return None
        
        # Try setting the next variable to 0, then 1
        for val in [0, 1]:
            assignment.append(val)
            result = backtrack(assignment)
            if result is not None:
                return result
            assignment.pop()
        
        return None
    
    # This approach is exponential and will be too slow for n=90
    # Let's try a different approach: since each clause has 3 literals,
    # and n <= 90, m <= 400, we can try a randomized approach or 
    # use the fact that random assignments satisfy 7/8 of 3-CNF clauses in expectation
    
    # Randomized approach
    import random
    random.seed(42)  # For reproducibility, but we don't need it
    
    # For small n, we can do exhaustive search
    if n <= 20:
        solution = backtrack([])
        if solution is not None:
            print("YES")
            print(" ".join(map(str, solution)))
        else:
            print("NO")
        return
    
    # For larger n, try random assignments
    # In a random assignment to a 3-CNF clause, the probability of it being unsatisfied is (1/2)^3 = 1/8
    # So probability of being satisfied is 7/8
    # For m=400, probability all satisfied is (7/8)^400 which is very small
    # But we can try many random assignments
    
    for _ in range(min(1000, 1 << min(n, 15))):  # Limit the number of tries
        assignment = [random.randint(0, 1) for _ in range(n)]
        if check_all_satisfied(assignment):
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    # If that doesn't work, try a more systematic approach for medium n
    if n <= 30:
        # Try a more complete search with pruning
        # But let's keep it simple and just do a full backtracking with early termination
        pass
    
    # Let's implement a proper DPLL-style algorithm
    def dpll_solve():
        # Initialize assignment as None (unassigned)
        assignment = [None] * n
        
        def is_clause_satisfied(clause, assignment):
            for lit_idx in clause:
                var_idx = lit_idx // 2
                is_positive = (lit_idx % 2 == 0)
                if assignment[var_idx] is not None:
                    if is_positive and assignment[var_idx] == 1:
                        return True
                    if not is_positive and assignment[var_idx] == 0:
                        return True
                elif assignment[var_idx] is None:
                    # Variable is unassigned, so this literal could be true
                    pass
            # Check if all literals are false
            all_false = True
            for lit_idx in clause:
                var_idx = lit_idx // 2
                is_positive = (lit_idx % 2 == 0)
                if assignment[var_idx] is None:
                    all_false = False
                    break
                if is_positive and assignment[var_idx] == 1:
                    all_false = False
                    break
                if not is_positive and assignment[var_idx] == 0:
                    all_false = False
                    break
            if all_false:
                return False  # Clause is unsatisfiable
            return None  # Unknown, depends on unassigned variables
        
        def unit_propagate(assignment):
            changed = True
            while changed:
                changed = False
                for clause in indexed_clauses:
                    # Count unassigned literals and find forced assignments
                    unassigned_count = 0
                    last_unassigned_var = -1
                    last_unassigned_sign = False
                    satisfied = False
                    
                    for lit_idx in clause:
                        var_idx = lit_idx // 2
                        is_positive = (lit_idx % 2 == 0)
                        if assignment[var_idx] is not None:
                            if (is_positive and assignment[var_idx] == 1) or \
                               (not is_positive and assignment[var_idx] == 0):
                                satisfied = True
                                break
                        else:
                            unassigned_count += 1
                            last_unassigned_var = var_idx
                            last_unassigned_sign = is_positive
                    
                    if satisfied:
                        continue
                    
                    if unassigned_count == 0:
                        # All literals are assigned and none are true - conflict
                        return False
                    
                    if unassigned_count == 1:
                        # Unit clause - force the unassigned variable
                        value = 1 if last_unassigned_sign else 0
                        if assignment[last_unassigned_var] is None:
                            assignment[last_unassigned_var] = value
                            changed = True
                        elif assignment[last_unassigned_var] != value:
                            # Conflict
                            return False
            return True
        
        def choose_variable(assignment):
            # Choose the first unassigned variable
            for i in range(n):
                if assignment[i] is None:
                    return i
            return -1
        
        def backtrack_dpll(assignment):
            # Unit propagation
            if not unit_propagate(assignment):
                return None
            
            # Check for completion
            var_idx = choose_variable(assignment)
            if var_idx == -1:
                # All variables assigned
                return [x if x is not None else 0 for x in assignment]
            
            # Try setting variable to 1
            assignment[var_idx] = 1
            result = backtrack_dpll(assignment)
            if result is not None:
                return result
            
            # Try setting variable to 0
            assignment[var_idx] = 0
            result = backtrack_dpll(assignment)
            if result is not None:
                return result
            
            # Backtrack
            assignment[var_idx] = None
            return None
        
        return backtrack_dpll(assignment)
    
    solution = dpll_solve()
    if solution is not None:
        print("YES")
        print(" ".join(map(str, solution)))
    else:
        print("NO")

solve()