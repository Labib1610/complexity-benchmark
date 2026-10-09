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
        c1 = int(next(it)); c2 = int(next(it)); c3 = int(next(it))
        clauses.append((c1, c2, c3))

    assign = [-1] * (n + 1)          # -1 unassigned, 0 false, 1 true

    # ---------- helper ----------
    def lit_val(lit):
        var = abs(lit)
        val = assign[var]
        if val == -1:
            return None
        if lit > 0:
            return bool(val)
        else:
            return not bool(val)

    # ---------- unit propagation ----------
    def propagate() -> bool:
        changed = True
        while changed:
            changed = False
            for cl in clauses:
                # check clause status
                satisfied = False
                unassigned_lit = None
                falses = 0
                for lit in cl:
                    v = lit_val(lit)
                    if v is True:
                        satisfied = True
                        break
                    elif v is False:
                        falses += 1
                    else:
                        unassigned_lit = lit
                if satisfied:
                    continue
                if falses == 3:          # all false -> conflict
                    return False
                if falses == 2 and unassigned_lit is not None:
                    # unit clause, must set this literal true
                    var = abs(unassigned_lit)
                    needed = 1 if unassigned_lit > 0 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        changed = True
                    elif assign[var] != needed:
                        return False
        return True

    # ---------- DPLL ----------
    def dpll() -> bool:
        if not propagate():
            return False
        # check if all assigned
        try:
            v = assign.index(-1, 1)   # first unassigned (skip index 0)
        except ValueError:
            return True                # all assigned, solution found
        # try true then false
        saved = assign[:]
        assign[v] = 1
        if dpll():
            return True
        assign[:] = saved
        assign[v] = 0
        if dpll():
            return True
        assign[:] = saved
        return False

    if dpll():
        out = ['YES']
        out.append(' '.join('1' if assign[i] == 1 else '0' for i in range(1, n + 1)))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()