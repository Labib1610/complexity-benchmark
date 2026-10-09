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
        # Simplify clause: remove duplicate literals
        # If contains both x and -x, clause is always satisfied, can be ignored
        c_set = set(c)
        tautology = False
        for lit in c_set:
            if -lit in c_set:
                tautology = True
                break
        if not tautology:
            clauses.append(list(c_set))
            
    assignment = [0] * (n + 1)  # 0: unassigned, 1: True, -1: False
    
    def unit_propagate(assign):
        while True:
            unit_found = False
            for c in clauses:
                unassigned_lits = []
                satisfied = False
                for lit in c:
                    var = abs(lit)
                    sign = 1 if lit > 0 else -1
                    if assign[var] == sign:
                        satisfied = True
                        break
                    elif assign[var] == 0:
                        unassigned_lits.append(lit)
                
                if satisfied:
                    continue
                if len(unassigned_lits) == 0:
                    return False, []
                if len(unassigned_lits) == 1:
                    lit = unassigned_lits[0]
                    var = abs(lit)
                    sign = 1 if lit > 0 else -1
                    assign[var] = sign
                    unit_found = True
                    # Record newly assigned to handle backtrack if needed, but since we can copy, simple is fine.
            if not unit_found:
                break
        return True, assign

    def dpll(assign):
        # Count literal frequencies among unsatisfied clauses
        counts = {}
        all_satisfied = True
        
        for c in clauses:
            satisfied = False
            unassigned_in_c = []
            for lit in c:
                var = abs(lit)
                sign = 1 if lit > 0 else -1
                if assign[var] == sign:
                    satisfied = True
                    break
                elif assign[var] == 0:
                    unassigned_in_c.append(lit)
            if not satisfied:
                all_satisfied = False
                if len(unassigned_in_c) == 0:
                    return False, None
                for lit in unassigned_in_c:
                    counts[lit] = counts.get(lit, 0) + 1

        if all_satisfied:
            return True, assign

        # Choose literal with maximum count in unsatisfied clauses (DLIS heuristic)
        best_lit = max(counts.keys(), key=lambda l: counts[l])
        best_var = abs(best_lit)
        best_sign = 1 if best_lit > 0 else -1
        
        # Branch 1: try best_sign
        for sign in (best_sign, -best_sign):
            new_assign = list(assign)
            new_assign[best_var] = sign
            ok, prop_assign = unit_propagate(new_assign)
            if ok:
                res, final_assign = dpll(prop_assign)
                if res:
                    return True, final_assign
                    
        return False, None

    # Initial unit propagation
    init_assign = [0] * (n + 1)
    ok, init_assign = unit_propagate(init_assign)
    if not ok:
        print("NO")
        return
        
    sat, final_assign = dpll(init_assign)
    if sat:
        print("YES")
        res = []
        for i in range(1, n + 1):
            if final_assign[i] == 1:
                res.append("1")
            else:
                res.append("0")
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()