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
        lits = [int(next(it)) for _ in range(3)]
        clauses.append(lits)

    # assignment: -1 unknown, 0 false, 1 true
    assign = [-1] * (n + 1)

    # helper to get literal value under current assignment
    def lit_val(lit):
        v = assign[abs(lit)]
        if v == -1:
            return None
        return v if lit > 0 else 1 - v

    # unit propagation and pure literal elimination
    def propagate():
        while True:
            changed = False
            # unit clauses
            for cl in clauses:
                vals = [lit_val(l) for l in cl]
                # count true/false/unknown
                if any(v == 1 for v in vals):
                    continue  # already satisfied
                unknown_idxs = [i for i, v in enumerate(vals) if v is None]
                if not unknown_idxs:
                    return False  # all false -> conflict
                if len(unknown_idxs) == 1:
                    # must set this literal true
                    lit = cl[unknown_idxs[0]]
                    var = abs(lit)
                    needed = 1 if lit > 0 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        changed = True
                    elif assign[var] != needed:
                        return False
            if changed:
                continue

            # pure literal elimination
            pos = [0] * (n + 1)
            neg = [0] * (n + 1)
            for cl in clauses:
                for lit in cl:
                    var = abs(lit)
                    if assign[var] != -1:
                        continue
                    if lit > 0:
                        pos[var] += 1
                    else:
                        neg[var] += 1
            pure_found = False
            for var in range(1, n + 1):
                if assign[var] == -1:
                    if pos[var] and not neg[var]:
                        assign[var] = 1
                        pure_found = True
                    elif neg[var] and not pos[var]:
                        assign[var] = 0
                        pure_found = True
            if pure_found:
                continue
            break
        return True

    # recursive DPLL
    def dpll():
        if not propagate():
            return False
        # check if all clauses satisfied
        all_sat = True
        for cl in clauses:
            if not any(lit_val(l) == 1 for l in cl):
                all_sat = False
                break
        if all_sat:
            return True
        # choose unassigned variable
        var = next(i for i in range(1, n + 1) if assign[i] == -1)
        # try true then false
        saved = assign[:]
        assign[var] = 1
        if dpll():
            return True
        assign[:] = saved
        assign[var] = 0
        if dpll():
            return True
        assign[:] = saved
        return False

    if dpll():
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()