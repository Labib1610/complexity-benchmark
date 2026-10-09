import sys


def solve_sat():
    sys.setrecursionlimit(2000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    clauses = []
    idx = 2
    for _ in range(m):
        c = [
            int(input_data[idx]),
            int(input_data[idx + 1]),
            int(input_data[idx + 2]),
        ]
        idx += 3
        clauses.append(c)

    def dpll(assign):
        assign = list(assign)
        while True:
            unit_found = False
            for c in clauses:
                val = False
                unassigned_lits = []
                for lit in c:
                    var = abs(lit)
                    if assign[var] is not None:
                        if (lit > 0 and assign[var]) or (
                            lit < 0 and not assign[var]
                        ):
                            val = True
                            break
                    else:
                        unassigned_lits.append(lit)

                if val:
                    continue
                if len(unassigned_lits) == 0:
                    return None
                if len(unassigned_lits) == 1:
                    lit = unassigned_lits[0]
                    var = abs(lit)
                    new_val = lit > 0
                    if assign[var] is None:
                        assign[var] = new_val
                        unit_found = True
                    elif assign[var] != new_val:
                        return None

            if not unit_found:
                break

        unassigned = [v for v in range(1, n + 1) if assign[v] is None]
        if not unassigned:
            for c in clauses:
                sat = False
                for lit in c:
                    var = abs(lit)
                    if (lit > 0 and assign[var]) or (
                        lit < 0 and not assign[var]
                    ):
                        sat = True
                        break
                if not sat:
                    return None
            return assign

        scores_pos = {v: 0.0 for v in unassigned}
        scores_neg = {v: 0.0 for v in unassigned}

        all_satisfied = True
        for c in clauses:
            sat = False
            unres = []
            for lit in c:
                var = abs(lit)
                if assign[var] is not None:
                    if (lit > 0 and assign[var]) or (
                        lit < 0 and not assign[var]
                    ):
                        sat = True
                        break
                else:
                    unres.append(lit)
            if not sat:
                all_satisfied = False
                w = 2.0 ** (-len(unres))
                for lit in unres:
                    var = abs(lit)
                    if lit > 0:
                        scores_pos[var] += w
                    else:
                        scores_neg[var] += w

        if all_satisfied:
            for v in unassigned:
                assign[v] = True
            return assign

        best_v = None
        best_val = True
        best_score = -1.0

        for v in unassigned:
            if scores_pos[v] > best_score:
                best_score = scores_pos[v]
                best_v = v
                best_val = True
            if scores_neg[v] > best_score:
                best_score = scores_neg[v]
                best_v = v
                best_val = False

        assign[best_v] = best_val
        res = dpll(assign)
        if res is not None:
            return res

        assign[best_v] = not best_val
        return dpll(assign)

    initial_assign = [None] * (n + 1)
    result = dpll(initial_assign)
    if result is None:
        print("NO")
    else:
        print("YES")
        ans = ["1" if result[v] else "0" for v in range(1, n + 1)]
        print(" ".join(ans))


if __name__ == "__main__":
    solve_sat()