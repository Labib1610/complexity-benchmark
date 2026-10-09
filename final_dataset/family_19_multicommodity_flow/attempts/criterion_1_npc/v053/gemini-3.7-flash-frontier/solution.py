import sys

sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    compounds = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        compounds.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    num_vars = k * m
    base_eqs = []

    for e_idx, (u, v, cap) in enumerate(edges):
        row = [0.0] * num_vars
        for c_idx in range(k):
            row[c_idx * m + e_idx] = 1.0
        base_eqs.append((row, 1, float(cap)))

    for c_idx, (s, t, d) in enumerate(compounds):
        for node in range(n):
            if node == t:
                continue
            row = [0.0] * num_vars
            for e_idx, (u, v, cap) in enumerate(edges):
                if u == node:
                    row[c_idx * m + e_idx] += 1.0
                if v == node:
                    row[c_idx * m + e_idx] -= 1.0
            target = float(d) if node == s else 0.0
            base_eqs.append((row, 0, target))

    def solve_lp(extra_constraints):
        all_eqs = base_eqs + extra_constraints
        rows = []
        rhs = []
        num_slacks = 0
        slack_positions = []

        for row, op, val in all_eqs:
            if op == 1:  # <=
                slack_positions.append((len(rows), 1.0))
                num_slacks += 1
            elif op == -1:  # >=
                slack_positions.append((len(rows), -1.0))
                num_slacks += 1
            else:
                pass
            rows.append(list(row))
            rhs.append(val)

        M = len(rows)
        N = num_vars + num_slacks

        full_A = [[0.0] * N for _ in range(M)]
        slack_idx = 0
        for i in range(M):
            for j in range(num_vars):
                full_A[i][j] = rows[i][j]

        for r, coeff in slack_positions:
            full_A[r][num_vars + slack_idx] = coeff
            slack_idx += 1

        for i in range(M):
            if rhs[i] < -1e-9:
                for j in range(N):
                    full_A[i][j] = -full_A[i][j]
                rhs[i] = -rhs[i]
            elif rhs[i] < 0:
                rhs[i] = 0.0

        tab = [[0.0] * (N + M + 1) for _ in range(M + 1)]
        basis = [0] * M

        for i in range(M):
            for j in range(N):
                tab[i + 1][j] = full_A[i][j]
            tab[i + 1][N + i] = 1.0
            tab[i + 1][-1] = rhs[i]
            basis[i] = N + i

        for j in range(N + M + 1):
            s = 0.0
            for i in range(1, M + 1):
                s += tab[i][j]
            tab[0][j] = s

        for i in range(M):
            tab[0][N + i] = 0.0

        while True:
            enter = -1
            max_val = 1e-9
            for j in range(N + M):
                if tab[0][j] > max_val:
                    max_val = tab[0][j]
                    enter = j
            if enter == -1:
                break

            leave = -1
            min_ratio = 1e18
            for i in range(1, M + 1):
                if tab[i][enter] > 1e-9:
                    ratio = tab[i][-1] / tab[i][enter]
                    if ratio < min_ratio - 1e-11:
                        min_ratio = ratio
                        leave = i

            if leave == -1:
                break

            piv = tab[leave][enter]
            for j in range(N + M + 1):
                tab[leave][j] /= piv

            for i in range(M + 1):
                if i != leave and abs(tab[i][enter]) > 1e-12:
                    factor = tab[i][enter]
                    for j in range(N + M + 1):
                        tab[i][j] -= factor * tab[leave][j]

            basis[leave - 1] = enter

        if tab[0][-1] > 1e-6:
            return None

        sol = [0.0] * num_vars
        for i in range(M):
            if basis[i] < num_vars:
                sol[basis[i]] = tab[i + 1][-1]

        return sol

    def branch_and_bound(extra_constraints):
        sol = solve_lp(extra_constraints)
        if sol is None:
            return None

        frac_var = -1
        max_dist = 0.0
        for j in range(num_vars):
            val = sol[j]
            dist = abs(val - round(val))
            if dist > 1e-4 and dist > max_dist:
                max_dist = dist
                frac_var = j

        if frac_var == -1:
            return [int(round(x)) for x in sol]

        val = sol[frac_var]
        floor_val = float(int(val))
        ceil_val = floor_val + 1.0

        row = [0.0] * num_vars
        row[frac_var] = 1.0

        res = branch_and_bound(extra_constraints + [(row, 1, floor_val)])
        if res is not None:
            return res

        res = branch_and_bound(extra_constraints + [(row, -1, ceil_val)])
        if res is not None:
            return res

        return None

    solution = branch_and_bound([])
    if solution is None:
        print("NO")
    else:
        print("YES")
        for c_idx in range(k):
            start = c_idx * m
            end = start + m
            print(*(solution[start:end]))


if __name__ == "__main__":
    solve()