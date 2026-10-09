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
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        clauses.append((a, b, c))
    
    # DPLL solver
    assignment = [None] * (n + 1)  # 1-indexed, None = unassigned
    
    def literal_value(lit):
        var = abs(lit)
        if assignment[var] is None:
            return None
        val = assignment[var]
        if lit > 0:
            return val == 1
        else:
            return val == 0
    
    def clause_satisfied(clause):
        for lit in clause:
            v = literal_value(lit)
            if v is True:
                return True
        return False
    
    def clause_unsat(clause):
        for lit in clause:
            v = literal_value(lit)
            if v is None:
                return False
        # all assigned, none true
        return True
    
    def propagate():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unassigned = []
                true_found = False
                for lit in clause:
                    v = literal_value(lit)
                    if v is True:
                        true_found = True
                        break
                    elif v is None:
                        unassigned.append(lit)
                if true_found:
                    continue
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val = 1 if lit > 0 else 0
                    if assignment[var] is not None and assignment[var] != val:
                        return False
                    if assignment[var] is None:
                        assignment[var] = val
                        changed = True
        return True
    
    def backtrack():
        # find first unassigned variable
        for i in range(1, n + 1):
            if assignment[i] is None:
                # try 0 then 1
                for val in (0, 1):
                    assignment[i] = val
                    if propagate():
                        if backtrack():
                            return True
                    assignment[i] = None
                return False
        # all assigned
        return True
    
    if propagate() and backtrack():
        print("YES")
        print(" ".join(str(assignment[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()