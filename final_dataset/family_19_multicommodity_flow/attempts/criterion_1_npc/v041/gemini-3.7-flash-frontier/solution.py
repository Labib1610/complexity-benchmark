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

    # Variables: x_{c, e} for commodity c in 0..k-1, edge e in 0..m-1
    # Index: var_idx(c, e) = c * m + e
    num_vars = k * m

    # Constraints:
    # 1. Flow conservation for each commodity c and camp u (excluding t_c to avoid redundancy, or all u)
    #    sum_{e: out(u)} x_{c, e} - sum_{e: in(u)} x_{c, e} = supply(c, u)
    #    where supply(c, s_c) = d_c, supply(c, t_c) = -d_c, else 0.
    # 2. Capacity for each edge e:
    #    sum_{c} x_{c, e} <= cap_e
    # 3. Variable bounds: x_{c, e} >= 0 (and upper bounds can be added in B&B).

    # Let's build an exact ILP solver using Branch and Bound with Dual/Primal Simplex.
    
    eq_rows = []
    eq_rhs = []
    for c in range(k):
        s_c, t_c, d_c = commodities[c]
        for u in range(n):
            if u == t_c:
                continue  # redundant
            row = [0.0] * num_vars
            for e, (eu, ev, _) in enumerate(edges):
                if eu == u:
                    row[c * m + e] += 1.0
                if ev == u:
                    row[c * m + e] -= 1.0
            rhs = float(d_c) if u == s_c else 0.0
            eq_rows.append(row)
            eq_rhs.append(rhs)

    # Inequalities: A_ineq * x <= b_ineq
    ineq_rows = []
    ineq_rhs = []
    for e in range(m):
        row = [0.0] * num_vars
        for c in range(k):
            row[c * m + e] = 1.0
        ineq_rows.append(row)
        ineq_rhs.append(float(edges[e][2]))

    # Simplex solver for LP:
    # Convert all constraints to Ax <= b and Ax >= b (i.e. -Ax <= -b) or standard form.
    # For branch and bound, we maintain variable bounds: lb <= x_j <= ub.

    def solve_lp(lower_bounds, upper_bounds):
        # Build standard form:
        # x_j = x'_j + lb_j where 0 <= x'_j <= ub_j - lb_j
        # Or just use standard tableau with slacks/artificials.
        
        # We can construct:
        # Equalities: sum a_{i,j} x_j = b_i
        # Inequalities: sum a_{i,j} x_j <= b_i
        # Bound inequalities: x_j <= ub_j, -x_j <= -lb_j
        
        # Total inequalities:
        cur_ineq = [row[:] for row in ineq_rows]
        cur_ineq_rhs = ineq_rhs[:]
        
        for j in range(num_vars):
            if upper_bounds[j] < 1e8:
                row = [0.0] * num_vars
                row[j] = 1.0
                cur_ineq.append(row)
                cur_ineq_rhs.append(float(upper_bounds[j]))
            if lower_bounds[j] > 0:
                row = [0.0] * num_vars
                row[j] = -1.0
                cur_ineq.append(row)
                cur_ineq_rhs.append(-float(lower_bounds[j]))
                
        # Combine equalities into pairs of inequalities: Ax <= b and -Ax <= -b
        all_rows = []
        all_rhs = []
        for r, rhs in zip(eq_rows, eq_rhs):
            all_rows.append(r[:])
            all_rhs.append(rhs)
            all_rows.append([-val for val in r])
            all_rhs.append(-rhs)
            
        for r, rhs in zip(cur_ineq, cur_ineq_rhs):
            all_rows.append(r)
            all_rhs.append(rhs)

        num_constraints = len(all_rows)
        # Formulate Phase 1 Simplex to find a feasible solution x >= 0:
        # Variables: x_1..x_N, slack_1..slack_M
        # If rhs < 0, multiply by -1 and use artificial variable.
        
        # Standard Tableau construction:
        # We want to minimize sum of artificial variables.
        A = []
        b = []
        slack_cols = []
        art_cols = []
        
        num_slack = 0
        num_art = 0
        
        for i in range(num_constraints):
            row = all_rows[i][:]
            rhs = all_rhs[i]
            if rhs >= -1e-9:
                # row * x + s_i = rhs
                A.append((row, 1.0, None, rhs)) # (orig_row, slack_sign, art_id, rhs)
                num_slack += 1
            else:
                # -row * x - s_i + a_i = -rhs
                # Actually, standard: row * x <= rhs with rhs < 0 -> -row * x >= -rhs -> -row * x - s_i + a_i = -rhs
                A.append(([-val for val in row], -1.0, num_art, -rhs))
                num_slack += 1
                num_art += 1

        total_cols = num_vars + num_slack + num_art
        # Build matrix
        mat = []
        basis = []
        
        slack_idx = num_vars
        art_idx = num_vars + num_slack
        
        for i, (orig_row, s_sign, a_id, rhs) in enumerate(A):
            full_row = [0.0] * (total_cols + 1)
            for j in range(num_vars):
                full_row[j] = orig_row[j]
            full_row[slack_idx + i] = s_sign
            if a_id is not None:
                full_row[art_idx + a_id] = 1.0
                basis.append(art_idx + a_id)
            else:
                basis.append(slack_idx + i)
            full_row[-1] = rhs
            mat.append(full_row)

        if num_art == 0:
            # All slacks are basic and rhs >= 0, solution is already feasible!
            sol = [0.0] * num_vars
            for i in range(num_constraints):
                if basis[i] < num_vars:
                    sol[basis[i]] = mat[i][-1]
            return sol

        # Objective row for Phase 1: min sum of art variables -> max -sum(art)
        # Cost vector c: c[art] = -1, others 0
        obj = [0.0] * (total_cols + 1)
        for a in range(num_art):
            col = art_idx + a
            # subtract row where this art is basic
            # find row
            r_idx = basis.index(col)
            for c in range(total_cols + 1):
                obj[c] -= mat[r_idx][c]

        # Simplex loop
        def pivot(mat, basis, obj, pr, pc):
            piv_val = mat[pr][pc]
            for c in range(len(mat[0])):
                mat[pr][c] /= piv_val
            for r in range(len(mat)):
                if r != pr:
                    factor = mat[r][pc]
                    if abs(factor) > 1e-12:
                        for c in range(len(mat[0])):
                            mat[r][c] -= factor * mat[pr][c]
            factor = obj[pc]
            if abs(factor) > 1e-12:
                for c in range(len(mat[0])):
                    obj[c] -= factor * mat[pr][c]
            basis[pr] = pc

        # Run Phase 1
        steps = 0
        while steps < 2000:
            steps += 1
            # Find entering variable: min negative in obj (for maximization) -> most positive reduced cost
            # Here obj is maximized, so entering var has obj[c] > 1e-7
            best_c = -1
            max_val = 1e-7
            for c in range(total_cols):
                if obj[c] > max_val:
                    max_val = obj[c]
                    best_c = c
            if best_c == -1:
                break
            
            # Ratio test
            best_r = -1
            min_ratio = 1e18
            for r in range(len(mat)):
                if mat[r][best_c] > 1e-8:
                    ratio = mat[r][-1] / mat[r][best_c]
                    if ratio < min_ratio - 1e-10 or (abs(ratio - min_ratio) <= 1e-10 and (best_r == -1 or basis[r] > basis[best_r])):
                        min_ratio = ratio
                        best_r = r
            if best_r == -1:
                # Unbounded in phase 1 (shouldn't happen)
                break
            pivot(mat, basis, obj, best_r, best_c)

        if abs(obj[-1]) > 1e-5:
            return None # Infeasible

        sol = [0.0] * num_vars
        for r in range(len(mat)):
            if basis[r] < num_vars:
                sol[basis[r]] = mat[r][-1]
        return sol

    # Branch and bound
    best_sol = None
    
    lb = [0] * num_vars
    ub = [edges[e][2] for c in range(k) for e in range(m)]

    stack = [(lb, ub)]
    
    while stack:
        cur_lb, cur_ub = stack.pop()
        
        # Check simple bounds
        if any(cur_lb[j] > cur_ub[j] for j in range(num_vars)):
            continue
            
        lp_sol = solve_lp(cur_lb, cur_ub)
        if lp_sol is None:
            continue
            
        # Find first non-integer variable
        frac_var = -1
        max_dist = 0.0
        for j in range(num_vars):
            val = lp_sol[j]
            dist = abs(val - round(val))
            if dist > 1e-4:
                if dist > max_dist:
                    max_dist = dist
                    frac_var = j
                    
        if frac_var == -1:
            best_sol = [int(round(v)) for v in lp_sol]
            break
            
        val = lp_sol[frac_var]
        floor_val = int(val)
        ceil_val = floor_val + 1
        
        # Branch: x_j <= floor_val and x_j >= ceil_val
        # Branch floor first or ceil first
        lb1, ub1 = cur_lb[:], cur_ub[:]
        ub1[frac_var] = min(ub1[frac_var], floor_val)
        
        lb2, ub2 = cur_lb[:], cur_ub[:]
        lb2[frac_var] = max(lb2[frac_var], ceil_val)
        
        # Add to stack (prefer branch closer to LP solution)
        if val - floor_val > 0.5:
            stack.append((lb1, ub1))
            stack.append((lb2, ub2))
        else:
            stack.append((lb2, ub2))
            stack.append((lb1, ub1))

    if best_sol is None:
        print("NO")
    else:
        print("YES")
        for c in range(k):
            row_sol = [str(best_sol[c * m + e]) for e in range(m)]
            print(" ".join(row_sol))

if __name__ == '__main__':
    solve()