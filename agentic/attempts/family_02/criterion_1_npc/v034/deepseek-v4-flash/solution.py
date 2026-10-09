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
        clauses.append([l1, l2, l3])
    
    assignment = [None] * (n + 1)  # 1-indexed, None = unassigned
    
    def check_clause(clause):
        # Check if clause is satisfied, unsatisfied, or undetermined
        satisfied = False
        all_false = True
        for lit in clause:
            var = abs(lit)
            val = assignment[var]
            if val is None:
                all_false = False
            elif (lit > 0 and val == 1) or (lit < 0 and val == 0):
                satisfied = True
                break
        if satisfied:
            return True
        if all_false:
            return False
        return None  # undetermined
    
    def backtrack():
        # Find first unassigned variable
        try:
            var = next(i for i in range(1, n+1) if assignment[i] is None)
        except StopIteration:
            # All assigned, check all clauses
            for clause in clauses:
                if not check_clause(clause):
                    return False
            return True
        
        # Try assigning True (open)
        assignment[var] = 1
        ok = True
        for clause in clauses:
            res = check_clause(clause)
            if res is False:
                ok = False
                break
        if ok and backtrack():
            return True
        assignment[var] = None
        
        # Try assigning False (closed)
        assignment[var] = 0
        ok = True
        for clause in clauses:
            res = check_clause(clause)
            if res is False:
                ok = False
                break
        if ok and backtrack():
            return True
        assignment[var] = None
        return False
    
    if backtrack():
        print("YES")
        print(" ".join(str(assignment[i]) for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()