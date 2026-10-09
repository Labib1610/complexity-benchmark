import sys

sys.setrecursionlimit(10000)

def solve():
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

    assign = [-1] * (n + 1)  # 1-indexed, -1 unassigned, 0 false, 1 true

    # helper to get literal value under current assignment
    def lit_val(l):
        v = abs(l)
        a = assign[v]
        if a == -1:
            return None
        return a if l > 0 else 1 - a

    # propagation returns False if conflict, else list of variables assigned in this round
    def propagate(stack):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                vals = [lit_val(l) for l in clause]
                # if any true, clause satisfied
                if any(v == 1 for v in vals):
                    continue
                # count unassigned
                unassigned = [i for i, v in enumerate(vals) if v is None]
                if not unassigned:
                    # all false -> conflict
                    return False
                if len(unassigned) == 1:
                    # unit clause, must set that literal true
                    idx = unassigned[0]
                    l = clause[idx]
                    var = abs(l)
                    needed = 1 if l > 0 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        stack.append(var)
                        changed = True
                    elif assign[var] != needed:
                        return False
        return True

    # recursive DPLL
    def dfs():
        # find unassigned variable
        try:
            var = next(i for i in range(1, n + 1) if assign[i] == -1)
        except StopIteration:
            return True  # all assigned

        for val in (0, 1):
            # try setting var = val
            trail = []
            assign[var] = val
            trail.append(var)
            if propagate(trail):
                if dfs():
                    return True
            # backtrack
            for v in trail:
                assign[v] = -1
        return False

    if dfs():
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()