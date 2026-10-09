import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    orders = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        orders.append((s, t, d))
        
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))

    # Fast path: DFS / Path finding if k is small or total demand is small
    # Variables: x[i][j] = flow of order i on edge j
    # We can use ILP via Branch and Bound / Simplex, or if small, DFS.
    
    num_vars = k * m
    
    # Conservation constraints: k * n
    # Capacity constraints: m
    # Upper bounds: x[i][j] <= c_j
    
    # Let's set up the standard LP:
    # Minimize 0 subject to:
    # A_eq x = b_eq
    # A_ub x <= b_ub
    # x >= 0, integer
    
    eq_rows = []
    eq_b = []
    for i in range(k):
        s_i, t_i, d_i = orders[i]
        for node in range(n):
            row = [0.0] * num_vars
            # sum out - sum in
            for j in range(m):
                u, v, _ = edges[j]
                if u == node:
                    row[i * m + j] += 1.0
                if v == node:
                    row[i * m + j] -= 1.0
            rhs = 0.0
            if node == s_i:
                rhs = float(d_i)
            elif node == t_i:
                rhs = float(-d_i)
            eq_rows.append(row)
            eq_b.append(rhs)
            
    ub_rows = []
    ub_b = []
    for j in range(m):
        row = [0.0] * num_vars
        for i in range(k):
            row[i * m + j] = 1.0
        ub_rows.append(row)
        ub_b.append(float(edges[j][2]))

    # Simplex tableau implementation
    # We use Two-Phase Simplex to solve LP relaxations.
    
    # We will build a helper that solves LP with bounds on variables.
    def solve_lp(lower_bounds, upper_bounds):
        # We transform bounds: x_j = l_j + x'_j where 0 <= x'_j <= u_j - l_j
        # Or just add upper and lower bounds as inequality constraints.
        # Adding as constraints:
        # x_v <= ub_v
        # -x_v <= -lb_v
        
        # Constraints:
        # 1. eq_rows * x = eq_b
        # 2. ub_rows * x <= ub_b
        # 3. x_v <= upper_bounds[v]
        # 4. -x_v <= -lower_bounds[v]
        
        # Let's construct standard form:
        # All variables >= 0
        # Equalities and <= inequalities (with slack variables)
        
        # Total original variables: num_vars
        # Slack variables for ub_rows: len(ub_rows)
        # Slack variables for upper_bounds: num_vars
        # Slack variables for lower_bounds: num_vars
        
        rows = []
        rhs = []
        
        # Equalities
        for r, b in zip(eq_rows, eq_b):
            rows.append(list(r))
            rhs.append(b)
            
        # Capacities
        slack_count = 0
        for r, b in zip(ub_rows, ub_b):
            row = list(r)
            rows.append(row)
            rhs.append(b)
            slack_count += 1
            
        # Variable bounds
        for v in range(num_vars):
            if upper_bounds[v] < 1e9:
                row = [0.0] * num_vars
                row[v] = 1.0
                rows.append(row)
                rhs.append(float(upper_bounds[v]))
                slack_count += 1
                
        for v in range(num_vars):
            if lower_bounds[v] > 0:
                row = [0.0] * num_vars
                row[v] = -1.0
                rows.append(row)
                rhs.append(-float(lower_bounds[v]))
                slack_count += 1

        num_constraints = len(rows)
        # Build tableau with slack and artificial variables
        # For rows with rhs < 0, multiply by -1
        # Tableau columns: original vars (num_vars), slack vars, artificial vars, RHS
        
        # Expand rows with slack vars
        expanded_rows = []
        slack_idx = 0
        art_idx = 0
        art_rows = []
        
        num_eq = len(eq_rows)
        
        for i in range(num_constraints):
            r = list(rows[i])
            b = rhs[i]
            if b < -1e-9:
                r = [-x for x in r]
                b = -b
                is_ge = True
            else:
                is_ge = False
                
            # Slacks
            r_slacks = [0.0] * slack_count
            if i >= num_eq:
                if not is_ge:
                    r_slacks[slack_idx] = 1.0
                else:
                    r_slacks[slack_idx] = -1.0
                slack_idx += 1
            
            expanded_rows.append((r, r_slacks, b, i < num_eq or is_ge))
        
        num_art = sum(1 for _, _, _, need_art in expanded_rows if need_art)
        
        total_cols = num_vars + slack_count + num_art
        tableau = []
        basis = []
        
        art_curr = 0
        slack_curr = 0
        for i in range(num_constraints):
            r, r_slacks, b, need_art = expanded_rows[i]
            full_row = r + r_slacks + [0.0] * num_art + [b]
            if need_art:
                full_row[num_vars + slack_count + art_curr] = 1.0
                basis.append(num_vars + slack_count + art_curr)
                art_curr += 1
            else:
                basis.append(num_vars + slack_curr)
                slack_curr += 1
            tableau.append(full_row)
            
        # Phase 1 Objective: Minimize sum of artificial variables
        # Obj row:
        obj_row = [0.0] * (total_cols + 1)
        for i in range(num_constraints):
            _, _, _, need_art = expanded_rows[i]
            if need_art:
                for c in range(total_cols + 1):
                    obj_row[c] -= tableau[i][c]
        tableau.append(obj_row)
        
        # Simplex Phase 1
        def pivot(tableau, basis, r, c):
            p = tableau[r][c]
            for col in range(len(tableau[r])):
                tableau[r][col] /= p
            for row in range(len(tableau)):
                if row != r:
                    factor = tableau[row][c]
                    if abs(factor) > 1e-12:
                        for col in range(len(tableau[row])):
                            tableau[row][col] -= factor * tableau[r][col]
            basis[r] = c

        while True:
            # Bland's rule or most negative
            min_v = -1e-9
            pivot_col = -1
            for c in range(total_cols):
                if tableau[-1][c] < min_v:
                    min_v = tableau[-1][c]
                    pivot_col = c
            if pivot_col == -1:
                break
                
            min_ratio = float('inf')
            pivot_row = -1
            for r in range(num_constraints):
                val = tableau[r][pivot_col]
                if val > 1e-9:
                    ratio = tableau[r][-1] / val
                    if ratio < min_ratio - 1e-9:
                        min_ratio = ratio
                        pivot_row = r
            if pivot_row == -1:
                # Unbounded (should not happen in phase 1)
                return None
            pivot(tableau, basis, pivot_row, pivot_col)
            
        if tableau[-1][-1] < -1e-5:
            # Infeasible
            return None
            
        # Extract solution
        sol = [0.0] * num_vars
        for r in range(num_constraints):
            var = basis[r]
            if var < num_vars:
                sol[var] = tableau[r][-1]
        return sol

    # Branch and bound for integer solution
    lower_b = [0] * num_vars
    upper_b = [edges[j][2] for i in range(k) for j in range(m)]
    
    # Priority queue / stack for B&B
    stack = [(lower_b, upper_b)]
    
    while stack:
        lb, ub = stack.pop()
        sol = solve_lp(lb, ub)
        if sol is None:
            continue
            
        # Check if integer
        first_non_int = -1
        max_dist = 0.0
        for i in range(num_vars):
            val = sol[i]
            dist = abs(val - round(val))
            if dist > 1e-4 and dist > max_dist:
                max_dist = dist
                first_non_int = i
                
        if first_non_int == -1:
            # Found integer solution!
            print("YES")
            int_sol = [int(round(x)) for x in sol]
            for i in range(k):
                row_flows = [int_sol[i * m + j] for j in range(m)]
                print(*(row_flows))
            return
            
        var = first_non_int
        val = sol[var]
        
        # Branch 1: <= floor(val)
        branch1_ub = list(ub)
        branch1_ub[var] = min(branch1_ub[var], int(val))
        if branch1_ub[var] >= lb[var]:
            stack.append((lb, branch1_ub))
            
        # Branch 2: >= ceil(val)
        branch2_lb = list(lb)
        branch2_lb[var] = max(branch2_lb[var], int(val) + 1)
        if branch2_lb[var] <= ub[var]:
            stack.append((branch2_lb, ub))
            
    print("NO")

if __name__ == '__main__':
    solve()