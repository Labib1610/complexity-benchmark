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
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        clauses.append((a, b, c))

    # assignment: -1 unknown, 0 false, 1 true
    assign0 = [-1] * (n + 1)

    # helper: evaluate literal under current assignment
    def lit_val(lit, assign):
        v = abs(lit)
        val = assign[v]
        if val == -1:
            return None
        if lit > 0:
            return val == 1
        else:
            return val == 0

    # propagation, returns (True, new_assign) or (False, None) on conflict
    def propagate(assign):
        changed = True
        while changed:
            changed = False
            for (a, b, c) in clauses:
                vals = [lit_val(a, assign), lit_val(b, assign), lit_val(c, assign)]
                # count true / false / unknown
                if any(v is True for v in vals):
                    continue  # already satisfied
                false_cnt = sum(v is False for v in vals)
                unk_idxs = [i for i, v in enumerate(vals) if v is None]
                if false_cnt == 3:
                    return False, None  # conflict
                if false_cnt == 2 and len(unk_idxs) == 1:
                    # unit clause, force the remaining literal to be true
                    idx = unk_idxs[0]
                    lit = (a, b, c)[idx]
                    var = abs(lit)
                    needed = 1 if lit > 0 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        changed = True
                    elif assign[var] != needed:
                        return False, None
        return True, assign

    # recursive DPLL
    def dfs(assign):
        ok, assign = propagate(assign)
        if not ok:
            return None
        # check if complete
        if all(v != -1 for v in assign[1:]):
            return assign
        # choose variable (first unknown)
        v = next(i for i in range(1, n + 1) if assign[i] == -1)
        for val in (0, 1):
            new_assign = assign[:]  # copy
            new_assign[v] = val
            res = dfs(new_assign)
            if res is not None:
                return res
        return None

    result = dfs(assign0)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()