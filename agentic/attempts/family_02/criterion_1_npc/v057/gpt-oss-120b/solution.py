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
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        clauses.append([a, b, c])

    # assignment: None = unassigned, 0 = false, 1 = true
    assign = [None] * (n + 1)

    # helper to get literal value under current assignment
    def lit_val(lit):
        v = abs(lit)
        val = assign[v]
        if val is None:
            return None
        return val if lit > 0 else 1 - val

    # unit propagation and pure literal elimination
    def propagate():
        changed = True
        while changed:
            changed = False
            # unit clauses
            for cl in clauses:
                unassigned = []
                satisfied = False
                for lit in cl:
                    val = lit_val(lit)
                    if val is None:
                        unassigned.append(lit)
                    elif val == 1:
                        satisfied = True
                        break
                if satisfied:
                    continue
                if not unassigned:   # all false -> conflict
                    return False
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    needed = 1 if lit > 0 else 0
                    if assign[var] is None:
                        assign[var] = needed
                        changed = True
                    elif assign[var] != needed:
                        return False
            # pure literals
            pos = [False] * (n + 1)
            neg = [False] * (n + 1)
            for cl in clauses:
                clause_sat = False
                for lit in cl:
                    v = abs(lit)
                    if assign[v] is None:
                        if lit > 0:
                            pos[v] = True
                        else:
                            neg[v] = True
                    else:
                        if lit_val(lit) == 1:
                            clause_sat = True
                            break
                if clause_sat:
                    continue
            for v in range(1, n + 1):
                if assign[v] is None:
                    if pos[v] and not neg[v]:
                        assign[v] = 1
                        changed = True
                    elif neg[v] and not pos[v]:
                        assign[v] = 0
                        changed = True
        return True

    # recursive DPLL
    def dpll():
        if not propagate():
            return False
        # check if all clauses satisfied
        all_sat = True
        for cl in clauses:
            clause_sat = False
            for lit in cl:
                val = lit_val(lit)
                if val == 1:
                    clause_sat = True
                    break
            if not clause_sat:
                all_sat = False
                break
        if all_sat:
            return True
        # choose unassigned variable
        for v in range(1, n + 1):
            if assign[v] is None:
                var = v
                break
        # try true then false
        saved = assign[:]
        assign[var] = 1
        if dpll():
            return True
        assign[:] = saved
        assign[var] = 0
        if dpll():
            return True
        assign[:] = saved
        return False

    if dpll():
        print("YES")
        print(' '.join(str(assign[i] if assign[i] is not None else 0) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()