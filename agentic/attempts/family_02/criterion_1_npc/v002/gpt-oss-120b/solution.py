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
        clause = [int(next(it)) for _ in range(3)]
        clauses.append(clause)

    # assignment: None = unassigned, True = IN (1), False = OUT (0)
    assign = [None] * (n + 1)

    # helper to get literal value under current assignment
    def lit_val(lit):
        v = assign[abs(lit)]
        if v is None:
            return None
        return v if lit > 0 else (not v)

    # unit propagation, returns False if conflict
    def propagate():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                # evaluate clause
                satisfied = False
                unassigned_lits = []
                for lit in clause:
                    val = lit_val(lit)
                    if val is True:
                        satisfied = True
                        break
                    if val is None:
                        unassigned_lits.append(lit)
                if satisfied:
                    continue
                if not unassigned_lits:
                    # all false -> conflict
                    return False
                if len(unassigned_lits) == 1:
                    # unit clause
                    unit = unassigned_lits[0]
                    var = abs(unit)
                    val = unit > 0
                    if assign[var] is None:
                        assign[var] = val
                        changed = True
                    elif assign[var] != val:
                        return False
        return True

    # pure literal elimination (optional but helps)
    def pure_eliminate():
        while True:
            counts = {}
            for clause in clauses:
                for lit in clause:
                    if assign[abs(lit)] is not None:
                        continue
                    counts[lit] = counts.get(lit, 0) + 1
            pure = None
            for lit, cnt in counts.items():
                if -lit not in counts:
                    pure = lit
                    break
            if pure is None:
                break
            var = abs(pure)
            assign[var] = pure > 0

    def choose_var():
        for i in range(1, n + 1):
            if assign[i] is None:
                return i
        return None

    def backtrack() -> bool:
        if not propagate():
            return False
        pure_eliminate()
        var = choose_var()
        if var is None:
            return True  # all assigned
        # try True then False
        saved = assign[:]
        assign[var] = True
        if backtrack():
            return True
        assign[:] = saved
        assign[var] = False
        if backtrack():
            return True
        assign[:] = saved
        return False

    if backtrack():
        print("YES")
        print(' '.join('1' if assign[i] else '0' for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()