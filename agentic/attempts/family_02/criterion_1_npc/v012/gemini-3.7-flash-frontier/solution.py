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
        c_set = set(c)
        if any(-x in c_set for x in c_set):
            continue
        clauses.append(list(c_set))
    
    # DPLL with Jeroslow-Wang heuristic and unit propagation
    assignment = [None] * (n + 1)

    def get_lit_val(lit):
        v = assignment[abs(lit)]
        if v is None:
            return None
        return v if lit > 0 else 1 - v

    def unit_propagate():
        while True:
            unit_found = False
            for c in clauses:
                unassigned_lit = None
                satisfied = False
                unassigned_count = 0
                
                for lit in c:
                    val = get_lit_val(lit)
                    if val == 1:
                        satisfied = True
                        break
                    elif val is None:
                        unassigned_lit = lit
                        unassigned_count += 1
                
                if satisfied:
                    continue
                if unassigned_count == 0:
                    return False, []  # Conflict
                if unassigned_count == 1:
                    # Unit clause
                    var = abs(unassigned_lit)
                    val = 1 if unassigned_lit > 0 else 0
                    if assignment[var] is None:
                        assignment[var] = val
                        trail.append(var)
                        unit_found = True
                    elif assignment[var] != val:
                        return False, []
            if not unit_found:
                break
        return True, []

    def dpll():
        # 1. Unit propagation
        cur_trail = []
        
        while True:
            unit_found = False
            for c in clauses:
                unassigned_lit = None
                satisfied = False
                unassigned_count = 0
                
                for lit in c:
                    val = get_lit_val(lit)
                    if val == 1:
                        satisfied = True
                        break
                    elif val is None:
                        unassigned_lit = lit
                        unassigned_count += 1
                
                if satisfied:
                    continue
                if unassigned_count == 0:
                    for v in cur_trail:
                        assignment[v] = None
                    return False
                if unassigned_count == 1:
                    var = abs(unassigned_lit)
                    val = 1 if unassigned_lit > 0 else 0
                    if assignment[var] is None:
                        assignment[var] = val
                        cur_trail.append(var)
                        unit_found = True
                    elif assignment[var] != val:
                        for v in cur_trail:
                            assignment[v] = None
                        return False
            if not unit_found:
                break

        # Check if all clauses are satisfied
        all_sat = True
        for c in clauses:
            sat = False
            for lit in c:
                if get_lit_val(lit) == 1:
                    sat = True
                    break
            if not sat:
                all_sat = False
                break
        
        if all_sat:
            return True

        # Jeroslow-Wang Heuristic
        jw_pos = [0.0] * (n + 1)
        jw_neg = [0.0] * (n + 1)
        for c in clauses:
            sat = False
            open_lits = []
            for lit in c:
                val = get_lit_val(lit)
                if val == 1:
                    sat = True
                    break
                elif val is None:
                    open_lits.append(lit)
            if not sat:
                weight = 2.0 ** (-len(open_lits))
                for lit in open_lits:
                    if lit > 0:
                        jw_pos[lit] += weight
                    else:
                        jw_neg[-lit] += weight

        best_var = None
        best_score = -1.0
        best_val = 1

        for v in range(1, n + 1):
            if assignment[v] is None:
                score = jw_pos[v] + jw_neg[v]
                if score > best_score:
                    best_score = score
                    best_var = v
                    best_val = 1 if jw_pos[v] >= jw_neg[v] else 0

        if best_var is None:
            return True

        # Try best_val first, then 1 - best_val
        for val in (best_val, 1 - best_val):
            assignment[best_var] = val
            if dpll():
                return True
            assignment[best_var] = None

        for v in cur_trail:
            assignment[v] = None
        return False

    if dpll():
        print("YES")
        res = [str(assignment[i] if assignment[i] is not None else 0) for i in range(1, n + 1)]
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()