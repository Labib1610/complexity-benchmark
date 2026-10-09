import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    clauses = []
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx+1])
        l3 = int(input_data[idx+2])
        idx += 3
        clauses.append((l1, l2, l3))
    
    assignment = [None] * (n + 1)  # None = unassigned, True/False = value
    
    # Precompute clause variable indices for quick checks
    clause_vars = []
    for clause in clauses:
        vars_in_clause = set()
        for lit in clause:
            vars_in_clause.add(abs(lit))
        clause_vars.append(vars_in_clause)
    
    def is_clause_satisfied(clause, assignment):
        for lit in clause:
            var = abs(lit)
            val = assignment[var]
            if val is not None:
                if lit > 0 and val:
                    return True
                if lit < 0 and not val:
                    return True
        return False
    
    def backtrack(var_idx):
        if var_idx > n:
            # Check all clauses
            for clause in clauses:
                if not is_clause_satisfied(clause, assignment):
                    return False
            return True
        
        # Try both values
        for val in (True, False):
            assignment[var_idx] = val
            # Check if any clause is now definitely unsatisfiable
            possible = True
            for i, clause in enumerate(clauses):
                if var_idx in clause_vars[i]:
                    # If all variables in clause are assigned and none satisfied
                    all_assigned = True
                    satisfied = False
                    for lit in clause:
                        v = abs(lit)
                        if assignment[v] is None:
                            all_assigned = False
                            break
                        if (lit > 0 and assignment[v]) or (lit < 0 and not assignment[v]):
                            satisfied = True
                            break
                    if all_assigned and not satisfied:
                        possible = False
                        break
            if possible:
                if backtrack(var_idx + 1):
                    return True
            assignment[var_idx] = None
        return False
    
    if backtrack(1):
        print("YES")
        print(" ".join("1" if assignment[i] else "0" for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()