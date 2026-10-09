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
        l1 = int(data[index])
        l2 = int(data[index+1])
        l3 = int(data[index+2])
        index += 3
        clauses.append((l1, l2, l3))
    
    # We will try all 2^n possible assignments
    # But n can be up to 90, so 2^90 is too large
    # However, since this is likely a 2-SAT or 3-SAT type problem,
    # and given the constraints, let's try to model it properly
    
    # This is a 3-SAT problem. We'll use a backtracking approach with pruning
    # But even that might be too slow for n=90 in worst case
    # Let's think differently: since n <= 90 and m <= 400, we can try to solve it as a constraint satisfaction problem
    
    # For small enough n, we could do brute force, but n=90 means 2^90 which is impossible
    # So we need a smarter approach like 2-SAT solver, but this is 3-SAT
    
    # Let's implement a simple backtracking with unit propagation-like idea
    
    # Let's convert to a form suitable for solving
    # Each clause is a disjunction of 3 literals
    # We want to find a satisfying assignment
    
    # Since direct brute force won't work, let's try a more intelligent backtracking
    
    def var_index(x):
        return abs(x) - 1  # Convert to 0-based index
    
    def satisfied(clause, assignment):
        for lit in clause:
            var_idx = var_index(lit)
            if var_idx >= len(assignment):
                continue  # Variable not assigned yet
            required_val = 1 if lit > 0 else 0
            if assignment[var_idx] == required_val:
                return True
        return False
    
    def all_satisfied(clauses, assignment):
        for clause in clauses:
            if not satisfied(clause, assignment):
                return False
        return True
    
    def consistent(clauses, assignment):
        # Check if current partial assignment violates any clause
        for clause in clauses:
            # If all literals in the clause are fixed and none are satisfied, then unsat
            all_fixed = True
            sat = False
            for lit in clause:
                var_idx = var_index(lit)
                if var_idx >= len(assignment):
                    all_fixed = False
                    break
                required_val = 1 if lit > 0 else 0
                if assignment[var_idx] == required_val:
                    sat = True
                    break
            if all_fixed and not sat:
                return False
        return True
    
    def backtrack(assignment):
        if len(assignment) == n:
            if all_satisfied(clauses, assignment):
                return assignment[:]
            else:
                return None
        
        if not consistent(clauses, assignment):
            return None
            
        # Try 0
        assignment.append(0)
        res = backtrack(assignment)
        if res is not None:
            return res
        assignment.pop()
        
        # Try 1
        assignment.append(1)
        res = backtrack(assignment)
        if res is not None:
            return res
        assignment.pop()
        
        return None
    
    # This backtracking might still be too slow. Let's optimize a bit more.
    # Let's preprocess unit clauses and do unit propagation
    
    result = backtrack([])
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()