import sys, random
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

    # adjacency for variable occurrence
    var_pos = [[] for _ in range(n + 1)]
    var_neg = [[] for _ in range(n + 1)]
    for idx, cl in enumerate(clauses):
        for lit in cl:
            v = abs(lit)
            if lit > 0:
                var_pos[v].append(idx)
            else:
                var_neg[v].append(idx)

    assign = [None] * (n + 1)   # None, 0, 1

    # helper to evaluate literal under current assignment
    def lit_val(lit):
        v = abs(lit)
        a = assign[v]
        if a is None:
            return None
        return a if lit > 0 else 1 - a

    # unit propagation stack
    def propagate(stack):
        while stack:
            lit = stack.pop()
            v = abs(lit)
            val = 1 if lit > 0 else 0
            if assign[v] is not None:
                if assign[v] != val:
                    return False
                continue
            assign[v] = val
            # clauses where this literal appears become satisfied; ignore
            # clauses where opposite literal appears may become unit/unsat
            opp = -lit
            for cid in (var_neg[v] if lit > 0 else var_pos[v]):
                cl = clauses[cid]
                # check clause status
                sat = False
                unassigned = []
                for l in cl:
                    lv = lit_val(l)
                    if lv == 1:
                        sat = True
                        break
                    if lv is None:
                        unassigned.append(l)
                if sat:
                    continue
                if not unassigned:   # all false
                    return False
                if len(unassigned) == 1:
                    stack.append(unassigned[0])
        return True

    # pure literal elimination
    def pure_eliminate():
        changed = True
        while changed:
            changed = False
            for v in range(1, n + 1):
                if assign[v] is not None:
                    continue
                pos = any(assign[abs(l)] is None for l in var_pos[v])
                neg = any(assign[abs(l)] is None for l in var_neg[v])
                # actually need to see if clause contains only this literal polarity
                # Simplify: if variable appears only with one polarity in all unsatisfied clauses
                appears_pos = False
                appears_neg = False
                for cid in var_pos[v]:
                    cl = clauses[cid]
                    if any(lit_val(l) != 0 for l in cl):  # clause already satisfied
                        continue
                    appears_pos = True
                    break
                for cid in var_neg[v]:
                    cl = clauses[cid]
                    if any(lit_val(l) != 0 for l in cl):
                        continue
                    appears_neg = True
                    break
                if appears_pos ^ appears_neg:
                    val = 1 if appears_pos else 0
                    assign[v] = val
                    changed = True

    # recursive DPLL
    def dpll():
        # unit propagation
        unit_stack = []
        for cid, cl in enumerate(clauses):
            sat = False
            unassigned = []
            for l in cl:
                v = lit_val(l)
                if v == 1:
                    sat = True
                    break
                if v is None:
                    unassigned.append(l)
            if sat:
                continue
            if not unassigned:
                return False
            if len(unassigned) == 1:
                unit_stack.append(unassigned[0])
        if not propagate(unit_stack):
            return False

        pure_eliminate()

        # check if all clauses satisfied
        all_sat = True
        for cl in clauses:
            if any(lit_val(l) == 1 for l in cl):
                continue
            all_sat = False
            break
        if all_sat:
            return True

        # choose variable heuristically: most occurrences in unsatisfied clauses
        best_v = None
        best_score = -1
        for v in range(1, n + 1):
            if assign[v] is None:
                score = 0
                for cid in var_pos[v] + var_neg[v]:
                    cl = clauses[cid]
                    if any(lit_val(l) == 1 for l in cl):
                        continue
                    score += 1
                if score > best_score:
                    best_score = score
                    best_v = v
        v = best_v
        # try true then false
        saved = assign[:]
        for val in (1, 0):
            assign[v] = val
            if dpll():
                return True
            assign[:] = saved[:]
        return False

    if dpll():
        print("YES")
        print(' '.join(str(assign[i] if assign[i] is not None else 0) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()