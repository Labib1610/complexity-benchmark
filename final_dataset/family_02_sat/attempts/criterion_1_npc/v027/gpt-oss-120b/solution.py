import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        clauses.append((a, b, c))

    # ---------- helper functions ----------
    def lit_value(lit, assign):
        """None = unassigned, True/False otherwise"""
        var = abs(lit)
        if var not in assign:
            return None
        val = assign[var]
        return val if lit > 0 else (not val)

    def propagate(assign):
        """unit propagation, returns (new_assign, conflict_flag)"""
        assign = dict(assign)          # copy
        while True:
            unit_lit = None
            for (a, b, c) in clauses:
                vals = (lit_value(a, assign), lit_value(b, assign), lit_value(c, assign))
                # clause already satisfied
                if any(v is True for v in vals):
                    continue
                # count falses
                false_cnt = sum(v is False for v in vals)
                if false_cnt == 3:
                    return assign, True          # conflict
                if false_cnt == 2:
                    # the remaining literal must be true
                    for lit, v in zip((a, b, c), vals):
                        if v is None:
                            unit_lit = lit
                            break
                    break
            else:
                # no unit clause found
                break
            # assign the unit literal
            var = abs(unit_lit)
            val = unit_lit > 0
            if var in assign:
                if assign[var] != val:
                    return assign, True          # conflict
            else:
                assign[var] = val
        return assign, False

    def pure_eliminate(assign):
        """assign pure literals, return new assign"""
        assign = dict(assign)
        while True:
            pos = set()
            neg = set()
            for (a, b, c) in clauses:
                for lit in (a, b, c):
                    var = abs(lit)
                    if var in assign:
                        continue
                    if lit > 0:
                        pos.add(var)
                    else:
                        neg.add(var)
            pure = []
            for v in pos - neg:
                pure.append((v, True))
            for v in neg - pos:
                pure.append((v, False))
            if not pure:
                break
            for v, val in pure:
                assign[v] = val
        return assign

    # ---------- DPLL ----------
    def dpll(assign):
        assign, conflict = propagate(assign)
        if conflict:
            return None
        assign = pure_eliminate(assign)
        if len(assign) == n:
            # all variables assigned
            return assign
        # choose an unassigned variable
        for v in range(1, n + 1):
            if v not in assign:
                var = v
                break
        # try True
        for val in (True, False):
            new_assign = dict(assign)
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
        out = []
        for i in range(1, n + 1):
            out.append('1' if result.get(i, False) else '0')
        print(' '.join(out))

if __name__ == "__main__":
    solve()