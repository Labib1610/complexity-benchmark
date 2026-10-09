import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m = int(input_data[0]), int(input_data[1])
    clauses = []
    idx = 2
    for _ in range(m):
        l1, l2, l3 = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])
        idx += 3
        clause = []
        for lit in (l1, l2, l3):
            var = abs(lit) - 1
            val = lit > 0
            clause.append((var, val))
        clauses.append(clause)
    
    assignment = [None] * n
    
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
                    return False
                if len(unassigned) == 1:
                    var, val = unassigned[0]
                    if assignment[var] is None:
                        assignment[var] = val
                        changed = True
                    elif assignment[var] != val:
                        return False
        return True
    
    def pure_literal_elimination(clauses, assignment):
        # Find pure literals
        pos_count = {}
        neg_count = {}
        for clause in clauses:
            for var, val in clause:
                if assignment[var] is not None:
                    continue
                if val:
                    pos_count[var] = pos_count.get(var, 0) + 1
                else:
                    neg_count[var] = neg_count.get(var, 0) + 1
        for var in range(n):
            if assignment[var] is not None:
                continue
            p = pos_count.get(var, 0)
            q = neg_count.get(var, 0)
            if p > 0 and q == 0:
                assignment[var] = True
            elif q > 0 and p == 0:
                assignment[var] = False
    
    def dpll(clauses, assignment):
        if not propagate(clauses, assignment):
            return False
        pure_literal_elimination(clauses, assignment)
        # Check if all clauses satisfied
        all_satisfied = True
        for clause in clauses:
            sat = False
            for var, val in clause:
                if assignment[var] == val:
                    sat = True
                    break
            if not sat:
                all_satisfied = False
                break
        if all_satisfied:
            return True
        
        # Choose an unassigned variable
        for var in range(n):
            if assignment[var] is None:
                # Try True
                assignment[var] = True
                if dpll(clauses, assignment):
                    return True
                assignment[var] = False
                if dpll(clauses, assignment):
                    return True
                assignment[var] = None
                return False
        return False
    
    if dpll(clauses, assignment):
        print("YES")
        print(" ".join("1" if v else "0" for v in assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()