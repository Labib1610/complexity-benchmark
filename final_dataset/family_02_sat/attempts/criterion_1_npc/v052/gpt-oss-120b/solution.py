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

    # assignment: -1 unassigned, 0 false, 1 true
    assign = [-1] * (n + 1)

    # For quick lookup of clauses containing each variable
    var_clauses = [[] for _ in range(n + 1)]
    for idx, cl in enumerate(clauses):
        for lit in cl:
            var = abs(lit)
            var_clauses[var].append(idx)

    # evaluate clause status given current assignment
    # returns: 0 = unsatisfied, 1 = satisfied, 2 = undetermined (some literals unassigned, none true yet)
    def clause_status(cl):
        sat = False
        undet = False
        for lit in cl:
            v = abs(lit)
            a = assign[v]
            if a == -1:
                undet = True
            else:
                val = a if lit > 0 else 1 - a
                if val == 1:
                    sat = True
                    break
        if sat:
            return 1
        return 2 if undet else 0

    # check for conflict; also collect unit literals if any
    def propagate():
        stack = []
        while True:
            unit_lit = None
            for idx, cl in enumerate(clauses):
                st = clause_status(cl)
                if st == 0:
                    return False
                if st == 2:
                    # count unassigned literals
                    unassigned = []
                    for lit in cl:
                        v = abs(lit)
                        if assign[v] == -1:
                            unassigned.append(lit)
                    if len(unassigned) == 1:
                        unit_lit = unassigned[0]
                        break
            if unit_lit is None:
                break
            v = abs(unit_lit)
            val = 1 if unit_lit > 0 else 0
            if assign[v] != -1:
                if assign[v] != val:
                    return False
                continue
            assign[v] = val
            stack.append(v)
        return True

    # simple heuristic: choose unassigned variable with most occurrences
    order = sorted(range(1, n + 1), key=lambda x: -len(var_clauses[x]))

    def dfs(pos: int) -> bool:
        if pos == n:
            # all assigned, check all clauses
            for cl in clauses:
                if clause_status(cl) != 1:
                    return False
            return True
        var = order[pos]
        if assign[var] != -1:
            return dfs(pos + 1)

        # try true then false
        saved = assign[:]
        for val in (1, 0):
            assign[var] = val
            if propagate():
                if dfs(pos + 1):
                    return True
            # restore
            assign[:] = saved[:]
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()