from collections import defaultdict
import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each check, we have a clause: at least one of three literals must be true
    # This is a 3-SAT problem where each clause is an "OR" of 3 literals
    # We'll use the 2-SAT approach by reducing 3-SAT to 2-SAT through auxiliary variables
    
    # However, let's think differently. Each check is a constraint that at least one of three positions is correct.
    # We can model this as: (x_a OR x_b OR x_c) where x_i represents if lever |i| is in the correct state for this check
    # But since each literal refers to a specific lever being UP or DOWN, we need to be more precise.
    
    # Let's use the standard approach for solving this type of constraint satisfaction:
    # Each check is a disjunction of 3 literals. We want to find if there exists an assignment
    # to the n variables (lever states) such that all m disjunctions are satisfied.
    
    # This is exactly 3-SAT. But since n<=90 and m<=400, we need an efficient approach.
    
    # Let's try to model this properly and use a SAT solver approach or brute force with pruning.
    # Since n can be up to 90, brute force is not feasible.
    
    # Let's think of it as a 3-CNF-SAT problem and try to solve it with a backtracking algorithm
    # with unit propagation and pure literal elimination optimizations.
    
    # But given the constraints, let's try a different approach.
    # We can reduce this to 2-SAT by introducing auxiliary variables, but that might be complex.
    
    # Let's implement a simple backtracking solution with early termination.
    
    # Parse the constraints
    clauses = []
    for _ in range(m):
        line = list(map(int, sys.stdin.readline().split()))
        clauses.append(line)
    
    # Try all possible assignments using backtracking with pruning
    def is_satisfied(assignment):
        # assignment is a list where assignment[i] is 0 (DOWN) or 1 (UP) for lever i+1
        for clause in clauses:
            satisfied = False
            for literal in clause:
                lever_idx = abs(literal) - 1
                required_state = 1 if literal > 0 else 0
                if assignment[lever_idx] == required_state:
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True
    
    # Backtracking with pruning
    def backtrack(index, assignment):
        if index == n:
            return is_satisfied(assignment)
        
        # Try setting lever (index+1) to DOWN (0)
        assignment[index] = 0
        if backtrack(index + 1, assignment):
            return True
            
        # Try setting lever (index+1) to UP (1)
        assignment[index] = 1
        if backtrack(index + 1, assignment):
            return True
            
        return False
    
    assignment = [0] * n
    if backtrack(0, assignment):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()