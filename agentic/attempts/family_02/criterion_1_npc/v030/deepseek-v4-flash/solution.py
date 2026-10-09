import sys
sys.setrecursionlimit(10000000)

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
        # convert to internal representation: variable = abs(val); positive => True
        clauses.append((a, b, c))
    
    # DPLL solver
    assignment = [None] * (n + 1)  # None = unassigned, True/False

    def evaluate_lit(lit, assign):
        var = abs(lit)
        if assign[var] is None:
            return None
        val = assign[var]
        if lit > 0:
            return val
        else:
            return not val

    def simplify_clauses(clauses, assign):
        # returns (new_clauses, conflict)
        new_clauses = []
        for clause in clauses:
            vals = [evaluate_lit(l, assign) for l in clause]
            if any(v is True for v in vals):
                continue  # clause satisfied
            if all(v is False for v in vals):
                return None, True  # conflict
            # otherwise remove false literals
            new_clause = []
            for lit, val in zip(clause, vals):
                if val is None:
                    new_clause.append(lit)
            if len(new_clause) == 0:
                return None, True
            new_clauses.append(new_clause)
        return new_clauses, False

    def dpll(clauses, assign):
        # simplify
        clauses, conflict = simplify_clauses(clauses, assign)
        if conflict:
            return False
        if not clauses:
            return True

        # unit propagation
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unassigned = [lit for lit in clause if assign[abs(lit)] is None]
                if len(unassigned) == 0:
                    continue
                # if only one unassigned, assign to satisfy clause
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val = (lit > 0)
                    assign[var] = val
                    changed = True
                    break  # restart simplification
            if changed:
                clauses, conflict = simplify_clauses(clauses, assign)
                if conflict:
                    return False
                if not clauses:
                    return True

        # choose unassigned variable
        for var in range(1, n+1):
            if assign[var] is None:
                # try True first
                assign[var] = True
                if dpll(clauses, assign):
                    return True
                assign[var] = False
                if dpll(clauses, assign):
                    return True
                assign[var] = None
                return False
        return True  # all assigned

    if dpll(clauses, assignment):
        print("YES")
        print(" ".join("1" if assignment[i] else "0" for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()