import sys, random, time

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        lits = []
        for _ in range(3):
            v = int(next(it))
            var = abs(v) - 1
            sign = v > 0          # True means variable should be 1 (OPEN)
            lits.append((var, sign))
        clauses.append(lits)

    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return

    start_time = time.time()
    TIME_LIMIT = 1.8  # seconds, leave margin

    # helper to evaluate clause
    def clause_ok(assign, clause):
        for var, sign in clause:
            if assign[var] == sign:
                return True
        return False

    # main randomized walk
    while time.time() - start_time < TIME_LIMIT:
        # random initial assignment
        assign = [random.choice([False, True]) for _ in range(n)]
        unsat = [i for i, cl in enumerate(clauses) if not clause_ok(assign, cl)]
        steps = 0
        max_steps = 2 * m
        while unsat and steps < max_steps:
            steps += 1
            ci = random.choice(unsat)
            clause = clauses[ci]
            # pick a random literal from the clause to flip
            var, _ = random.choice(clause)
            assign[var] = not assign[var]
            # recompute unsatisfied list (fast enough for given limits)
            unsat = [i for i, cl in enumerate(clauses) if not clause_ok(assign, cl)]
        if not unsat:
            # found solution
            print("YES")
            print(" ".join('1' if v else '0' for v in assign))
            return

    # if random search failed, fall back to deterministic DFS with pruning
    # simple recursive backtracking with early clause checking
    sys.setrecursionlimit(10000)
    clause_by_var = [[] for _ in range(n)]
    for idx, cl in enumerate(clauses):
        for var, _ in cl:
            clause_by_var[var].append(idx)

    assign = [None] * n
    clause_sat = [False] * m

    def dfs(pos: int) -> bool:
        if pos == n:
            return all(clause_sat)
        for val in (False, True):
            assign[pos] = val
            changed = []
            ok = True
            for ci in clause_by_var[pos]:
                if clause_sat[ci]:
                    continue
                cl = clauses[ci]
                if any(assign[v] is not None and assign[v] == s for v, s in cl):
                    clause_sat[ci] = True
                    changed.append(ci)
                else:
                    # check if clause can still become true later
                    if all(assign[v] is not None for v, _ in cl):
                        ok = False
                        break
            if ok and dfs(pos + 1):
                return True
            for ci in changed:
                clause_sat[ci] = False
        assign[pos] = None
        return False

    if dfs(0):
        print("YES")
        print(" ".join('1' if v else '0' for v in assign))
    else:
        print("NO")

if __name__ == "__main__":
    solve()