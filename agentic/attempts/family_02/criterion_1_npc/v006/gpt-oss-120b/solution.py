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
    # for backtracking we store a trail of assigned variables
    trail = []

    # helper to get literal value under current assignment
    def lit_val(lit: int):
        v = assign[abs(lit)]
        if v == -1:
            return None
        return v if lit > 0 else 1 - v

    # unit propagation
    def propagate() -> bool:
        while True:
            unit_lit = None
            for clause in clauses:
                vals = [lit_val(l) for l in clause]
                # count satisfied literals
                if any(v == 1 for v in vals):
                    continue  # clause already satisfied
                # count unassigned
                unassigned = [clause[i] for i, v in enumerate(vals) if v is None]
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    unit_lit = unassigned[0]
                    break
            if unit_lit is None:
                break
            var = abs(unit_lit)
            val = 1 if unit_lit > 0 else 0
            if assign[var] == -1:
                assign[var] = val
                trail.append(var)
            elif assign[var] != val:
                return False
        return True

    # pure literal elimination (optional but cheap)
    def pure_eliminate() -> bool:
        while True:
            count = {}
            for clause in clauses:
                for lit in clause:
                    v = assign[abs(lit)]
                    if v != -1:
                        continue
                    count[lit] = count.get(lit, 0) + 1
            pure = None
            for lit, cnt in count.items():
                if -lit not in count:
                    pure = lit
                    break
            if pure is None:
                break
            var = abs(pure)
            val = 1 if pure > 0 else 0
            assign[var] = val
            trail.append(var)
            if not propagate():
                return False
        return True

    # recursive DPLL
    def dpll() -> bool:
        if not propagate():
            return False
        if not pure_eliminate():
            return False
        # check if all assigned
        if all(v != -1 for v in assign[1:]):
            return True
        # choose variable (first unassigned)
        for var in range(1, n + 1):
            if assign[var] == -1:
                break
        # try true then false
        saved_len = len(trail)
        for val in (1, 0):
            assign[var] = val
            trail.append(var)
            if dpll():
                return True
            # backtrack
            while len(trail) > saved_len:
                v = trail.pop()
                assign[v] = -1
        return False

    if dpll():
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()