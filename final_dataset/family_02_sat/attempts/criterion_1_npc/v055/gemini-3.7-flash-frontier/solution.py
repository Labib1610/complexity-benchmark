import sys

# Increase recursion depth just in case
sys.setrecursionlimit(5000)


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
        clauses.append(c)

    assign = [None] * (n + 1)
    trail = []

    def get_lit_val(lit):
        v = assign[abs(lit)]
        if v is None:
            return None
        return v if lit > 0 else not v

    def unit_propagate():
        while True:
            unit_found = False
            for c in clauses:
                unassigned_lit = None
                satisfied = False
                unassigned_count = 0
                for lit in c:
                    val = get_lit_val(lit)
                    if val is True:
                        satisfied = True
                        break
                    elif val is None:
                        unassigned_count += 1
                        unassigned_lit = lit

                if satisfied:
                    continue
                if unassigned_count == 0:
                    return False  # Conflict
                if unassigned_count == 1:
                    var = abs(unassigned_lit)
                    target_val = True if unassigned_lit > 0 else False
                    assign[var] = target_val
                    trail.append(var)
                    unit_found = True
                    break
            if not unit_found:
                break
        return True

    def dpll():
        start_len = len(trail)
        if not unit_propagate():
            while len(trail) > start_len:
                assign[trail.pop()] = None
            return False

        jw_pos = [0.0] * (n + 1)
        jw_neg = [0.0] * (n + 1)
        unassigned_vars = set()

        all_satisfied = True
        for c in clauses:
            satisfied = False
            open_lits = []
            for lit in c:
                val = get_lit_val(lit)
                if val is True:
                    satisfied = True
                    break
                elif val is None:
                    open_lits.append(lit)
            if not satisfied:
                all_satisfied = False
                weight = 2.0 ** (-len(open_lits))
                for lit in open_lits:
                    var = abs(lit)
                    unassigned_vars.add(var)
                    if lit > 0:
                        jw_pos[var] += weight
                    else:
                        jw_neg[var] += weight

        if all_satisfied:
            return True

        best_var = max(unassigned_vars, key=lambda v: jw_pos[v] + jw_neg[v])
        first_val = jw_pos[best_var] >= jw_neg[best_var]

        for val in [first_val, not first_val]:
            branch_start = len(trail)
            assign[best_var] = val
            trail.append(best_var)
            if dpll():
                return True
            while len(trail) > branch_start:
                assign[trail.pop()] = None

        while len(trail) > start_len:
            assign[trail.pop()] = None
        return False

    if dpll():
        print("YES")
        res = [1 if assign[i] is True else 0 for i in range(1, n + 1)]
        print(*(res))
    else:
        print("NO")


if __name__ == "__main__":
    solve()