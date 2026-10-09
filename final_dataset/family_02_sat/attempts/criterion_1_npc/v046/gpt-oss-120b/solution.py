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
        clause = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(clause)

    # DPLL
    def unit_propagate(assign, clauses):
        """perform unit propagation, return (assign, conflict)"""
        changed = True
        while changed:
            changed = False
            for cl in clauses:
                # evaluate clause under current assignment
                val = 0  # 0 unknown, 1 satisfied, -1 unsatisfied so far
                unassigned_lit = None
                for lit in cl:
                    var = abs(lit)
                    if var in assign:
                        lit_val = assign[var] if lit > 0 else 1 - assign[var]
                        if lit_val == 1:
                            val = 1
                            break
                    else:
                        if unassigned_lit is None:
                            unassigned_lit = lit
                        else:
                            # more than one unassigned, clause not unit
                            pass
                if val == 1:
                    continue
                if unassigned_lit is None:
                    # all literals assigned and none true -> conflict
                    return assign, True
                # check if clause is unit: exactly one unassigned and others false
                # we need to ensure all other literals are false
                all_false = True
                for lit in cl:
                    var = abs(lit)
                    if var in assign:
                        lit_val = assign[var] if lit > 0 else 1 - assign[var]
                        if lit_val == 1:
                            all_false = False
                            break
                    elif lit == unassigned_lit:
                        continue
                    else:
                        all_false = False
                        break
                if all_false:
                    # force unassigned_lit to true
                    var = abs(unassigned_lit)
                    val_needed = 1 if unassigned_lit > 0 else 0
                    if var in assign:
                        if assign[var] != val_needed:
                            return assign, True
                    else:
                        assign[var] = val_needed
                        changed = True
        return assign, False

    def choose_var(assign):
        for v in range(1, n + 1):
            if v not in assign:
                return v
        return None

    def dpll(assign):
        assign, conflict = unit_propagate(assign, clauses)
        if conflict:
            return None
        var = choose_var(assign)
        if var is None:
            # all assigned
            return assign
        # try true (1)
        for val in (1, 0):
            new_assign = assign.copy()
            new_assign[var] = val
            res = dpll(new_assign)
            if res is not None:
                return res
        return None

    result = dpll({})
    if result is None:
        print("NO")
    else:
        print("YES")
        out = [str(result.get(i, 0)) for i in range(1, n + 1)]
        print(" ".join(out))

if __name__ == "__main__":
    solve()