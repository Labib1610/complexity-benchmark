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

    # variable indices 1..n, value: True=1, False=0, None=unassigned
    assign = [None] * (n + 1)

    # occurrence lists for heuristic
    var_pos = [set() for _ in range(n + 1)]
    var_neg = [set() for _ in range(n + 1)]
    for idx, cl in enumerate(clauses):
        for lit in cl:
            v = abs(lit)
            if lit > 0:
                var_pos[v].add(idx)
            else:
                var_neg[v].add(idx)

    # helper to evaluate literal under current assignment
    def lit_val(lit):
        v = abs(lit)
        val = assign[v]
        if val is None:
            return None
        return val if lit > 0 else (not val)

    # unit propagation and pure literal elimination
    def propagate():
        changed = True
        while changed:
            changed = False
            # unit clauses
            for cl in clauses:
                vals = [lit_val(l) for l in cl]
                if any(v is True for v in vals):
                    continue  # clause already satisfied
                unassigned = [cl[i] for i, v in enumerate(vals) if v is None]
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    v = abs(lit)
                    val = lit > 0
                    if assign[v] is None:
                        assign[v] = val
                        changed = True
                    elif assign[v] != val:
                        return False
            # pure literals
            for v in range(1, n + 1):
                if assign[v] is not None:
                    continue
                pos = any(assign[abs(lit)] is not False for lit in var_pos[v])
                neg = any(assign[abs(lit)] is not True for lit in var_neg[v])
                # actually we need to check if variable appears only with one polarity in unsatisfied clauses
                # Simpler: check remaining clauses
                appears_pos = appears_neg = False
                for idx in var_pos[v]:
                    cl = clauses[idx]
                    if any(lit_val(l) is True for l in cl):
                        continue
                    appears_pos = True
                    break
                for idx in var_neg[v]:
                    cl = clauses[idx]
                    if any(lit_val(l) is True for l in cl):
                        continue
                    appears_neg = True
                    break
                if appears_pos and not appears_neg:
                    assign[v] = True
                    changed = True
                elif appears_neg and not appears_pos:
                    assign[v] = False
                    changed = True
        return True

    # check if all clauses satisfied
    def all_satisfied():
        for cl in clauses:
            if not any(lit_val(l) is True for l in cl):
                return False
        return True

    # choose unassigned variable with highest occurrence
    def choose_var():
        best = None
        best_cnt = -1
        for v in range(1, n + 1):
            if assign[v] is None:
                cnt = len(var_pos[v]) + len(var_neg[v])
                if cnt > best_cnt:
                    best_cnt = cnt
                    best = v
        return best

    def dfs():
        if not propagate():
            return False
        if all(assign[v] is not None for v in range(1, n + 1)):
            return all_satisfied()
        v = choose_var()
        saved = assign[:]
        assign[v] = True
        if dfs():
            return True
        assign[:] = saved
        assign[v] = False
        if dfs():
            return True
        assign[:] = saved
        return False

    if dfs():
        print("YES")
        print(' '.join('1' if assign[i] else '0' for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()