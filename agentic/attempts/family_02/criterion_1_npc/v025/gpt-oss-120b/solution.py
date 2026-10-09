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
    occ_pos = [[] for _ in range(n + 1)]
    occ_neg = [[] for _ in range(n + 1)]

    for idx in range(m):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        clause = [a, b, c]
        clauses.append(clause)
        for lit in clause:
            v = abs(lit)
            if lit > 0:
                occ_pos[v].append(idx)
            else:
                occ_neg[v].append(idx)

    assign = [None] * (n + 1)          # 1‑based

    # ---------- helper ----------
    def lit_value(lit):
        v = abs(lit)
        a = assign[v]
        if a is None:
            return None
        return (a == 1) if lit > 0 else (a == 0)

    # ---------- unit propagation ----------
    def unit_propagate():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                vals = [lit_value(l) for l in clause]
                # if any literal already true -> clause satisfied
                if any(v is True for v in vals):
                    continue
                # count unassigned literals
                unassigned = [clause[i] for i, v in enumerate(vals) if v is None]
                if len(unassigned) == 0:          # all false -> conflict
                    return False
                if len(unassigned) == 1:          # unit clause
                    lit = unassigned[0]
                    v = abs(lit)
                    needed = 1 if lit > 0 else 0
                    if assign[v] is not None:
                        if assign[v] != needed:
                            return False
                    else:
                        assign[v] = needed
                        changed = True
        return True

    # ---------- pure literal elimination ----------
    def pure_literal_eliminate():
        # simple scan, repeat until no change
        changed = True
        while changed:
            changed = False
            for v in range(1, n + 1):
                if assign[v] is not None:
                    continue
                pos = any(assign[abs(lit)] is None for lit in occ_pos[v])
                neg = any(assign[abs(lit)] is None for lit in occ_neg[v])
                # if appears only positively
                if pos and not neg:
                    assign[v] = 1
                    changed = True
                # only negatively
                elif neg and not pos:
                    assign[v] = 0
                    changed = True

    # ---------- variable selection ----------
    occ_total = [len(occ_pos[i]) + len(occ_neg[i]) for i in range(n + 1)]
    def choose_var():
        best = -1
        bestcnt = -1
        for v in range(1, n + 1):
            if assign[v] is None and occ_total[v] > bestcnt:
                bestcnt = occ_total[v]
                best = v
        return best

    # ---------- DPLL ----------
    def dpll():
        # check if all assigned
        if all(a is not None for a in assign[1:]):
            return True
        if not unit_propagate():
            return False
        pure_literal_eliminate()
        if all(a is not None for a in assign[1:]):
            return True
        v = choose_var()
        saved = assign[v]
        for val in (0, 1):
            assign[v] = val
            if dpll():
                return True
            # backtrack
            assign[v] = None
        assign[v] = saved
        return False

    sat = dpll()
    out = sys.stdout
    if not sat:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(' '.join(str(assign[i]) for i in range(1, n + 1)))
        out.write('\n')

if __name__ == "__main__":
    solve()