import sys

# Increase recursion depth for deep DPLL search trees
sys.setrecursionlimit(20000)


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
        trivially_true = False
        for lit in c_set:
            if -lit in c_set:
                trivially_true = True
                break
        if not trivially_true:
            clauses.append(list(c_set))

    def dpll(clauses, assignment):
        assignment = list(assignment)
        # Unit propagation loop
        while True:
            unit_found = False
            for c in clauses:
                sat = False
                unassigned = []
                for lit in c:
                    var = abs(lit)
                    val = assignment[var]
                    if (lit > 0 and val == 1) or (lit < 0 and val == -1):
                        sat = True
                        break
                    elif val == 0:
                        unassigned.append(lit)
                if sat:
                    continue
                if not unassigned:
                    return None
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    req_val = 1 if lit > 0 else -1
                    if assignment[var] == -req_val:
                        return None
                    if assignment[var] == 0:
                        assignment[var] = req_val
                        unit_found = True
            if not unit_found:
                break

        # Check clause satisfaction and collect active clauses for branching
        all_sat = True
        active_clauses = []
        for c in clauses:
            sat = False
            unassigned_lits = []
            for lit in c:
                var = abs(lit)
                val = assignment[var]
                if (lit > 0 and val == 1) or (lit < 0 and val == -1):
                    sat = True
                    break
                elif val == 0:
                    unassigned_lits.append(lit)
            if not sat:
                all_sat = False
                active_clauses.append(unassigned_lits)

        if all_sat:
            return assignment

        # Two-sided Jeroslow-Wang Heuristic
        j_pos = [0.0] * (n + 1)
        j_neg = [0.0] * (n + 1)
        for c in active_clauses:
            weight = 2 ** (-len(c))
            for lit in c:
                if lit > 0:
                    j_pos[lit] += weight
                else:
                    j_neg[-lit] += weight

        best_var = 0
        best_score = -1.0
        for v in range(1, n + 1):
            if assignment[v] == 0:
                score = j_pos[v] + j_neg[v]
                if score > best_score:
                    best_score = score
                    best_var = v

        if best_var == 0:
            return assignment

        first_val = 1 if j_pos[best_var] >= j_neg[best_var] else -1

        # Branch on best variable
        assignment[best_var] = first_val
        res = dpll(clauses, assignment)
        if res is not None:
            return res

        assignment[best_var] = -first_val
        res = dpll(clauses, assignment)
        if res is not None:
            return res

        return None

    assignment = [0] * (n + 1)
    ans = dpll(clauses, assignment)
    if ans is None:
        print("NO")
    else:
        print("YES")
        out = [1 if ans[i] == 1 else 0 for i in range(1, n + 1)]
        print(*(out))


if __name__ == "__main__":
    solve()