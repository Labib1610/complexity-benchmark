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

    # unit propagation, returns False if conflict
    def propagate(assign):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                vals = [lit_val(l) for l in clause]
                # if any true, clause satisfied
                if any(v == 1 for v in vals):
                    continue
                # count falses and unknowns
                falses = sum(1 for v in vals if v == 0)
                unknowns = [i for i, v in enumerate(vals) if v is None]
                if falses == 3:
                    return False  # conflict
                if len(unknowns) == 1:
                    # unit clause, set that literal true
                    idx = unknowns[0]
                    lit = clause[idx]
                    var = abs(lit)
                    val = 1 if lit > 0 else 0
                    if assign[var] == -1:
                        assign[var] = val
                        changed = True
                    elif assign[var] != val:
                        return False
        return True

    def dfs(assign):
        if not propagate(assign):
            return None
        # find unassigned variable
        try:
            var = next(i for i in range(1, n + 1) if assign[i] == -1)
        except StopIteration:
            return assign  # all assigned, solution found
        # branch true
        for val in (1, 0):
            new_assign = assign[:]  # copy
            new_assign[var] = val
            res = dfs(new_assign)
            if res is not None:
                return res
        return None

    result = dfs(assign)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()