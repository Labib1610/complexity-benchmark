import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    contracts = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        contracts.append((s, t, d))
        
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))
        
    # Variables: x_{i, e} for i in range(k), e in range(m)
    # Total primary variables = k * m
    num_vars = k * m
    
    def var_idx(i, e):
        return i * m + e

    # Constraints:
    # 1. Flow conservation for each contract i and each node u:
    # sum_{e out of u} x_{i, e} - sum_{e into u} x_{i, e} = b_{i, u}
    # where b_{i, s_i} = d_i, b_{i, t_i} = -d_i, else 0
    #
    # 2. Capacity for each edge e:
    # sum_{i} x_{i, e} <= c_e
    
    # Let's collect linear constraints:
    # A_eq * x = b_eq
    # A_ub * x <= b_ub
    # x >= 0
    
    eq_rows = []
    eq_b = []
    
    for i in range(k):
        s_i, t_i, d_i = contracts[i]
        for u in range(n):
            if u == t_i:
                continue # Redundant equation
            row = [0.0] * num_vars
            for e, (u_e, v_e, _) in enumerate(edges):
                if u_e == u:
                    row[var_idx(i, e)] += 1.0
                if v_e == u:
                    row[var_idx(i, e)] -= 1.0
            rhs = 0.0
            if u == s_i:
                rhs = float(d_i)
            eq_rows.append(row)
            eq_b.append(rhs)
            
    ub_rows = []
    ub_b = []
    for e, (_, _, c) in enumerate(edges):
        row = [0.0] * num_vars
        for i in range(k):
            row[var_idx(i, e)] = 1.0
        ub_rows.append(row)
        ub_b.append(float(c))
        
    # Simplex Tableau Solver
    EPS = 1e-7

    def solve_lp(extra_bounds):
        # extra_bounds: list of (var_index, op, val) where op is '<=' or '>='
        # Build tableau
        # All equalities: eq_rows
        # All upper bounds: ub_rows + extra bounds
        
        # Total inequalities: len(ub_rows) + len(extra_bounds)
        curr_ub_rows = [list(r) for r in ub_rows]
        curr_ub_b = list(ub_b)
        
        for v_idx, op, val in extra_bounds:
            row = [0.0] * num_vars
            if op == '<=':
                row[v_idx] = 1.0
                curr_ub_rows.append(row)
                curr_ub_b.append(float(val))
            else: # '>='
                row[v_idx] = -1.0
                curr_ub_rows.append(row)
                curr_ub_b.append(-float(val))

        num_eq = len(eq_rows)
        num_ineq = len(curr_ub_rows)
        num_slacks = num_ineq
        
        # Standard form:
        # A x + I s = b
        # If any b < 0, multiply row by -1 and handle artificials.
        # Phase 1 tableau:
        # Rows: num_eq + num_ineq
        # Columns: num_vars + num_slacks + num_artificial + 1 (RHS)
        
        rows = []
        # Add inequalities with slack
        for j in range(num_ineq):
            r = curr_ub_rows[j] + [0.0] * num_slacks
            r[num_vars + j] = 1.0
            rhs = curr_ub_b[j]
            rows.append((r, rhs))
            
        # Add equalities
        for j in range(num_eq):
            r = eq_rows[j] + [0.0] * num_slacks
            rhs = eq_b[j]
            rows.append((r, rhs))
            
        total_constrs = len(rows)
        
        # Ensure all RHS >= 0
        mat = []
        rhs_vec = []
        for r, rhs in rows:
            if rhs < -EPS:
                mat.append([-x for x in r])
                rhs_vec.append(-rhs)
            else:
                mat.append(list(r))
                rhs_vec.append(max(0.0, rhs))
                
        # Phase 1:
        # Determine basic variables:
        # For rows with standard slack (+1 slack and rhs >= 0), that slack can be basic.
        # Otherwise, need artificial variable.
        basis = []
        art_count = 0
        art_indices = []
        
        for i in range(total_constrs):
            # Check if there is an existing unit column
            found = False
            if i < num_ineq and curr_ub_b[i] >= -EPS:
                # slack variable num_vars + i is +1 in this row, 0 elsewhere
                basis.append(num_vars + i)
                found = True
            if not found:
                art_indices.append(i)
                basis.append(-1) # to be filled
                art_count += 1
                
        tot_cols = num_vars + num_slacks + art_count
        tableau = [[0.0] * (tot_cols + 1) for _ in range(total_constrs + 1)]
        
        curr_art = 0
        for i in range(total_constrs):
            for c in range(num_vars + num_slacks):
                tableau[i][c] = mat[i][c]
            if basis[i] == -1:
                col = num_vars + num_slacks + curr_art
                tableau[i][col] = 1.0
                basis[i] = col
                curr_art += 1
            tableau[i][-1] = rhs_vec[i]
            
        # Phase 1 objective: minimize sum of artificials
        # Phase 1 row: z = sum of art_vars. In tableau: z - sum(art) = 0
        # Substitute out basic artificial variables:
        for i in range(total_constrs):
            if basis[i] >= num_vars + num_slacks:
                for c in range(tot_cols + 1):
                    tableau[-1][c] -= tableau[i][c]
                    
        def pivot(r, c):
            piv = tableau[r][c]
            inv = 1.0 / piv
            for j in range(tot_cols + 1):
                tableau[r][j] *= inv
            tableau[r][c] = 1.0
            
            for i in range(total_constrs + 1):
                if i != r:
                    factor = tableau[i][c]
                    if abs(factor) > 1e-12:
                        for j in range(tot_cols + 1):
                            tableau[i][j] -= factor * tableau[r][j]
                        tableau[i][c] = 0.0
            basis[r] = c

        # Phase 1 simplex
        while True:
            # Find entering variable (most negative in last row)
            entering = -1
            min_val = -EPS
            for c in range(tot_cols):
                if tableau[-1][c] < min_val:
                    min_val = tableau[-1][c]
                    entering = c
            if entering == -1:
                break
                
            # Ratio test
            leaving = -1
            min_ratio = 1e18
            for r in range(total_constrs):
                if tableau[r][entering] > EPS:
                    ratio = tableau[r][-1] / tableau[r][entering]
                    if ratio < min_ratio - 1e-12:
                        min_ratio = ratio
                        leaving = r
            if leaving == -1:
                return None # Unbounded
            pivot(leaving, entering)
            
        if tableau[-1][-1] < -EPS:
            return None # Infeasible Phase 1
            
        # Extract solution for first num_vars
        sol = [0.0] * num_vars
        for r in range(total_constrs):
            if basis[r] < num_vars:
                sol[basis[r]] = tableau[r][-1]
        return sol

    # Branch and Bound
    stack = [[]]
    
    while stack:
        bounds = stack.pop()
        sol = solve_lp(bounds)
        if sol is None:
            continue
            
        # Check if integral
        fractional_var = -1
        max_frac = 0.0
        for i in range(num_vars):
            val = sol[i]
            diff = abs(val - round(val))
            if diff > 1e-4:
                if diff > max_frac:
                    max_frac = diff
                    fractional_var = i
                    
        if fractional_var == -1:
            # Found integer solution!
            print("YES")
            int_sol = [int(round(x)) for x in sol]
            for i in range(k):
                row = [str(int_sol[var_idx(i, e)]) for e in range(m)]
                print(" ".join(row))
            return
            
        # Branch
        val = sol[fractional_var]
        import math
        floor_val = math.floor(val)
        ceil_val = math.ceil(val)
        
        stack.append(bounds + [(fractional_var, '>=', ceil_val)])
        stack.append(bounds + [(fractional_var, '<=', floor_val)])
        
    print("NO")

if __name__ == '__main__':
    solve()