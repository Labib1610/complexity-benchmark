from collections import defaultdict
import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    clauses = []
    for _ in range(m):
        clause = list(map(int, sys.stdin.readline().split()))
        clauses.append(clause)
    return n, m, clauses

def solve_2sat(n, clauses):
    # Convert to 2-SAT format
    # Each variable x_i corresponds to channel i+1
    # x_i = 1 means phase 1, x_i = 0 means phase 0
    
    # For each clause [a, b, c], at least one must be satisfied
    # This is equivalent to saying it's NOT the case that all are false
    # So we add implications based on when all would be false
    
    # We'll convert to CNF and use implication graph
    # But let's think differently: for each clause, enumerate all assignments
    # that satisfy it, and build a constraint satisfaction problem
    
    # Actually, let's model this more directly
    # For each monitor, at least one connection must be satisfied
    # A connection is satisfied if:
    # - It's +i and channel i is set to 1
    # - It's -i and channel i is set to 0
    
    # Let's try all 2^n possibilities for small n, but n can be up to 90
    # That's too large for brute force
    
    # Let's reduce to 2-SAT properly
    # For each clause (a OR b OR c), we can convert it to:
    # (!a => b OR c) which is equivalent to (!a => b) OR (!a => c)
    # Which gives us (!a OR b) AND (!a OR c)
    # But this creates new variables...
    
    # Simpler approach: 
    # For each clause [a,b,c], create constraints that at least one is true
    # This is a 3-SAT clause, but we can reduce to 2-SAT
    
    # Let's use the standard reduction from 3-SAT to 2-SAT by introducing auxiliary variables
    # But that might be overkill
    
    # Let's instead model this as a constraint satisfaction problem and use a SAT solver approach
    
    # Map variable indices: channel i (1-based) -> index i-1 (0-based)
    
    # For each clause (a OR b OR c), we want at least one to be true
    # This is equivalent to NOT(a AND NOT(b) AND NOT(c))
    # Which doesn't directly help
    
    # Let's think of it this way:
    # For clause [1, 2, 3]: at least one of these should have its expected value
    # Channel 1 should be 1 OR Channel 2 should be 1 OR Channel 3 should be 1
    
    # For clause [-1, 2, -3]: 
    # Channel 1 should be 0 OR Channel 2 should be 1 OR Channel 3 should be 0
    
    # So each clause is of the form: 
    # (x_a == val_a) OR (x_b == val_b) OR (x_c == val_c)
    
    # To convert to 2-SAT, we introduce an auxiliary variable y for each clause
    # and represent the 3-clause as 2-SAT with y:
    # y => (x_a == val_a) OR (x_b == val_b)
    # (x_a == val_a) OR (x_b == val_b) => y
    # y => (x_c == val_c) OR (aux_literal)
    # But this gets complex
    
    # Let's implement a backtracking solution with pruning
    
    def get_var_value(assignment, var):
        # var is signed integer
        idx = abs(var) - 1
        if idx >= len(assignment):
            return None
        val = assignment[idx]
        if val is None:
            return None
        expected = 1 if var > 0 else 0
        return 1 if val == expected else 0
    
    def is_clause_satisfied(assignment, clause):
        for lit in clause:
            val = get_var_value(assignment, lit)
            if val is None:  # Variable not assigned yet
                return True  # Could still be satisfied
            if val == 1:  # Literal is satisfied
                return True
        return False  # All literals are false
    
    def is_all_clauses_satisfied(assignment, clauses):
        for clause in clauses:
            if not is_clause_satisfied(assignment, clause):
                return False
        return True
    
    def is_consistent_so_far(assignment, clauses):
        for clause in clauses:
            # Check if clause is already violated
            satisfied = False
            all_determined = True
            for lit in clause:
                val = get_var_value(assignment, lit)
                if val == 1:
                    satisfied = True
                    break
                elif val is None:
                    all_determined = False
            
            if not satisfied and all_determined:
                return False
        return True
    
    def backtrack(assignment, index):
        if index == n:
            return is_all_clauses_satisfied(assignment, clauses)
        
        if not is_consistent_so_far(assignment, clauses):
            return False
        
        # Try setting to 0
        assignment[index] = 0
        if backtrack(assignment, index + 1):
            return True
            
        # Try setting to 1
        assignment[index] = 1
        if backtrack(assignment, index + 1):
            return True
            
        # Backtrack
        assignment[index] = None
        return False
    
    assignment = [None] * n
    if backtrack(assignment, 0):
        return [0 if x == 0 else 1 for x in assignment]
    else:
        return None

def main():
    n, m, clauses = read_input()
    result = solve_2sat(n, clauses)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()