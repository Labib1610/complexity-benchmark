import sys

sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        clause = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(clause)

    # assignment: -1 unassigned, 0 false, 1 true
    assign = [-1] * (n + 1)

    def lit_value(lit):
        var = abs(lit)
        val = assign[var]
        if val == -1:
            return None
        return val if lit > 0 else 1 - val

    def clause_status(cl):
        # returns: 1 if satisfied, 0 if falsified, -1 if undetermined
        any_true = False
        any_undef = False
        for lit in cl:
            v = lit_value(lit)
            if v == 1:
                return 1
            if v is None:
                any_undef = True
        return -1 if any_undef else 0

    def propagate():
        changed = True
        while changed:
            changed = False
            # unit clauses
            for cl in clauses:
                status = clause_status(cl)
                if status == 1:
                    continue
                # count undefined literals
                undef = []
                for lit in cl:
                    if lit_value(lit) is None:
                        undef.append(lit)
                if not undef:  # falsified
                    return False
                if len(undef) == 1:
                    lit = undef[0]
                    var = abs(lit)
                    val = 1 if lit > 0 else 0
                    if assign[var] == -1:
                        assign[var] = val
                        changed = True
                    elif assign[var] != val:
                        return False
            # pure literals
            pos = [0] * (n + 1)
            neg = [0] * (n + 1)
            for cl in clauses:
                if clause_status(cl) == 1:
                    continue
                for lit in cl:
                    var = abs(lit)
                    if assign[var] != -1:
                        continue
                    if lit > 0:
                        pos[var] = 1
                    else:
                        neg[var] = 1
            for var in range(1, n + 1):
                if assign[var] == -1:
                    if pos[var] and not neg[var]:
                        assign[var] = 1
                        changed = True
                    elif neg[var] and not pos[var]:
                        assign[var] = 0
                        changed = True
        return True

    def dfs():
        if not propagate():
            return None
        # check if all variables assigned
        if all(v != -1 for v in assign[1:]):
            # final verification
            for cl in clauses:
                if clause_status(cl) != 1:
                    return None
            return assign[1:]
        # pick unassigned variable
        var = next(i for i in range(1, n + 1) if assign[i] == -1)
        # try 0 then 1
        saved = assign[:]
        assign[var] = 0
        res = dfs()
        if res is not None:
            return res
        assign[:] = saved
        assign[var] = 1
        res = dfs()
        if res is not None:
            return res
        assign[:] = saved
        return None

    result = dfs()
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()