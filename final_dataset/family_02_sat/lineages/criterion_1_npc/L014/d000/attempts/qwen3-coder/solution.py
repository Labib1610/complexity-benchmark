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
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        l3 = int(data[idx+2])
        idx += 3
        clauses.append((l1, l2, l3))
    
    # We will solve this as a 3-SAT problem.
    # Each station i has a variable x_i where:
    # x_i = True means station i is alkaline (1)
    # x_i = False means station i is acidic (0)
    
    # Each clause is a disjunction of three literals.
    # A literal is either x_i (if positive) or not x_i (if negative).
    
    # We'll use the randomized algorithm (randomized local search) or 
    # a simple brute-force for small n, but since n <= 90, brute-force is infeasible.
    # However, since this is a 3-CNF-SAT, and constraints are small,
    # we can try a randomized approach or backtracking with pruning.
    
    # Let's try a randomized approach: try random assignments and check.
    # But for correctness, let's implement a backtracking solution.
    
    # For n up to 90, even backtracking might be too slow.
    # But given the constraints and that this is a standard 3-SAT,
    # we can model it and solve with a SAT solver approach.
    
    # Let's implement a simple backtracking with unit propagation.
    
    # Let's represent the problem as a 3-SAT instance.
    # Variables: 1 to n (station 1 to n)
    # Literals: positive for alkaline, negative for acidic
    
    # We'll use a recursive backtracking algorithm.
    
    def is_satisfied(clauses, assignment):
        for clause in clauses:
            satisfied = False
            for lit in clause:
                var = abs(lit)
                if var not in assignment:
                    # Variable not assigned yet
                    continue
                val = assignment[var]
                required = lit > 0
                if val == required:
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True
    
    def is_clause_satisfied(clause, assignment):
        for lit in clause:
            var = abs(lit)
            if var not in assignment:
                return None  # Unknown
            val = assignment[var]
            required = lit > 0
            if val == required:
                return True
        return False
    
    def unit_propagate(clauses, assignment):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unknown_literals = []
                satisfied = False
                for lit in clause:
                    var = abs(lit)
                    if var in assignment:
                        val = assignment[var]
                        required = lit > 0
                        if val == required:
                            satisfied = True
                            break
                    else:
                        unknown_literals.append(lit)
                if satisfied:
                    continue
                if len(unknown_literals) == 0:
                    return False  # Conflict
                if len(unknown_literals) == 1:
                    # Unit clause
                    lit = unknown_literals[0]
                    var = abs(lit)
                    required = lit > 0
                    if var in assignment:
                        if assignment[var] != required:
                            return False
                    else:
                        assignment[var] = required
                        changed = True
        return True
    
    def get_unassigned_var(clauses, assignment, n):
        # Pick the first unassigned variable
        for i in range(1, n+1):
            if i not in assignment:
                return i
        return None
    
    def solve(clauses, assignment, n):
        # Unit propagation
        if not unit_propagate(clauses, assignment):
            return False
        
        # Check if all clauses are satisfied
        if is_satisfied(clauses, assignment):
            return True
        
        # Pick an unassigned variable
        var = get_unassigned_var(clauses, assignment, n)
        if var is None:
            return True  # All variables assigned and satisfied
        
        # Try True first
        assignment[var] = True
        if solve(clauses, assignment, n):
            return True
        del assignment[var]
        
        # Try False
        assignment[var] = False
        if solve(clauses, assignment, n):
            return True
        del assignment[var]
        
        return False
    
    assignment = {}
    if solve(clauses, assignment, n):
        print("YES")
        result = []
        for i in range(1, n+1):
            if i in assignment and assignment[i]:
                result.append("1")
            else:
                result.append("0")
        print(" ".join(result))
    else:
        print("NO")

if __name__ == "__main__":
    main()