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

    # assignment: -1 unassigned, 0 false, 1 true
    assign = [-1] * (n + 1)

    # helper to get literal value under current assignment
    def lit_val(lit):
        v = assign[abs(lit)]
        if v == -1:
            return None
        return v if lit > 0 else 1 - v

    # unit propagation and pure literal elimination
    def propagate():
        changed = True
        while changed:
            changed = False
            # unit clauses
            for clause in clauses:
                cnt_un = 0
                last_un = None
                satisfied = False
                for lit in clause:
                    val = lit_val(lit)
                    if val is None:
                        cnt_un += 1
                        last_un = lit
                    elif val == 1:
                        satisfied = True
                        break
                if satisfied:
                    continue
                if cnt_un == 0:  # all false -> conflict
                    return False
                if cnt_un == 1:
                    # force last_un to be true
                    var = abs(last_un)
                    needed = 1 if last_un > 0 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        changed = True
                    elif assign[var] != needed:
                        return False
            # pure literals
            pos = [False] * (n + 1)
            neg = [False] * (n + 1)
            for clause in clauses:
                for lit in clause:
                    v = assign[abs(lit)]
                    if v != -1:
                        continue
                    if lit > 0:
                        pos[abs(lit)] = True
                    else:
                        neg[abs(lit)] = True
            for var in range(1, n + 1):
                if assign[var] != -1:
                    continue
                if pos[var] and not neg[var]:
                    assign[var] = 1
                    changed = True
                elif neg[var] and not pos[var]:
                    assign[var] = 0
                    changed = True
        return True

    # choose next variable (most occurrences)
    occ = [0] * (n + 1)
    for clause in clauses:
        for lit in clause:
            occ[abs(lit)] += 1
    order = sorted(range(1, n + 1), key=lambda x: -occ[x])

    def dfs(idx: int) -> bool:
        if not propagate():
            return False
        # check if all assigned
        if all(assign[i] != -1 for i in range(1, n + 1)):
            return True
        # pick next unassigned variable according to order
        for var in order:
            if assign[var] == -1:
                break
        # try true then false
        saved = assign[:]
        assign[var] = 1
        if dfs(idx + 1):
            return True
        assign[:] = saved
        assign[var] = 0
        if dfs(idx + 1):
            return True
        assign[:] = saved
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()