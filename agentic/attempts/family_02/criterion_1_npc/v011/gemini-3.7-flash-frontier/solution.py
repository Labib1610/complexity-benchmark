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
        # Remove duplicate literals in the clause
        c = list(set(c))
        # If clause contains both x and -x, it's always satisfied, so we can ignore it
        has_tautology = False
        for lit in c:
            if -lit in c:
                has_tautology = True
                break
        if not has_tautology:
            clauses.append(c)

    def unit_propagate(clauses, assignment):
        while True:
            unit_clauses = [c for c in clauses if len(c) == 1]
            if not unit_clauses:
                break
            unit = unit_clauses[0][0]
            var = abs(unit)
            val = 1 if unit > 0 else 0
            if var in assignment:
                if assignment[var] != val:
                    return None, None
            else:
                assignment[var] = val
            
            new_clauses = []
            for c in clauses:
                if unit in c:
                    continue
                if -unit in c:
                    new_c = [l for l in c if l != -unit]
                    if not new_c:
                        return None, None
                    new_clauses.append(new_c)
                else:
                    new_clauses.append(c)
            clauses = new_clauses
        return clauses, assignment

    def dpll(clauses, assignment):
        clauses, assignment = unit_propagate(clauses, assignment.copy())
        if clauses is None:
            return None
        if not clauses:
            return assignment

        # Jeroslow-Wang heuristic
        jw = {}
        for c in clauses:
            weight = 2 ** (-len(c))
            for lit in c:
                jw[lit] = jw.get(lit, 0.0) + weight

        best_var = None
        best_score = -1.0
        for var in range(1, n + 1):
            if var not in assignment:
                score = jw.get(var, 0.0) + jw.get(-var, 0.0)
                if score > best_score:
                    best_score = score
                    best_var = var

        if best_var is None:
            return assignment

        # Try the literal with higher JW weight first
        pos_weight = jw.get(best_var, 0.0)
        neg_weight = jw.get(-best_var, 0.0)
        first_lit = best_var if pos_weight >= neg_weight else -best_var

        for lit in [first_lit, -first_lit]:
            res = dpll(clauses + [[lit]], assignment)
            if res is not None:
                return res

        return None

    # Check for empty clauses initially
    for c in clauses:
        if len(c) == 0:
            print("NO")
            return

    res = dpll(clauses, {})
    if res is None:
        print("NO")
    else:
        print("YES")
        ans = [str(res.get(i, 0)) for i in range(1, n + 1)]
        print(" ".join(ans))

if __name__ == '__main__':
    solve()