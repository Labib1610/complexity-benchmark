import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    commodities = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        commodities.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # Number of variables = k * m
    num_vars = k * m

    # Node balance equations for each commodity: k * n equations
    # Edge capacity inequalities: m inequalities (sum_i x_{i, e} <= cap_e)
    # x_{i, e} >= 0

    # Build matrix for Simplex / Branch-and-Bound
    # Equality constraints: A_eq * x = b_eq
    # Inequality constraints: A_ub * x <= b_ub
    # x >= 0 integer

    A_eq = []
    b_eq = []
    for c_idx, (s, t, d) in enumerate(commodities):
        for node in range(n):
            if node == t:
                # We can omit one redundant balance equation per connected component/commodity,
                # but keeping all is also fine for simplex.
                pass
            row = [0.0] * num_vars
            for e_idx, (u, v, _) in enumerate(edges):
                if u == node:
                    row[c_idx * m + e_idx] += 1.0
                if v == node:
                    row[c_idx * m + e_idx] -= 1.0
            rhs = 0.0
            if node == s:
                rhs = float(d)
            elif node == t:
                rhs = -float(d)

            A_eq.append(row)
            b_eq.append(rhs)

    A_ub = []
    b_ub = []
    for e_idx, (_, _, cap) in enumerate(edges):
        row = [0.0] * num_vars
        for c_idx in range(k):
            row[c_idx * m + e_idx] = 1.0
        A_ub.append(row)
        b_ub.append(float(cap))

    # We will use a pure Python Branch and Bound with Revised / Tableau Simplex
    # Convert all constraints to standard inequality form:
    # A_ub * x <= b_ub
    # A_eq * x <= b_eq
    # -A_eq * x <= -b_eq
    # x >= 0

    all_A = []
    all_b = []

    for row, rhs in zip(A_ub, b_ub):
        all_A.append(list(row))
        all_b.append(rhs)

    for row, rhs in zip(A_eq, b_eq):
        all_A.append(list(row))
        all_b.append(rhs)
        all_A.append([-val for val in row])
        all_b.append(-rhs)

    num_constraints = len(all_b)
    # Variable bounds: lower bound 0, upper bound min(cap_e, d_i)
    # We can handle variable bounds as additional constraints or directly.

    # Simplex solver implementation
    EPS = 1e-7

    class Simplex:

        def __init__(self, A, b, c):
            # min c^T x s.t. A x <= b, x >= 0
            # Phase I + Phase II using Two-Phase Simplex Tableau
            self.m = len(b)
            self.n = len(c)
            # Add slack variables: A x + s = b, s >= 0
            # Tableau size: (m + 2) x (n + m + 1)
            # Row 0: Phase 1 objective
            # Row 1: Phase 2 objective
            # Rows 2..m+1: Constraints
            self.T = [[0.0] * (self.n + self.m + 1) for _ in range(self.m + 2)]
            self.basis = [self.n + i for i in range(self.m)]

            for i in range(self.m):
                for j in range(self.n):
                    self.T[i + 2][j] = A[i][j]
                self.T[i + 2][self.n + i] = 1.0
                self.T[i + 2][-1] = b[i]

            for j in range(self.n):
                self.T[1][j] = c[j]

            # If any b[i] < 0, we need artificial variables or dual simplex,
            # but Two-Phase handles it with artificials if formulated properly.
            # Simpler Two-Phase:
            # Let's set up standard Two-Phase:
            # For each constraint i:
            # if b[i] < 0, multiply row by -1, and add an artificial variable.
            # Actually, standard Two-Phase Simplex:
            self.artificial = []
            for i in range(self.m):
                if self.T[i + 2][-1] < -EPS:
                    for j in range(len(self.T[i + 2])):
                        self.T[i + 2][j] = -self.T[i + 2][j]
                    # Add artificial variable
                    for r in range(self.m + 2):
                        self.T[r].append(0.0)
                    art_col = len(self.T[0]) - 1
                    # Swap with RHS
                    for r in range(self.m + 2):
                        self.T[r][art_col], self.T[r][-2] = (
                            self.T[r][-2],
                            self.T[r][art_col],
                        )
                    art_col = len(self.T[0]) - 2
                    self.T[i + 2][art_col] = 1.0
                    self.basis[i] = art_col
                    self.artificial.append((i, art_col))

        def pivot(self, r, c):
            inv = 1.0 / self.T[r][c]
            for j in range(len(self.T[r])):
                self.T[r][j] *= inv
            for i in range(len(self.T)):
                if i != r:
                    factor = self.T[i][c]
                    if abs(factor) > 1e-12:
                        for j in range(len(self.T[r])):
                            self.T[i][j] -= factor * self.T[r][j]
            self.basis[r - 2] = c

        def solve_phase(self, phase_row):
            while True:
                # Find entering variable
                c_min = -EPS
                pivot_col = -1
                for j in range(len(self.T[0]) - 1):
                    if self.T[phase_row][j] < c_min:
                        c_min = self.T[phase_row][j]
                        pivot_col = j
                if pivot_col == -1:
                    return True  # Optimal

                # Find leaving variable (minimum ratio test)
                min_ratio = float("inf")
                pivot_row = -1
                for i in range(self.m):
                    coeff = self.T[i + 2][pivot_col]
                    if coeff > EPS:
                        ratio = self.T[i + 2][-1] / coeff
                        if ratio < min_ratio - 1e-12:
                            min_ratio = ratio
                            pivot_row = i + 2
                if pivot_row == -1:
                    return False  # Unbounded
                self.pivot(pivot_row, pivot_col)

        def solve(self):
            if self.artificial:
                # Phase 1: minimize sum of artificial variables
                for j in range(len(self.T[0])):
                    self.T[0][j] = 0.0
                for _, art_col in self.artificial:
                    self.T[0][art_col] = 1.0
                # Make tableau canonical for Phase 1
                for i, art_col in self.artificial:
                    for j in range(len(self.T[0])):
                        self.T[0][j] -= self.T[i + 2][j]

                self.solve_phase(0)

                if self.T[0][-1] > EPS:
                    return None  # Infeasible

            # Phase 2
            # Make tableau canonical for Phase 2 objective
            for i in range(self.m):
                b_var = self.basis[i]
                factor = self.T[1][b_var]
                if abs(factor) > 1e-12:
                    for j in range(len(self.T[0])):
                        self.T[1][j] -= factor * self.T[i + 2][j]

            if not self.solve_phase(1):
                return None

            sol = [0.0] * self.n
            for i in range(self.m):
                if self.basis[i] < self.n:
                    sol[self.basis[i]] = self.T[i + 2][-1]
            return sol

    def lp_solve(extra_constraints):
        curr_A = [list(r) for r in all_A]
        curr_b = list(all_b)
        for var_idx, is_upper, val in extra_constraints:
            row = [0.0] * num_vars
            if is_upper:  # x <= val
                row[var_idx] = 1.0
                curr_A.append(row)
                curr_b.append(float(val))
            else:  # x >= val -> -x <= -val
                row[var_idx] = -1.0
                curr_A.append(row)
                curr_b.append(-float(val))

        c = [0.0] * num_vars
        simplex = Simplex(curr_A, curr_b, c)
        return simplex.solve()

    # Branch and Bound
    best_sol = None
    stack = [[]]

    while stack:
        extra_constrs = stack.pop()
        sol = lp_solve(extra_constrs)
        if sol is None:
            continue

        # Check if integer
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
            best_sol = [int(round(x)) for x in sol]
            break

        val = sol[frac_var]
        floor_val = int(val)
        ceil_val = floor_val + 1

        # Branch
        stack.append(extra_constrs + [(frac_var, False, ceil_val)])
        stack.append(extra_constrs + [(frac_var, True, floor_val)])

    if best_sol is None:
        print("NO")
    else:
        print("YES")
        for c_idx in range(k):
            row_ans = best_sol[c_idx * m : (c_idx + 1) * m]
            print(*(max(0, x) for x in row_ans))


if __name__ == "__main__":
    solve()