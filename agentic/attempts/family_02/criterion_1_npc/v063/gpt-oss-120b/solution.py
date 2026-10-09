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
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        clauses.append([a, b, c])

    # ------------------------------------------------------------
    # DPLL recursive solver
    # ------------------------------------------------------------
    def dpll(assign):
        """assign: list of length n, -1 = unknown, 0 or 1 = fixed.
           returns a full assignment list or None."""
        # ----- unit propagation -----
        while True:
            changed = False
            for cl in clauses:
                # check if clause already satisfied
                satisfied = False
                unassigned = []
                for lit in cl:
                    v = abs(lit) - 1
                    a = assign[v]
                    if a == -1:
                        unassigned.append(lit)
                    else:
                        lit_true = (a == 1 and lit > 0) or (a == 0 and lit < 0)
                        if lit_true:
                            satisfied = True
                            break
                if satisfied:
                    continue
                if not unassigned:          # all false -> conflict
                    return None
                if len(unassigned) == 1:    # unit clause
                    lit = unassigned[0]
                    v = abs(lit) - 1
                    val = 1 if lit > 0 else 0
                    if assign[v] == -1:
                        assign[v] = val
                        changed = True
                    elif assign[v] != val:
                        return None
            if not changed:
                break

        # ----- pure literal elimination -----
        pos = [False] * n
        neg = [False] * n
        for cl in clauses:
            # skip already satisfied clauses
            clause_sat = False
            for lit in cl:
                v = abs(lit) - 1
                a = assign[v]
                if a != -1:
                    lit_true = (a == 1 and lit > 0) or (a == 0 and lit < 0)
                    if lit_true:
                        clause_sat = True
                        break
            if clause_sat:
                continue
            for lit in cl:
                v = abs(lit) - 1
                if assign[v] == -1:
                    if lit > 0:
                        pos[v] = True
                    else:
                        neg[v] = True

        pure_assigned = False
        for v in range(n):
            if assign[v] == -1:
                if pos[v] and not neg[v]:
                    assign[v] = 1
                    pure_assigned = True
                elif neg[v] and not pos[v]:
                    assign[v] = 0
                    pure_assigned = True
        if pure_assigned:
            # after pure assignments we may get new units
            return dpll(assign)

        # ----- all variables assigned ? -----
        if all(a != -1 for a in assign):
            return assign

        # ----- choose variable (most occurrences) -----
        occ = [0] * n
        for cl in clauses:
            # ignore satisfied clauses
            clause_sat = False
            for lit in cl:
                v = abs(lit) - 1
                a = assign[v]
                if a != -1:
                    lit_true = (a == 1 and lit > 0) or (a == 0 and lit < 0)
                    if lit_true:
                        clause_sat = True
                        break
            if clause_sat:
                continue
            for lit in cl:
                v = abs(lit) - 1
                if assign[v] == -1:
                    occ[v] += 1
        var = max(range(n), key=lambda i: occ[i])

        # ----- branch on the chosen variable -----
        for val in (1, 0):
            new_assign = assign.copy()
            new_assign[var] = val
            res = dpll(new_assign)
            if res is not None:
                return res
        return None

    # start with all unknown
    answer = dpll([-1] * n)

    if answer is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(x) for x in answer))

if __name__ == "__main__":
    solve()