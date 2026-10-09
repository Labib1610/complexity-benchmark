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

    # assignment: -1 unassigned, 0 false, 1 true
    assign = [-1] * (n + 1)

    # helper to get literal value under current assignment
    def lit_val(lit):
        var = abs(lit)
        val = assign[var]
        if val == -1:
            return None
        return val if lit > 0 else 1 - val

    # unit propagation and pure literal elimination
    def propagate():
        changed = True
        while changed:
            changed = False
            # unit clauses
            for clause in clauses:
                vals = [lit_val(l) for l in clause]
                # if any true, clause satisfied
                if any(v == 1 for v in vals):
                    continue
                # count unassigned
                unassigned = [i for i, v in enumerate(vals) if v is None]
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    idx = unassigned[0]
                    lit = clause[idx]
                    var = abs(lit)
                    needed = 1 if lit > 0 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        changed = True
                    elif assign[var] != needed:
                        return False
            # pure literals
            count_pos = [0] * (n + 1)
            count_neg = [0] * (n + 1)
            for clause in clauses:
                for lit in clause:
                    var = abs(lit)
                    if assign[var] != -1:
                        continue
                    if lit > 0:
                        count_pos[var] += 1
                    else:
                        count_neg[var] += 1
            for var in range(1, n + 1):
                if assign[var] == -1:
                    if count_pos[var] and not count_neg[var]:
                        assign[var] = 1
                        changed = True
                    elif count_neg[var] and not count_pos[var]:
                        assign[var] = 0
                        changed = True
        return True

    # recursive DPLL
    def dpll():
        if not propagate():
            return False
        # check if all clauses satisfied
        all_sat = True
        for clause in clauses:
            if not any(lit_val(l) == 1 for l in clause):
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
        print(' '.join(str(assign[i] if assign[i] != -1 else 0) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()