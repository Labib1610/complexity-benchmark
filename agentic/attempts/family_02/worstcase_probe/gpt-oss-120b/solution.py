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

    # ---------- helper functions ----------
    def literal_value(lit, assign):
        """None = unknown, True/False = value of literal."""
        var = abs(lit)
        a = assign[var]
        if a == -1:
            return None
        return (a == 1) if lit > 0 else (a == 0)

    def clause_status(clause, assign):
        """1 = satisfied, 0 = falsified, -1 = undetermined."""
        unknown = False
        for lit in clause:
            val = literal_value(lit, assign)
            if val is True:
                return 1
            if val is None:
                unknown = True
        return -1 if unknown else 0

    def all_clauses_satisfied(assign):
        for cl in clauses:
            if clause_status(cl, assign) != 1:
                return False
        return True

    # ---------- unit propagation ----------
    def unit_propagate(assign):
        changed = True
        while changed:
            changed = False
            for cl in clauses:
                st = clause_status(cl, assign)
                if st == 1:
                    continue
                # collect unassigned literals
                unassigned = []
                for lit in cl:
                    var = abs(lit)
                    if assign[var] == -1:
                        unassigned.append(lit)
                if not unassigned:          # all false -> conflict
                    return True
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    needed = 1 if lit > 0 else 0
                    if assign[var] == -1:
                        assign[var] = needed
                        changed = True
                    elif assign[var] != needed:
                        return True
        return False  # no conflict

    # ---------- pure literal elimination ----------
    def pure_literal_assign(assign):
        while True:
            pos = set()
            neg = set()
            for cl in clauses:
                if clause_status(cl, assign) == 1:
                    continue
                for lit in cl:
                    var = abs(lit)
                    if assign[var] == -1:
                        if lit > 0:
                            pos.add(var)
                        else:
                            neg.add(var)
            pure_found = False
            for var in range(1, n + 1):
                if assign[var] != -1:
                    continue
                if var in pos and var not in neg:
                    assign[var] = 1
                    pure_found = True
                elif var in neg and var not in pos:
                    assign[var] = 0
                    pure_found = True
            if not pure_found:
                break

    # ---------- variable selection ----------
    def choose_unassigned(assign):
        for i in range(1, n + 1):
            if assign[i] == -1:
                return i
        return -1  # should not happen

    # ---------- DPLL ----------
    def dpll(assign):
        if unit_propagate(assign):
            return None
        pure_literal_assign(assign)

        if all_clauses_satisfied(assign):
            return assign

        var = choose_unassigned(assign)
        for val in (1, 0):
            new_assign = assign[:]
            new_assign[var] = val
            res = dpll(new_assign)
            if res is not None:
                return res
        return None

    # ---------- start ----------
    start_assign = [-1] * (n + 1)
    result = dpll(start_assign)

    out = []
    if result is None:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(result[i]) for i in range(1, n + 1)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()