import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        clauses.append((l1, l2, l3))
    
    # variable assignment: 1 = True (primary), 0 = False (secondary)
    assignment = [None] * (n + 1)  # None = unassigned
    
    # Convert literal to (var, value) where value True means primary
    def lit_to_varval(lit):
        if lit > 0:
            return lit, True
        else:
            return -lit, False
    
    # Check if clause is satisfied under current assignment
    def clause_satisfied(clause):
        for lit in clause:
            var, val = lit_to_varval(lit)
            if assignment[var] is not None and assignment[var] == val:
                return True
        return False
    
    # Unit propagation: returns False if conflict
    def propagate():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                if clause_satisfied(clause):
                    continue
                unassigned = []
                for lit in clause:
                    var, val = lit_to_varval(lit)
                    if assignment[var] is None:
                        unassigned.append((var, val))
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    var, val = unassigned[0]
                    if assignment[var] is None:
                        assignment[var] = val
                        changed = True
                    elif assignment[var] != val:
                        return False
        return True
    
    # Pure literal elimination
    def pure_literal_elimination():
        changed = False
        for val in [True, False]:
            for var in range(1, n+1):
                if assignment[var] is not None:
                    continue
                appears_pos = False
                appears_neg = False
                for clause in clauses:
                    for lit in clause:
                        v, vv = lit_to_varval(lit)
                        if v == var:
                            if vv == True:
                                appears_pos = True
                            else:
                                appears_neg = True
                if appears_pos and not appears_neg:
                    assignment[var] = True
                    changed = True
                elif appears_neg and not appears_pos:
                    assignment[var] = False
                    changed = True
        return changed
    
    # Backtracking search
    def backtrack():
        # Propagate and pure literal
        if not propagate():
            return False
        while pure_literal_elimination():
            if not propagate():
                return False
        
        # Find unassigned variable
        var = None
        for i in range(1, n+1):
            if assignment[i] is None:
                var = i
                break
        if var is None:
            return True  # all assigned
        
        # Try both values
        for val in [True, False]:
            assignment[var] = val
            saved = assignment[:]
            if backtrack():
                return True
            assignment[:] = saved
        assignment[var] = None
        return False
    
    if backtrack():
        print("YES")
        print(" ".join('1' if assignment[i] else '0' for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()