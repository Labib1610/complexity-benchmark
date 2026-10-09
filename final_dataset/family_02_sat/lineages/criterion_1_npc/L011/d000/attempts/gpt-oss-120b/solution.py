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
        lits = [int(next(it)) for _ in range(3)]
        clauses.append(lits)

    # assignment: -1 = unassigned, 0 = false (secondary), 1 = true (primary)
    assign = [-1] * (n + 1)

    # check if clause is satisfied under current assignment
    def clause_sat(cl):
        for lit in cl:
            v = abs(lit)
            val = assign[v]
            if val == -1:
                continue
            if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                return True
        return False

    # check if clause is falsified (all literals assigned and false)
    def clause_false(cl):
        for lit in cl:
            v = abs(lit)
            val = assign[v]
            if val == -1:
                return False
            if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                return False
        return True

    # pick first unsatisfied clause
    def pick_clause():
        for cl in clauses:
            if not clause_sat(cl):
                return cl
        return None

    # recursive search with depth limit = n
    def dfs(depth: int) -> bool:
        # all clauses satisfied?
        if all(clause_sat(cl) for cl in clauses):
            return True
        if depth == n:
            return False
        cl = pick_clause()
        if cl is None:
            return True
        # try each literal in the clause
        for lit in cl:
            v = abs(lit)
            needed = 1 if lit > 0 else 0
            old = assign[v]
            if old != -1 and old != needed:
                continue  # conflict, cannot set this way
            # set and recurse
            assign[v] = needed
            if dfs(depth + 1):
                return True
            assign[v] = old  # backtrack
        return False

    possible = dfs(0)
    if not possible:
        print("NO")
    else:
        print("YES")
        res = [str(assign[i] if assign[i] != -1 else 0) for i in range(1, n + 1)]
        print(" ".join(res))

if __name__ == "__main__":
    solve()