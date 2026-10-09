import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    clauses = []
    for _ in range(m):
        c = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(c)

    # helper to get literal value under assignment
    def lit_val(lit, assign):
        var = abs(lit)
        if var not in assign:
            return None
        val = assign[var]
        return val if lit > 0 else not val

    # recursive DPLL
    def dpll(clauses, assign):
        # unit propagation and pure literal elimination
        while True:
            # check clauses status
            unit = None
            pure_pos = set()
            pure_neg = set()
            var_seen = {}
            changed = False
            for c in clauses:
                sat = False
                unassigned = []
                for lit in c:
                    v = lit_val(lit, assign)
                    if v is True:
                        sat = True
                        break
                    elif v is None:
                        unassigned.append(lit)
                if sat:
                    continue
                if not unassigned:  # all false
                    return None
                if len(unassigned) == 1:
                    unit = unassigned[0]
                    break
                # collect for pure literal detection
                for lit in unassigned:
                    var = abs(lit)
                    if var in assign:
                        continue
                    if var not in var_seen:
                        var_seen[var] = 0
                    var_seen[var] |= (1 if lit > 0 else 2)
            if unit is not None:
                var = abs(unit)
                val = unit > 0
                if var in assign:
                    if assign[var] != val:
                        return None
                else:
                    assign[var] = val
                    changed = True
                continue
            # pure literals
            for var, mask in var_seen.items():
                if mask == 1:
                    pure_pos.add(var)
                elif mask == 2:
                    pure_neg.add(var)
            if pure_pos or pure_neg:
                for var in pure_pos:
                    assign[var] = True
                for var in pure_neg:
                    assign[var] = False
                changed = True
                continue
            if not changed:
                break

        # check if all clauses satisfied
        all_sat = True
        for c in clauses:
            if any(lit_val(l, assign) is True for l in c):
                continue
            all_sat = False
            break
        if all_sat:
            return assign

        # choose a variable from first unsatisfied clause
        for c in clauses:
            if any(lit_val(l, assign) is True for l in c):
                continue
            for lit in c:
                var = abs(lit)
                if var not in assign:
                    # branch
                    for val in (True, False):
                        new_assign = assign.copy()
                        new_assign[var] = val
                        res = dpll(clauses, new_assign)
                        if res is not None:
                            return res
                    return None
        return None

    result = dpll(clauses, {})
    if result is None:
        print("NO")
    else:
        print("YES")
        out = [str(1 if result.get(i, False) else 0) for i in range(1, n+1)]
        print(" ".join(out))

if __name__ == "__main__":
    solve()