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

    # assignment: None = unassigned, 0 = false, 1 = true
    assign = [None] * (n + 1)

    # helper to get literal value under current assignment
    def lit_val(lit):
        v = abs(lit)
        a = assign[v]
        if a is None:
            return None
        return a if lit > 0 else 1 - a

    # unit propagation and pure literal elimination
    def propagate():
        changed = True
        while changed:
            changed = False
            # unit clauses
            for clause in clauses:
                vals = [lit_val(l) for l in clause]
                if any(v == 1 for v in vals):
                    continue  # already satisfied
                # count unassigned
                unassigned = [clause[i] for i, v in enumerate(vals) if v is None]
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val = 1 if lit > 0 else 0
                    if assign[var] is None:
                        assign[var] = val
                        changed = True
            # pure literals
            count = {}
            for clause in clauses:
                for lit in clause:
                    var = abs(lit)
                    if assign[var] is not None:
                        continue
                    count.setdefault(var, set()).add(lit > 0)
            for var, signs in list(count.items()):
                if len(signs) == 1:
                    # pure
                    val = 1 if True in signs else 0
                    assign[var] = val
                    changed = True
        return True

    def dfs():
        if not propagate():
            return False
        # check if all clauses satisfied
        all_sat = True
        for clause in clauses:
            if not any(lit_val(l) == 1 for l in clause):
                all_sat = False
                break
        if all_sat:
            return True
        # pick unassigned variable
        for v in range(1, n + 1):
            if assign[v] is None:
                var = v
                break
        # try true then false
        saved = assign[:]
        assign[var] = 1
        if dfs():
            return True
        assign[:] = saved
        assign[var] = 0
        if dfs():
            return True
        assign[:] = saved
        return False

    if dfs():
        print("YES")
        print(' '.join(str(assign[i] if assign[i] is not None else 0) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()