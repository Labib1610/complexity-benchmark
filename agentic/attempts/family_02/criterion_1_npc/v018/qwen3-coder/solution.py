from collections import defaultdict
import sys

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each clause (criterion), we need at least one literal to be true
    # This is a 3-SAT variant where each clause has exactly 3 literals
    # We'll use the 2-SAT approach by reducing 3-SAT to 2-SAT
    
    # However, let's think differently. Since each clause needs at least one literal true,
    # the negation would be all literals false.
    # So we can model this as: for each clause, NOT(a AND b AND c)
    # Which is equivalent to (NOT a OR NOT b OR NOT c)
    # But 3-SAT is NP-complete, so let's try a different approach.
    
    # Let's enumerate all possible assignments since n <= 90 but that's too many.
    # Actually, let's think of this as a constraint satisfaction problem.
    
    # Better approach: Use the fact that this is essentially 3-SAT.
    # But since constraints are small, we can try backtracking or use the fact that
    # each clause is a disjunction of 3 literals.
    
    # Let's model this properly:
    # Each clause is of the form (x1 OR x2 OR x3) where xi can be a variable or its negation
    # We want to find an assignment that satisfies all clauses.
    
    # Since n can be up to 90, brute force won't work. 
    # But m is up to 400, which suggests we might be able to solve it with SAT solving techniques.
    
    # Let's implement a simple backtracking solution with pruning.
    
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        clauses.append(clause)
    
    def evaluate_clause(clause, assignment):
        for lit in clause:
            var = abs(lit)
            if lit > 0:
                if assignment[var] == 1:
                    return True
            else:
                if assignment[var] == 0:
                    return True
        return False
    
    def is_satisfied(assignment):
        for clause in clauses:
            if not evaluate_clause(clause, assignment):
                return False
        return True
    
    # Try all possible assignments - but this is 2^n which is too large for n=90
    # Need a smarter approach
    
    # Let's try to build a graph-based approach similar to 2-SAT but adapted for 3-SAT
    # Or use the fact that we can reduce 3-SAT to 2-SAT by introducing new variables
    
    # For a clause (a OR b OR c), we can replace it with:
    # (a OR b OR d) AND (NOT d OR c) where d is a new variable
    # But this complicates things.
    
    # Let's try a different approach: use the fact that for small m we can do local search
    # or constraint propagation.
    
    # Actually, let's just implement a smart backtracking with early termination
    
    # But given time limits, let's see if we can model this as 2-SAT by transformation
    
    # Another idea: for each 3-clause (a OR b OR c), it's equivalent to:
    # (a OR b) OR c, which means if (a OR b) is false then c must be true
    # This doesn't directly help either.
    
    # Let's go back to a backtracking approach but with optimizations
    
    assignment = [-1] * (n + 1)  # index 0 unused
    
    def propagate():
        # Simple constraint propagation
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                # Count how many literals are false
                false_count = 0
                unknown_vars = []
                true_found = False
                
                for lit in clause:
                    var = abs(lit)
                    if lit > 0:
                        if assignment[var] == 1:
                            true_found = True
                            break
                        elif assignment[var] == 0:
                            false_count += 1
                        else:
                            unknown_vars.append((var, True))  # (variable, should_be_true)
                    else:
                        if assignment[var] == 0:
                            true_found = True
                            break
                        elif assignment[var] == 1:
                            false_count += 1
                        else:
                            unknown_vars.append((var, False)) # (variable, should_be_false)
                
                if true_found:
                    continue
                    
                if false_count == 2 and len(unknown_vars) == 1:
                    # Only one variable left, it must satisfy the clause
                    var, should_be_true = unknown_vars[0]
                    required_value = 1 if should_be_true else 0
                    if assignment[var] == -1:
                        assignment[var] = required_value
                        changed = True
                    elif assignment[var] != required_value:
                        return False  # Contradiction
                elif false_count == 3:
                    return False  # All literals are false, clause unsatisfiable
        return True
    
    def backtrack(index):
        if index > n:
            return is_satisfied(assignment)
            
        if assignment[index] != -1:
            return backtrack(index + 1)
        
        # Try setting to 0
        assignment[index] = 0
        if propagate():
            if backtrack(index + 1):
                return True
                
        # Backtrack
        assignment[index] = -1
        
        # Try setting to 1
        assignment[index] = 1
        if propagate():
            if backtrack(index + 1):
                return True
                
        # Backtrack
        assignment[index] = -1
        return False
    
    # Initial propagation
    if not propagate():
        print("NO")
        return
        
    if backtrack(1):
        print("YES")
        result = []
        for i in range(1, n + 1):
            result.append(str(assignment[i]))
        print(" ".join(result))
    else:
        print("NO")

solve()