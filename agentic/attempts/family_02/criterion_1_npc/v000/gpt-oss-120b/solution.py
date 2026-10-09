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
        l1 = int(next(it)); l2 = int(next(it)); l3 = int(next(it))
        clauses.append((l1, l2, l3))

    # assignment: None = unassigned, 0 = false, 1 = true
    assign = [None] * n

    # helper to get literal value under current assignment
    def lit_val(lit):
        v = assign[abs(lit) - 1]
        if v is None:
            return None
        return v if lit > 0 else 1 - v

    # unit propagation, returns False if conflict
    def propagate():
        changed = True
        while changed:
            changed = False
            for c in clauses:
                vals = [lit_val(l) for l in c]
                if any(v == 1 for v in vals):
                    continue  # clause already satisfied
                # count unassigned
                unassigned = [c[i] for i, v in enumerate(vals) if v is None]
                if not unassigned:
                    # all false -> conflict
                    return False
                if len(unassigned) == 1:
                    # force this literal to true
                    lit = unassigned[0]
                    var = abs(lit) - 1
                    needed = 1 if lit > 0 else 0
                    if assign[var] is None:
                        assign[var] = needed
                        changed = True
                    elif assign[var] != needed:
                        return False
        return True

    # recursive DPLL
    def dpll():
        if not propagate():
            return False
        # check if all assigned
        if all(v is not None for v in assign):
            return True
        # choose unassigned variable
        var = next(i for i, v in enumerate(assign) if v is None)
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
        print(' '.join(str(v) for v in assign))
    else:
        print("NO")

if __name__ == "__main__":
    solve()