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

    # adjacency for pure literal detection
    var_pos = [set() for _ in range(n + 1)]
    var_neg = [set() for _ in range(n + 1)]
    for idx, cl in enumerate(clauses):
        for lit in cl:
            v = abs(lit)
            if lit > 0:
                var_pos[v].add(idx)
            else:
                var_neg[v].add(idx)

    assign = [-1] * (n + 1)  # -1 unassigned, 0 false, 1 true

    # helper to evaluate literal under current assignment
    def lit_val(lit):
        v = abs(lit)
        a = assign[v]
        if a == -1:
            return None
        return a if lit > 0 else 1 - a

    # propagation: unit clauses and pure literals
    def propagate():
        changed = True
        while changed:
            changed = False
            # unit clause propagation
            for cl in clauses:
                vals = [lit_val(l) for l in cl]
                if any(v == 1 for v in vals):
                    continue  # already satisfied
                falses = sum(1 for v in vals if v == 0)
                unassigned = [cl[i] for i, v in enumerate(vals) if v is None]
                if falses == 3:
                    return False  # conflict
                if len(unassigned) == 1 and falses == 2:
                    lit = unassigned[0]
                    v = abs(lit)
                    val = 1 if lit > 0 else 0
                    if assign[v] == -1:
                        assign[v] = val
                        changed = True
                    elif assign[v] != val:
                        return False
            # pure literal detection
            for v in range(1, n + 1):
                if assign[v] != -1:
                    continue
                pos = any(assign[abs(lit)] in (-1, 1) for idx in var_pos[v] for lit in clauses[idx] if abs(lit) == v)
                neg = any(assign[abs(lit)] in (-1, 0) for idx in var_neg[v] for lit in clauses[idx] if abs(lit) == v)
                # actually we just need to see if variable appears only with one polarity in *all* clauses
                # compute presence in unsatisfied clauses
                appears_pos = False
                appears_neg = False
                for idx in var_pos[v]:
                    cl = clauses[idx]
                    if any(lit_val(l) != 0 for l in cl):  # clause not already false
                        appears_pos = True
                        break
                for idx in var_neg[v]:
                    cl = clauses[idx]
                    if any(lit_val(l) != 0 for l in cl):
                        appears_neg = True
                        break
                if appears_pos ^ appears_neg:
                    val = 1 if appears_pos else 0
                    assign[v] = val
                    changed = True
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
        # choose unassigned variable (heuristic: most occurrences)
        best = -1
        best_cnt = -1
        for v in range(1, n + 1):
            if assign[v] == -1:
                cnt = len(var_pos[v]) + len(var_neg[v])
                if cnt > best_cnt:
                    best_cnt = cnt
                    best = v
        v = best
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
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()