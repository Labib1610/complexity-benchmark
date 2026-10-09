import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    clauses = []
    idx = 2
    for _ in range(m):
        c = [int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])]
        idx += 3
        # Remove duplicate literals in the same clause
        c = list(set(c))
        # If clause contains both x and -x, it's trivially satisfied, ignore it
        has_tautology = False
        lit_set = set(c)
        for lit in c:
            if -lit in lit_set:
                has_tautology = True
                break
        if not has_tautology:
            clauses.append(c)
    
    # assign: 1-indexed, None if unassigned, True/False
    assign = [None] * (n + 1)
    
    def unit_propagate(assignment):
        assignment = dict(assignment)
        while True:
            unit_found = False
            for c in clauses:
                unassigned_lits = []
                satisfied = False
                for lit in c:
                    var = abs(lit)
                    val = assignment.get(var, None)
                    if val is not None:
                        if (lit > 0 and val) or (lit < 0 and not val):
                            satisfied = True
                            break
                    else:
                        unassigned_lits.append(lit)
                
                if satisfied:
                    continue
                if len(unassigned_lits) == 0:
                    return None  # Conflict
                if len(unassigned_lits) == 1:
                    unit_lit = unassigned_lits[0]
                    var = abs(unit_lit)
                    val = (unit_lit > 0)
                    if var in assignment:
                        if assignment[var] != val:
                            return None
                    else:
                        assignment[var] = val
                        unit_found = True
            if not unit_found:
                break
        return assignment

    def dpll(assignment):
        assignment = unit_propagate(assignment)
        if assignment is None:
            return None
        
        # Check if all variables assigned
        unassigned_vars = [i for i in range(1, n + 1) if i not in assignment]
        if not unassigned_vars:
            return assignment
        
        # Choose variable: Maximum Occurrences in clauses of Minimum size (MOM's heuristic)
        # or simple frequency of unassigned literals
        counts_pos = {v: 0 for v in unassigned_vars}
        counts_neg = {v: 0 for v in unassigned_vars}
        
        for c in clauses:
            satisfied = False
            unassigned_in_c = []
            for lit in c:
                var = abs(lit)
                val = assignment.get(var, None)
                if val is not None:
                    if (lit > 0 and val) or (lit < 0 and not val):
                        satisfied = True
                        break
                else:
                    unassigned_in_c.append(lit)
            if not satisfied:
                for lit in unassigned_in_c:
                    var = abs(lit)
                    if lit > 0:
                        counts_pos[var] += 1
                    else:
                        counts_neg[var] += 1
                        
        best_var = max(unassigned_vars, key=lambda v: counts_pos[v] + counts_neg[v])
        
        # Prefer the polarity that appears more frequently
        if counts_pos[best_var] >= counts_neg[best_var]:
            branches = [True, False]
        else:
            branches = [False, True]
            
        for val in branches:
            next_assignment = dict(assignment)
            next_assignment[best_var] = val
            res = dpll(next_assignment)
            if res is not None:
                return res
                
        return None

    result = dpll({})
    if result is None:
        print("NO")
    else:
        print("YES")
        ans = []
        for i in range(1, n + 1):
            val = result.get(i, False)
            ans.append("1" if val else "0")
        print(" ".join(ans))

if __name__ == '__main__':
    solve()