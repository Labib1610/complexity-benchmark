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
        # Remove duplicate literals in the same clause
        c = list(set(c))
        # If clause contains both x and -x, it is trivially true, ignore it
        tautology = False
        for lit in c:
            if -lit in c:
                tautology = True
                break
        if not tautology:
            clauses.append(c)

    # DPLL solver
    # assignment: array of size n+1, values: 0 (unassigned), 1 (true), -1 (false)
    # lit > 0: var lit is True (+1)
    # lit < 0: var -lit is False (-1)
    
    # We will use iterative or recursive DPLL with unit propagation.
    
    def get_unit_clause(current_clauses, assign):
        for c in current_clauses:
            unassigned = []
            satisfied = False
            for lit in c:
                var = abs(lit)
                val = assign[var]
                if val != 0:
                    if (lit > 0 and val == 1) or (lit < 0 and val == -1):
                        satisfied = True
                        break
                else:
                    unassigned.append(lit)
            if satisfied:
                continue
            if len(unassigned) == 0:
                return None, False # Conflict
            if len(unassigned) == 1:
                return unassigned[0], True
        return 0, True # No unit clause

    def unit_propagate(current_clauses, assign):
        # returns (success, list_of_assigned_vars)
        trail = []
        while True:
            unit, ok = get_unit_clause(current_clauses, assign)
            if not ok:
                return False, trail
            if unit == 0:
                return True, trail
            var = abs(unit)
            val = 1 if unit > 0 else -1
            if assign[var] != 0 and assign[var] != val:
                return False, trail
            if assign[var] == 0:
                assign[var] = val
                trail.append(var)

    def choose_literal(current_clauses, assign):
        # Jeroslow-Wang 2-sided heuristic
        weights = {}
        for c in current_clauses:
            unassigned = []
            satisfied = False
            for lit in c:
                var = abs(lit)
                val = assign[var]
                if val != 0:
                    if (lit > 0 and val == 1) or (lit < 0 and val == -1):
                        satisfied = True
                        break
                else:
                    unassigned.append(lit)
            if not satisfied:
                w = 2 ** (-len(unassigned))
                for lit in unassigned:
                    weights[lit] = weights.get(lit, 0.0) + w
                    
        if not weights:
            # Pick any unassigned
            for i in range(1, n + 1):
                if assign[i] == 0:
                    return i
            return 0
        
        # Pick lit with max weight, or var with max (J(l) + J(-l))
        best_var = 0
        best_score = -1
        for i in range(1, n + 1):
            if assign[i] == 0:
                pos = weights.get(i, 0.0)
                neg = weights.get(-i, 0.0)
                score = pos + neg
                if score > best_score:
                    best_score = score
                    best_var = i if pos >= neg else -i
        return best_var

    def dpll(assign):
        ok, trail = unit_propagate(clauses, assign)
        if not ok:
            for v in trail:
                assign[v] = 0
            return False
        
        lit = choose_literal(clauses, assign)
        if lit == 0:
            # All assigned and satisfied
            return True
        
        var = abs(lit)
        val = 1 if lit > 0 else -1
        
        # Try best branch first
        assign[var] = val
        if dpll(assign):
            return True
        assign[var] = 0
        
        # Try opposite branch
        assign[var] = -val
        if dpll(assign):
            return True
        assign[var] = 0
        
        for v in trail:
            assign[v] = 0
        return False

    assign = [0] * (n + 1)
    if dpll(assign):
        print("YES")
        res = []
        for i in range(1, n + 1):
            res.append(1 if assign[i] == 1 else 0)
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()