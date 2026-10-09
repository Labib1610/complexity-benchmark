import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # each clause: list of (var_index, sign)   sign = +1 for positive, -1 for negative
    clauses = []
    for _ in range(m):
        lits = []
        for _ in range(3):
            v = int(next(it))
            var = abs(v) - 1          # 0‑based
            sign = 1 if v > 0 else -1
            lits.append((var, sign))
        clauses.append(lits)

    assign = [-1] * n          # -1 unassigned, 0 or 1 assigned
    trail = []                 # stack of variables assigned in current recursion level

    # ---------- helper ----------
    def lit_value(var, sign):
        """return True / False / None for the literal (var, sign)"""
        a = assign[var]
        if a == -1:
            return None
        return (a == 1) if sign == 1 else (a == 0)

    # ---------- unit propagation ----------
    def propagate():
        """return True if no conflict, False otherwise. May assign variables."""
        while True:
            changed = False
            for lits in clauses:
                # evaluate clause
                true_found = False
                false_cnt = 0
                unknown = None
                for var, sign in lits:
                    val = lit_value(var, sign)
                    if val is True:
                        true_found = True
                        break
                    elif val is False:
                        false_cnt += 1
                    else:
                        unknown = (var, sign)
                if true_found:
                    continue
                if false_cnt == 3:          # all false -> conflict
                    return False
                if false_cnt == 2 and unknown is not None:
                    var, sign = unknown
                    # force this literal to be true
                    needed = 1 if sign == 1 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        trail.append(var)
                        changed = True
                    elif assign[var] != needed:
                        return False
            if not changed:
                break
        return True

    # ---------- pure literal elimination ----------
    def pure_eliminate():
        """assign pure literals, return list of newly assigned vars"""
        pos = [False] * n
        neg = [False] * n
        for lits in clauses:
            # clause already satisfied? we can ignore it for purity detection
            satisfied = False
            for var, sign in lits:
                val = lit_value(var, sign)
                if val is True:
                    satisfied = True
                    break
            if satisfied:
                continue
            for var, sign in lits:
                if assign[var] != -1:
                    continue
                if sign == 1:
                    pos[var] = True
                else:
                    neg[var] = True
        added = []
        for v in range(n):
            if assign[v] == -1:
                if pos[v] and not neg[v]:
                    assign[v] = 1
                    added.append(v)
                elif neg[v] and not pos[v]:
                    assign[v] = 0
                    added.append(v)
        trail.extend(added)
        return added

    # ---------- recursive DPLL ----------
    def dfs() -> bool:
        # check if all clauses satisfied
        all_sat = True
        for lits in clauses:
            clause_sat = False
            for var, sign in lits:
                val = lit_value(var, sign)
                if val is True:
                    clause_sat = True
                    break
            if not clause_sat:
                all_sat = False
                break
        if all_sat:
            return True

        # propagation
        if not propagate():
            # undo assignments made in this call
            while trail and assign[trail[-1]] != -1:
                assign[trail.pop()] = -1
            return False

        # pure literal elimination (optional)
        pure_eliminate()

        # choose unassigned variable
        for v in range(n):
            if assign[v] == -1:
                var = v
                break
        else:
            # all assigned, must be satisfied (checked earlier)
            return True

        # try 0 then 1
        for val in (0, 1):
            assign[var] = val
            trail.append(var)
            if dfs():
                return True
            # backtrack this branch
            while trail and assign[trail[-1]] != -1:
                assign[trail.pop()] = -1
        return False

    # start search
    if dfs():
        print("YES")
        print(' '.join(str(assign[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()