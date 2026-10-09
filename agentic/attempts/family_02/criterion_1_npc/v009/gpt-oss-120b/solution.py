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
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        clauses.append((a, b, c))

    assign = [None] * (n + 1)          # 1‑based

    # ---------- helper ----------
    def lit_is_true(lit):
        v = assign[abs(lit)]
        if v is None:
            return None
        return v == 1 if lit > 0 else v == 0

    # ---------- unit propagation + pure literal ----------
    def propagate():
        # queue of literals that must become true
        queue = []
        while True:
            # pure literal detection
            pos = [0] * (n + 1)
            neg = [0] * (n + 1)
            for cl in clauses:
                satisfied = False
                for lit in cl:
                    val = lit_is_true(lit)
                    if val is True:
                        satisfied = True
                        break
                if satisfied:
                    continue
                for lit in cl:
                    if assign[abs(lit)] is None:
                        if lit > 0:
                            pos[abs(lit)] = 1
                        else:
                            neg[abs(lit)] = 1
            for v in range(1, n + 1):
                if assign[v] is None:
                    if pos[v] and not neg[v]:
                        queue.append(v)          # set to 1
                    elif neg[v] and not pos[v]:
                        queue.append(-v)         # set to 0

            # unit clauses
            for cl in clauses:
                # check if already satisfied
                if any(lit_is_true(l) is True for l in cl):
                    continue
                unassigned = []
                for lit in cl:
                    if assign[abs(lit)] is None:
                        unassigned.append(lit)
                if not unassigned:          # all false -> conflict
                    return False
                if len(unassigned) == 1:
                    queue.append(unassigned[0])

            if not queue:
                break
            lit = queue.pop()
            var = abs(lit)
            needed = 1 if lit > 0 else 0
            if assign[var] is not None:
                if assign[var] != needed:
                    return False
                continue
            assign[var] = needed
        return True

    # ---------- DPLL ----------
    def dpll():
        if not propagate():
            return False
        # check if all assigned
        if all(v is not None for v in assign[1:]):
            return True
        # choose first unassigned variable
        for v in range(1, n + 1):
            if assign[v] is None:
                var = v
                break
        # try 0 then 1
        saved = assign[:]
        assign[var] = 0
        if dpll():
            return True
        assign[:] = saved
        assign[var] = 1
        if dpll():
            return True
        assign[:] = saved
        return False

    if dpll():
        print("YES")
        print(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()