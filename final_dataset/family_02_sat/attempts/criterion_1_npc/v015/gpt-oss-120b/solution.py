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
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        clauses.append((a, b, c))

    # assignment: index 1..n, values None / True / False
    def value(lit, assign):
        v = assign[abs(lit)]
        if v is None:
            return None
        return v if lit > 0 else (not v)

    # unit propagation, modifies assign, returns False on conflict
    def propagate(assign):
        changed = True
        while changed:
            changed = False
            for (a, b, c) in clauses:
                vals = [value(a, assign), value(b, assign), value(c, assign)]
                if True in vals:
                    continue          # clause already satisfied
                # count falsified literals
                falses = sum(1 for v in vals if v is False)
                if falses == 3:
                    return False      # conflict
                if falses == 2:
                    # unit clause, find the non-false literal
                    for lit, val in zip((a, b, c), vals):
                        if val is None:
                            var = abs(lit)
                            needed = (lit > 0)
                            if assign[var] is None:
                                assign[var] = needed
                                changed = True
                            elif assign[var] != needed:
                                return False
        return True

    def choose_var(assign):
        for i in range(1, n + 1):
            if assign[i] is None:
                return i
        return None

    def dpll(assign):
        if not propagate(assign):
            return None
        var = choose_var(assign)
        if var is None:          # all assigned
            return assign
        # try True
        for val in (True, False):
            new_assign = assign[:]   # copy
            new_assign[var] = val
            res = dpll(new_assign)
            if res is not None:
                return res
        return None

    init_assign = [None] * (n + 1)
    result = dpll(init_assign)
    out = []
    if result is None:
        out.append("NO")
    else:
        out.append("YES")
        out.append(' '.join('1' if result[i] else '0' for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()