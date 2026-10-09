import sys


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
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        products.append((s, t, d))

    routes = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        routes.append((u, v, cap))

    # Fast path: check trivial reachability
    # Also if k == 1, it's just max flow / standard flow.
    # We can use ILP with Branch and Bound.

    num_vars = k * m
    # Variable indexing: var(p, r) = p * m + r

    # Build equality and inequality constraints for LP
    # Form: A_eq * x = b_eq, A_ub * x <= b_ub, x >= 0 integer.

    eq_rows = []
    eq_rhs = []

    # Flow conservation constraints
    for p in range(k):
        s_p, t_p, d_p = products[p]
        for u in range(1, n + 1):
            if u == t_p:
                continue  # redundant with others
            row = [0.0] * num_vars
            for r in range(m):
                u_r, v_r, _ = routes[r]
                if u_r == u:
                    row[p * m + r] += 1.0
                if v_r == u:
                    row[p * m + r] -= 1.0

            target = 0.0
            if u == s_p:
                target = float(d_p)

            eq_rows.append(row)
            eq_rhs.append(target)

    ub_rows = []
    ub_rhs = []

    # Capacity constraints
    for r in range(m):
        row = [0.0] * num_vars
        for p in range(k):
            row[p * m + r] = 1.0
        ub_rows.append(row)
        ub_rhs.append(float(routes[r][2]))

    # We can use a revised simplex / tableau solver with branch and bound.
    # To be extremely lightweight and robust:

    class Simplex:

        def __init__(self, A_eq, b_eq, A_ub, b_ub, bounds, obj):
            # Convert to standard form: A x = b, x >= 0
            # bounds: list of (low, high) for each original var
            # obj: maximize c^T x (we can just find feasible or min sum)
            self.num_orig = len(obj)
            self.bounds = bounds

            # Convert variables with lower bounds: x_i = x'_i + low_i
            # If high_i is finite, add x'_i <= high_i - low_i as ub constraint.

            eq_mat = []
            eq_b = []

            for row, rhs in zip(A_eq, b_eq):
                r = list(row)
                adj_rhs = rhs
                for j in range(self.num_orig):
                    low, _ = bounds[j]
                    adj_rhs -= r[j] * low
                eq_mat.append(r)
                eq_b.append(adj_rhs)

            ub_mat = []
            ub_b = []

            for row, rhs in zip(A_ub, b_ub):
                r = list(row)
                adj_rhs = rhs
                for j in range(self.num_orig):
                    low, _ = bounds[j]
                    adj_rhs -= r[j] * low
                ub_mat.append(r)
                ub_b.append(adj_rhs)

            for j in range(self.num_orig):
                low, high = bounds[j]
                if high < 1e12:
                    r = [0.0] * self.num_orig
                    r[j] = 1.0
                    ub_mat.append(r)
                    ub_b.append(high - low)

            # Standard form:
            # eq_mat * x' = eq_b
            # ub_mat * x' + s = ub_b (s >= 0)
            # Make all RHS non-negative
            m_eq = len(eq_mat)
            m_ub = len(ub_mat)
            total_m = m_eq + m_ub

            # Matrix: [total_m rows] x [num_orig + m_ub slack vars]
            total_cols = self.num_orig + m_ub
            A = []
            b = []

            for i in range(m_eq):
                r = eq_mat[i] + [0.0] * m_ub
                rhs = eq_b[i]
                if rhs < -1e-9:
                    r = [-x for x in r]
                    rhs = -rhs
                A.append(r)
                b.append(rhs)

            for i in range(m_ub):
                r = ub_mat[i] + [0.0] * m_ub
                r[self.num_orig + i] = 1.0
                rhs = ub_b[i]
                if rhs < -1e-9:
                    # Negative slack constraint means infeasible or need artificial
                    r = [-x for x in r]
                    rhs = -rhs
                A.append(r)
                b.append(rhs)

            self.A = A
            self.b = b
            self.total_m = total_m
            self.total_n = total_cols
            self.c = [obj[j] for j in range(self.num_orig)] + [0.0] * m_ub

        def solve(self):
            # Two-phase simplex
            M = self.total_m
            N = self.total_n

            # Phase 1: Add artificial variables
            # Tableau shape: (M + 2) x (N + M + 1)
            # Row 0: Phase 1 objective (min sum of artificials -> max -sum)
            # Row 1..M: constraints
            # Row M+1: Phase 2 objective
            tableau = [[0.0] * (N + M + 1) for _ in range(M + 2)]
            basis = [0] * M

            for i in range(M):
                for j in range(N):
                    tableau[i + 1][j] = self.A[i][j]
                tableau[i + 1][N + i] = 1.0  # Artificial variable
                tableau[i + 1][-1] = self.b[i]
                basis[i] = N + i

            # Phase 1 objective: -sum of artificials
            # Initially w = - sum(artificials) = - sum(b_i - sum A_ij x_j)
            # So w - sum(A_ij) x_j = -sum(b_i) -> reduced costs
            for i in range(M):
                for j in range(N):
                    tableau[0][j] += self.A[i][j]
                tableau[0][-1] += self.b[i]

            # Phase 2 objective
            for j in range(self.num_orig):
                tableau[M + 1][j] = -self.c[j]

            def pivot(r, c):
                inv = 1.0 / tableau[r][c]
                for j in range(len(tableau[0])):
                    tableau[r][j] *= inv
                for i in range(M + 2):
                    if i != r and abs(tableau[i][c]) > 1e-12:
                        factor = tableau[i][c]
                        for j in range(len(tableau[0])):
                            tableau[i][j] -= factor * tableau[r][j]
                basis[r - 1] = c

            # Phase 1 simplex
            while True:
                # Find entering variable
                c = -1
                max_val = 1e-8
                for j in range(N + M):
                    if tableau[0][j] > max_val:
                        max_val = tableau[0][j]
                        c = j
                if c == -1:
                    break

                # Find leaving variable
                r = -1
                min_ratio = 1e18
                for i in range(1, M + 1):
                    if tableau[i][c] > 1e-9:
                        ratio = tableau[i][-1] / tableau[i][c]
                        if ratio < min_ratio:
                            min_ratio = ratio
                            r = i
                if r == -1:
                    return None  # Unbounded (should not happen in phase 1)

                pivot(r, c)

            if tableau[0][-1] > 1e-6:
                return None  # Infeasible

            # Remove artificial variables from basis if any remain
            for i in range(M):
                if basis[i] >= N:
                    # Try to pivot with a non-artificial column
                    for j in range(N):
                        if abs(tableau[i + 1][j]) > 1e-9:
                            pivot(i + 1, j)
                            break

            # Adjust Phase 2 objective row for current basis
            for i in range(M):
                b_var = basis[i]
                if b_var < N:
                    factor = tableau[M + 1][b_var]
                    if abs(factor) > 1e-12:
                        for j in range(len(tableau[0])):
                            tableau[M + 1][j] -= factor * tableau[i + 1][j]

            # Phase 2 simplex
            while True:
                c = -1
                min_val = -1e-8
                for j in range(N):
                    if tableau[M + 1][j] < min_val:
                        min_val = tableau[M + 1][j]
                        c = j
                if c == -1:
                    break

                r = -1
                min_ratio = 1e18
                for i in range(1, M + 1):
                    if tableau[i][c] > 1e-9:
                        ratio = tableau[i][-1] / tableau[i][c]
                        if ratio < min_ratio:
                            min_ratio = ratio
                            r = i
                if r == -1:
                    break  # Unbounded

                pivot(r, c)

            sol = [0.0] * self.num_orig
            for i in range(M):
                if basis[i] < self.num_orig:
                    sol[basis[i]] = max(0.0, tableau[i + 1][-1])

            # Convert back from shifted variables
            for j in range(self.num_orig):
                sol[j] += self.bounds[j][0]

            return sol

    # Objective: min sum of flows (or any feasible)
    obj = [1.0] * num_vars
    initial_bounds = [(0.0, float(routes[r][2])) for p in range(k) for r in range(m)]

    # Branch and Bound for integer solution
    best_sol = None
    stack = [initial_bounds]

    while stack:
        bounds = stack.pop()
        simplex = Simplex(eq_rows, eq_rhs, ub_rows, ub_rhs, bounds, obj)
        sol = simplex.solve()
        if sol is None:
            continue

        # Check integrality
        frac_var = -1
        max_frac = 0.0
        for i in range(num_vars):
            val = sol[i]
            frac = abs(val - round(val))
            if frac > 1e-4:
                if frac > max_frac:
                    max_frac = frac
                    frac_var = i

        if frac_var == -1:
            # Integer solution found!
            best_sol = [int(round(x)) for x in sol]
            break

        val = sol[frac_var]
        # Branch on frac_var
        import math

        floor_val = math.floor(val + 1e-9)
        ceil_val = math.ceil(val - 1e-9)

        # Branch 1: <= floor_val
        b1 = list(bounds)
        if floor_val >= b1[frac_var][0]:
            b1[frac_var] = (b1[frac_var][0], min(b1[frac_var][1], float(floor_val)))
            stack.append(b1)

        # Branch 2: >= ceil_val
        b2 = list(bounds)
        if ceil_val <= b2[frac_var][1]:
            b2[frac_var] = (max(b2[frac_var][0], float(ceil_val)), b2[frac_var][1])
            stack.append(b2)

    if best_sol is None:
        print("NO")
    else:
        print("YES")
        for p in range(k):
            row = best_sol[p * m : (p + 1) * m]
            print(*(int(x) for x in row))


if __name__ == "__main__":
    solve()