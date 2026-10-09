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

    # Fast feasibility checks
    # If s_i == t_i and d_i == 0, simple. If s_i == t_i and d_i > 0, handled by net flow = 0.
    
    # We want to find an integer assignment x_{i, e} >= 0 for i in 0..k-1, e in 0..m-1.
    # Total integer variables: num_vars = k * m.
    # Let's index x_{i, e} as i * m + e.
    
    num_vars = k * m
    
    # Conservation constraints:
    # For each product i, node u (u != t_i):
    # sum_{e out of u} x_{i, e} - sum_{e into u} x_{i, e} = d_i if u == s_i else 0
    # Capacity constraints:
    # For each edge e:
    # sum_i x_{i, e} <= cap_e
    
    # We can use a Branch-and-Bound / DFS with LP or DFS with residual graphs if small,
    # or a robust ILP solver via Simplex.
    
    # Let's build LP tableau:
    # Variables: x_0, ..., x_{num_vars-1}
    # Bounds: l_j <= x_j <= u_j (initially 0 <= x_j <= cap_e)
    
    # Equality constraints: A_eq x = b_eq
    # Inequality constraints: A_ub x <= b_ub
    
    eq_rows = []
    eq_rhs = []
    for i in range(k):
        s_i, t_i, d_i = products[i]
        for u in range(n):
            if u == t_i:
                continue
            row = [0.0] * num_vars
            for e in range(m):
                uu, vv, _ = edges[e]
                if uu == u:
                    row[i * m + e] += 1.0
                if vv == u:
                    row[i * m + e] -= 1.0
            rhs = float(d_i if u == s_i else 0)
            eq_rows.append(row)
            eq_rhs.append(rhs)
            
    ub_rows = []
    ub_rhs = []
    for e in range(m):
        row = [0.0] * num_vars
        for i in range(k):
            row[i * m + e] = 1.0
        ub_rows.append(row)
        ub_rhs.append(float(edges[e][2]))

    # Using standard Simplex for LP relaxation with bounds:
    # To be extremely fast and self-contained, let's implement Dual Simplex or Primal Simplex with upper/lower bounds.
    # Alternatively, convert everything to standard form Ax = b, x >= 0:
    # For each ub constraint: sum_i x_{i, e} + s_e = cap_e (s_e >= 0).
    # Bounds on x_j: we can enforce lower bounds by shifting x_j' = x_j - l_j >= 0,
    # and upper bounds x_j' + slack = u_j - l_j.
    
    def solve_lp(lower_bounds, upper_bounds):
        # Shift variables by lower_bounds: x_j = l_j + y_j, 0 <= y_j
        # For each variable, if upper_bound < lower_bound: infeasible
        for j in range(num_vars):
            if lower_bounds[j] > upper_bounds[j]:
                return None
                
        # Build constraints for y:
        # Eq constraints: A_eq y = b_eq - A_eq * l
        # Ub constraints: A_ub y + slack = b_ub - A_ub * l
        # Var ub constraints: y_j + s_j = u_j - l_j
        
        # Total equality constraints (including slacks):
        # A y_all = b, y_all >= 0
        rows = []
        rhs = []
        
        for r, b in zip(eq_rows, eq_rhs):
            shift = sum(r[j] * lower_bounds[j] for j in range(num_vars))
            rows.append(list(r))
            rhs.append(b - shift)
            
        for r, b in zip(ub_rows, ub_rhs):
            shift = sum(r[j] * lower_bounds[j] for j in range(num_vars))
            rows.append(list(r))
            rhs.append(b - shift)
            
        num_slacks = len(ub_rows)
        # Add variable upper bound constraints
        for j in range(num_vars):
            if upper_bounds[j] < 1e8:
                r = [0.0] * num_vars
                r[j] = 1.0
                rows.append(r)
                rhs.append(float(upper_bounds[j] - lower_bounds[j]))
                
        total_rows = len(rows)
        total_slacks = total_rows - len(eq_rows)
        total_vars = num_vars + total_slacks
        
        # Pad rows with slack variables
        slack_idx = 0
        for i in range(len(eq_rows), total_rows):
            for r_idx in range(total_rows):
                if r_idx == i:
                    rows[r_idx].append(1.0)
                else:
                    rows[r_idx].append(0.0)
            slack_idx += 1
        for i in range(len(eq_rows)):
            for _ in range(total_slacks):
                rows[i].append(0.0)
                
        # Now we have standard form: A y = rhs, y >= 0
        # Make all rhs >= 0 by multiplying by -1
        for i in range(total_rows):
            if rhs[i] < -1e-9:
                for j in range(total_vars):
                    rows[i][j] = -rows[i][j]
                rhs[i] = -rhs[i]
            elif rhs[i] < 0:
                rhs[i] = 0.0

        # Phase I / Phase II Simplex using Two-Phase Tableau
        # Tableau size: (total_rows + 2) x (total_vars + total_rows + 1)
        # We add artificial variables for each row
        M = total_rows
        N = total_vars
        
        tableau = [[0.0] * (N + M + 1) for _ in range(M + 2)]
        
        for i in range(M):
            for j in range(N):
                tableau[i][j] = rows[i][j]
            tableau[i][N + i] = 1.0
            tableau[i][-1] = rhs[i]
            
        basis = [N + i for i in range(M)]
        
        # Phase 1 objective: minimize sum of artificials
        # Row M is Phase 1 objective
        for j in range(N + M + 1):
            tableau[M][j] = -sum(tableau[i][j] for i in range(M))
            
        # Simplex pivot helper
        def pivot(r, c, obj_row, cols_cnt):
            inv = 1.0 / tableau[r][c]
            for j in range(cols_cnt):
                tableau[r][j] *= inv
            for i in range(M + 2):
                if i != r:
                    factor = tableau[i][c]
                    if abs(factor) > 1e-12:
                        for j in range(cols_cnt):
                            tableau[i][j] -= factor * tableau[r][j]
            basis[r] = c

        # Phase 1 loop
        while True:
            # Bland's rule or min reduced cost
            c = -1
            min_val = -1e-8
            for j in range(N + M):
                if tableau[M][j] < min_val:
                    min_val = tableau[M][j]
                    c = j
            if c == -1:
                break
                
            r = -1
            min_ratio = float('inf')
            for i in range(M):
                if tableau[i][c] > 1e-8:
                    ratio = tableau[i][-1] / tableau[i][c]
                    if ratio < min_ratio - 1e-11:
                        min_ratio = ratio
                        r = i
            if r == -1:
                break
            pivot(r, c, M, N + M + 1)
            
        if tableau[M][-1] < -1e-5:
            return None # Infeasible
            
        # Extract solution for original variables
        sol = [0.0] * num_vars
        for i in range(M):
            if basis[i] < num_vars:
                sol[basis[i]] = tableau[i][-1]
                
        # Shift back
        for j in range(num_vars):
            sol[j] += lower_bounds[j]
            
        return sol

    # Branch and Bound
    best_sol = None
    
    init_lb = [0] * num_vars
    init_ub = [edges[e][2] for i in range(k) for e in range(m)]
    
    # Priority queue / stack for DFS
    stack = [(init_lb, init_ub)]
    
    while stack:
        lb, ub = stack.pop()
        sol = solve_lp(lb, ub)
        if sol is None:
            continue
            
        # Check integrality
        frac_var = -1
        max_dist = -1
        for j in range(num_vars):
            val = sol[j]
            dist = abs(val - round(val))
            if dist > 1e-4:
                if dist > max_dist:
                    max_dist = dist
                    frac_var = j
                    
        if frac_var == -1:
            # Integer solution found!
            best_sol = [int(round(x)) for x in sol]
            break
            
        val = sol[frac_var]
        floor_val = int(val)
        ceil_val = floor_val + 1
        
        # Branch: x <= floor_val and x >= ceil_val
        # To find solution faster, order branches based on which integer is closer
        branch1_lb, branch1_ub = list(lb), list(ub)
        branch1_ub[frac_var] = min(branch1_ub[frac_var], floor_val)
        
        branch2_lb, branch2_ub = list(lb), list(ub)
        branch2_lb[frac_var] = max(branch2_lb[frac_var], ceil_val)
        
        if val - floor_val < 0.5:
            stack.append((branch2_lb, branch2_ub))
            stack.append((branch1_lb, branch1_ub))
        else:
            stack.append((branch1_lb, branch1_ub))
            stack.append((branch2_lb, branch2_ub))

    if best_sol is None:
        print("NO")
    else:
        print("YES")
        for i in range(k):
            print(*(best_sol[i * m + e] for e in range(m)))

if __name__ == '__main__':
    solve()