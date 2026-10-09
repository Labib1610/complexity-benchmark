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
        lits = [int(next(it)), int(next(it)), int(next(it))]
        clauses.append(lits)

    # helper to get var index and required value from literal
    def lit_info(lit):
        v = abs(lit) - 1
        val = 1 if lit > 0 else 0
        return v, val

    def propagate(assign):
        """perform unit propagation, return (conflict, new_assign)"""
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                sat = False
                unassigned = []
                for lit in clause:
                    v, val = lit_info(lit)
                    a = assign[v]
                    if a == -1:
                        unassigned.append(lit)
                    elif a == val:
                        sat = True
                        break
                if sat:
                    continue
                if not unassigned:
                    return True, assign  # conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    v, val = lit_info(lit)
                    if assign[v] == -1:
                        assign[v] = val
                        changed = True
                    elif assign[v] != val:
                        return True, assign  # conflict
        return False, assign

    def dfs(assign):
        conflict, assign = propagate(assign)
        if conflict:
            return None
        # check if all assigned
        if all(v != -1 for v in assign):
            return assign
        # choose variable with heuristic: first unassigned
        v = assign.index(-1)
        for val in (0, 1):
            new_assign = assign[:]
            new_assign[v] = val
            res = dfs(new_assign)
            if res is not None:
                return res
        return None

    initial = [-1] * n
    result = dfs(initial)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(x) for x in result))

if __name__ == "__main__":
    solve()