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
    
    # Variable assignment: 0 = unassigned, 1 = True, -1 = False
    assignment = [0] * (n + 1)
    
    # Precompute clause literal lists as (var, is_neg)
    clause_lits = []
    for cl in clauses:
        lits = []
        for v in cl:
            var = abs(v)
            neg = v < 0
            lits.append((var, neg))
        clause_lits.append(lits)
    
    # Check if clause is satisfied under current assignment
    def clause_satisfied(lits):
        for var, neg in lits:
            val = assignment[var]
            if val == 0:
                continue
            if (val == 1 and not neg) or (val == -1 and neg):
                return True
        return False
    
    # Check if clause is unsatisfiable (all assigned and none match)
    def clause_conflict(lits):
        for var, neg in lits:
            val = assignment[var]
            if val == 0:
                return False
            if (val == 1 and not neg) or (val == -1 and neg):
                return False
        return True
    
    # Backtracking search
    def backtrack():
        # Find an unassigned variable
        var = -1
        for i in range(1, n+1):
            if assignment[i] == 0:
                var = i
                break
        if var == -1:
            return True  # all assigned, check all clauses
        # Try True then False
        for val in (1, -1):
            assignment[var] = val
            ok = True
            for lits in clause_lits:
                if clause_conflict(lits):
                    ok = False
                    break
            if ok and backtrack():
                return True
            assignment[var] = 0
        return False
    
    if backtrack():
        print("YES")
        print(' '.join('1' if assignment[i] == 1 else '0' for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()