import sys

sys.setrecursionlimit(10000)

def solve_sat(clauses, n, assign):
    # unit propagation
    while True:
        unit = None
        new_clauses = []
        for cl in clauses:
            # evaluate clause under current assignment
            satisfied = False
            unassigned = []
            for lit in cl:
                var = abs(lit)
                if var in assign:
                    val = assign[var]
                    if (lit > 0 and val) or (lit < 0 and not val):
                        satisfied = True
                        break
                else:
                    unassigned.append(lit)
            if satisfied:
                continue
            if not unassigned:          # all false -> conflict
                return None
            if len(unassigned) == 1:
                unit = unassigned[0]
                break
            new_clauses.append(unassigned)
        if unit is None:
            clauses = new_clauses
            break
        # assign unit literal
        var = abs(unit)
        val = unit > 0
        if var in assign:
            if assign[var] != val:
                return None
        else:
            assign[var] = val
        clauses = new_clauses

    # pure literal elimination
    while True:
        counts = {}
        for cl in clauses:
            for lit in cl:
                counts[lit] = counts.get(lit, 0) + 1
        pure = None
        for lit, cnt in counts.items():
            if -lit not in counts:
                pure = lit
                break
        if pure is None:
            break
        var = abs(pure)
        val = pure > 0
        assign[var] = val
        # remove clauses satisfied by pure literal
        clauses = [cl for cl in clauses if not any((l > 0 and assign.get(abs(l), False) and l > 0) or
                                                    (l < 0 and not assign.get(abs(l), True) and l < 0) for l in cl)]

    if not clauses:
        # all satisfied
        return assign

    # choose variable from first clause
    for lit in clauses[0]:
        var = abs(lit)
        if var not in assign:
            break

    # try True then False
    for val in (True, False):
        new_assign = assign.copy()
        new_assign[var] = val
        res = solve_sat(clauses, n, new_assign)
        if res is not None:
            return res
    return None


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        l1 = int(next(it)); l2 = int(next(it)); l3 = int(next(it))
        clauses.append([l1, l2, l3])

    result = solve_sat(clauses, n, {})
    if result is None:
        print("NO")
    else:
        print("YES")
        out = []
        for i in range(1, n + 1):
            out.append('1' if result.get(i, False) else '0')
        print(' '.join(out))

if __name__ == "__main__":
    main()