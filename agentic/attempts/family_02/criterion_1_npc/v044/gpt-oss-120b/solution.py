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
        clauses.append((a, b, c))

    assign = [-1] * (n + 1)          # -1 unknown, 0 false, 1 true

    def lit_value(lit):
        v = assign[abs(lit)]
        if v == -1:
            return None
        return (v == 1) if lit > 0 else (v == 0)

    def undo(stack):
        for var in stack:
            assign[var] = -1

    def dfs() -> bool:
        # ---- unit propagation -----------------------------------------
        forced = []          # variables forced in this call
        while True:
            changed = False
            for a, b, c in clauses:
                vals = [lit_value(a), lit_value(b), lit_value(c)]
                if any(v is True for v in vals):
                    continue
                # clause not yet satisfied
                unassigned = [l for v, l in zip(vals, (a, b, c)) if v is None]
                if not unassigned:          # all false -> conflict
                    undo(forced)
                    return False
                if len(unassigned) == 1:    # unit clause
                    lit = unassigned[0]
                    var = abs(lit)
                    need = 1 if lit > 0 else 0
                    if assign[var] == -1:
                        assign[var] = need
                        forced.append(var)
                        changed = True
                    elif assign[var] != need:
                        undo(forced)
                        return False
            if not changed:
                break

        # ---- all assigned? --------------------------------------------
        if all(v != -1 for v in assign[1:]):
            return True

        # ---- choose variable, branch ----------------------------------
        var = next(i for i in range(1, n + 1) if assign[i] == -1)
        for val in (0, 1):
            assign[var] = val
            if dfs():
                return True
            assign[var] = -1
        undo(forced)
        return False

    if dfs():
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()