import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    clauses = []
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx+1])
        l3 = int(input_data[idx+2])
        idx += 3
        clauses.append((l1, l2, l3))
    
    # We'll use a simple DPLL-like backtracking
    assignment = [None] * (n + 1)  # 1-indexed, None = unassigned
    
    def evaluate_literal(lit, assignment):
        var = abs(lit)
        val = assignment[var]
        if val is None:
            return None
        if lit > 0:
            return val == 1
        else:
            return val == 0
    
    def clause_satisfied(clause, assignment):
        for lit in clause:
            res = evaluate_literal(lit, assignment)
            if res is True:
                return True
        return False
    
    def clause_unsat(clause, assignment):
        # returns True if all literals are assigned and false
        all_assigned = True
        for lit in clause:
            var = abs(lit)
            if assignment[var] is None:
                all_assigned = False
                break
        if all_assigned:
            return not clause_satisfied(clause, assignment)
        return False
    
    def unit_clause(clause, assignment):
        # returns (var, value) if clause is unit, else None
        unassigned = []
        for lit in clause:
            var = abs(lit)
            if assignment[var] is None:
                unassigned.append(lit)
        if len(unassigned) == 1:
            lit = unassigned[0]
            var = abs(lit)
            val = 1 if lit > 0 else 0
            return (var, val)
        return None
    
    def propagate(assignment, clauses):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                if clause_satisfied(clause, assignment):
                    continue
                if clause_unsat(clause, assignment):
                    return False
                unit = unit_clause(clause, assignment)
                if unit is not None:
                    var, val = unit
                    if assignment[var] is None:
                        assignment[var] = val
                        changed = True
                    elif assignment[var] != val:
                        return False
        return True
    
    def backtrack(assignment, clauses):
        # propagate
        if not propagate(assignment, clauses):
            return False
        # find unassigned variable
        var = None
        for i in range(1, n+1):
            if assignment[i] is None:
                var = i
                break
        if var is None:
            return True  # all assigned
        # try both values
        for val in (0, 1):
            assignment[var] = val
            if backtrack(assignment, clauses):
                return True
            assignment[var] = None
        return False
    
    if backtrack(assignment, clauses):
        print("YES")
        print(" ".join(str(assignment[i]) for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()