import sys

input = sys.stdin.readline

n, m = map(int, input().split())
clauses = []
for _ in range(m):
    a, b, c = map(int, input().split())
    clauses.append((a, b, c))

# Assign: 1 for ACTIVE, 0 for STANDBY
# For positive x, we need var[x] = 1; for negative -x, need var[x] = 0

# Use simple backtracking with early pruning
assignment = [None] * (n + 1)

def is_clause_satisfiable(clause, assignment):
    for lit in clause:
        var = abs(lit)
        val = assignment[var]
        if val is not None:
            if lit > 0 and val == 1:
                return True
            if lit < 0 and val == 0:
                return True
    # If any unassigned variable, clause might still be satisfied
    for lit in clause:
        var = abs(lit)
        if assignment[var] is None:
            return True
    # All assigned, check if any matches
    return False

def backtrack(var):
    if var > n:
        # Check all clauses are satisfied
        for clause in clauses:
            sat = False
            for lit in clause:
                val = assignment[abs(lit)]
                if lit > 0 and val == 1:
                    sat = True
                    break
                if lit < 0 and val == 0:
                    sat = True
                    break
            if not sat:
                return False
        return True

    # Try assigning 0 and 1
    for value in (0, 1):
        assignment[var] = value
        # Quick check: all clauses that are fully assigned must be satisfied
        ok = True
        for clause in clauses:
            # Check if clause fully assigned
            fully_assigned = all(assignment[abs(lit)] is not None for lit in clause)
            if fully_assigned:
                if not is_clause_satisfiable(clause, assignment):
                    ok = False
                    break
        if ok:
            if backtrack(var + 1):
                return True
        assignment[var] = None
    return False

if backtrack(1):
    print("YES")
    print(" ".join(str(assignment[i]) for i in range(1, n + 1)))
else:
    print("NO")