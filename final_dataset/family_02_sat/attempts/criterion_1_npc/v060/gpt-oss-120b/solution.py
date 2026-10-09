import sys
sys.setrecursionlimit(10000)

def solve_instance(n, clauses):
    # value of a literal under current assignment
    def lit_val(lit, assign):
        v = assign[abs(lit)]
        if v == -1:
            return -1
        return 1 if (lit > 0 and v == 1) or (lit < 0 and v == 0) else 0

    # unit propagation, returns False on conflict
    def propagate(assign):
        while True:
            unit = None
            for c in clauses:
                cnt_true = 0
                cnt_un = 0
                last_un = None
                for lit in c:
                    v = lit_val(lit, assign)
                    if v == 1:
                        cnt_true += 1
                        break
                    elif v == -1:
                        cnt_un += 1
                        last_un = lit
                if cnt_true:
                    continue
                if cnt_un == 0:          # all false
                    return False
                if cnt_un == 1:
                    unit = last_un
                    break
            if unit is None:
                return True
            var = abs(unit)
            val = 1 if unit > 0 else 0
            if assign[var] != -1:
                if assign[var] != val:
                    return False
            else:
                assign[var] = val

    # pure literal elimination
    def pure_eliminate(assign):
        while True:
            pos = [False] * (n + 1)
            neg = [False] * (n + 1)
            for c in clauses:
                for lit in c:
                    v = assign[abs(lit)]
                    if v != -1:
                        continue
                    if lit > 0:
                        pos[abs(lit)] = True
                    else:
                        neg[abs(lit)] = True
            changed = False
            for v in range(1, n + 1):
                if assign[v] == -1:
                    if pos[v] and not neg[v]:
                        assign[v] = 1
                        changed = True
                    elif neg[v] and not pos[v]:
                        assign[v] = 0
                        changed = True
            if not changed:
                return True
            if not propagate(assign):
                return False

    def dpll(assign):
        if not propagate(assign):
            return None
        if not pure_eliminate(assign):
            return None
        if all(assign[i] != -1 for i in range(1, n + 1)):
            return assign
        # choose first unassigned variable
        for v in range(1, n + 1):
            if assign[v] == -1:
                var = v
                break
        for val in (1, 0):
            new_assign = assign[:]
            new_assign[var] = val
            res = dpll(new_assign)
            if res is not None:
                return res
        return None

    init_assign = [-1] * (n + 1)
    return dpll(init_assign)


def main():
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
    ans = solve_instance(n, clauses)
    if ans is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()