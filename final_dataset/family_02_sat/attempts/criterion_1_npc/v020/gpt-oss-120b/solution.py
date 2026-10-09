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
    occ = [[] for _ in range(n + 1)]          # (clause_id, sign) sign:1 positive,0 negative
    for cid in range(m):
        lits = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(lits)
        for lit in lits:
            var = abs(lit)
            sign = 1 if lit > 0 else 0
            occ[var].append((cid, sign))

    assign = [-1] * (n + 1)   # -1 unassigned, 0 Dormant, 1 Activated

    # ---------- helper ----------
    def lit_value(lit):
        v = assign[abs(lit)]
        if v == -1:
            return None
        return v == 1 if lit > 0 else v == 0

    # ---------- propagation ----------
    def propagate(stack):
        """perform unit propagation, record newly assigned vars in stack.
           return False if a conflict is found."""
        changed = True
        while changed:
            changed = False
            for cid, cl in enumerate(clauses):
                # evaluate clause
                true_found = False
                unassigned_lit = None
                for lit in cl:
                    val = lit_value(lit)
                    if val is True:
                        true_found = True
                        break
                    if val is None:
                        unassigned_lit = lit
                if true_found:
                    continue
                # no true literal
                if unassigned_lit is None:
                    # all false -> conflict
                    return False
                # check if unit: exactly one unassigned and others false
                # we already know there is at least one unassigned;
                # need to ensure the other two are false
                # count unassigned literals
                cnt_un = 0
                last_un = None
                for lit in cl:
                    val = lit_value(lit)
                    if val is None:
                        cnt_un += 1
                        last_un = lit
                if cnt_un == 1:
                    var = abs(last_un)
                    needed = 1 if last_un > 0 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        stack.append(var)
                        changed = True
                    elif assign[var] != needed:
                        return False
        return True

    # ---------- DPLL ----------
    def dfs() -> bool:
        # unit propagation
        unit_stack = []
        if not propagate(unit_stack):
            # undo assignments made by this propagation
            for v in unit_stack:
                assign[v] = -1
            return False

        # check if all assigned
        if all(a != -1 for a in assign[1:]):
            return True

        # choose variable (first unassigned)
        for v in range(1, n + 1):
            if assign[v] == -1:
                var = v
                break

        # try true then false
        for val in (1, 0):
            assign[var] = val
            local_stack = []
            if propagate(local_stack):
                if dfs():
                    return True
            # undo
            for u in local_stack:
                assign[u] = -1
            assign[var] = -1
        return False

    if dfs():
        out = ['YES']
        out.append(' '.join('1' if assign[i] == 1 else '0' for i in range(1, n + 1)))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()