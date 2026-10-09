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
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        clauses.append((l1, l2, l3))

    # assignment: -1 unknown, 0 false, 1 true
    assign = [-1] * (n + 1)

    # For fast lookup: for each variable, list of clause indices where it appears positively/negatively
    pos_occ = [[] for _ in range(n + 1)]
    neg_occ = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(clauses):
        for lit in (a, b, c):
            var = abs(lit)
            if lit > 0:
                pos_occ[var].append(idx)
            else:
                neg_occ[var].append(idx)

    # Helper to get literal value under current assignment
    def lit_val(lit: int) -> int:
        v = assign[abs(lit)]
        if v == -1:
            return -1
        return v if lit > 0 else 1 - v

    # Propagation stack: list of (var, value) to set
    def propagate(stack):
        while stack:
            var, val = stack.pop()
            if assign[var] != -1:
                if assign[var] != val:
                    return False
                continue
            assign[var] = val
            # check clauses where this literal appears positively/negatively
            related = pos_occ[var] if val == 1 else neg_occ[var]
            for ci in related:
                # clause satisfied, skip
                pass
            # For clauses where the opposite literal appears, we may create unit clauses or conflicts
            opp = neg_occ[var] if val == 1 else pos_occ[var]
            for ci in opp:
                a, b, c = clauses[ci]
                vals = [lit_val(a), lit_val(b), lit_val(c)]
                if 1 in vals:
                    continue  # already satisfied
                if -1 not in vals:  # all false
                    return False
                # exactly one unassigned -> unit
                if vals.count(-1) == 1:
                    # find that literal
                    for lit in (a, b, c):
                        if lit_val(lit) == -1:
                            v = abs(lit)
                            needed = 1 if lit > 0 else 0
                            stack.append((v, needed))
                            break
        return True

    # DPLL recursive search
    def dfs():
        # unit propagation loop
        while True:
            unit = None
            for idx, (a, b, c) in enumerate(clauses):
                vals = [lit_val(a), lit_val(b), lit_val(c)]
                if 1 in vals:
                    continue
                if -1 not in vals:
                    return False  # conflict
                if vals.count(-1) == 1:
                    # unit clause
                    for lit in (a, b, c):
                        if lit_val(lit) == -1:
                            unit = (abs(lit), 1 if lit > 0 else 0)
                            break
                    break
            if unit is None:
                break
            if not propagate([unit]):
                return False

        # check if all assigned
        if all(v != -1 for v in assign[1:]):
            return True

        # choose variable with heuristic (first unassigned)
        var = next(i for i in range(1, n + 1) if assign[i] == -1)

        # try 0 then 1
        saved = assign[:]
        if propagate([(var, 0)]):
            if dfs():
                return True
        assign[:] = saved[:]
        if propagate([(var, 1)]):
            if dfs():
                return True
        assign[:] = saved[:]
        return False

    if dfs():
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()