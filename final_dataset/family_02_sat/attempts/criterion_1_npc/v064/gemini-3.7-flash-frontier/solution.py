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
        # If clause contains both x and -x, it's trivially true and can be ignored
        c_set = set(c)
        tautology = False
        for lit in c_set:
            if -lit in c_set:
                tautology = True
                break
        if not tautology:
            clauses.append(list(c_set))
            
    assignment = {}  # var -> bool (1 to n)

    def get_unit_clauses(cur_clauses):
        units = []
        for c in cur_clauses:
            if len(c) == 1:
                units.append(c[0])
        return units

    def simplify(cur_clauses, lit):
        # lit is set to True
        new_clauses = []
        for c in cur_clauses:
            if lit in c:
                continue  # clause is satisfied
            if -lit in c:
                new_c = [x for x in c if x != -lit]
                if not new_c:
                    return None  # empty clause -> contradiction
                new_clauses.append(new_c)
            else:
                new_clauses.append(c)
        return new_clauses

    def dpll(cur_clauses, cur_assignment):
        # Unit propagation
        while True:
            unit = None
            for c in cur_clauses:
                if len(c) == 1:
                    unit = c[0]
                    break
            if unit is None:
                break
            
            var = abs(unit)
            val = True if unit > 0 else False
            cur_assignment[var] = val
            cur_clauses = simplify(cur_clauses, unit)
            if cur_clauses is None:
                return None

        if not cur_clauses:
            return cur_assignment

        # Choose a variable using heuristic: most frequent literal
        counts = {}
        for c in cur_clauses:
            for lit in c:
                counts[lit] = counts.get(lit, 0) + 1

        best_lit = max(counts, key=counts.get)
        best_var = abs(best_lit)

        # Try best_lit first
        for lit in [best_lit, -best_lit]:
            var = abs(lit)
            val = True if lit > 0 else False
            
            next_clauses = simplify(cur_clauses, lit)
            if next_clauses is not None:
                next_assignment = cur_assignment.copy()
                next_assignment[var] = val
                res = dpll(next_clauses, next_assignment)
                if res is not None:
                    return res

        return None

    res = dpll(clauses, {})
    if res is None:
        print("NO")
    else:
        print("YES")
        ans = []
        for i in range(1, n + 1):
            val = res.get(i, False)
            ans.append(1 if val else 0)
        print(*(ans))

if __name__ == '__main__':
    solve()