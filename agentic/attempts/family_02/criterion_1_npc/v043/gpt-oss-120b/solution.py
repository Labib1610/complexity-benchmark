import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    clauses = []
    for _ in range(m):
        clause = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(clause)

    assign = [ -1 ] * (n + 1)   # -1 unassigned, 0 false, 1 true

    # helper to get literal value under current assignment
    def lit_val(lit):
        v = assign[abs(lit)]
        if v == -1:
            return None
        return v if lit > 0 else 1 - v

    # unit propagation, returns False if conflict
    def propagate():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                # evaluate clause
                satisfied = False
                unassigned = []
                for lit in clause:
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
                    # unit clause, force literal true
                    lit = unassigned[0]
                    var = abs(lit)
                    needed = 1 if lit > 0 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        changed = True
                    elif assign[var] != needed:
                        return False
        return True

    # pure literal elimination
    def pure_eliminate():
        while True:
            counts = {}
            for clause in clauses:
                for lit in clause:
                    if assign[abs(lit)] != -1:
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
            assign[var] = 1 if pure > 0 else 0

    # recursive DPLL
    def dpll():
        if not propagate():
            return False
        pure_eliminate()
        # check if all variables assigned
        if all(v != -1 for v in assign[1:]):
            return True
        # choose unassigned variable
        var = next(i for i in range(1, n+1) if assign[i] == -1)
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
        print(' '.join(str(assign[i]) for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()