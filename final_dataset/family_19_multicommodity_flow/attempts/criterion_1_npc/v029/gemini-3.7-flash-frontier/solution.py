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
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        commodities.append((s, t, d))

    links = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        links.append((u, v, cap))

    K_vars = k * m
    base_rows = []
    base_b = []

    # 1. Capacity constraints: sum_{i} x_{i, j} + s_j = cap_j
    for j in range(m):
        row = [0.0] * (K_vars + m)
        for i in range(k):
            row[i * m + j] = 1.0
        row[K_vars + j] = 1.0
        base_rows.append(row)
        base_b.append(float(links[j][2]))

    # 2. Flow conservation constraints
    for i in range(k):
        s_i, t_i, d_i = commodities[i]
        for u in range(1, n + 1):
            row = [0.0] * (K_vars + m)
            for j in range(m):
                uj, vj, _ = links[j]
                if uj == u:
                    row[i * m + j] += 1.0
                if vj == u:
                    row[i * m + j] -= 1.0

            rhs = 0.0
            if u == s_i:
                rhs += d_i
            if u == t_i:
                rhs -= d_i
            base_rows.append(row)
            base_b.append(rhs)

    EPS = 1e-7

    def solve_lp(extra_constraints):
        rows = [list(r) for r in base_rows]
        b_vals = list(base_b)

        total_vars = K_vars + m + len(extra_constraints)
        for r in rows:
            r.extend([0.0] * len(extra_constraints))

        for idx, (var_idx, op, val) in enumerate(extra_constraints):
            row = [0.0] * total_vars
            row[var_idx] = 1.0
            slack_idx = K_vars + m + idx
            if op == "<=":
                row[slack_idx] = 1.0
                b_vals.append(float(val))
            else:  # '>='
                row[slack_idx] = -1.0
                b_vals.append(float(val))
            rows.append(row)

        M = len(rows)
        N = total_vars

        for i in range(M):
            if b_vals[i] < 0:
                b_vals[i] = -b_vals[i]
                for j in range(N):
                    rows[i][j] = -rows[i][j]

        tableau = [rows[i] + [0.0] * M + [b_vals[i]] for i in range(M)]
        obj_row = [0.0] * (N + M + 1)
        for i in range(M):
            tableau[i][N + i] = 1.0
            for j in range(N):
                obj_row[j] += rows[i][j]
            obj_row[N + M] += b_vals[i]
        tableau.append(obj_row)

        basis = [N + i for i in range(M)]

        while True:
            best_c = EPS
            q = -1
            for j in range(N + M):
                if tableau[M][j] > best_c:
                    best_c = tableau[M][j]
                    q = j
            if q == -1:
                break

            min_ratio = float("inf")
            p = -1
            for i in range(M):
                if tableau[i][q] > EPS:
                    ratio = tableau[i][N + M] / tableau[i][q]
                    if ratio < min_ratio - EPS:
                        min_ratio = ratio
                        p = i
            if p == -1:
                break

            pivot_val = tableau[p][q]
            for j in range(N + M + 1):
                tableau[p][j] /= pivot_val
            for i in range(M + 1):
                if i != p and abs(tableau[i][q]) > 1e-12:
                    factor = tableau[i][q]
                    for j in range(N + M + 1):
                        tableau[i][j] -= factor * tableau[p][j]
            basis[p] = q

        if abs(tableau[M][N + M]) > 1e-5:
            return None

        sol = [0.0] * N
        for i in range(M):
            if basis[i] < N:
                sol[basis[i]] = tableau[i][N + M]
        return sol

    def branch_and_bound(extra_constraints):
        sol = solve_lp(extra_constraints)
        if sol is None:
            return None

        most_frac_idx = -1
        max_dist = 0.0
        for i in range(K_vars):
            val = sol[i]
            dist = abs(val - round(val))
            if dist > 1e-4:
                if dist > max_dist:
                    max_dist = dist
                    most_frac_idx = i

        if most_frac_idx == -1:
            return sol

        val = sol[most_frac_idx]
        floor_val = int(val)
        ceil_val = floor_val + 1

        if val - floor_val >= 0.5:
            branches = [
                (most_frac_idx, ">=", ceil_val),
                (most_frac_idx, "<=", floor_val),
            ]
        else:
            branches = [
                (most_frac_idx, "<=", floor_val),
                (most_frac_idx, ">=", ceil_val),
            ]

        for branch in branches:
            res = branch_and_bound(extra_constraints + [branch])
            if res is not None:
                return res

        return None

    solution = branch_and_bound([])

    if solution is None:
        print("NO")
    else:
        print("YES")
        for i in range(k):
            row = [int(round(solution[i * m + j])) for j in range(m)]
            print(*(row))


if __name__ == "__main__":
    solve()