import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    clauses = []
    idx = 2
    for _ in range(m):
        c = [int(input_data[idx]), int(input_data[idx + 1]), int(input_data[idx + 2])]
        idx += 3
        c_set = set(c)
        tautology = False
        for lit in list(c_set):
            if -lit in c_set:
                tautology = True
                break
        if not tautology:
            clauses.append(list(c_set))

    assignment = [None] * (n + 1)

    def dpll(clauses, assignment):
        # Unit propagation
        while True:
            unit_literals = set()
            for c in clauses:
                unassigned = []
                sat = False
                for lit in c:
                    var = abs(lit)
                    val = assignment[var]
                    if val is not None:
                        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                            sat = True
                            break
                    else:
                        unassigned.append(lit)
                if sat:
                    continue
                if len(unassigned) == 0:
                    return False
                if len(unassigned) == 1:
                    unit_literals.add(unassigned[0])

            if not unit_literals:
                break

            for lit in unit_literals:
                var = abs(lit)
                val = 1 if lit > 0 else 0
                if assignment[var] is not None:
                    if assignment[var] != val:
                        return False
                else:
                    assignment[var] = val

        # Evaluate active clauses
        active_clauses = []
        for c in clauses:
            sat = False
            for lit in c:
                var = abs(lit)
                val = assignment[var]
                if val is not None and ((lit > 0 and val == 1) or (lit < 0 and val == 0)):
                    sat = True
                    break
            if not sat:
                active_clauses.append([lit for lit in c if assignment[abs(lit)] is None])

        if not active_clauses:
            for i in range(1, n + 1):
                if assignment[i] is None:
                    assignment[i] = 0
            return True

        # Heuristic: Jeroslow-Wang
        score_pos = [0.0] * (n + 1)
        score_neg = [0.0] * (n + 1)
        for c in active_clauses:
            w = 2.0 ** (-len(c))
            for lit in c:
                if lit > 0:
                    score_pos[lit] += w
                else:
                    score_neg[-lit] += w

        best_var = -1
        best_score = -1.0
        for var in range(1, n + 1):
            if assignment[var] is None:
                sc = score_pos[var] + score_neg[var] + score_pos[var] * score_neg[var]
                if sc > best_score:
                    best_score = sc
                    best_var = var

        if best_var == -1:
            for i in range(1, n + 1):
                if assignment[i] is None:
                    assignment[i] = 0
            return True

        first_val = 1 if score_pos[best_var] >= score_neg[best_var] else 0

        saved = assignment[:]
        assignment[best_var] = first_val
        if dpll(clauses, assignment):
            return True

        assignment[:] = saved
        assignment[best_var] = 1 - first_val
        if dpll(clauses, assignment):
            return True

        assignment[:] = saved
        return False

    if dpll(clauses, assignment):
        print("YES")
        print(*(assignment[1 : n + 1]))
    else:
        print("NO")


if __name__ == "__main__":
    solve()