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
        clause = []
        for lit in (l1, l2, l3):
            var = abs(lit) - 1
            val = 1 if lit > 0 else 0
            clause.append((var, val))
        clauses.append(clause)
    
    assignment = [None] * n
    
    # DPLL with unit propagation
    def propagate(clauses, assignment):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unassigned = []
                satisfied = False
                for var, val in clause:
                    if assignment[var] is None:
                        unassigned.append((var, val))
                    elif assignment[var] == val:
                        satisfied = True
                        break
                if satisfied:
                    continue
                if not unassigned:
                    return False  # conflict
                if len(unassigned) == 1:
                    var, val = unassigned[0]
                    if assignment[var] is None:
                        assignment[var] = val
                        changed = True
                    elif assignment[var] != val:
                        return False
        return True
    
    def dpll(clauses, assignment):
        if not propagate(clauses, assignment):
            return False
        # Check if all clauses satisfied
        all_sat = True
        for clause in clauses:
            sat = False
            for var, val in clause:
                if assignment[var] == val:
                    sat = True
                    break
            if not sat:
                all_sat = False
                break
        if all_sat:
            return True
        
        # Choose an unassigned variable
        for i in range(n):
            if assignment[i] is None:
                # Try True
                assignment[i] = 1
                if dpll(clauses, assignment):
                    return True
                assignment[i] = 0
                if dpll(clauses, assignment):
                    return True
                assignment[i] = None
                return False
        return False
    
    if dpll(clauses, assignment):
        print("YES")
        print(" ".join(str(1 if x else 0) for x in assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()