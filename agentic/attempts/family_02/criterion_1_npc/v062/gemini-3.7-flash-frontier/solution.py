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
        clauses.append(c)
        
    assignment = [None] * (n + 1)
    
    def get_lit_val(lit):
        var = abs(lit)
        val = assignment[var]
        if val is None:
            return None
        return (val == 1) if lit > 0 else (val == 0)

    def unit_propagate():
        while True:
            unit_found = False
            for c in clauses:
                unassigned_lit = None
                num_unassigned = 0
                is_sat = False
                for lit in c:
                    val = get_lit_val(lit)
                    if val is True:
                        is_sat = True
                        break
                    elif val is None:
                        num_unassigned += 1
                        unassigned_lit = lit
                if is_sat:
                    continue
                if num_unassigned == 0:
                    return False
                if num_unassigned == 1:
                    var = abs(unassigned_lit)
                    val = 1 if unassigned_lit > 0 else 0
                    if assignment[var] is None:
                        assignment[var] = val
                        unit_found = True
                    elif assignment[var] != val:
                        return False
            if not unit_found:
                break
        return True

    def dpll():
        saved_assignment = list(assignment)
        if not unit_propagate():
            assignment[:] = saved_assignment
            return False
        
        # Check if all clauses are satisfied
        all_sat = True
        for c in clauses:
            sat = False
            for lit in c:
                if get_lit_val(lit) is True:
                    sat = True
                    break
            if not sat:
                all_sat = False
                break
        
        if all_sat:
            return True
        
        # Choose next variable: DLCS heuristic (Dynamic Largest Combined Sum)
        pos_count = [0] * (n + 1)
        neg_count = [0] * (n + 1)
        for c in clauses:
            sat = False
            for lit in c:
                if get_lit_val(lit) is True:
                    sat = True
                    break
            if not sat:
                for lit in c:
                    if assignment[abs(lit)] is None:
                        if lit > 0:
                            pos_count[lit] += 1
                        else:
                            neg_count[-lit] += 1
                            
        best_var = None
        best_score = -1
        preferred_val = 1
        for var in range(1, n + 1):
            if assignment[var] is None:
                score = pos_count[var] + neg_count[var]
                if score > best_score:
                    best_score = score
                    best_var = var
                    preferred_val = 1 if pos_count[var] >= neg_count[var] else 0
                    
        if best_var is None:
            # All variables assigned
            return True

        # Try preferred value first
        for val in (preferred_val, 1 - preferred_val):
            assignment[best_var] = val
            if dpll():
                return True
            assignment[:] = saved_assignment

        return False

    if dpll():
        print("YES")
        res = [str(assignment[i] if assignment[i] is not None else 0) for i in range(1, n + 1)]
        print(" ".join(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()