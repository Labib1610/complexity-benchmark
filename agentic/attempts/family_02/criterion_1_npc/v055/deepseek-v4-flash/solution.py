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
    
    def propagate(clauses, assignment):
        # Returns (new_clauses, conflict)
        changed = True
        while changed:
            changed = False
            new_clauses = []
            for clause in clauses:
                # Check if clause is already satisfied
                satisfied = False
                remaining = []
                for lit in clause:
                    var = abs(lit)
                    val = assignment[var]
                    if val is not None:
                        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                            satisfied = True
                            break
                        # else literal is false, skip it
                    else:
                        remaining.append(lit)
                if satisfied:
                    continue
                if not remaining:
                    return None, True  # conflict
                if len(remaining) == 1:
                    # unit clause
                    lit = remaining[0]
                    var = abs(lit)
                    val = 1 if lit > 0 else 0
                    if assignment[var] is not None and assignment[var] != val:
                        return None, True
                    assignment[var] = val
                    changed = True
                else:
                    new_clauses.append(remaining)
            clauses = new_clauses
        return clauses, False
    
    def backtrack(clauses, assignment):
        clauses, conflict = propagate(clauses, assignment)
        if conflict:
            return False
        # Check if all clauses satisfied
        if not clauses:
            return True
        # Choose an unassigned variable
        for i in range(1, n + 1):
            if assignment[i] is None:
                var = i
                break
        else:
            return True  # all assigned and no conflict
        
        # Try var = 1
        assignment[var] = 1
        if backtrack([list(c) for c in clauses], assignment):
            return True
        assignment[var] = 0
        if backtrack([list(c) for c in clauses], assignment):
            return True
        assignment[var] = None
        return False
    
    if backtrack(clauses, assignment):
        print("YES")
        print(" ".join(str(1 if assignment[i] == 1 else 0) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()