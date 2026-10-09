import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        c = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(c)

    # ------------------------------------------------------------
    # helper functions working on a given assignment
    # ------------------------------------------------------------
    def literal_is_true(lit, assign):
        v = assign[abs(lit)]
        if v == -1:
            return None
        return (lit > 0 and v == 1) or (lit < 0 and v == 0)

    # ------------------------------------------------------------
    # DPLL recursive solver
    # ------------------------------------------------------------
    def dpll(assign):
        # ---- unit propagation ----
        while True:
            unit_lit = None
            for cl in clauses:
                sat = False
                unknown = []
                for lit in cl:
                    val = literal_is_true(lit, assign)
                    if val is True:
                        sat = True
                        break
                    elif val is None:
                        unknown.append(lit)
                if sat:
                    continue
                if not unknown:          # all false -> conflict
                    return None
                if len(unknown) == 1:   # unit clause
                    unit_lit = unknown[0]
                    break
            if unit_lit is None:
                break
            var = abs(unit_lit)
            needed = 1 if unit_lit > 0 else 0
            if assign[var] != -1:
                if assign[var] != needed:
                    return None
            else:
                assign[var] = needed

        # ---- pure literal elimination ----
        while True:
            pos = [0] * (n + 1)
            neg = [0] * (n + 1)
            for cl in clauses:
                # skip already satisfied clauses
                satisfied = False
                for lit in cl:
                    if literal_is_true(lit, assign):
                        satisfied = True
                        break
                if satisfied:
                    continue
                for lit in cl:
                    if assign[abs(lit)] == -1:
                        if lit > 0:
                            pos[abs(lit)] += 1
                        else:
                            neg[abs(lit)] += 1
            pure_var = 0
            pure_val = 0
            for v in range(1, n + 1):
                if assign[v] != -1:
                    continue
                if pos[v] > 0 and neg[v] == 0:
                    pure_var = v
                    pure_val = 1
                    break
                if neg[v] > 0 and pos[v] == 0:
                    pure_var = v
                    pure_val = 0
                    break
            if pure_var == 0:
                break
            assign[pure_var] = pure_val

        # ---- check if all clauses are satisfied ----
        all_sat = True
        for cl in clauses:
            if not any(literal_is_true(lit, assign) for lit in cl):
                all_sat = False
                break
        if all_sat:
            return assign

        # ---- choose a variable (first unassigned) ----
        for v in range(1, n + 1):
            if assign[v] == -1:
                var = v
                break
        for val in (1, 0):
            new_assign = assign[:]
            new_assign[var] = val
            res = dpll(new_assign)
            if res is not None:
                return res
        return None

    # ------------------------------------------------------------
    initial_assign = [-1] * (n + 1)
    result = dpll(initial_assign)

    if result is None:
        print("NO")
    else:
        # replace any still-unassigned variables by 0 (any value works)
        for i in range(1, n + 1):
            if result[i] == -1:
                result[i] = 0
        print("YES")
        print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()