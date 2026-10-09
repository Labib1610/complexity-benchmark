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
    def dpll(clauses, assign):
        # unit propagation
        while True:
            unit = None
            for c in clauses:
                # evaluate clause under current assignment
                val = False
                unassigned = None
                for lit in c:
                    var = abs(lit)
                    if var in assign:
                        if (assign[var] == 1 and lit > 0) or (assign[var] == 0 and lit < 0):
                            val = True
                            break
                    else:
                        if unassigned is None:
                            unassigned = lit
                if val:
                    continue
                if unassigned is None:  # all assigned and clause false -> conflict
                    return None
                # clause not satisfied, exactly one unassigned -> unit
                if all((abs(l) in assign) for l in c):
                    # all assigned but not satisfied -> conflict
                    return None
                # check if only one literal is unassigned and others false
                cnt_un = sum(1 for l in c if abs(l) not in assign)
                if cnt_un == 1:
                    unit = unassigned
                    break
            if unit is None:
                break
            var = abs(unit)
            val = 1 if unit > 0 else 0
            assign[var] = val

        # pure literal elimination
        while True:
            counts = {}
            for c in clauses:
                for lit in c:
                    var = abs(lit)
                    if var in assign:
                        continue
                    counts.setdefault(var, set()).add(lit > 0)
            pure = None
            for var, signs in counts.items():
                if len(signs) == 1:
                    pure = (var, 1 if True in signs else 0)
                    break
            if pure is None:
                break
            assign[pure[0]] = pure[1]

        # check if all clauses satisfied
        all_sat = True
        for c in clauses:
            sat = False
            for lit in c:
                var = abs(lit)
                if var in assign:
                    if (assign[var] == 1 and lit > 0) or (assign[var] == 0 and lit < 0):
                        sat = True
                        break
            if not sat:
                all_sat = False
                break
        if all_sat:
            return assign

        # choose variable
        for c in clauses:
            for lit in c:
                var = abs(lit)
                if var not in assign:
                    chosen = var
                    break
            else:
                continue
            break

        # try true then false
        for val in (1, 0):
            new_assign = assign.copy()
            new_assign[chosen] = val
            res = dpll(clauses, new_assign)
            if res is not None:
                return res
        return None

    result = dpll(clauses, {})
    if result is None:
        print("NO")
    else:
        print("YES")
        out = [str(result.get(i, 0)) for i in range(1, n + 1)]
        print(' '.join(out))

if __name__ == "__main__":
    solve()