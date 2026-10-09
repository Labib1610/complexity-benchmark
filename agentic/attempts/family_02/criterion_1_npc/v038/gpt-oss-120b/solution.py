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

    assign = [None] * (n + 1)          # 1-indexed, values 0/1/None

    # helper to get literal value under current assignment
    def lit_val(lit):
        v = abs(lit)
        a = assign[v]
        if a is None:
            return None
        return a if lit > 0 else 1 - a

    # unit propagation and pure literal elimination
    def propagate(stack):
        while True:
            changed = False
            # unit clauses
            for cl in clauses:
                # check if clause already satisfied
                satisfied = False
                unassigned = []
                for lit in cl:
                    val = lit_val(lit)
                    if val == 1:
                        satisfied = True
                        break
                    elif val is None:
                        unassigned.append(lit)
                if satisfied:
                    continue
                if not unassigned:          # all false -> conflict
                    return False
                if len(unassigned) == 1:    # unit
                    lit = unassigned[0]
                    var = abs(lit)
                    val = 1 if lit > 0 else 0
                    if assign[var] is None:
                        assign[var] = val
                        stack.append(var)
                        changed = True
                    elif assign[var] != val:
                        return False
            if changed:
                continue

            # pure literals
            pos = [0] * (n + 1)
            neg = [0] * (n + 1)
            for cl in clauses:
                # skip satisfied clauses
                if any(lit_val(l) == 1 for l in cl):
                    continue
                for lit in cl:
                    v = abs(lit)
                    if assign[v] is None:
                        if lit > 0:
                            pos[v] = 1
                        else:
                            neg[v] = 1
            pure_found = False
            for v in range(1, n + 1):
                if assign[v] is None and (pos[v] ^ neg[v]):  # exactly one polarity appears
                    val = 1 if pos[v] else 0
                    assign[v] = val
                    stack.append(v)
                    pure_found = True
            if pure_found:
                continue
            break
        return True

    # recursive DPLL
    def dfs():
        stack = []
        if not propagate(stack):
            # undo
            for v in stack:
                assign[v] = None
            return False

        # check if all clauses satisfied
        all_sat = True
        for cl in clauses:
            if not any(lit_val(l) == 1 for l in cl):
                all_sat = False
                break
        if all_sat:
            return True

        # choose unassigned variable (heuristic: most occurrences)
        occ = [0] * (n + 1)
        for cl in clauses:
            if any(lit_val(l) == 1 for l in cl):
                continue
            for lit in cl:
                v = abs(lit)
                if assign[v] is None:
                    occ[v] += 1
        var = max(range(1, n + 1), key=lambda i: occ[i])
        # try 0 then 1
        for val in (0, 1):
            assign[var] = val
            if dfs():
                return True
            assign[var] = None
        # undo propagation assignments
        for v in stack:
            assign[v] = None
        return False

    possible = dfs()
    if not possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(assign[i] if assign[i] is not None else 0) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()