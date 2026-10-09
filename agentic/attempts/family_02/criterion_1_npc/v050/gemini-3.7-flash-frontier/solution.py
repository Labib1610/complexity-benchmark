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
        w1 = int(input_data[idx])
        w2 = int(input_data[idx+1])
        w3 = int(input_data[idx+2])
        idx += 3
        clauses.append((w1, w2, w3))

    # assignment: 1-indexed, None / True / False
    assign = [None] * (n + 1)
    
    def unit_propagate():
        while True:
            unit_found = False
            for clause in clauses:
                val_true = False
                unassigned = []
                for lit in clause:
                    var = abs(lit)
                    val = assign[var]
                    if val is not None:
                        if (lit > 0 and val) or (lit < 0 and not val):
                            val_true = True
                            break
                    else:
                        unassigned.append(lit)
                
                if val_true:
                    continue
                if len(unassigned) == 0:
                    return False, []  # Conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    assign[var] = (lit > 0)
                    yield_assigned.append(var)
                    unit_found = True
            if not unit_found:
                break
        return True, yield_assigned

    def dpll():
        # Unit propagation
        units = []
        while True:
            unit_found = False
            for clause in clauses:
                val_true = False
                unassigned = []
                for lit in clause:
                    var = abs(lit)
                    val = assign[var]
                    if val is not None:
                        if (lit > 0 and val) or (lit < 0 and not val):
                            val_true = True
                            break
                    else:
                        unassigned.append(lit)
                
                if val_true:
                    continue
                if len(unassigned) == 0:
                    # backtrack units
                    for v in units:
                        assign[v] = None
                    return False
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    assign[var] = (lit > 0)
                    units.append(var)
                    unit_found = True
            if not unit_found:
                break

        # Check if all satisfied / find next branch variable
        # Heuristic: pick variable that appears most in unsatisfied clauses
        counts_pos = [0] * (n + 1)
        counts_neg = [0] * (n + 1)
        unresolved_clauses = 0

        for clause in clauses:
            val_true = False
            for lit in clause:
                var = abs(lit)
                val = assign[var]
                if val is not None:
                    if (lit > 0 and val) or (lit < 0 and not val):
                        val_true = True
                        break
            if not val_true:
                unresolved_clauses += 1
                for lit in clause:
                    var = abs(lit)
                    if assign[var] is None:
                        if lit > 0:
                            counts_pos[var] += 1
                        else:
                            counts_neg[var] += 1

        if unresolved_clauses == 0:
            return True

        best_var = -1
        max_c = -1
        for i in range(1, n + 1):
            if assign[i] is None:
                c = counts_pos[i] + counts_neg[i]
                if c > max_c:
                    max_c = c
                    best_var = i

        if best_var == -1:
            return True

        first_choice = counts_pos[best_var] >= counts_neg[best_var]

        for choice in (first_choice, not first_choice):
            assign[best_var] = choice
            if dpll():
                return True
            assign[best_var] = None

        for v in units:
            assign[v] = None
        return False

    if dpll():
        print("YES")
        res = []
        for i in range(1, n + 1):
            res.append(1 if assign[i] else 0)
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()