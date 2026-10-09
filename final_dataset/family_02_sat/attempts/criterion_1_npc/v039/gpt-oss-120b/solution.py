import sys

sys.setrecursionlimit(10000)

def solve_sat(n, clauses):
    # assignment: -1 unassigned, 0 false, 1 true
    assign = [-1] * n

    def propagate(assign, clauses):
        while True:
            unit = None
            for c in clauses:
                if len(c) == 1:
                    unit = c[0]
                    break
            if unit is None:
                break
            var = abs(unit) - 1
            val = 1 if unit > 0 else 0
            if assign[var] != -1:
                if assign[var] != val:
                    return None, None  # conflict
            else:
                assign[var] = val
                # simplify clauses
                new_clauses = []
                for cl in clauses:
                    if unit in cl:
                        continue  # clause satisfied
                    if -unit in cl:
                        new = [l for l in cl if l != -unit]
                        if not new:
                            return None, None  # empty clause
                        new_clauses.append(new)
                    else:
                        new_clauses.append(cl)
                clauses = new_clauses
        return assign, clauses

    def dpll(assign, clauses):
        assign, clauses = propagate(assign[:], clauses)
        if assign is None:
            return None
        if not clauses:
            return assign
        # choose variable
        for i in range(n):
            if assign[i] == -1:
                var = i
                break
        for val in (1, 0):  # try true then false
            new_assign = assign[:]
            new_assign[var] = val
            # simplify clauses with this assignment
            lit = var + 1 if val == 1 else -(var + 1)
            new_clauses = []
            conflict = False
            for cl in clauses:
                if lit in cl:
                    continue
                if -lit in cl:
                    new = [l for l in cl if l != -lit]
                    if not new:
                        conflict = True
                        break
                    new_clauses.append(new)
                else:
                    new_clauses.append(cl)
            if conflict:
                continue
            res = dpll(new_assign, new_clauses)
            if res is not None:
                return res
        return None

    return dpll(assign, clauses)


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        c = [int(next(it)), int(next(it)), int(next(it))]
        # remove duplicates within clause
        uniq = []
        seen = set()
        for lit in c:
            if lit not in seen:
                uniq.append(lit)
                seen.add(lit)
        clauses.append(uniq)

    ans = solve_sat(n, clauses)
    if ans is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(v if v != -1 else 0) for v in ans))

if __name__ == "__main__":
    main()