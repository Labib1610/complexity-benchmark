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
        c = [int(next(it)) for _ in range(3)]
        clauses.append(c)

    assign = [-1] * (n + 1)  # 1-indexed

    # helper to evaluate clause under current assignment
    def clause_status(cl):
        """return 1 if satisfied, 0 if unsatisfied, -1 if undetermined"""
        unk = False
        for lit in cl:
            var = abs(lit)
            val = assign[var]
            if val == -1:
                unk = True
            else:
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    return 1
        return -1 if unk else 0

    # unit propagation and pure literal elimination
    def propagate():
        while True:
            changed = False
            # unit clauses
            for cl in clauses:
                status = clause_status(cl)
                if status == 0:
                    return False
                if status == -1:
                    # count unassigned literals
                    unassigned = []
                    for lit in cl:
                        var = abs(lit)
                        if assign[var] == -1:
                            unassigned.append(lit)
                    if len(unassigned) == 1:
                        lit = unassigned[0]
                        var = abs(lit)
                        val = 1 if lit > 0 else 0
                        if assign[var] != -1 and assign[var] != val:
                            return False
                        if assign[var] == -1:
                            assign[var] = val
                            changed = True
            if changed:
                continue
            # pure literals
            polarity = [0] * (n + 1)  # 0 none, 1 only positive, -1 only negative, 2 both
            for cl in clauses:
                if clause_status(cl) == 1:
                    continue
                for lit in cl:
                    var = abs(lit)
                    if assign[var] != -1:
                        continue
                    if lit > 0:
                        if polarity[var] == 0:
                            polarity[var] = 1
                        elif polarity[var] == -1:
                            polarity[var] = 2
                    else:
                        if polarity[var] == 0:
                            polarity[var] = -1
                        elif polarity[var] == 1:
                            polarity[var] = 2
            for var in range(1, n + 1):
                if assign[var] == -1 and polarity[var] in (1, -1):
                    assign[var] = 1 if polarity[var] == 1 else 0
                    changed = True
            if not changed:
                break
        return True

    # recursive DPLL
    def dpll():
        if not propagate():
            return False
        # check if all clauses satisfied
        all_sat = True
        for cl in clauses:
            if clause_status(cl) != 1:
                all_sat = False
                break
        if all_sat:
            return True
        # choose unassigned variable
        var = next(i for i in range(1, n + 1) if assign[i] == -1)
        # try 0 then 1
        saved = assign[:]
        assign[var] = 0
        if dpll():
            return True
        assign[:] = saved
        assign[var] = 1
        if dpll():
            return True
        assign[:] = saved
        return False

    if dpll():
        print("YES")
        print(' '.join(str(assign[i] if assign[i]!=-1 else 0) for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()