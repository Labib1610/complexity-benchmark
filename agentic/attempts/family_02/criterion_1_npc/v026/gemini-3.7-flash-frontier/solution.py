import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    idx = 2
    raw_clauses = []
    for _ in range(m):
        c = [int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])]
        idx += 3
        
        # Simplify clause
        tautology = False
        simplified = []
        for lit in c:
            if -lit in simplified:
                tautology = True
                break
            if lit not in simplified:
                simplified.append(lit)
        if not tautology:
            raw_clauses.append(simplified)
            
    # Check for empty clauses
    for c in raw_clauses:
        if len(c) == 0:
            print("NO")
            return

    clauses = raw_clauses
    
    # 2-Watched Literals DPLL
    # Variable values: -1 = unassigned, 0 = False, 1 = True
    val = [-1] * (n + 1)
    
    # watches[lit_idx] -> list of clause indices
    # Lit encoding: lit > 0 -> 2 * lit, lit < 0 -> 2 * (-lit) + 1
    def lit_to_idx(l):
        return 2 * l if l > 0 else 2 * (-l) + 1
    
    def lit_val(l):
        v = val[abs(l)]
        if v == -1:
            return -1
        return 1 if (v == 1 if l > 0 else v == 0) else 0

    watch = [[] for _ in range(2 * n + 2)]
    clause_list = []
    
    for c in clauses:
        clause_list.append(list(c))
        c_idx = len(clause_list) - 1
        if len(c) >= 2:
            watch[lit_to_idx(c[0])].append(c_idx)
            watch[lit_to_idx(c[1])].append(c_idx)
        else:
            watch[lit_to_idx(c[0])].append(c_idx)

    trail = []
    
    def assign(lit):
        var = abs(lit)
        v = 1 if lit > 0 else 0
        if val[var] != -1:
            return val[var] == v
        val[var] = v
        trail.append(var)
        return True

    def bcp(trail_start):
        p = trail_start
        while p < len(trail):
            var = trail[p]
            p += 1
            # The literal that became FALSE:
            # If val[var] == 1, then -var is False, so lit_to_idx(-var) is false_lit_idx
            false_lit = -var if val[var] == 1 else var
            false_idx = lit_to_idx(false_lit)
            
            i = 0
            watch_list = watch[false_idx]
            while i < len(watch_list):
                c_idx = watch_list[i]
                c = clause_list[c_idx]
                
                if len(c) == 1:
                    # 1-literal clause where the only literal became false -> conflict
                    return False
                
                # Ensure false_lit is at c[0]
                if c[1] == false_lit:
                    c[0], c[1] = c[1], c[0]
                
                # If the other watched literal is satisfied, clause is satisfied
                other_lit = c[1]
                if lit_val(other_lit) == 1:
                    i += 1
                    continue
                
                # Look for a replacement watch
                found = False
                for k in range(2, len(c)):
                    if lit_val(c[k]) != 0:
                        c[0], c[k] = c[k], c[0]
                        watch[lit_to_idx(c[0])].append(c_idx)
                        watch_list[i] = watch_list[-1]
                        watch_list.pop()
                        found = True
                        break
                
                if not found:
                    # No replacement found. c[1] must be satisfied.
                    v = lit_val(other_lit)
                    if v == 0:
                        return False # Conflict
                    if v == -1:
                        if not assign(other_lit):
                            return False
                    i += 1
        return True

    # Pre-assign unit clauses
    for c in clause_list:
        if len(c) == 1:
            if not assign(c[0]):
                print("NO")
                return
            
    if not bcp(0):
        print("NO")
        return

    def dpll():
        # Heuristic: Jeroslow-Wang or Mom's
        # Find unassigned variable with highest weight
        best_var = -1
        best_score = -1
        best_val = 1
        
        counts_pos = [0.0] * (n + 1)
        counts_neg = [0.0] * (n + 1)
        
        for c in clause_list:
            sat = False
            unassigned_count = 0
            for lit in c:
                lv = lit_val(lit)
                if lv == 1:
                    sat = True
                    break
                elif lv == -1:
                    unassigned_count += 1
            if not sat and unassigned_count > 0:
                weight = 2.0 ** (-unassigned_count)
                for lit in c:
                    if lit_val(lit) == -1:
                        if lit > 0:
                            counts_pos[lit] += weight
                        else:
                            counts_neg[-lit] += weight

        for var in range(1, n + 1):
            if val[var] == -1:
                score = counts_pos[var] + counts_neg[var]
                if score > best_score:
                    best_score = score
                    best_var = var
                    best_val = 1 if counts_pos[var] >= counts_neg[var] else 0

        if best_var == -1:
            return True

        # Try best_val first, then 1 - best_val
        for branch_val in (best_val, 1 - best_val):
            trail_len = len(trail)
            lit = best_var if branch_val == 1 else -best_var
            if assign(lit) and bcp(trail_len):
                if dpll():
                    return True
            # Backtrack
            while len(trail) > trail_len:
                v = trail.pop()
                val[v] = -1

        return False

    if dpll():
        print("YES")
        res = [str(val[i] if val[i] != -1 else 0) for i in range(1, n + 1)]
        print(" ".join(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()