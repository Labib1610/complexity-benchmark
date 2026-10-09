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
    
    # Convert to 0-indexed variables: positive x -> (x-1), negative -x -> ~(x-1)
    # We'll store as list of literals: (var, is_true)
    cnf = []
    for clause in clauses:
        lits = []
        for lit in clause:
            if lit > 0:
                lits.append((lit - 1, True))
            else:
                lits.append((-lit - 1, False))
        cnf.append(lits)
    
    assignment = [None] * n
    
    # Unit propagation and pure literal elimination can be added, but simple backtracking is enough for these limits.
    def backtrack():
        # Find an unassigned variable
        for var in range(n):
            if assignment[var] is None:
                break
        else:
            # All assigned, check all clauses
            for clause in cnf:
                satisfied = False
                for v, val in clause:
                    if assignment[v] == val:
                        satisfied = True
                        break
                if not satisfied:
                    return False
            return True
        
        # Try both values
        for val in (True, False):
            assignment[var] = val
            # Quick check: any clause already falsified?
            ok = True
            for clause in cnf:
                sat = False
                falsified = True
                for v, need in clause:
                    if assignment[v] is None:
                        falsified = False
                    elif assignment[v] == need:
                        sat = True
                        break
                if not sat and falsified:
                    ok = False
                    break
            if ok:
                if backtrack():
                    return True
            assignment[var] = None
        return False
    
    if backtrack():
        print("YES")
        print(" ".join('1' if assignment[i] else '0' for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()