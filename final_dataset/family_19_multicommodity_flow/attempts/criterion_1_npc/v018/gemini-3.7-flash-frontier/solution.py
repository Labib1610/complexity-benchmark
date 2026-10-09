import sys
import math

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    products = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        products.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))

    # Fast feasibility check: total demand cannot exceed sum of capacities from sources, etc.
    # We will formulate this as an Integer Linear Program (ILP) and solve via Branch and Bound.
    
    num_vars = k * m
    # Variable index: var(p, e) = p * m + e
    def var_idx(p, e):
        return p * m + e

    # Equality constraints: for each commodity p and node u
    # sum_{e out of u} x(p, e) - sum_{e into u} x(p, e) = demand_balance(p, u)
    # Inequality constraints: for each edge e, sum_p x(p, e) <= c_e

    # Construct the base constraint matrix:
    # A_eq * x = b_eq
    # A_ub * x <= b_ub
    # x >= 0

    eq_rows = []
    eq_rhs = []
    for p in range(k):
        s, t, d = products[p]
        if s == t:
            continue
        for u in range(n):
            row = {}
            for e in range(m):
                u_e, v_e, _ = edges[e]
                if u_e == u:
                    row[var_idx(p, e)] = row.get(var_idx(p, e), 0.0) + 1.0
                if v_e == u:
                    row[var_idx(p, e)] = row.get(var_idx(p, e), 0.0) - 1.0
            rhs = 0.0
            if u == s:
                rhs = float(d)
            elif u == t:
                rhs = float(-d)
            # Remove zero entries
            row = {k: v for k, v in row.items() if abs(v) > 1e-9}
            if row or abs(rhs) > 1e-9:
                eq_rows.append(row)
                eq_rhs.append(rhs)

    ub_rows = []
    ub_rhs = []
    for e in range(m):
        row = {}
        for p in range(k):
            row[var_idx(p, e)] = 1.0
        ub_rows.append(row)
        ub_rhs.append(float(edges[e][2]))

    # Simplex Tableau Solver for Phase 1 / Phase 2
    # Convert all constraints to standard equality form with slack/artificial variables.
    # Rows:
    # 1. Capacity constraints: sum x <= c  ==> sum x + s_e = c (slack s_e >= 0)
    # 2. Flow conservation: sum +/- x = rhs. If rhs < 0, multiply by -1.
    #    Add artificial variable a_i: sum +/- x + a_i = rhs (if rhs >= 0).
    # Additional variable bounds from branch-and-bound will be added as <= or >= constraints.

    class LP:
        def __init__(self, num_vars, eq_rows, eq_rhs, ub_rows, ub_rhs):
            self.num_orig_vars = num_vars
            self.base_eq_rows = eq_rows
            self.base_eq_rhs = eq_rhs
            self.base_ub_rows = ub_rows
            self.base_ub_rhs = ub_rhs

        def solve_lp(self, var_bounds):
            # var_bounds: dict of var_idx -> (lower_bound, upper_bound)
            # Builds standard tableau and solves Phase 1 (find feasible) + Phase 2 (any or min cost).
            # Form: A x = b, x >= 0
            
            rows = []
            rhs = []
            
            # Base capacity constraints
            for r, b in zip(self.base_ub_rows, self.base_ub_rhs):
                rows.append((r.copy(), 1.0)) # <= constraint, will add slack
                rhs.append(b)
                
            # Base flow conservation
            for r, b in zip(self.base_eq_rows, self.base_eq_rhs):
                rows.append((r.copy(), 0.0)) # == constraint
                rhs.append(b)

            # Additional variable bounds
            for v, (lb, ub) in var_bounds.items():
                if lb > 0:
                    # x_v >= lb  ==>  -x_v <= -lb  ==>  -x_v + slack = -lb ==> x_v - slack = lb
                    rows.append(({v: 1.0}, -1.0)) # >= constraint, surplus
                    rhs.append(float(lb))
                if ub is not None:
                    rows.append(({v: 1.0}, 1.0)) # <= constraint, slack
                    rhs.append(float(ub))

            m_c = len(rows)
            # Count extra variables: slack/surplus and artificials
            # For each constraint:
            # if <= (slack_coeff == 1.0):
            #    if rhs >= 0: slack var is basic
            #    if rhs < 0: multiply by -1 => >= constraint => surplus + artificial
            # if == (slack_coeff == 0.0):
            #    if rhs < 0: multiply by -1
            #    needs artificial
            # if >= (slack_coeff == -1.0):
            #    if rhs >= 0: surplus + artificial
            #    if rhs < 0: multiply by -1 => <= constraint => slack var is basic

            # Build full matrix
            # Let's standardize each row to rhs >= 0:
            std_rows = []
            std_rhs = []
            slacks = [] # list of (row_idx, sign)
            for i in range(m_c):
                r, s_type = rows[i]
                b = rhs[i]
                if b < 0:
                    r = {k: -v for k, v in r.items()}
                    b = -b
                    s_type = -s_type
                std_rows.append(r)
                std_rhs.append(b)
                slacks.append(s_type)

            # Number of slack variables needed:
            num_slacks = sum(1 for s in slacks if s != 0)
            # Number of artificial variables needed:
            # artificial needed if s_type == 0 or s_type == -1
            num_art = sum(1 for s in slacks if s <= 0)

            # Total columns: num_orig_vars + num_slacks + num_art
            # We index: orig: 0..n_orig-1, slack: n_orig..n_orig+num_slacks-1, art: ...
            total_cols = self.num_orig_vars + num_slacks + num_art
            
            # Tableau shape: (m_c + 1) x (total_cols + 1)
            # Row 0 is Phase 1 objective (minimize sum of artificials)
            tableau = [[0.0] * (total_cols + 1) for _ in range(m_c + 1)]
            basic_vars = [-1] * m_c

            slack_idx = self.num_orig_vars
            art_idx = self.num_orig_vars + num_slacks

            for i in range(m_c):
                r = std_rows[i]
                b = std_rhs[i]
                s_type = slacks[i]

                for v, val in r.items():
                    tableau[i + 1][v] = val
                tableau[i + 1][-1] = b

                if s_type == 1.0: # <= with b >= 0, slack is basic
                    tableau[i + 1][slack_idx] = 1.0
                    basic_vars[i] = slack_idx
                    slack_idx += 1
                elif s_type == -1.0: # >= with b >= 0, surplus + art
                    tableau[i + 1][slack_idx] = -1.0
                    slack_idx += 1
                    tableau[i + 1][art_idx] = 1.0
                    basic_vars[i] = art_idx
                    art_idx += 1
                else: # == with b >= 0, art
                    tableau[i + 1][art_idx] = 1.0
                    basic_vars[i] = art_idx
                    art_idx += 1

            # Setup Phase 1 objective: minimize sum of artificial variables
            # sum_{art} a_i = 0 ==> Obj row initially has +1 for each art var.
            # In standard tableau, we subtract rows containing basic artificial vars.
            for i in range(m_c):
                if basic_vars[i] >= self.num_orig_vars + num_slacks:
                    # Row i+1 has basic artificial var
                    for col in range(total_cols + 1):
                        tableau[0][col] -= tableau[i + 1][col]

            # Pivot helper
            def pivot(pivot_row, pivot_col):
                piv_val = tableau[pivot_row][pivot_col]
                for c in range(total_cols + 1):
                    tableau[pivot_row][c] /= piv_val
                for r in range(m_c + 1):
                    if r != pivot_row:
                        factor = tableau[r][pivot_col]
                        if abs(factor) > 1e-12:
                            for c in range(total_cols + 1):
                                tableau[r][c] -= factor * tableau[pivot_row][c]
                basic_vars[pivot_row - 1] = pivot_col

            # Simplex Phase 1
            max_pivots = 5000 + 10 * total_cols
            pivots = 0
            while pivots < max_pivots:
                pivots += 1
                # Find entering variable (most negative in row 0)
                min_val = -1e-8
                enter_col = -1
                for c in range(total_cols):
                    if tableau[0][c] < min_val:
                        min_val = tableau[0][c]
                        enter_col = c
                if enter_col == -1:
                    break # Optimal for Phase 1

                # Ratio test
                min_ratio = float('inf')
                pivot_row = -1
                for r in range(1, m_c + 1):
                    val = tableau[r][enter_col]
                    if val > 1e-8:
                        ratio = tableau[r][-1] / val
                        if ratio < min_ratio - 1e-9:
                            min_ratio = ratio
                            pivot_row = r

                if pivot_row == -1:
                    return None # Unbounded / Infeasible
                pivot(pivot_row, enter_col)

            # Check Phase 1 objective value
            if tableau[0][-1] < -1e-5:
                return None # Infeasible

            # Extract solution for original variables
            sol = [0.0] * self.num_orig_vars
            for i in range(m_c):
                bv = basic_vars[i]
                if bv < self.num_orig_vars:
                    sol[bv] = max(0.0, tableau[i + 1][-1])
            return sol

    lp_solver = LP(num_vars, eq_rows, eq_rhs, ub_rows, ub_rhs)

    # Branch and Bound
    best_sol = None

    # Stack for DFS branch and bound
    # state: var_bounds dict
    stack = [{}]

    while stack:
        bounds = stack.pop()
        sol = lp_solver.solve_lp(bounds)
        if sol is None:
            continue

        # Find most fractional variable
        fractional = []
        for i, val in enumerate(sol):
            f = abs(val - round(val))
            if f > 1e-4:
                fractional.append((f, i, val))

        if not fractional:
            # Found integer solution!
            best_sol = [int(round(v)) for v in sol]
            break

        # Pick the variable with fraction closest to 0.5
        fractional.sort(key=lambda x: -x[0])
        _, best_var, val = fractional[0]

        floor_val = math.floor(val + 1e-8)
        ceil_val = math.ceil(val - 1e-8)

        # Branch 1: x_v <= floor_val
        b1 = bounds.copy()
        lb, ub = b1.get(best_var, (0, None))
        new_ub = floor_val if ub is None else min(ub, floor_val)
        if lb <= new_ub:
            b1[best_var] = (lb, new_ub)
            stack.append(b1)

        # Branch 2: x_v >= ceil_val
        b2 = bounds.copy()
        lb, ub = b2.get(best_var, (0, None))
        new_lb = max(lb, ceil_val)
        if ub is None or new_lb <= ub:
            b2[best_var] = (new_lb, ub)
            stack.append(b2)

    if best_sol is None:
        print("NO")
    else:
        print("YES")
        for p in range(k):
            row = [best_sol[var_idx(p, e)] for e in range(m)]
            print(*(row))

solve()