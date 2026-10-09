import sys

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
        # Remove duplicate literals in clause
        c = list(set(c))
        # If clause contains both x and -x, it's always satisfied, can be ignored
        has_tautology = False
        for lit in c:
            if -lit in c:
                has_tautology = True
                break
        if not has_tautology:
            clauses.append(c)

    # DPLL solver
    # assignment: array of size n + 1, values: None (unassigned), True, False
    assignment = [None] * (n + 1)

    def unit_propagate(clauses, assignment):
        assignment = list(assignment)
        while True:
            unit_found = False
            for c in clauses:
                unassigned_lits = []
                satisfied = False
                for lit in c:
                    var = abs(lit)
                    val = assignment[var]
                    if val is not None:
                        if (lit > 0 and val) or (lit < 0 and not val):
                            satisfied = True
                            break
                    else:
                        unassigned_lits.append(lit)
                if satisfied:
                    continue
                if len(unassigned_lits) == 0:
                    return None, False  # Conflict
                if len(unassigned_lits) == 1:
                    lit = unassigned_lits[0]
                    var = abs(lit)
                    val = lit > 0
                    assignment[var] = val
                    unit_found = True
            if not unit_found:
                break
        return assignment, True

    def choose_variable(clauses, assignment):
        # Count occurrences of unassigned variables
        counts = {}
        for c in clauses:
            satisfied = False
            unassigned_in_c = []
            for lit in c:
                var = abs(lit)
                val = assignment[var]
                if val is not None:
                    if (lit > 0 and val) or (lit < 0 and not val):
                        satisfied = True
                        break
                else:
                    unassigned_in_c.append(lit)
            if not satisfied:
                for lit in unassigned_in_c:
                    var = abs(lit)
                    counts[var] = counts.get(var, 0) + 1
        if not counts:
            for i in range(1, n + 1):
                if assignment[i] is None:
                    return i
            return None
        return max(counts, key=counts.get)

    def dpll(clauses, assignment):
        assignment, ok = unit_propagate(clauses, assignment)
        if not ok:
            return None
        
        # Check if all satisfied or find variable
        var = choose_variable(clauses, assignment)
        if var is None:
            return assignment

        # Try True then False (or heuristic based on positive/negative counts)
        for val in [True, False]:
            assignment[var] = val
            res = dpll(clauses, assignment)
            if res is not None:
                return res
            assignment[var] = None

        return None

    # Initial run
    res = dpll(clauses, assignment)
    if res is None:
        print("NO")
    else:
        print("YES")
        out = []
        for i in range(1, n + 1):
            val = res[i]
            if val is None or val is True:
                out.append("1")
            else:
                out.append("0")
        print(" ".join(out))

if __name__ == '__main__':
    solve()