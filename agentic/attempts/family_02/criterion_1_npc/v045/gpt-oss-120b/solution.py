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

    # assignment: None = unassigned, True = 1, False = 0
    assign = [None] * (n + 1)

    # helper to get literal value under current assignment
    def lit_val(lit):
        v = assign[abs(lit)]
        if v is None:
            return None
        return v if lit > 0 else (not v)

    # unit propagation + pure literal elimination
    def propagate():
        while True:
            changed = False
            # unit clauses
            for clause in clauses:
                unassigned = None
                satisfied = False
                for lit in clause:
                    val = lit_val(lit)
                    if val is True:
                        satisfied = True
                        break
                    if val is None:
                        if unassigned is None:
                            unassigned = lit
                        else:
                            unassigned = None  # more than one unassigned
                if satisfied:
                    continue
                if unassigned is None:
                    # all literals false -> conflict
                    return False
                # exactly one unassigned literal -> unit
                var = abs(unassigned)
                val = unassigned > 0
                if assign[var] is None:
                    assign[var] = val
                    changed = True
                elif assign[var] != val:
                    return False
            if not changed:
                break
        # pure literal elimination (optional, improves speed)
        # find for each variable if it appears only with one polarity in unsatisfied clauses
        pos = [False] * (n + 1)
        neg = [False] * (n + 1)
        for clause in clauses:
            clause_sat = any(lit_val(lit) is True for lit in clause)
            if clause_sat:
                continue
            for lit in clause:
                v = abs(lit)
                if assign[v] is not None:
                    continue
                if lit > 0:
                    pos[v] = True
                else:
                    neg[v] = True
        for v in range(1, n + 1):
            if assign[v] is None:
                if pos[v] and not neg[v]:
                    assign[v] = True
                elif neg[v] and not pos[v]:
                    assign[v] = False
        return True

    # recursive DPLL
    def dpll():
        if not propagate():
            return False
        # check if all clauses satisfied
        all_sat = True
        for clause in clauses:
            if not any(lit_val(lit) is True for lit in clause):
                all_sat = False
                break
        if all_sat:
            return True
        # choose unassigned variable
        var = next(i for i in range(1, n + 1) if assign[i] is None)
        # try True
        saved = assign[:]
        assign[var] = True
        if dpll():
            return True
        # backtrack, try False
        assign[:] = saved
        assign[var] = False
        if dpll():
            return True
        assign[:] = saved
        return False

    if dpll():
        print("YES")
        print(' '.join('1' if assign[i] else '0' for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()