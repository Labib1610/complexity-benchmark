from collections import defaultdict
import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each module, we have a clause: at least one of three literals must be true
    # This is a 3-SAT variant where each clause is an OR of 3 literals
    # We can solve this with a SAT solver approach or brute force for small n
    # But since n <= 90, we need an efficient approach
    
    # Let's model this as 2-SAT if possible, but it's 3-SAT
    # We'll use a randomized approach or try to convert
    
    # Actually, let's think differently. Each module is a clause with 3 literals
    # We need to satisfy all clauses
    # This is exactly 3-SAT problem
    
    # Since n <= 90 and m <= 400, we can't brute force
    # But we can use the fact that each clause only has 3 literals
    
    # Let's try a greedy approach with backtracking optimization
    # Or use a SAT solver technique
    
    # For small instances, we can try local search
    # But let's implement a proper solution using implication graph for 2-SAT
    # Wait, this is 3-SAT, not 2-SAT
    
    # Let's try to solve with a SAT approach
    # We'll convert to 3-CNF and try to find a solution
    
    # Actually, let's implement a simple backtracking with constraint propagation
    
    clauses = []
    for _ in range(m):
        l1, l2, l3 = map(int, sys.stdin.readline().split())
        clauses.append((l1, l2, l3))
    
    # Try all assignments - not feasible for n=90
    # Need a smarter approach
    
    # Let's use a randomized local search or walkSAT approach
    # But for a guaranteed solution, let's try a complete algorithm
    
    # We'll use a backtracking approach with optimizations
    
    def is_satisfied(assignment):
        for l1, l2, l3 in clauses:
            val1 = assignment[abs(l1)] if l1 > 0 else 1 - assignment[abs(l1)]
            val2 = assignment[abs(l2)] if l2 > 0 else 1 - assignment[abs(l2)]
            val3 = assignment[abs(l3)] if l3 > 0 else 1 - assignment[abs(l3)]
            if not (val1 or val2 or val3):
                return False
        return True
    
    # For small n, we can try brute force
    if n <= 20:
        for mask in range(1 << n):
            assignment = [0] * (n + 1)
            for i in range(n):
                assignment[i + 1] = (mask >> i) & 1
            if is_satisfied(assignment):
                print("YES")
                print(" ".join(str(assignment[i]) for i in range(1, n + 1)))
                return
        print("NO")
        return
    
    # For larger n, we need a more sophisticated approach
    # Let's try a greedy + local search approach
    
    from random import randint, shuffle
    
    def random_assignment():
        assignment = [0] * (n + 1)
        for i in range(1, n + 1):
            assignment[i] = randint(0, 1)
        return assignment
    
    def unsatisfied_clauses(assignment):
        unsat = []
        for idx, (l1, l2, l3) in enumerate(clauses):
            val1 = assignment[abs(l1)] if l1 > 0 else 1 - assignment[abs(l1)]
            val2 = assignment[abs(l2)] if l2 > 0 else 1 - assignment[abs(l2)]
            val3 = assignment[abs(l3)] if l3 > 0 else 1 - assignment[abs(l3)]
            if not (val1 or val2 or val3):
                unsat.append(idx)
        return unsat
    
    def flip_to_satisfy(assignment, clause_idx):
        l1, l2, l3 = clauses[clause_idx]
        vars_in_clause = [l1, l2, l3]
        # Try flipping each variable to satisfy the clause
        best_var = None
        min_unsat = len(clauses)
        
        for var in vars_in_clause:
            # Flip the variable
            assignment[abs(var)] = 1 - assignment[abs(var)]
            unsat_count = len(unsatisfied_clauses(assignment))
            if unsat_count < min_unsat:
                min_unsat = unsat_count
                best_var = abs(var)
            # Flip back
            assignment[abs(var)] = 1 - assignment[abs(var)]
            
        if best_var is not None:
            assignment[best_var] = 1 - assignment[best_var]
    
    # WalkSAT approach
    for _ in range(1000):  # Try 1000 random starts
        assignment = random_assignment()
        for _ in range(2000):  # Try 2000 flips
            unsat = unsatisfied_clauses(assignment)
            if not unsat:
                print("YES")
                print(" ".join(str(assignment[i]) for i in range(1, n + 1)))
                return
            
            # Pick a random unsatisfied clause
            clause_idx = unsat[randint(0, len(unsat) - 1)]
            
            # With probability 0.5, flip the variable that minimizes unsatisfied clauses
            # Otherwise, flip a random variable in the clause
            if randint(0, 1) == 0:
                flip_to_satisfy(assignment, clause_idx)
            else:
                l1, l2, l3 = clauses[clause_idx]
                var_to_flip = abs([l1, l2, l3][randint(0, 2)])
                assignment[var_to_flip] = 1 - assignment[var_to_flip]
    
    # If local search fails, try a systematic approach for smaller subsets
    # Let's try with a SAT solver simulation
    
    # Since this is getting complex, let's implement a simple DPLL-style backtracking
    # But optimized for this specific case
    
    def dpll_solve():
        # Simple backtracking
        assignment = [-1] * (n + 1)  # -1 means unassigned
        
        def is_currently_satisfied():
            for l1, l2, l3 in clauses:
                val1 = assignment[abs(l1)] if l1 > 0 else 1 - assignment[abs(l1)] if assignment[abs(l1)] != -1 else -1
                val2 = assignment[abs(l2)] if l2 > 0 else 1 - assignment[abs(l2)] if assignment[abs(l2)] != -1 else -1
                val3 = assignment[abs(l3)] if l3 > 0 else 1 - assignment[abs(l3)] if assignment[abs(l3)] != -1 else -1
                
                # If any is true, clause is satisfied
                if val1 == 1 or val2 == 1 or val3 == 1:
                    continue
                # If all are assigned and false, clause is unsatisfied
                if val1 == 0 and val2 == 0 and val3 == 0:
                    return False
                # If any is unassigned, clause is not yet determined to be false
            return True
        
        def is_completely_satisfied():
            for l1, l2, l3 in clauses:
                val1 = assignment[abs(l1)] if l1 > 0 else 1 - assignment[abs(l1)]
                val2 = assignment[abs(l2)] if l2 > 0 else 1 - assignment[abs(l2)]
                val3 = assignment[abs(l3)] if l3 > 0 else 1 - assignment[abs(l3)]
                if not (val1 or val2 or val3):
                    return False
            return True
        
        def backtrack(var_index):
            if var_index > n:
                return is_completely_satisfied()
            
            for value in [0, 1]:
                assignment[var_index] = value
                if is_currently_satisfied():
                    if backtrack(var_index + 1):
                        return True
            assignment[var_index] = -1
            return False
        
        if backtrack(1):
            return [assignment[i] for i in range(1, n + 1)]
        else:
            return None
    
    # This might be too slow for n=90, let's limit it
    if n <= 30:
        result = dpll_solve()
        if result is not None:
            print("YES")
            print(" ".join(map(str, result)))
            return
    
    print("NO")

solve()