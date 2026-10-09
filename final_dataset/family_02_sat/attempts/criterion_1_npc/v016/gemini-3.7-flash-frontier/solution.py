import sys

sys.setrecursionlimit(5000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    raw_clauses = []
    idx = 2
    for _ in range(m):
        c = [int(input_data[idx]), int(input_data[idx + 1]), int(input_data[idx + 2])]
        idx += 3
        c_set = set(c)
        tautology = False
        for x in c_set:
            if -x in c_set:
                tautology = True
                break
        if not tautology:
            raw_clauses.append(list(c_set))

    clauses = raw_clauses
    assignment = [None] * (n + 1)
    pow2 = [1.0, 0.5, 0.25, 0.125, 0.0625]

    def get_lit_val(lit):
        v = abs(lit)
        val = assignment[v]
        if val is None:
            return None
        return (val == 1) if lit > 0 else (val == 0)

    def solve_dpll():
        trail = []

        while True:
            unit_found = False
            for c in clauses:
                sat = False
                unassigned_lit = None
                unassigned_cnt = 0
                for lit in c:
                    val = get_lit_val(lit)
                    if val is True:
                        sat = True
                        break
                    elif val is None:
                        unassigned_cnt += 1
                        unassigned_lit = lit
                if sat:
                    continue
                if unassigned_cnt == 0:
                    for v in trail:
                        assignment[v] = None
                    return False
                if unassigned_cnt == 1:
                    v = abs(unassigned_lit)
                    val = 1 if unassigned_lit > 0 else 0
                    if assignment[v] is None:
                        assignment[v] = val
                        trail.append(v)
                        unit_found = True
                    elif assignment[v] != val:
                        for v_t in trail:
                            assignment[v_t] = None
                        return False
            if not unit_found:
                break

        pos_score = [0.0] * (n + 1)
        neg_score = [0.0] * (n + 1)
        all_sat = True

        for c in clauses:
            sat = False
            unassigned_lits = []
            for lit in c:
                val = get_lit_val(lit)
                if val is True:
                    sat = True
                    break
                elif val is None:
                    unassigned_lits.append(lit)
            if not sat:
                all_sat = False
                k = len(unassigned_lits)
                w = pow2[k] if k < len(pow2) else 2.0**-k
                for lit in unassigned_lits:
                    if lit > 0:
                        pos_score[lit] += w
                    else:
                        neg_score[-lit] += w

        if all_sat:
            return True

        best_var = -1
        best_score = -1.0
        for v in range(1, n + 1):
            if assignment[v] is None:
                s = pos_score[v] + neg_score[v]
                if s > best_score:
                    best_score = s
                    best_var = v

        if best_var == -1:
            return True

        if pos_score[best_var] >= neg_score[best_var]:
            first_val, second_val = 1, 0
        else:
            first_val, second_val = 0, 1

        assignment[best_var] = first_val
        if solve_dpll():
            return True
        assignment[best_var] = None

        assignment[best_var] = second_val
        if solve_dpll():
            return True
        assignment[best_var] = None

        for v in trail:
            assignment[v] = None
        return False

    if solve_dpll():
        print("YES")
        res = [str(assignment[i] if assignment[i] is not None else 0) for i in range(1, n + 1)]
        print(*(res))
    else:
        print("NO")


if __name__ == "__main__":
    solve()