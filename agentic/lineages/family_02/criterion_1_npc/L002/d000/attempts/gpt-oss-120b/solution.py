import sys

sys.setrecursionlimit(10000)

def solve_instance(n, clauses):
    # ---------- propagation ----------
    def propagate(assign):
        while True:
            unit_lit = None
            for cl in clauses:
                satisfied = False
                unassigned = []
                for lit in cl:
                    v = abs(lit) - 1
                    val = assign[v]
                    if val == -1:
                        unassigned.append(lit)
                    else:
                        lit_true = (val == 1 and lit > 0) or (val == 0 and lit < 0)
                        if lit_true:
                            satisfied = True
                            break
                if satisfied:
                    continue
                if not unassigned:          # all false -> conflict
                    return None
                if len(unassigned) == 1:   # unit clause
                    unit_lit = unassigned[0]
                    break
            if unit_lit is None:
                break
            v = abs(unit_lit) - 1
            needed = 1 if unit_lit > 0 else 0
            if assign[v] != -1 and assign[v] != needed:
                return None
            assign[v] = needed
        return assign

    # ---------- pure literal elimination ----------
    def pure_eliminate(assign):
        while True:
            pos = [False] * n
            neg = [False] * n
            for cl in clauses:
                # skip already satisfied clauses
                satisfied = False
                for lit in cl:
                    v = abs(lit) - 1
                    val = assign[v]
                    if val != -1:
                        lit_true = (val == 1 and lit > 0) or (val == 0 and lit < 0)
                        if lit_true:
                            satisfied = True
                            break
                if satisfied:
                    continue
                for lit in cl:
                    v = abs(lit) - 1
                    if assign[v] == -1:
                        if lit > 0:
                            pos[v] = True
                        else:
                            neg[v] = True
            pure_var = -1
            pure_val = None
            for i in range(n):
                if assign[i] == -1:
                    if pos[i] and not neg[i]:
                        pure_var = i
                        pure_val = 1
                        break
                    if neg[i] and not pos[i]:
                        pure_var = i
                        pure_val = 0
                        break
            if pure_var == -1:
                break
            assign[pure_var] = pure_val
        return assign

    # ---------- recursive DPLL ----------
    def dpll(assign):
        assign = propagate(assign[:])
        if assign is None:
            return None
        assign = pure_eliminate(assign[:])
        if assign is None:
            return None
        if all(v != -1 for v in assign):
            return assign
        # choose first unassigned variable
        var = assign.index(-1)
        for val in (0, 1):
            new_assign = assign[:]
            new_assign[var] = val
            res = dpll(new_assign)
            if res is not None:
                return res
        return None

    # start with all unassigned
    start = [-1] * n
    return dpll(start)


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        l1 = int(next(it)); l2 = int(next(it)); l3 = int(next(it))
        clauses.append([l1, l2, l3])

    ans = solve_instance(n, clauses)
    if ans is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(v) for v in ans))

if __name__ == "__main__":
    main()