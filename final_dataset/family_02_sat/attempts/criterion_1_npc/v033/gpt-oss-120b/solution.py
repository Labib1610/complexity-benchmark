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
        c = [int(next(it)) for _ in range(3)]
        clauses.append(c)

    # assignment: 0=unassigned, 1=True (UP), -1=False (DOWN)
    assign = [0] * (n + 1)

    # helper: evaluate literal under current assignment
    def lit_val(lit):
        v = assign[abs(lit)]
        if v == 0:
            return 0
        return v if lit > 0 else -v

    # unit propagation, returns False if conflict
    def propagate():
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                # count satisfied literals, collect unassigned
                sat = False
                unassigned = None
                for lit in clause:
                    val = lit_val(lit)
                    if val == 1:
                        sat = True
                        break
                    if val == 0:
                        if unassigned is None:
                            unassigned = lit
                        else:
                            # more than one unassigned, can't be unit yet
                            unassigned = None
                if sat:
                    continue
                # clause not yet satisfied
                # check how many literals are false
                false_cnt = sum(1 for lit in clause if lit_val(lit) == -1)
                if false_cnt == 3:
                    return False  # conflict
                if false_cnt == 2 and unassigned is not None:
                    # unit clause, force the remaining literal true
                    var = abs(unassigned)
                    val = 1 if unassigned > 0 else -1
                    if assign[var] == 0:
                        assign[var] = val
                        changed = True
                    elif assign[var] != val:
                        return False
        return True

    # recursive DPLL
    def dpll():
        if not propagate():
            return False
        # check if all variables assigned
        if all(v != 0 for v in assign[1:]):
            return True
        # choose unassigned variable (simple heuristic)
        var = next(i for i in range(1, n + 1) if assign[i] == 0)
        # try True then False
        saved = assign[:]
        assign[var] = 1
        if dpll():
            return True
        assign[:] = saved
        assign[var] = -1
        if dpll():
            return True
        assign[:] = saved
        return False

    if dpll():
        print("YES")
        print(' '.join('1' if assign[i] == 1 else '0' for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()