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

    # unit propagation, returns False if conflict
    def propagate(stack):
        while True:
            unit_lit = None
            for clause in clauses:
                satisfied = False
                unassigned = []
                for l in clause:
                    val = lit_val(l)
                    if val == 1:
                        satisfied = True
                        break
                    elif val is None:
                        unassigned.append(l)
                if satisfied:
                    continue
                if not unassigned:  # all false
                    return False
                if len(unassigned) == 1:
                    unit_lit = unassigned[0]
                    break
            if unit_lit is None:
                break
            v = abs(unit_lit)
            val = 1 if unit_lit > 0 else 0
            if assign[v] != -1:
                if assign[v] != val:
                    return False
                continue
            assign[v] = val
            stack.append(v)
        return True

    # recursive DPLL
    def dfs():
        # first propagate
        stack = []
        if not propagate(stack):
            for v in stack:
                assign[v] = -1
            return False

        # check if all assigned
        if all(a != -1 for a in assign[1:]):
            return True

        # choose variable (simple heuristic: first unassigned)
        for v in range(1, n + 1):
            if assign[v] == -1:
                var = v
                break

        # try true then false
        for val in (1, 0):
            assign[var] = val
            if dfs():
                return True
            assign[var] = -1  # backtrack
        # undo propagation assignments
        for v in stack:
            assign[v] = -1
        return False

    if dfs():
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()