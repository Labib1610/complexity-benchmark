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
        c = (int(next(it)), int(next(it)), int(next(it)))
        clauses.append(c)

    # occurrence count for heuristic
    occ = [0] * (n + 1)
    for c in clauses:
        for lit in c:
            occ[abs(lit)] += 1

    # assignment: -1 unassigned, 0 false, 1 true
    assign = [-1] * (n + 1)

    # helper to get literal value under current assignment
    def lit_val(lit):
        v = assign[abs(lit)]
        if v == -1:
            return None
        return v if lit > 0 else 1 - v

    # propagation: returns False if conflict, else True
    def propagate(stack):
        # stack contains variables just assigned (var indices)
        while stack:
            var = stack.pop()
            val = assign[var]
            # scan all clauses for unit/conflict
            for c in clauses:
                vals = [lit_val(l) for l in c]
                # if any literal already true, clause satisfied
                if any(v == 1 for v in vals):
                    continue
                # count unassigned
                unassigned = [i for i, v in enumerate(vals) if v is None]
                if not unassigned:
                    # all false -> conflict
                    return False
                if len(unassigned) == 1:
                    # unit clause, force literal true
                    lit = c[unassigned[0]]
                    var2 = abs(lit)
                    needed = 1 if lit > 0 else 0
                    if assign[var2] == -1:
                        assign[var2] = needed
                        stack.append(var2)
                    elif assign[var2] != needed:
                        return False
        return True

    # choose next variable (unassigned) with max occurrence
    def choose_var():
        best = -1
        bestcnt = -1
        for i in range(1, n + 1):
            if assign[i] == -1 and occ[i] > bestcnt:
                bestcnt = occ[i]
                best = i
        return best

    def dfs():
        # find any clause unsatisfied? propagation already handled
        # check if all assigned
        if all(v != -1 for v in assign[1:]):
            return True
        var = choose_var()
        for val in (0, 1):
            # save state
            saved = assign[:]
            assign[var] = val
            if propagate([var]):
                if dfs():
                    return True
            # restore
            assign[:] = saved
        return False

    if dfs():
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()