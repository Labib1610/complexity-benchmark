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

    assign = {}          # var -> bool
    trail = []           # list of (var, old_value_or_None)

    # ---------- propagation ----------
    def propagate() -> bool:
        """return True if no conflict, False otherwise"""
        changed = True
        while changed:
            changed = False
            for cl in clauses:
                # evaluate clause under current assignment
                unk = None
                satisfied = False
                for lit in cl:
                    var = abs(lit)
                    sign = lit > 0
                    if var in assign:
                        if assign[var] == sign:
                            satisfied = True
                            break
                    else:
                        if unk is None:
                            unk = lit
                if satisfied:
                    continue
                if unk is None:          # all three false -> conflict
                    return False
                # unit clause
                var = abs(unk)
                val = unk > 0
                if var in assign:
                    if assign[var] != val:
                        return False
                    continue
                # assign it
                trail.append((var, None))
                assign[var] = val
                changed = True
        return True

    # ---------- DPLL ----------
    def dpll() -> bool:
        if len(assign) == n:
            return True
        if not propagate():
            return False
        # pick unassigned variable
        for v in range(1, n + 1):
            if v not in assign:
                var = v
                break
        # try True then False
        for val in (True, False):
            checkpoint = len(trail)
            trail.append((var, None))
            assign[var] = val
            if dpll():
                return True
            # backtrack
            while len(trail) > checkpoint:
                v_back, _ = trail.pop()
                del assign[v_back]
        return False

    if dpll():
        out = ['YES']
        vals = [ '1' if assign.get(i, False) else '0' for i in range(1, n + 1) ]
        out.append(' '.join(vals))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()