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
        c1 = int(next(it))
        c2 = int(next(it))
        c3 = int(next(it))
        clauses.append((c1, c2, c3))
    
    assignment = [-1] * (n + 1)  # -1 unassigned, 0 or 1 assigned
    
    def check_clause(clause):
        # returns True if clause is satisfied or not yet determined
        satisfied = False
        for c in clause:
            var = abs(c)
            expected = 1 if c > 0 else 0
            if assignment[var] != -1:
                if assignment[var] == expected:
                    satisfied = True
            # if unassigned, clause might still be satisfied later
        if satisfied:
            return True
        # if all variables assigned and none matched, clause fails
        for c in clause:
            if assignment[abs(c)] == -1:
                return True  # still possible
        return False
    
    def backtrack(idx):
        if idx > n:
            return True
        # try both values
        for val in (0, 1):
            assignment[idx] = val
            ok = True
            for clause in clauses:
                if not check_clause(clause):
                    ok = False
                    break
            if ok:
                if backtrack(idx + 1):
                    return True
            assignment[idx] = -1
        return False
    
    if backtrack(1):
        print("YES")
        print(" ".join(str(assignment[i]) for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()