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
        c = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(c)

    # assignment: -1 unknown, 0 false, 1 true
    assign0 = [-1] * (n + 1)

    def lit_value(lit, assign):
        v = assign[abs(lit)]
        if v == -1:
            return None
        return v if lit > 0 else 1 - v

    def clause_status(clause, assign):
        # returns: 1 if satisfied, -1 if conflict, 0 otherwise (undetermined)
        unknown = False
        for lit in clause:
            val = lit_value(lit, assign)
            if val == 1:
                return 1
            if val is None:
                unknown = True
        return -1 if not unknown else 0

    def propagate(assign):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                status = clause_status(clause, assign)
                if status == -1:
                    return False
                if status == 0:
                    # check for unit
                    unassigned = []
                    for lit in clause:
                        if lit_value(lit, assign) is None:
                            unassigned.append(lit)
                    if len(unassigned) == 1:
                        lit = unassigned[0]
                        var = abs(lit)
                        val = 1 if lit > 0 else 0
                        if assign[var] == -1:
                            assign[var] = val
                            changed = True
                        elif assign[var] != val:
                            return False
        return True

    def dpll(assign):
        if not propagate(assign):
            return None
        # check if all clauses satisfied
        all_sat = True
        for clause in clauses:
            if clause_status(clause, assign) != 1:
                all_sat = False
                break
        if all_sat:
            return assign
        # pick unassigned variable
        for var in range(1, n + 1):
            if assign[var] == -1:
                break
        # try true
        for val in (1, 0):
            new_assign = assign[:]
            new_assign[var] = val
            res = dpll(new_assign)
            if res is not None:
                return res
        return None

    result = dpll(assign0)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()