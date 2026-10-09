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
    
    # If no clauses, any assignment works
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    assignment = [None] * (n + 1)  # 1-indexed, None = unassigned
    
    # Convert literal to (var, value) where value True means ON (1)
    def lit_to_var_val(lit):
        var = abs(lit)
        val = lit > 0
        return var, val
    
    # Check if clause is satisfied under current assignment
    def clause_satisfied(clause):
        for lit in clause:
            var, val = lit_to_var_val(lit)
            if assignment[var] is not None and assignment[var] == val:
                return True
        return False
    
    # Check if clause is violated (all literals false)
    def clause_violated(clause):
        for lit in clause:
            var, val = lit_to_var_val(lit)
            if assignment[var] is None or assignment[var] == val:
                return False
        return True
    
    # Unit propagation: returns False if conflict
    def propagate():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                if clause_satisfied(clause):
                    continue
                # Count unassigned literals
                unassigned = []
                for lit in clause:
                    var, val = lit_to_var_val(lit)
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
    
    # Pure literal elimination: if a variable appears with only one polarity in unresolved clauses, set it
    def pure_literal():
        counts = {}
        for clause in clauses:
            if clause_satisfied(clause):
                continue
            for lit in clause:
                var, val = lit_to_var_val(lit)
                if assignment[var] is None:
                    counts.setdefault(var, set()).add(val)
        for var, vals in counts.items():
            if len(vals) == 1:
                val = vals.pop()
                assignment[var] = val
    
    def backtrack():
        if not propagate():
            return False
        # Check if all clauses satisfied
        all_sat = True
        for clause in clauses:
            if not clause_satisfied(clause):
                all_sat = False
                break
        if all_sat:
            return True
        
        # Choose an unassigned variable
        var = None
        for i in range(1, n+1):
            if assignment[i] is None:
                var = i
                break
        if var is None:
            return True  # all assigned and satisfied
        
        # Try both values
        for val in [True, False]:
            assignment[var] = val
            # Save state for backtracking
            saved = assignment[:]
            if backtrack():
                return True
            assignment[:] = saved
        assignment[var] = None
        return False
    
    if backtrack():
        print("YES")
        # Convert True -> 1, False -> 0
        result = []
        for i in range(1, n+1):
            result.append("1" if assignment[i] else "0")
        print(" ".join(result))
    else:
        print("NO")

if __name__ == "__main__":
    solve()