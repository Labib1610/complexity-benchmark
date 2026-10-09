import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    groups = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        groups.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # Number of primary variables: k * m
    num_vars = k * m

    # Build equality constraints: A_eq * x = b_eq
    # 1. Flow conservation for each group i and zone u
    # 2. Capacity constraints: sum_i x_{i, e} + slack_e = cap_e
    eq_rows = []
    eq_rhs = []

    for i in range(k):
        s_i, t_i, d_i = groups[i]
        for u in range(n):
            if u == n - 1:
                # redundant constraint for each commodity
                continue
            row = [0.0] * (num_vars + m)
            for e_idx, (u_e, v_e, _) in enumerate(edges):
                if u_e == u:
                    row[i * m + e_idx] += 1.0
                if v_e == u:
                    row[i * m + e_idx] -= 1.0
            rhs = 0.0
            if u == s_i:
                rhs += d_i
            if u == t_i:
                rhs -= d_i
            eq_rows.append(row)
            eq_rhs.append(rhs)

    for e_idx, (_, _, cap) in enumerate(edges):
        row = [0.0] * (num_vars + m)
        for i in range(k):
            row[i * m + e_idx] = 1.0
        row[num_vars + e_idx] = 1.0
        eq_rows.append(row)
        eq_rhs.append(float(cap))

    num_total_vars = num_vars + m
    num_eq = len(eq_rows)

    # Branch and Bound with simplex
    # Bounds on variables: [0, inf) for all, but we will add upper/lower bounds during branching

    EPS = 1e-7

    def solve_lp(var_lbs, var_ubs):
        # Build standard form:
        # Constraints:
        # eq_rows
        # x_j >= lb -> -x_j + s_lb = -lb => x_j - s_lb = lb
        # x_j <= ub -> x_j + s_ub = ub
        rows = []
        rhs = []

        for r, b in zip(eq_rows, eq_rhs):
            rows.append(list(r))
            rhs.append(b)

        extra_slacks = 0
        for j in range(num_total_vars):
            lb = var_lbs[j]
            ub = var_ubs[j]
            if lb > 0:
                extra_slacks += 1
            if ub < 1e9:
                extra_slacks += 1

        slack_idx = num_total_vars
        for j in range(num_total_vars):
            lb = var_lbs[j]
            ub = var_ubs[j]
            if lb > 0:
                row = [0.0] * (num_total_vars + extra_slacks)
                row[j] = 1.0
                row[slack_idx] = -1.0
                slack_idx += 1
                rows.append(row)
                rhs.append(float(lb))
            if ub < 1e9:
                row = [0.0] * (num_total_vars + extra_slacks)
                row[j] = 1.0
                row[slack_idx] = 1.0
                slack_idx += 1
                rows.append(row)
                rhs.append(float(ub))

        tot_cols = num_total_vars + extra_slacks
        for r in rows[:num_eq]:
            r.extend([0.0] * extra_slacks)

        M = len(rows)
        # Fix negative RHS
        for i in range(M):
            if rhs[i] < -EPS:
                for j in range(tot_cols):
                    rows[i][j] = -rows[i][j]
                rhs[i] = -rhs[i]
            elif rhs[i] < 0:
                rhs[i] = 0.0

        # Two-Phase Simplex
        # Phase 1: add artificial variables for each row
        # Tableau size: (M + 1) x (tot_cols + M + 1)
        tab = [[0.0] * (tot_cols + M + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(tot_cols):
                tab[i][j] = rows[i][j]
            tab[i][tot_cols + i] = 1.0
            tab[i][-1] = rhs[i]

        basis = [tot_cols + i for i in range(M)]

        # Objective of phase 1: min sum(artificials) -> max -sum(artificials)
        for j in range(tot_cols + M + 1):
            s = sum(tab[i][j] for i in range(M))
            tab[M][j] = -s

        def pivot(r, c):
            basis[r] = c
            pivot_val = tab[r][c]
            inv = 1.0 / pivot_val
            for j in range(len(tab[0])):
                tab[r][j] *= inv
            for i in range(len(tab)):
                if i != r:
                    factor = tab[i][c]
                    if abs(factor) > 1e-12:
                        for j in range(len(tab[0])):
                            tab[i][j] -= factor * tab[r][j]

        # Phase 1 Simplex iterations
        total_cols_phase1 = tot_cols + M
        while True:
            # Find entering column (most positive in cost row since we maximize)
            enter = -1
            best_c = EPS
            for j in range(total_cols_phase1):
                if tab[M][j] > best_c:
                    best_c = tab[M][j]
                    enter = j
            if enter == -1:
                break

            # Ratio test
            leave = -1
            min_ratio = float("inf")
            for i in range(M):
                if tab[i][enter] > EPS:
                    ratio = tab[i][-1] / tab[i][enter]
                    if ratio < min_ratio:
                        min_ratio = ratio
                        leave = i
            if leave == -1:
                break
            pivot(leave, enter)

        # Check feasibility
        if abs(tab[M][-1]) > 1e-4:
            return None

        # Extract solution
        sol = [0.0] * num_total_vars
        for i in range(M):
            if basis[i] < num_total_vars:
                sol[basis[i]] = tab[i][-1]

        return sol

    # Branch and bound
    init_lbs = [0] * num_total_vars
    init_ubs = [10**9] * num_total_vars

    stack = [(init_lbs, init_ubs)]

    while stack:
        lbs, ubs = stack.pop()
        sol = solve_lp(lbs, ubs)
        if sol is None:
            continue

        # Check if integer on primary vars
        best_frac_var = -1
        best_frac_diff = 0.0

        for j in range(num_vars):
            val = sol[j]
            diff = abs(val - round(val))
            if diff > 1e-4:
                if diff > best_frac_diff:
                    best_frac_diff = diff
                    best_frac_var = j

        if best_frac_var == -1:
            # Found integer solution!
            print("YES")
            for i in range(k):
                row_res = [int(round(sol[i * m + j])) for j in range(m)]
                print(*(row_res))
            return

        val = sol[best_frac_var]
        floor_val = int(val)
        ceil_val = floor_val + 1

        # Branch 1: x <= floor_val
        lbs1 = list(lbs)
        ubs1 = list(ubs)
        ubs1[best_frac_var] = min(ubs1[best_frac_var], floor_val)
        if lbs1[best_frac_var] <= ubs1[best_frac_var]:
            stack.append((lbs1, ubs1))

        # Branch 2: x >= ceil_val
        lbs2 = list(lbs)
        ubs2 = list(ubs)
        lbs2[best_frac_var] = max(lbs2[best_frac_var], ceil_val)
        if lbs2[best_frac_var] <= ubs2[best_frac_var]:
            stack.append((lbs2, ubs2))

    print("NO")


if __name__ == "__main__":
    solve()