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
        p1 = int(next(it))
        p2 = int(next(it))
        p3 = int(next(it))
        clauses.append((p1, p2, p3))
    
    # assignment: 0 = unassigned, 1 = True (Northern), -1 = False (Southern)
    assignment = [0] * (n + 1)
    
    # Watch literals: for each clause, keep track of unassigned literals
    # We'll implement DPLL with unit propagation.
    
    # Convert literal to (var, value) where value True means var=1
    def lit_to_pair(lit):
        var = abs(lit)
        val = lit > 0
        return var, val
    
    # Check if clause is satisfied under current assignment
    def clause_satisfied(clause):
        for lit in clause:
            var, val = lit_to_pair(lit)
            if assignment[var] != 0:
                if (assignment[var] == 1) == val:
                    return True
        return False
    
    # Check if clause is unsatisfiable (all assigned and none match)
    def clause_conflict(clause):
        all_assigned = True
        for lit in clause:
            var, _ = lit_to_pair(lit)
            if assignment[var] == 0:
                all_assigned = False
                break
        if not all_assigned:
            return False
        return not clause_satisfied(clause)
    
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
                    var, val = lit_to_pair(lit)
                    if assignment[var] == 0:
                        unassigned.append((var, val))
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    var, val = unassigned[0]
                    if assignment[var] == 0:
                        assignment[var] = 1 if val else -1
                        changed = True
        return True
    
    # Backtracking search
    def backtrack():
        if not propagate():
            return False
        # Find an unassigned variable
        var = -1
        for i in range(1, n + 1):
            if assignment[i] == 0:
                var = i
                break
        if var == -1:
            return True  # all assigned and no conflict
        
        # Try both values
        for val in (1, -1):
            assignment[var] = val
            if backtrack():
                return True
            assignment[var] = 0
        return False
    
    if backtrack():
        print("YES")
        print(" ".join("1" if assignment[i] == 1 else "0" for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()