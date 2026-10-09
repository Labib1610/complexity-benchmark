import sys

sys.setrecursionlimit(10000)

def solve_sat(n, clauses):
    # ------------------------------------------------------------
    # helpers
    def clause_satisfied(cl):
        """return True if clause already satisfied under current assign"""
        for lit in cl:
            v = abs(lit)
            a = assign[v]
            if a != -1 and ((a == 1 and lit > 0) or (a == 0 and lit < 0)):
                return True
        return False

    def unit_propagate():
        """perform unit propagation, return True if conflict detected"""
        while True:
            unit_lit = None
            for cl in clauses:
                # skip satisfied clauses
                if clause_satisfied(cl):
                    continue
                unassigned = []
                for lit in cl:
                    v = abs(lit)
                    a = assign[v]
                    if a == -1:
                        unassigned.append(lit)
                    else:
                        # literal already false, continue
                        pass
                if not unassigned:          # all three false -> conflict
                    return True
                if len(unassigned) == 1:    # unit clause
                    unit_lit = unassigned[0]
                    break
            else:
                break          # no unit clause found

            # assign the forced literal
            v = abs(unit_lit)
            val = 1 if unit_lit > 0 else 0
            if assign[v] == -1:
                assign[v] = val
            elif assign[v] != val:
                return True    # contradictory assignment
        return False

    def pure_literal_assign():
        """assign pure literals, return True if conflict occurs"""
        while True:
            pos = [False] * (n + 1)
            neg = [False] * (n + 1)
            any_unsat = False
            for cl in clauses:
                if clause_satisfied(cl):
                    continue
                any_unsat = True
                for lit in cl:
                    v = abs(lit)
                    if assign[v] == -1:
                        if lit > 0:
                            pos[v] = True
                        else:
                            neg[v] = True
            if not any_unsat:
                break
            changed = False
            for v in range(1, n + 1):
                if assign[v] != -1:
                    continue
                if pos[v] and not neg[v]:
                    assign[v] = 1
                    changed = True
                elif neg[v] and not pos[v]:
                    assign[v] = 0
                    changed = True
            if not changed:
                break
            if unit_propagate():
                return True
        return False

    def all_clauses_satisfied():
        for cl in clauses:
            if not clause_satisfied(cl):
                return False
        return True

    def choose_variable():
        """heuristic: variable occurring most often in unsatisfied clauses"""
        cnt = [0] * (n + 1)
        for cl in clauses:
            if clause_satisfied(cl):
                continue
            for lit in cl:
                v = abs(lit)
                if assign[v] == -1:
                    cnt[v] += 1
        best = -1
        var = -1
        for v in range(1, n + 1):
            if assign[v] == -1 and cnt[v] > best:
                best = cnt[v]
                var = v
        return var

    # ------------------------------------------------------------
    # recursive DPLL
    def dpll():
        if unit_propagate():
            return None
        if pure_literal_assign():
            return None
        if all_clauses_satisfied():
            return assign[:]

        var = choose_variable()
        if var == -1:          # all variables assigned but some clause unsatisfied
            return None

        for val in (1, 0):
            saved = assign[:]
            assign[var] = val
            res = dpll()
            if res is not None:
                return res
            assign[:] = saved
        return None

    # start with all unassigned
    assign = [-1] * (n + 1)
    return dpll()


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        clauses.append([l1, l2, l3])

    result = solve_sat(n, clauses)
    if result is None:
        print("NO")
    else:
        print("YES")
        # result[0] is dummy
        print(' '.join(str(result[i]) if result[i] != -1 else '0' for i in range(1, n + 1)))

if __name__ == "__main__":
    main()