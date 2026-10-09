import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    streams = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        streams.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))

    # Number of variables = k * m
    num_vars = k * m

    # Build equality constraints (flow conservation)
    # For each stream i, for each node u: out - in = b
    eq_rows = []
    eq_rhs = []
    for i in range(k):
        s_i, t_i, d_i = streams[i]
        for u in range(1, n + 1):
            row = [0.0] * num_vars
            b = 0.0
            if u == s_i:
                b = float(d_i)
            elif u == t_i:
                b = float(-d_i)
            else:
                b = 0.0

            # out edges
            for e_idx, (src, dst, _) in enumerate(edges):
                var_idx = i * m + e_idx
                if src == u:
                    row[var_idx] += 1.0
                if dst == u:
                    row[var_idx] -= 1.0

            eq_rows.append(row)
            eq_rhs.append(b)

    # Build inequality constraints: sum_{i} f_{i, e} <= cap_e
    ineq_rows = []
    ineq_rhs = []
    for e_idx in range(m):
        row = [0.0] * num_vars
        for i in range(k):
            var_idx = i * m + e_idx
            row[var_idx] = 1.0
        ineq_rows.append(row)
        ineq_rhs.append(float(edges[e_idx][2]))

    # LP Solver using standard Tableau (Phase 1 & 2)
    def solve_lp(extra_bounds):
        # extra_bounds is a list of (var_idx, '<=' or '>=', val)
        # All original vars are >= 0
        # Convert all to standard form: A x = b, x >= 0
        # Rows:
        # eq_rows: row * x = rhs
        # ineq_rows: row * x + slack = rhs
        # extra_bounds:
        #   x_j <= v  =>  x_j + slack = v
        #   x_j >= v  =>  x_j - surplus = v

        num_slacks = len(ineq_rows)
        for _, op, _ in extra_bounds:
            num_slacks += 1

        total_vars = num_vars + num_slacks

        # We will build equality system: M * x_all = rhs_all
        # where x_all >= 0
        M = []
        rhs_all = []

        for r, b in zip(eq_rows, eq_rhs):
            M.append(list(r) + [0.0] * num_slacks)
            rhs_all.append(b)

        slack_idx = 0
        for r, b in zip(ineq_rows, ineq_rhs):
            row = list(r) + [0.0] * num_slacks
            row[num_vars + slack_idx] = 1.0
            slack_idx += 1
            M.append(row)
            rhs_all.append(b)

        for var_idx, op, val in extra_bounds:
            row = [0.0] * total_vars
            row[var_idx] = 1.0
            if op == "<=":
                row[num_vars + slack_idx] = 1.0
                rhs_all.append(float(val))
            else:  # '>='
                row[num_vars + slack_idx] = -1.0
                rhs_all.append(float(val))
            slack_idx += 1
            M.append(row)

        num_constraints = len(M)

        # Make all rhs >= 0
        for i in range(num_constraints):
            if rhs_all[i] < -1e-9:
                for j in range(total_vars):
                    M[i][j] = -M[i][j]
                rhs_all[i] = -rhs_all[i]
            elif abs(rhs_all[i]) <= 1e-9:
                rhs_all[i] = 0.0

        # Phase 1: Add artificial variables
        # Minimize sum of artificial variables
        # Tableau size: (num_constraints + 1) x (total_vars + num_constraints + 1)
        # Columns: [total_vars] [artificial_vars] [RHS]
        tableau = []
        for i in range(num_constraints):
            row = (
                M[i][:]
                + [0.0] * num_constraints
                + [rhs_all[i]]
            )
            row[total_vars + i] = 1.0
            tableau.append(row)

        # Phase 1 objective row: minimize sum(a_i)
        # Initially, cost row is sum of rows with artificial vars
        obj_row = [0.0] * (total_vars + num_constraints + 1)
        for i in range(num_constraints):
            for j in range(len(obj_row)):
                obj_row[j] -= tableau[i][j]
        tableau.append(obj_row)

        basis = [total_vars + i for i in range(num_constraints)]
        cols = total_vars + num_constraints

        # Simplex Phase 1
        while True:
            # Find entering column (most negative in obj row)
            pivot_col = -1
            min_val = -1e-8
            for j in range(cols):
                if tableau[-1][j] < min_val:
                    min_val = tableau[-1][j]
                    pivot_col = j

            if pivot_col == -1:
                break

            # Find leaving row (min ratio test)
            pivot_row = -1
            min_ratio = float("inf")
            for i in range(num_constraints):
                if tableau[i][pivot_col] > 1e-9:
                    ratio = tableau[i][-1] / tableau[i][pivot_col]
                    if ratio < min_ratio - 1e-9:
                        min_ratio = ratio
                        pivot_row = i

            if pivot_row == -1:
                # Unbounded in phase 1 (should not happen)
                break

            # Pivot
            p_val = tableau[pivot_row][pivot_col]
            for j in range(len(tableau[0])):
                tableau[pivot_row][j] /= p_val
            for i in range(num_constraints + 1):
                if i != pivot_row and abs(tableau[i][pivot_col]) > 1e-12:
                    factor = tableau[i][pivot_col]
                    for j in range(len(tableau[0])):
                        tableau[i][j] -= factor * tableau[pivot_row][j]
            basis[pivot_row] = pivot_col

        # Check if phase 1 found a feasible solution
        if abs(tableau[-1][-1]) > 1e-5:
            return None  # Infeasible

        # Extract solution
        sol = [0.0] * num_vars
        for i in range(num_constraints):
            if basis[i] < num_vars:
                sol[basis[i]] = tableau[i][-1]

        return sol

    # Branch and Bound
    best_sol = None
    stack = [[]]

    while stack:
        bounds = stack.pop()
        lp_res = solve_lp(bounds)
        if lp_res is None:
            continue

        # Check integrality
        frac_var = -1
        max_frac = 0.0
        for idx in range(num_vars):
            val = lp_res[idx]
            diff = abs(val - round(val))
            if diff > 1e-4 and diff > max_frac:
                max_frac = diff
                frac_var = idx

        if frac_var == -1:
            best_sol = [int(round(x)) for x in lp_res]
            break

        val = lp_res[frac_var]
        # Branch on frac_var
        stack.append(bounds + [(frac_var, ">=", int(val) + 1)])
        stack.append(bounds + [(frac_var, "<=", int(val))])

    if best_sol is None:
        print("NO")
    else:
        print("YES")
        for i in range(k):
            row = best_sol[i * m : (i + 1) * m]
            print(*(max(0, x) for x in row))


if __name__ == "__main__":
    solve()