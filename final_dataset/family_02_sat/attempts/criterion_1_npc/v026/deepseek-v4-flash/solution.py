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
    
    # DPLL SAT solver
    assignment = [None] * (n + 1)  # 1-indexed, None = unassigned
    
    def propagate(assign):
        # Returns (new_assign, conflict)
        assign = assign[:]
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                # Check if clause is already satisfied
                satisfied = False
                unassigned_lit = None
                for lit in clause:
                    var = abs(lit)
                    val = assign[var]
                    if val is not None:
                        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                            satisfied = True
                            break
                    else:
                        unassigned_lit = lit
                if satisfied:
                    continue
                if unassigned_lit is None:
                    # All literals assigned and false -> conflict
                    return None, True
                # Only one unassigned literal -> must set it to satisfy clause
                var = abs(unassigned_lit)
                val = 1 if unassigned_lit > 0 else 0
                if assign[var] is not None and assign[var] != val:
                    return None, True
                assign[var] = val
                changed = True
        return assign, False
    
    def dpll(assign):
        assign, conflict = propagate(assign)
        if conflict:
            return None
        # Check if all clauses satisfied
        all_sat = True
        for clause in clauses:
            sat = False
            for lit in clause:
                var = abs(lit)
                val = assign[var]
                if val is not None and ((lit > 0 and val == 1) or (lit < 0 and val == 0)):
                    sat = True
                    break
            if not sat:
                all_sat = False
                break
        if all_sat:
            return assign
        # Choose unassigned variable
        var = None
        for i in range(1, n+1):
            if assign[i] is None:
                var = i
                break
        if var is None:
            return None
        # Try both values
        for val in (0, 1):
            new_assign = assign[:]
            new_assign[var] = val
            result = dpll(new_assign)
            if result is not None:
                return result
        return None
    
    result = dpll(assignment)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(result[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    solve()