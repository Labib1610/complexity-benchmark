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
        c1 = int(next(it))
        c2 = int(next(it))
        c3 = int(next(it))
        clauses.append([c1, c2, c3])

    # assignment: -1 unassigned, 0 false, 1 true
    assign = [-1] * (n + 1)

    # helper to get literal value under current assignment
    def lit_val(lit):
        var = abs(lit)
        val = assign[var]
        if val == -1:
            return None
        return (val == 1) if lit > 0 else (val == 0)

    # unit propagation and pure literal elimination
    def propagate():
        while True:
            changed = False
            # unit clauses
            for cl in clauses:
                sat = False
                unassigned = None
                for lit in cl:
                    v = lit_val(lit)
                    if v is True:
                        sat = True
                        break
                    if v is None:
                        unassigned = lit
                if sat:
                    continue
                # none true
                if unassigned is None:
                    return False  # conflict
                # check if all others are false
                all_false = True
                for lit in cl:
                    if lit is unassigned:
                        continue
                    v = lit_val(lit)
                    if v is not False:
                        all_false = False
                        break
                if all_false:
                    # unit clause, must set unassigned literal true
                    var = abs(unassigned)
                    val = 1 if unassigned > 0 else 0
                    if assign[var] != -1:
                        if assign[var] != val:
                            return False
                    else:
                        assign[var] = val
                        changed = True
            if changed:
                continue

            # pure literals
            pos = [False] * (n + 1)
            neg = [False] * (n + 1)
            for cl in clauses:
                clause_sat = any(lit_val(lit) is True for lit in cl)
                if clause_sat:
                    continue
                for lit in cl:
                    v = lit_val(lit)
                    if v is not None:
                        continue
                    if lit > 0:
                        pos[abs(lit)] = True
                    else:
                        neg[abs(lit)] = True
            pure_found = False
            for var in range(1, n + 1):
                if assign[var] != -1:
                    continue
                if pos[var] and not neg[var]:
                    assign[var] = 1
                    pure_found = True
                elif neg[var] and not pos[var]:
                    assign[var] = 0
                    pure_found = True
            if pure_found:
                continue
            break
        return True

    def dfs():
        if not propagate():
            return False
        # check if all clauses satisfied
        all_sat = True
        for cl in clauses:
            if not any(lit_val(lit) is True for lit in cl):
                all_sat = False
                break
        if all_sat:
            return True
        # pick unassigned variable
        var = next(i for i in range(1, n + 1) if assign[i] == -1)
        # try true then false
        saved = assign[:]
        assign[var] = 1
        if dfs():
            return True
        assign[:] = saved
        assign[var] = 0
        if dfs():
            return True
        assign[:] = saved
        return False

    if dfs():
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()