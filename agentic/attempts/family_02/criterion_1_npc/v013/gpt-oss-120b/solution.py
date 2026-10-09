import sys

sys.setrecursionlimit(10000)

def solve_instance():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    clauses = []          # list of [(var, sign), ...]  sign = +1 for x, -1 for ¬x
    occ = [[] for _ in range(n)]   # clause indices per variable

    for ci in range(m):
        lits = []
        for _ in range(3):
            v = int(next(it))
            var = abs(v) - 1
            sign = 1 if v > 0 else -1
            lits.append((var, sign))
            occ[var].append(ci)
        clauses.append(lits)

    assign = [-1] * n   # -1 unassigned, 0/1 assigned

    # ----- helper functions -----
    def lit_value(lit):
        var, sign = lit
        a = assign[var]
        if a == -1:
            return None
        return a if sign == 1 else 1 - a

    def clause_status(cl):
        """return True (satisfied), False (falsified), None (undetermined)"""
        any_true = False
        any_undef = False
        for lit in cl:
            v = lit_value(lit)
            if v is None:
                any_undef = True
            elif v == 1:
                any_true = True
                break
        if any_true:
            return True
        if any_undef:
            return None
        return False

    # unit propagation
    def propagate():
        stack = []
        while True:
            unit = None
            for idx, cl in enumerate(clauses):
                status = clause_status(cl)
                if status is False:
                    return False
                if status is True:
                    continue
                # undetermined: count unassigned literals
                unassigned = []
                for lit in cl:
                    if lit_value(lit) is None:
                        unassigned.append(lit)
                if len(unassigned) == 1:
                    unit = unassigned[0]
                    break
            if unit is None:
                break
            var, sign = unit
            val = 1 if sign == 1 else 0
            if assign[var] != -1:
                if assign[var] != val:
                    return False
                continue
            assign[var] = val
            stack.append(var)
        return True

    # choose variable with most occurrences among unassigned
    def choose_var():
        best = -1
        best_cnt = -1
        for v in range(n):
            if assign[v] == -1:
                cnt = len(occ[v])
                if cnt > best_cnt:
                    best_cnt = cnt
                    best = v
        return best

    def dfs():
        if not propagate():
            return False
        if all(a != -1 for a in assign):
            return True
        v = choose_var()
        saved = assign[v]
        for val in (0, 1):
            assign[v] = val
            if dfs():
                return True
            # backtrack assignments made during deeper recursion
            # reset all variables that were assigned after this level
            # easiest: copy whole assign list before recursion
            # but n is tiny, we can just restore whole array from a snapshot
            # We'll use snapshot technique:
        assign[v] = saved
        # need proper backtrack: use snapshot
        return False

    # To handle backtracking cleanly, we implement dfs with explicit snapshots
    def dfs_snapshot():
        if not propagate():
            return False
        if all(a != -1 for a in assign):
            return True
        v = choose_var()
        # snapshot current assignment
        saved_assign = assign[:]
        for val in (0, 1):
            assign[v] = val
            if dfs_snapshot():
                return True
            assign[:] = saved_assign[:]   # restore
        return False

    if dfs_snapshot():
        print("YES")
        print(' '.join(str(x) for x in assign))
    else:
        print("NO")

if __name__ == "__main__":
    solve_instance()