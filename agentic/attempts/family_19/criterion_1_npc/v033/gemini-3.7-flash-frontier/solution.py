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
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        products.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # Variable index: for commodity p and edge e, var = p * m + e
    num_vars = k * m

    # Flow conservation constraints:
    # For each commodity p and node u (except t_p to avoid redundancy):
    # sum_{e out of u} f_{p,e} - sum_{e into u} f_{p,e} = b
    # where b = d_p if u == s_p else 0
    A_eq = []
    b_eq = []

    for p in range(k):
        s_p, t_p, d_p = products[p]
        for u in range(n):
            if u == t_p:
                continue
            row = [0.0] * num_vars
            b_val = float(d_p) if u == s_p else 0.0
            for e in range(m):
                u_e, v_e, _ = edges[e]
                if u_e == u:
                    row[p * m + e] += 1.0
                if v_e == u:
                    row[p * m + e] -= 1.0
            A_eq.append(row)
            b_eq.append(b_val)

    # Edge capacity constraints: sum_p f_{p,e} <= cap_e
    A_ub = []
    b_ub = []
    for e in range(m):
        row = [0.0] * num_vars
        for p in range(k):
            row[p * m + e] = 1.0
        A_ub.append(row)
        b_ub.append(float(edges[e][2]))

    # Bounds on variables: lower bounds (initially 0) and upper bounds (initially edge capacity)
    var_lb = [0.0] * num_vars
    var_ub = [float(edges[e % m][2]) for e in range(num_vars)]

    EPS = 1e-7

    class Simplex:
        def __init__(self, A_eq, b_eq, A_ub, b_ub, lbs, ubs):
            # Transform bounded LP into standard form:
            # Ax = b, x >= 0
            # With variable bounds: x_i = lb_i + x'_i, 0 <= x'_i <= ub_i - lb_i
            # x'_i + s_i = ub_i - lb_i
            self.n_orig = len(lbs)
            self.lbs = list(lbs)
            self.ubs = list(ubs)

            for i in range(self.n_orig):
                if self.lbs[i] > self.ubs[i] + EPS:
                    self.infeasible = True
                    return

            self.infeasible = False
            rows = []
            rhs = []

            # Eq constraints: A_eq * (lb + x') = b_eq  =>  A_eq * x' = b_eq - A_eq * lb
            for row, b in zip(A_eq, b_eq):
                adj_b = b - sum(row[j] * self.lbs[j] for j in range(self.n_orig))
                r = list(row)
                rows.append(r)
                rhs.append(adj_b)

            # UB constraints on original variables: x'_i + slack = ub_i - lb_i
            self.slack_vars_count = 0
            for i in range(self.n_orig):
                r = [0.0] * self.n_orig
                r[i] = 1.0
                rows.append(r)
                rhs.append(self.ubs[i] - self.lbs[i])
                self.slack_vars_count += 1

            # Capacity inequalities: A_ub * x' <= b_ub - A_ub * lb => A_ub * x' + slack = b'
            for row, b in zip(A_ub, b_ub):
                adj_b = b - sum(row[j] * self.lbs[j] for j in range(self.n_orig))
                r = list(row)
                rows.append(r)
                rhs.append(adj_b)
                self.slack_vars_count += 1

            m_total = len(rows)
            # Add slack variables
            total_cols = self.n_orig + self.slack_vars_count
            slack_idx = self.n_orig
            for i in range(len(A_eq), m_total):
                for r_idx in range(m_total):
                    if r_idx == i:
                        rows[r_idx].append(1.0)
                    else:
                        rows[r_idx].append(0.0)
                slack_idx += 1

            # Make rhs non-negative
            for i in range(m_total):
                if rhs[i] < -EPS:
                    for j in range(len(rows[i])):
                        rows[i][j] = -rows[i][j]
                    rhs[i] = -rhs[i]

            self.m = m_total
            self.n = len(rows[0])
            self.A = rows
            self.b = rhs

        def solve_lp(self):
            if self.infeasible:
                return None

            m, n = self.m, self.n
            # Two-phase simplex
            # Create tableau for Phase 1
            # Add m artificial variables
            # Tableau: (m + 2) x (n + m + 1)
            tableau = [[0.0] * (n + m + 1) for _ in range(m + 2)]
            for i in range(m):
                for j in range(n):
                    tableau[i][j] = self.A[i][j]
                tableau[i][n + i] = 1.0
                tableau[i][-1] = self.b[i]

            # Phase 1 objective: minimize sum of artificial variables
            # Row m is phase 1 objective
            for i in range(m):
                for j in range(n + m + 1):
                    tableau[m][j] -= tableau[i][j]

            basis = [n + i for i in range(m)]

            def pivot(r, c, phase1=True):
                nonlocal tableau, basis
                num_rows = m + 2 if phase1 else m + 1
                inv = 1.0 / tableau[r][c]
                for j in range(len(tableau[0])):
                    tableau[r][j] *= inv
                for i in range(num_rows):
                    if i != r and abs(tableau[i][c]) > EPS:
                        factor = tableau[i][c]
                        for j in range(len(tableau[0])):
                            tableau[i][j] -= factor * tableau[r][j]
                basis[r] = c

            # Phase 1 simplex
            while True:
                min_val = -EPS
                pivot_col = -1
                for j in range(n + m):
                    if tableau[m][j] < min_val:
                        min_val = tableau[m][j]
                        pivot_col = j
                if pivot_col == -1:
                    break

                min_ratio = float("inf")
                pivot_row = -1
                for i in range(m):
                    if tableau[i][pivot_col] > EPS:
                        ratio = tableau[i][-1] / tableau[i][pivot_col]
                        if ratio < min_ratio - EPS:
                            min_ratio = ratio
                            pivot_row = i
                if pivot_row == -1:
                    return None
                pivot(pivot_row, pivot_col, True)

            if abs(tableau[m][-1]) > 1e-4:
                return None  # Infeasible

            # Remove artificial variables
            # Reconstruct tableau for Phase 2 (objective = 0, just feasibility)
            for i in range(m):
                if basis[i] >= n:
                    # Try to pivot out of artificial variable
                    for j in range(n):
                        if abs(tableau[i][j]) > EPS:
                            pivot(i, j, True)
                            break

            sol = [0.0] * self.n_orig
            for i in range(m):
                if basis[i] < self.n_orig:
                    sol[basis[i]] = tableau[i][-1]

            # Restore original variable values
            for i in range(self.n_orig):
                sol[i] += self.lbs[i]

            return sol

    # Branch and Bound
    best_sol = None

    def branch_and_bound(lbs, ubs):
        nonlocal best_sol
        if best_sol is not None:
            return

        sp = Simplex(A_eq, b_eq, A_ub, b_ub, lbs, ubs)
        sol = sp.solve_lp()
        if sol is None:
            return

        # Check integrality
        best_frac_dist = 0
        best_var = -1
        for i in range(num_vars):
            val = sol[i]
            frac = abs(val - round(val))
            if frac > 1e-4:
                if frac > best_frac_dist:
                    best_frac_dist = frac
                    best_var = i

        if best_var == -1:
            best_sol = [int(round(x)) for x in sol]
            return

        val = sol[best_var]
        floor_val = int(val)
        ceil_val = floor_val + 1

        # Branch left: var <= floor_val
        if floor_val >= lbs[best_var] - EPS:
            new_ubs = list(ubs)
            new_ubs[best_var] = min(new_ubs[best_var], float(floor_val))
            branch_and_bound(lbs, new_ubs)

        if best_sol is not None:
            return

        # Branch right: var >= ceil_val
        if ceil_val <= ubs[best_var] + EPS:
            new_lbs = list(lbs)
            new_lbs[best_var] = max(new_lbs[best_var], float(ceil_val))
            branch_and_bound(new_lbs, ubs)

    branch_and_bound(var_lb, var_ub)

    if best_sol is None:
        print("NO")
    else:
        print("YES")
        for p in range(k):
            row = [best_sol[p * m + e] for e in range(m)]
            print(*(row))


if __name__ == "__main__":
    solve()