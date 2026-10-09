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
        c = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(c)

    # variable assignment: -1 unassigned, 0 false, 1 true
    assign = [-1] * (n + 1)

    # for each variable, store clauses where it appears positively / negatively
    pos_occ = [[] for _ in range(n + 1)]
    neg_occ = [[] for _ in range(n + 1)]
    for idx, cl in enumerate(clauses):
        for lit in cl:
            var = abs(lit)
            if lit > 0:
                pos_occ[var].append(idx)
            else:
                neg_occ[var].append(idx)

    # helper to get literal value under current assignment
    def lit_val(lit: int) -> int:
        v = assign[abs(lit)]
        if v == -1:
            return -1
        return v if lit > 0 else 1 - v  # true if matches sign

    # propagation stack
    stack = []

    def propagate() -> bool:
        """perform unit propagation, return False if conflict."""
        while True:
            unit_found = False
            for idx, cl in enumerate(clauses):
                # evaluate clause
                vals = [lit_val(l) for l in cl]
                if any(v == 1 for v in vals):
                    continue  # already satisfied
                # count unassigned
                unassigned = [i for i, v in enumerate(vals) if v == -1]
                if not unassigned:
                    # all false -> conflict
                    return False
                if len(unassigned) == 1:
                    # unit clause, force literal
                    lit = cl[unassigned[0]]
                    var = abs(lit)
                    needed = 1 if lit > 0 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        stack.append(var)
                        unit_found = True
                    elif assign[var] != needed:
                        return False
            if not unit_found:
                break
        return True

    # heuristic: choose unassigned variable with most occurrences
    occ_count = [len(pos_occ[i]) + len(neg_occ[i]) for i in range(n + 1)]

    def choose_var() -> int:
        best = -1
        bestc = -1
        for v in range(1, n + 1):
            if assign[v] == -1 and occ_count[v] > bestc:
                bestc = occ_count[v]
                best = v
        return best

    def dfs() -> bool:
        if not propagate():
            return False
        # check if all assigned
        if all(a != -1 for a in assign[1:]):
            return True
        var = choose_var()
        # try true then false
        saved_len = len(stack)
        for val in (1, 0):
            assign[var] = val
            stack.append(var)
            if dfs():
                return True
            # backtrack
            while len(stack) > saved_len:
                v = stack.pop()
                assign[v] = -1
        return False

    if dfs():
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()