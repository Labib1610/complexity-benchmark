import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    
    commodities = []
    for _ in range(k):
        s = int(next(iterator)) - 1
        t = int(next(iterator)) - 1
        d = int(next(iterator))
        commodities.append((s, t, d))
        
    edges = []
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        cap = int(next(iterator))
        edges.append((u, v, cap))

    # Total variables: k * m
    # Variable index for commodity c and edge e: c * m + e
    num_vars = k * m
    
    # Constraints:
    # 1. Flow conservation: for each c and each node v:
    # sum_{e out of v} x_{c, e} - sum_{e into v} x_{c, e} = rhs
    # 2. Capacity constraints: for each edge e:
    # sum_c x_{c, e} <= cap_e
    # 3. Non-negativity and upper bounds: 0 <= x_{c, e} <= cap_e

    # Build constraint matrix
    # Standard form for Two-Phase Simplex or Branch and Bound
    # A_eq * x = b_eq
    # A_ub * x <= b_ub
    
    eq_rows = []
    eq_rhs = []
    
    for c in range(k):
        s, t, d = commodities[c]
        for v in range(n):
            row = [0.0] * num_vars
            has_edges = False
            for e_idx, (u_edge, v_edge, _) in enumerate(edges):
                if u_edge == v:
                    row[c * m + e_idx] += 1.0
                    has_edges = True
                if v_edge == v:
                    row[c * m + e_idx] -= 1.0
                    has_edges = True
            
            rhs = 0.0
            if v == s:
                rhs += d
            if v == t:
                rhs -= d
            
            if not has_edges and rhs != 0:
                print("NO")
                return
            
            eq_rows.append(row)
            eq_rhs.append(rhs)
            
    ub_rows = []
    ub_rhs = []
    for e_idx, (_, _, cap) in enumerate(edges):
        row = [0.0] * num_vars
        for c in range(k):
            row[c * m + e_idx] = 1.0
        ub_rows.append(row)
        ub_rhs.append(float(cap))
        
    # Bounds on variables
    bounds = [(0.0, float(edges[e_idx][2])) for c in range(k) for e_idx in range(m)]

    # Simplex solver for LP relaxation
    # Convert all inequalities to equalities with slack variables
    # A x = b, bounds on x
    
    # Simplex tableau implementation
    # We will use standard Two-Phase Simplex
    
    def solve_lp(extra_bounds):
        # extra_bounds: list of (low, high) for each var
        # Transform variables: x_i = low_i + x'_i, where 0 <= x'_i <= high_i - low_i
        # If low_i > high_i: infeasible
        var_low = [max(bounds[i][0], extra_bounds[i][0]) for i in range(num_vars)]
        var_high = [min(bounds[i][1], extra_bounds[i][1]) for i in range(num_vars)]
        for i in range(num_vars):
            if var_low[i] > var_high[i] + 1e-7:
                return None
        
        # Build system A * x' <= / == b'
        # Ub constraints: sum A_ub * x' <= b_ub - sum A_ub * low
        # Upper bounds on vars: x'_i <= high_i - low_i
        # Eq constraints: sum A_eq * x' == b_eq - sum A_eq * low
        
        rows = []
        rhs = []
        is_eq = []
        
        for r, b_val in zip(eq_rows, eq_rhs):
            shift = sum(r[i] * var_low[i] for i in range(num_vars))
            rows.append(list(r))
            rhs.append(b_val - shift)
            is_eq.append(True)
            
        for r, b_val in zip(ub_rows, ub_rhs):
            shift = sum(r[i] * var_low[i] for i in range(num_vars))
            rows.append(list(r))
            rhs.append(b_val - shift)
            is_eq.append(False)
            
        for i in range(num_vars):
            r = [0.0] * num_vars
            r[i] = 1.0
            rows.append(r)
            rhs.append(var_high[i] - var_low[i])
            is_eq.append(False)
            
        # Standard form for Two-Phase Simplex
        # Ensure rhs >= 0
        num_constraints = len(rows)
        for i in range(num_constraints):
            if rhs[i] < -1e-9:
                rows[i] = [-val for val in rows[i]]
                rhs[i] = -rhs[i]
                if not is_eq[i]:
                    # was <=, now >=, which is not directly present, but our original ub was >= 0 so shift shouldn't easily make it negative unless low > high
                    # but if it was <=, multiplying by -1 makes it >=.
                    # Instead of general >= handling, let's just handle it properly:
                    pass
        
        # To make it robust and simple, let's use a standard tableau with slack and artificial variables
        # Constraints:
        # For <= : add slack s_i >= 0
        # For >= : subtract surplus, add artificial
        # For == : add artificial
        
        tableau = []
        basis = []
        
        total_cols = num_vars
        # First pass to count slacks and artificials
        num_slack = 0
        num_art = 0
        constraint_types = [] # 0: <=, 1: ==, 2: >=
        
        for i in range(num_constraints):
            b = rhs[i]
            # Since we multiplied if b < 0, check original
            # Let's re-normalize: if rhs[i] < 0:
            if rhs[i] < 0:
                rows[i] = [-v for v in rows[i]]
                rhs[i] = -rhs[i]
                if is_eq[i]:
                    constraint_types.append(1)
                    num_art += 1
                else:
                    constraint_types.append(2) # >=
                    num_slack += 1
                    num_art += 1
            else:
                if is_eq[i]:
                    constraint_types.append(1)
                    num_art += 1
                else:
                    constraint_types.append(0) # <=
                    num_slack += 1
                    
        # Total columns = num_vars + num_slack + num_art
        slack_idx = num_vars
        art_idx = num_vars + num_slack
        
        curr_slack = 0
        curr_art = 0
        
        A_full = []
        b_full = []
        
        for i in range(num_constraints):
            row = list(rows[i]) + [0.0] * (num_slack + num_art)
            ctype = constraint_types[i]
            if ctype == 0: # <=
                row[slack_idx + curr_slack] = 1.0
                basis.append(slack_idx + curr_slack)
                curr_slack += 1
            elif ctype == 1: # ==
                row[art_idx + curr_art] = 1.0
                basis.append(art_idx + curr_art)
                curr_art += 1
            elif ctype == 2: # >=
                row[slack_idx + curr_slack] = -1.0
                curr_slack += 1
                row[art_idx + curr_art] = 1.0
                basis.append(art_idx + curr_art)
                curr_art += 1
            A_full.append(row)
            b_full.append(rhs[i])
            
        N_vars = len(A_full[0])
        M_cons = len(A_full)
        
        # Phase 1: Minimize sum of artificial variables
        # Objective row 0: artificial variables have cost 1.0
        # Express obj in terms of non-basic variables
        obj = [0.0] * (N_vars + 1)
        for i in range(curr_art):
            obj[art_idx + i] = 1.0
            
        # Tableau: [row0; rows 1..M], each row is [coefficients..., rhs]
        T = []
        for i in range(M_cons):
            T.append(A_full[i] + [b_full[i]])
            
        # Row 0 in tableau (we maximize -sum(art))
        # Initially obj is: max -sum(art). So row 0 has +1 for art vars.
        row0 = [0.0] * (N_vars + 1)
        for i in range(curr_art):
            row0[art_idx + i] = 1.0
        
        # Pivot out basic artificial variables from row 0
        for i in range(M_cons):
            if basis[i] >= art_idx:
                for j in range(N_vars + 1):
                    row0[j] -= T[i][j]
        T.insert(0, row0)
        
        def pivot(r, c):
            pivot_val = T[r][c]
            for j in range(N_vars + 1):
                T[r][j] /= pivot_val
            for i in range(len(T)):
                if i != r:
                    factor = T[i][c]
                    if abs(factor) > 1e-12:
                        for j in range(N_vars + 1):
                            T[i][j] -= factor * T[r][j]
            basis[r - 1] = c
            
        # Simplex loop
        def run_simplex(max_iter=5000):
            it = 0
            while it < max_iter:
                it += 1
                # Find entering variable (most negative in row 0)
                min_val = -1e-8
                enter_col = -1
                for j in range(N_vars):
                    if T[0][j] < min_val:
                        min_val = T[0][j]
                        enter_col = j
                if enter_col == -1:
                    return True # Optimal
                
                # Min ratio test
                min_ratio = float('inf')
                pivot_row = -1
                for i in range(1, len(T)):
                    if T[i][enter_col] > 1e-8:
                        ratio = T[i][-1] / T[i][enter_col]
                        if ratio < min_ratio:
                            min_ratio = ratio
                            pivot_row = i
                if pivot_row == -1:
                    return False # Unbounded
                pivot(pivot_row, enter_col)
            return True

        if not run_simplex():
            return None
            
        # Check Phase 1 objective
        if abs(T[0][-1]) > 1e-5:
            return None # Infeasible
            
        # If any artificial variable is still in basis, try to pivot it out
        for i in range(M_cons):
            if basis[i] >= art_idx:
                pivoted = False
                for j in range(art_idx):
                    if abs(T[i+1][j]) > 1e-8:
                        pivot(i+1, j)
                        pivoted = True
                        break
                if not pivoted:
                    # Redundant constraint, keep as is
                    pass
                    
        # Extract solution
        sol = [0.0] * num_vars
        for i in range(M_cons):
            if basis[i] < num_vars:
                sol[basis[i]] = T[i+1][-1]
                
        # Add back shift
        real_sol = [sol[i] + var_low[i] for i in range(num_vars)]
        return real_sol

    # Branch and Bound
    # Stack for DFS
    stack = [[(0.0, float(edges[e_idx][2])) for c in range(k) for e_idx in range(m)]]
    
    while stack:
        cur_bounds = stack.pop()
        sol = solve_lp(cur_bounds)
        if sol is None:
            continue
            
        # Check integrality
        all_integer = True
        split_var = -1
        max_dist = 0.0
        
        for i in range(num_vars):
            val = sol[i]
            nearest = round(val)
            dist = abs(val - nearest)
            if dist > 1e-4:
                all_integer = False
                if dist > max_dist:
                    max_dist = dist
                    split_var = i
                    
        if all_integer:
            print("YES")
            # Format output
            int_sol = [int(round(x)) for x in sol]
            for c in range(k):
                row_sol = int_sol[c * m : (c + 1) * m]
                print(*(max(0, x) for x in row_sol))
            return
            
        val = sol[split_var]
        floor_val = float(int(val))
        ceil_val = floor_val + 1.0
        
        # Branch 1: var <= floor_val
        b1 = list(cur_bounds)
        b1[split_var] = (b1[split_var][0], min(b1[split_var][1], floor_val))
        
        # Branch 2: var >= ceil_val
        b2 = list(cur_bounds)
        b2[split_var] = (max(b2[split_var][0], ceil_val), b2[split_var][1])
        
        # Order branches
        if val - floor_val > 0.5:
            stack.append(b1)
            stack.append(b2)
        else:
            stack.append(b2)
            stack.append(b1)
            
    print("NO")

if __name__ == '__main__':
    solve()