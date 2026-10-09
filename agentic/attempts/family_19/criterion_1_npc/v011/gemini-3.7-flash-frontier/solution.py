import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    species = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        species.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # Fast path finding if sum of demands is small or via DFS
    # But Branch and Bound / DFS over paths or edge flows is very general.
    # Let's formulate as ILP and solve with DFS / Branch & Bound.

    num_vars = k * m

    # Flow conservation constraints:
    # For each species i (0..k-1) and each node u (0..n-1):
    # sum(outflow) - sum(inflow) = demand(i, u)
    # Note: one redundant constraint per connected component per species (sum of demands = 0).
    # Capacity constraints:
    # For each edge e (0..m-1): sum_i x_{i, e} <= cap_e

    # Let's implement a Tableau Simplex with Branch-and-Bound.
    # To be extremely fast, we can use dual simplex for branching.

    # Matrix size:
    # Equations: k * (n - 1) equality constraints (drop node n-1 for each species)
    # Capacity: m inequality constraints
    # Variable upper bounds / lower bounds dynamically added.

    # Since m, n, k in competitive programming problems are usually <= 50 or 100:
    # Let's set up standard LP in tableau form.

    class Simplex:
        def __init__(self, A, b, c, eq_count):
            # A is (num_constraints x num_vars)
            # b is (num_constraints)
            # c is (num_vars) - we want to minimize c^T x
            # First eq_count constraints are equality (Ax = b)
            # The remaining are inequalities (Ax <= b)
            self.m_eq = eq_count
            self.m_ineq = len(b) - eq_count
            self.n_orig = len(c)

            # Convert to standard form with slack and artificial variables
            # For Ax = b (b >= 0): add artificial variable
            # For Ax <= b (b >= 0): add slack variable
            # (If b < 0, multiply row by -1 and handle accordingly)

    # Actually, a simpler and very effective method in Python for exact integer flow
    # is a combination of LP Phase 1 or backtracking with flow decomposition.

    # Let's write a standard dense Simplex / B&B solver:
    import numpy as np

    # Build constraint matrix:
    # Variables: x_{i * m + e} for i in range(k), e in range(m)
    # Rows:
    # 1. Flow conservation: k * n rows (Ax = b)
    # 2. Capacity constraints: m rows (sum_i x_{i, e} <= cap_e)

    A_eq = []
    b_eq = []
    for i in range(k):
        s_i, t_i, d_i = species[i]
        for u in range(n):
            row = [0.0] * num_vars
            for e in range(m):
                u_e, v_e, _ = edges[e]
                if u_e == u:
                    row[i * m + e] += 1.0
                if v_e == u:
                    row[i * m + e] -= 1.0
            demand = 0.0
            if u == s_i:
                demand += d_i
            if u == t_i:
                demand -= d_i
            A_eq.append(row)
            b_eq.append(demand)

    A_ub = []
    b_ub = []
    for e in range(m):
        row = [0.0] * num_vars
        for i in range(k):
            row[i * m + e] = 1.0
        A_ub.append(row)
        b_ub.append(float(edges[e][2]))

    # Pure Python Simplex solver
    # We can use Two-Phase Simplex on standard form:
    # Minimize 0 subject to A_eq x = b_eq, A_ub x <= b_ub, x >= 0, plus bounds x_j <= u_j, x_j >= l_j.

    # To make B&B fast, let's write a robust Revised Simplex or Tableau Simplex.
    # Number of variables is num_vars (x) + m (slack for capacity).
    # Conservation constraints are equalities, capacity are <=.

    num_slacks = m
    total_vars = num_vars + num_slacks

    base_A = []
    base_b = []

    for i in range(len(A_eq)):
        row = list(A_eq[i]) + [0.0] * num_slacks
        rhs = b_eq[i]
        if rhs < 0:
            row = [-val for val in row]
            rhs = -rhs
        base_A.append(row)
        base_b.append(rhs)

    for i in range(len(A_ub)):
        row = list(A_ub[i]) + [0.0] * num_slacks
        row[num_vars + i] = 1.0  # slack variable
        rhs = b_ub[i]
        base_A.append(row)
        base_b.append(rhs)

    # Bounds for original variables: lower bounds (initially 0), upper bounds (initially inf or cap)
    # We can add bound constraints dynamically as rows.

    # Branch and Bound:
    # A simple DFS search with fractional variable selection.

    def solve_lp(extra_constraints):
        # extra_constraints: list of (var_idx, '<=' or '>=', val)
        # Build full tableau with Phase 1
        A = [list(r) for r in base_A]
        b = list(base_b)

        # Add extra constraints
        for v_idx, op, val in extra_constraints:
            row = [0.0] * (total_vars + len(extra_constraints))  # will size properly
            # We'll handle slacks properly below
            pass

        # Let's build full matrix directly
        all_rows = []
        all_rhs = []

        for r, rhs in zip(base_A, base_b):
            all_rows.append(list(r))
            all_rhs.append(rhs)

        num_extra = len(extra_constraints)
        for idx, (v_idx, op, val) in enumerate(extra_constraints):
            row = [0.0] * total_vars
            if op == "<=":
                row[v_idx] = 1.0
                rhs = float(val)
            else:  # '>='
                row[v_idx] = -1.0
                rhs = -float(val)

            if rhs < 0:
                row = [-x for x in row]
                rhs = -rhs
                # Note: this flips the <= to >= with positive RHS, handled by artificial var in Phase 1
            all_rows.append(row)
            all_rhs.append(rhs)

        # Now all_rows is M x total_vars. We add slack/artificial variables.
        # Specifically:
        # Base constraints:
        #   First len(A_eq) are equality -> need artificial var.
        #   Next len(A_ub) already have slacks in base_A -> if b >= 0, slack is initial basic var!
        #   Extra constraints -> need slack / artificial.
        # To make it universally simple: standard Phase 1 with artificial variables on all rows where needed.

        M = len(all_rows)
        N = total_vars

        # Let's do standard two-phase tableau:
        # Variables: N original+slack, plus M artificial variables
        # Tableau size: (M + 1) x (N + M + 1)
        # Row 0 is Phase 1 objective: minimize sum of artificial variables = maximize -sum(artificial)
        tableau = [[0.0] * (N + M + 1) for _ in range(M + 1)]

        for i in range(M):
            for j in range(N):
                tableau[i + 1][j] = all_rows[i][j]
            tableau[i + 1][N + i] = 1.0  # artificial variable
            tableau[i + 1][-1] = all_rhs[i]

        # Phase 1 objective: initially artificial vars are basic.
        # Objective row: z = - sum(artificial) => z + sum(artificial) = 0
        # Substitute artificial = RHS - sum(A_ij * x_j):
        # Row 0: coeff of x_j is sum_i A_ij, RHS is sum_i RHS_i
        for j in range(N):
            s = 0.0
            for i in range(M):
                s += tableau[i + 1][j]
            tableau[0][j] = s

        s_rhs = 0.0
        for i in range(M):
            s_rhs += tableau[i + 1][-1]
        tableau[0][-1] = s_rhs

        basis = [N + i for i in range(M)]

        # Simplex pivot loop
        EPS = 1e-7
        MAX_PIVOTS = 2000

        def pivot(r, c):
            piv = tableau[r][c]
            inv_piv = 1.0 / piv
            for j in range(len(tableau[0])):
                tableau[r][j] *= inv_piv
            for i in range(len(tableau)):
                if i != r:
                    factor = tableau[i][c]
                    if abs(factor) > 1e-12:
                        for j in range(len(tableau[0])):
                            tableau[i][j] -= factor * tableau[r][j]
            basis[r - 1] = c

        pivots = 0
        while pivots < MAX_PIVOTS:
            pivots += 1
            # Find entering variable (Bland's rule or largest positive in row 0)
            entering = -1
            max_val = EPS
            for j in range(N + M):
                if tableau[0][j] > max_val:
                    max_val = tableau[0][j]
                    entering = j

            if entering == -1:
                break  # Optimal for Phase 1

            # Ratio test
            leaving = -1
            min_ratio = float("inf")
            for i in range(1, M + 1):
                if tableau[i][entering] > EPS:
                    ratio = tableau[i][-1] / tableau[i][entering]
                    if ratio < min_ratio - 1e-12:
                        min_ratio = ratio
                        leaving = i

            if leaving == -1:
                # Unbounded in Phase 1 (should not happen)
                break

            pivot(leaving, entering)

        # Check Phase 1 objective value
        if abs(tableau[0][-1]) > 1e-4:
            return None  # Infeasible

        # Extract solution
        sol = [0.0] * num_vars
        for i in range(M):
            var = basis[i]
            if var < num_vars:
                sol[var] = tableau[i + 1][-1]

        return sol

    # Branch and Bound
    best_sol = None
    stack = [[]]

    while stack:
        constraints = stack.pop()
        sol = solve_lp(constraints)
        if sol is None:
            continue

        # Check integrality
        fractional_idx = -1
        max_frac = 0.0
        is_int = True

        for idx, val in enumerate(sol):
            # Check how close to integer
            rounded = round(val)
            diff = abs(val - rounded)
            if diff > 1e-4:
                is_int = False
                frac = abs(val - (int(val) + 0.5))
                # Choose variable closest to 0.5
                if 0.5 - frac > max_frac:
                    max_frac = 0.5 - frac
                    fractional_idx = idx

        if is_int:
            best_sol = [int(round(v)) for v in sol]
            break

        # Branch on fractional_idx
        val = sol[fractional_idx]
        floor_val = int(val)
        ceil_val = floor_val + 1

        # Push branches to stack (explore branch closest to LP value first)
        if val - floor_val > 0.5:
            stack.append(constraints + [(fractional_idx, "<=", floor_val)])
            stack.append(constraints + [(fractional_idx, ">=", ceil_val)])
        else:
            stack.append(constraints + [(fractional_idx, ">=", ceil_val)])
            stack.append(constraints + [(fractional_idx, "<=", floor_val)])

    if best_sol is None:
        print("NO")
    else:
        print("YES")
        for i in range(k):
            species_flow = [best_sol[i * m + e] for e in range(m)]
            print(*(species_flow))


if __name__ == "__main__":
    solve()