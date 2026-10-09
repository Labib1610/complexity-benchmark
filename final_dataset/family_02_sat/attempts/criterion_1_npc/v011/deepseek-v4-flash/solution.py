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
    
    assignment = [-1] * n  # -1 = unassigned, 0/1 = assigned
    
    # Precompute clause status: for each clause, count unassigned and satisfied
    # We'll just check on the fly.
    
    def check_clause(clause, assignment):
        # returns True if clause is satisfied, False if violated
        for lit in clause:
            var = abs(lit) - 1
            val = assignment[var]
            if val == -1:
                continue
            if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                return True
        # If all assigned and none satisfied -> violated
        for lit in clause:
            if assignment[abs(lit)-1] == -1:
                return True  # still possible
        return False
    
    def backtrack(pos):
        if pos == n:
            # check all clauses
            for clause in clauses:
                if not check_clause(clause, assignment):
                    return False
            return True
        # Try both values
        for val in (0, 1):
            assignment[pos] = val
            # quick check: any clause already violated?
            ok = True
            for clause in clauses:
                if not check_clause(clause, assignment):
                    ok = False
                    break
            if ok and backtrack(pos + 1):
                return True
            assignment[pos] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(assignment[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()