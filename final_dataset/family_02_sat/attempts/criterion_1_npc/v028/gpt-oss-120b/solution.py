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

    # assignment: -1 unassigned, 0 lower, 1 upper
    assign = [-1] * (n + 1)

    # For each variable, list of clause indices where it appears (positive or negative)
    var_pos = [[] for _ in range(n + 1)]
    var_neg = [[] for _ in range(n + 1)]
    for idx, cl in enumerate(clauses):
        for lit in cl:
            v = abs(lit)
            if lit > 0:
                var_pos[v].append(idx)
            else:
                var_neg[v].append(idx)

    # Helper to get literal value under current assignment
    def lit_val(lit):
        v = abs(lit)
        a = assign[v]
        if a == -1:
            return None
        return a if lit > 0 else 1 - a

    # Unit propagation stack
    def propagate(stack):
        while stack:
            v, val = stack.pop()
            if assign[v] != -1:
                if assign[v] != val:
                    return False
                continue
            assign[v] = val
            # check clauses where this literal appears positively/negatively
            affected = var_pos[v] if val == 1 else var_neg[v]
            for ci in affected:
                # clause satisfied, skip
                pass
            # check clauses where opposite literal appears (might become unit/conflict)
            opp = var_neg[v] if val == 1 else var_pos[v]
            for ci in opp:
                cl = clauses[ci]
                # evaluate clause
                true_found = False
                unassigned = []
                for lit in cl:
                    v2 = abs(lit)
                    a2 = assign[v2]
                    if a2 == -1:
                        unassigned.append(lit)
                    else:
                        if (lit > 0 and a2 == 1) or (lit < 0 and a2 == 0):
                            true_found = True
                            break
                if true_found:
                    continue
                if not unassigned:
                    return False  # all false
                if len(unassigned) == 1:
                    # unit clause, force it true
                    l = unassigned[0]
                    vv = abs(l)
                    need = 1 if l > 0 else 0
                    stack.append((vv, need))
        return True

    # Choose next variable (simple heuristic)
    def choose_var():
        for v in range(1, n + 1):
            if assign[v] == -1:
                return v
        return None

    def dfs():
        # find unassigned var
        v = choose_var()
        if v is None:
            return True
        # try 0 then 1
        saved = assign[:]
        for val in (0, 1):
            assign[:] = saved[:]
            if propagate([(v, val)]):
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