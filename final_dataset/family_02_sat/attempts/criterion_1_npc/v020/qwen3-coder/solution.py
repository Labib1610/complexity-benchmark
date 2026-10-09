from collections import defaultdict
import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each stabilizer, we have a clause of 3 literals
    # We need to satisfy all clauses (3-SAT variant)
    
    clauses = []
    for _ in range(m):
        clause = list(map(int, sys.stdin.readline().split()))
        clauses.append(clause)
    
    # Try all 2^n assignments
    # But n can be up to 90, so 2^90 is too large
    # However, since this is a 3-SAT problem with small clauses,
    # and given the constraints, let's try a more efficient approach
    
    # Actually, let's try brute force since n <= 90 but likely much smaller in practice
    # For larger n, this won't work, but let's see
    
    # Let's implement a backtracking solution
    # For each variable, try 0 and 1, and propagate constraints
    
    # We'll use a SAT solver approach
    
    # Since n can be up to 90, brute force won't work
    # Let's try to implement a simple DPLL-style algorithm
    
    def is_satisfied(assignment):
        # Check if all clauses are satisfied
        for clause in clauses:
            satisfied = False
            for lit in clause:
                var = abs(lit)
                if var > n:
                    continue
                if lit > 0:
                    if assignment[var-1] == 1:
                        satisfied = True
                        break
                else:
                    if assignment[var-1] == 0:
                        satisfied = True
                        break
            if not satisfied:
                return False
        return True
    
    # For small n, we can try all assignments
    if n <= 20:
        for mask in range(1 << n):
            assignment = []
            for i in range(n):
                assignment.append((mask >> i) & 1)
            
            if is_satisfied(assignment):
                print("YES")
                print(" ".join(map(str, assignment)))
                return
        print("NO")
        return
    
    # For larger n, we need a more sophisticated approach
    # Let's implement a simple backtracking with unit propagation
    
    # Initialize assignment as -1 (unassigned)
    assignment = [-1] * n
    
    def propagate_unit_clauses():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                # Count unassigned literals and find the unassigned one if only one
                unassigned_count = 0
                unassigned_literal = 0
                satisfied = False
                
                for lit in clause:
                    var = abs(lit)
                    if var > n:
                        continue
                    if assignment[var-1] == -1:
                        unassigned_count += 1
                        unassigned_literal = lit
                    elif (lit > 0 and assignment[var-1] == 1) or (lit < 0 and assignment[var-1] == 0):
                        satisfied = True
                        break
                
                if satisfied:
                    continue
                    
                if unassigned_count == 0:
                    # All literals are assigned but none satisfy the clause
                    return False  # Conflict
                    
                if unassigned_count == 1:
                    # Unit clause - force the unassigned literal
                    var = abs(unassigned_literal)
                    value = 1 if unassigned_literal > 0 else 0
                    if assignment[var-1] == -1:
                        assignment[var-1] = value
                        changed = True
                    elif assignment[var-1] != value:
                        return False  # Conflict
        return True
    
    def backtrack(index):
        if index == n:
            return True
            
        # Try 0 first
        assignment[index] = 0
        saved = assignment[:]
        if propagate_unit_clauses():
            if backtrack(index + 1):
                return True
        assignment[:] = saved
        
        # Try 1
        assignment[index] = 1
        saved = assignment[:]
        if propagate_unit_clauses():
            if backtrack(index + 1):
                return True
        assignment[:] = saved
        
        # Backtrack
        assignment[index] = -1
        return False
    
    # Start backtracking
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()