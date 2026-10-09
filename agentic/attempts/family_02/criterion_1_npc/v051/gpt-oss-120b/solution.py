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
        l1 = int(next(it)); l2 = int(next(it)); l3 = int(next(it))
        clauses.append([l1, l2, l3])

    # assignment: -1 unassigned, 0 false, 1 true
    assign = [-1] * (n + 1)

    # helper to get literal value under current assignment
    def lit_val(lit):
        v = abs(lit)
        a = assign[v]
        if a == -1:
            return None
        return a if lit > 0 else 1 - a

    # unit propagation and pure literal elimination
    def propagate(clauses):
        while True:
            # pure literals
            pos = [False] * (n + 1)
            neg = [False] * (n + 1)
            for cl in clauses:
                for lit in cl:
                    v = abs(lit)
                    if assign[v] != -1:
                        continue
                    if lit > 0:
                        pos[v] = True
                    else:
                        neg[v] = True
            changed = False
            for v in range(1, n + 1):
                if assign[v] == -1:
                    if pos[v] and not neg[v]:
                        assign[v] = 1
                        changed = True
                    elif neg[v] and not pos[v]:
                        assign[v] = 0
                        changed = True
            if changed:
                # after pure assignment, continue loop to simplify clauses
                continue

            # unit clauses
            unit_lit = None
            new_clauses = []
            for cl in clauses:
                satisfied = False
                unassigned = []
                for lit in cl:
                    val = lit_val(lit)
                    if val is True:
                        satisfied = True
                        break
                    elif val is None:
                        unassigned.append(lit)
                if satisfied:
                    continue
                if not unassigned:
                    return None  # conflict
                if len(unassigned) == 1:
                    unit_lit = unassigned[0]
                    break
                new_clauses.append(cl)
            if unit_lit is None:
                # no unit clause found
                return new_clauses
            # assign unit literal
            v = abs(unit_lit)
            assign[v] = 1 if unit_lit > 0 else 0
            # restart propagation
            clauses = new_clauses

    # DPLL recursive search
    def dpll(clauses):
        # simplify with propagation
        simplified = propagate(clauses)
        if simplified is None:
            return None
        # if all clauses satisfied
        if not simplified:
            return assign[1:].copy()
        # choose variable (first unassigned)
        for v in range(1, n + 1):
            if assign[v] == -1:
                var = v
                break
        # try true then false
        saved_assign = assign[:]
        for val in (1, 0):
            assign[var] = val
            res = dpll(simplified)
            if res is not None:
                return res
            assign[:] = saved_assign[:]
        return None

    result = dpll(clauses)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(x) for x in result))

if __name__ == "__main__":
    solve()