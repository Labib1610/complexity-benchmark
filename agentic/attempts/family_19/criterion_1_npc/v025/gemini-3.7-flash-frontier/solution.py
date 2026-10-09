import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    rituals = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        rituals.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    num_vars = k * m

    eq_rows = []
    eq_rhs = []
    for i in range(k):
        s_i, t_i, d_i = rituals[i]
        for u in range(n):
            row = [0.0] * num_vars
            for e in range(m):
                u_e, v_e, _ = edges[e]
                idx = i * m + e
                if u_e == u:
                    row[idx] += 1.0
                if v_e == u:
                    row[idx] -= 1.0

            rhs = 0.0
            if u == s_i:
                rhs = float(d_i)
            elif u == t_i:
                rhs = -float(d_i)

            eq_rows.append(row)
            eq_rhs.append(rhs)

    ineq_rows = []
    ineq_rhs = []
    for e in range(m):
        row = [0.0] * num_vars
        for i in range(k):
            row[i * m + e] = 1.0
        ineq_rows.append(row)
        ineq_rhs.append(float(edges[e][2]))

    def solve_lp(extra_bounds):
        A = []
        b = []

        for r, rhs in zip(eq_rows, eq_rhs):
            A.append(list(r))
            b.append(rhs)
            A.append([-x for x in r])
            b.append(-rhs)

        for r, rhs in zip(ineq_rows, ineq_rhs):
            A.append(list(r))
            b.append(rhs)

        for var_idx, (lb, ub) in extra_bounds.items():
            if lb > 0:
                row = [0.0] * num_vars
                row[var_idx] = -1.0
                A.append(row)
                b.append(-float(lb))
            if ub is not None:
                row = [0.0] * num_vars
                row[var_idx] = 1.0
                A.append(row)
                b.append(float(ub))

        num_constraints = len(A)
        n_total = num_vars + num_constraints
        tableau = [
            [0.0] * (n_total + 1) for _ in range(num_constraints + 2)
        ]  # +2 for Phase I and II

        for i in range(num_constraints):
            for j in range(num_vars):
                tableau[i][j] = A[i][j]
            tableau[i][num_vars + i] = 1.0
            tableau[i][-1] = b[i]

        basis = [num_vars + i for i in range(num_constraints)]

        for i in range(num_constraints):
            if tableau[i][-1] < -1e-9:
                for j in range(len(tableau[i])):
                    tableau[i][j] = -tableau[i][j]

        # Phase I
        art_vars = []
        for i in range(num_constraints):
            if b[i] < -1e-9:
                tableau[num_constraints][num_vars + i] = 1.0
                art_vars.append(i)

        p1_row = num_constraints
        for i in range(num_constraints):
            tableau[p1_row][-1] += 0.0

        for col in range(n_total):
            sum_val = 0.0
            for i in art_vars:
                sum_val += tableau[i][col]
            tableau[p1_row][col] -= sum_val
        for i in art_vars:
            tableau[p1_row][-1] -= tableau[i][-1]

        def pivot(r, c):
            basis[r] = c
            piv = tableau[r][c]
            for j in range(len(tableau[r])):
                tableau[r][j] /= piv
            for i in range(len(tableau)):
                if i != r:
                    factor = tableau[i][c]
                    if abs(factor) > 1e-12:
                        for j in range(len(tableau[r])):
                            tableau[i][j] -= factor * tableau[r][j]

        # Phase I simplex
        while True:
            c = -1
            min_val = -1e-7
            for j in range(n_total):
                if tableau[p1_row][j] < min_val:
                    min_val = tableau[p1_row][j]
                    c = j
            if c == -1:
                break

            r = -1
            min_ratio = float("inf")
            for i in range(num_constraints):
                if tableau[i][c] > 1e-9:
                    ratio = tableau[i][-1] / tableau[i][c]
                    if ratio < min_ratio - 1e-9:
                        min_ratio = ratio
                        r = i
            if r == -1:
                break
            pivot(r, c)

        if abs(tableau[p1_row][-1]) > 1e-5:
            return None

        sol = [0.0] * num_vars
        for i in range(num_constraints):
            if basis[i] < num_vars:
                sol[basis[i]] = max(0.0, tableau[i][-1])

        return sol

    def branch_and_bound(bounds):
        sol = solve_lp(bounds)
        if sol is None:
            return None

        frac_var = -1
        max_dist = 0.0
        for i, val in enumerate(sol):
            dist = abs(val - round(val))
            if dist > 1e-4 and dist > max_dist:
                max_dist = dist
                frac_var = i

        if frac_var == -1:
            return [int(round(x)) for x in sol]

        val = sol[frac_var]
        floor_val = int(val)
        ceil_val = floor_val + 1

        b1 = bounds.copy()
        cur_lb, cur_ub = b1.get(frac_var, (0, None))
        b1[frac_var] = (cur_lb, floor_val)
        res = branch_and_bound(b1)
        if res is not None:
            return res

        b2 = bounds.copy()
        cur_lb, cur_ub = b2.get(frac_var, (0, None))
        b2[frac_var] = (ceil_val, cur_ub)
        return branch_and_bound(b2)

    initial_bounds = {}
    for e in range(m):
        for i in range(k):
            initial_bounds[i * m + e] = (0, edges[e][2])

    result = branch_and_bound(initial_bounds)
    if result is None:
        print("NO")
    else:
        print("YES")
        for i in range(k):
            row = result[i * m : (i + 1) * m]
            print(*(max(0, x) for x in row))


if __name__ == "__main__":
    solve()