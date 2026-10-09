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
    total_demand = 0
    for _ in range(k):
        s = int(next(iterator)) - 1
        t = int(next(iterator)) - 1
        d = int(next(iterator))
        commodities.append((s, t, d))
        total_demand += d
        
    edges = []
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        cap = int(next(iterator))
        edges.append((u, v, cap))

    # Fast path: If all d_i == 0
    if total_demand == 0:
        print("YES")
        for _ in range(k):
            print(" ".join(["0"] * m))
        return

    # Check trivial feasibility: if s_i == t_i and d_i > 0, demand is 0 net flow, but d_i animals need to be routed.
    # Usually s_i != t_i. If s_i == t_i and d_i == 0, fine.
    for s, t, d in commodities:
        if s == t and d > 0:
            print("NO")
            return

    # Let's set up the LP / ILP formulation.
    # Variables: f[i][e] for i in range(k), e in range(m).
    # Number of variables V = k * m.
    # Constraints:
    # 1. Flow conservation for each commodity i and each node u:
    #    sum_{e: out(u)} f[i][e] - sum_{e: in(u)} f[i][e] = demand_i(u)
    #    where demand_i(s_i) = d_i, demand_i(t_i) = -d_i, else 0.
    # 2. Capacity constraints for each edge e:
    #    sum_{i} f[i][e] <= cap[e]
    # 3. f[i][e] >= 0, integer.

    num_vars = k * m
    
    # Pre-check: if total_demand is small (e.g. <= 150), DFS with heuristics might be very fast,
    # but a Branch-and-Bound / ILP solver or DFS can be used.
    # Let's write an exact Branch-and-Bound with LP relaxation (Simplex).
    
    # Node flow constraints
    # For each commodity i, n constraints:
    # We can omit one node constraint per commodity since sum of balances is 0.
    eq_rows = []
    eq_rhs = []
    
    for i in range(k):
        s_i, t_i, d_i = commodities[i]
        for u in range(n):
            if u == t_i: # omit redundant constraint
                continue
            row = [0.0] * num_vars
            for e in range(m):
                u_e, v_e, _ = edges[e]
                if u_e == u:
                    row[i * m + e] += 1.0
                if v_e == u:
                    row[i * m + e] -= 1.0
            rhs = 0.0
            if u == s_i:
                rhs = float(d_i)
            eq_rows.append(row)
            eq_rhs.append(rhs)
            
    # Edge capacity constraints
    ineq_rows = []
    ineq_rhs = []
    for e in range(m):
        row = [0.0] * num_vars
        for i in range(k):
            row[i * m + e] = 1.0
        ineq_rows.append(row)
        ineq_rhs.append(float(edges[e][2]))

    # Simplex solver for LP:
    # Standard form: min 0 subject to A_eq x = b_eq, A_ineq x <= b_ineq, x >= 0, plus bounds on x.
    # Since we need to branch, we can add bounds l_j <= x_j <= u_j.
    # To make LP solving very efficient and simple:
    # We can convert all constraints to <= and >= or use Two-Phase Simplex.
    
    # Alternatively, if we formulate as:
    # Minimize 0
    # Subject to:
    #   A x = b  (from eq_rows and ineq_rows with slack variables)
    #   l_j <= x_j <= u_j for j = 0..V-1
    #   slack_e >= 0
    
    num_slacks = len(ineq_rows)
    total_lp_vars = num_vars + num_slacks
    
    base_A = []
    base_b = []
    for r, b_val in zip(eq_rows, eq_rhs):
        base_A.append(list(r) + [0.0] * num_slacks)
        base_b.append(b_val)
    for idx, (r, b_val) in enumerate(zip(ineq_rows, ineq_rhs)):
        row = list(r) + [0.0] * num_slacks
        row[num_vars + idx] = 1.0
        base_A.append(row)
        base_b.append(b_val)

    # Let's implement Two-Phase Simplex
    # Matrix size: num_rows x (total_lp_vars)
    # With artificial variables for Phase 1.
    
    def solve_lp(lower_bounds, upper_bounds):
        # Substitute x_j = x'_j + l_j, so 0 <= x'_j <= u_j - l_j
        # Or just treat bounds as inequalities:
        # x_j <= u_j, x_j >= l_j
        # Given small number of variables and constraints, adding bound rows is straightforward.
        A = [row[:] for row in base_A]
        b = list(base_b)
        
        # Add bound constraints
        # x_j <= u_j  =>  x_j + slack = u_j
        # x_j >= l_j  =>  x_j - slack = l_j
        extra_slacks = 0
        for j in range(num_vars):
            if upper_bounds[j] < 1e8:
                extra_slacks += 1
            if lower_bounds[j] > 0:
                extra_slacks += 1
                
        n_cols = total_lp_vars + extra_slacks
        for row in A:
            row.extend([0.0] * extra_slacks)
            
        cur_slack = total_lp_vars
        for j in range(num_vars):
            if upper_bounds[j] < 1e8:
                row = [0.0] * n_cols
                row[j] = 1.0
                row[cur_slack] = 1.0
                cur_slack += 1
                A.append(row)
                b.append(float(upper_bounds[j]))
            if lower_bounds[j] > 0:
                row = [0.0] * n_cols
                row[j] = 1.0
                row[cur_slack] = -1.0
                cur_slack += 1
                A.append(row)
                b.append(float(lower_bounds[j]))
                
        # Now solve Ax = b, x >= 0 using Two-Phase Simplex
        m_rows = len(A)
        n_vars = n_cols
        
        # Ensure b >= 0
        for i in range(m_rows):
            if b[i] < -1e-9:
                for j in range(n_vars):
                    A[i][j] = -A[i][j]
                b[i] = -b[i]
                
        # Phase 1 tableau:
        # Variables: x (n_vars), artificials (m_rows)
        # Tableau size: (m_rows + 1) x (n_vars + m_rows + 1)
        tab = [[0.0] * (n_vars + m_rows + 1) for _ in range(m_rows + 1)]
        for i in range(m_rows):
            for j in range(n_vars):
                tab[i][j] = A[i][j]
            tab[i][n_vars + i] = 1.0
            tab[i][-1] = b[i]
            
        # Objective row for phase 1: sum of artificials
        # Phase 1 obj: min sum a_i => max -sum a_i
        # In terms of non-basic variables: tab[m_rows][j] = sum_i A[i][j]
        for j in range(n_vars):
            tab[m_rows][j] = sum(tab[i][j] for i in range(m_rows))
        tab[m_rows][-1] = sum(tab[i][-1] for i in range(m_rows))
        
        basis = [n_vars + i for i in range(m_rows)]
        
        def pivot(r, c):
            inv = 1.0 / tab[r][c]
            for j in range(len(tab[0])):
                tab[r][j] *= inv
            for i in range(len(tab)):
                if i != r:
                    factor = tab[i][c]
                    if abs(factor) > 1e-12:
                        for j in range(len(tab[0])):
                            tab[i][j] -= factor * tab[r][j]
            basis[r] = c

        # Simplex Phase 1
        while True:
            # Find entering variable
            c = -1
            max_val = 1e-9
            for j in range(n_vars + m_rows):
                if tab[m_rows][j] > max_val:
                    max_val = tab[m_rows][j]
                    c = j
            if c == -1:
                break
                
            # Find leaving variable
            r = -1
            min_ratio = 1e18
            for i in range(m_rows):
                if tab[i][c] > 1e-9:
                    ratio = tab[i][-1] / tab[i][c]
                    if ratio < min_ratio - 1e-12:
                        min_ratio = ratio
                        r = i
            if r == -1:
                break
            pivot(r, c)
            
        if tab[m_rows][-1] > 1e-6:
            return None # Infeasible
            
        # Extract solution
        sol = [0.0] * num_vars
        for i in range(m_rows):
            if basis[i] < num_vars:
                sol[basis[i]] = tab[i][-1]
        return sol

    # Branch and Bound
    lower_b = [0] * num_vars
    upper_b = [0] * num_vars
    for i in range(k):
        for e in range(m):
            upper_b[i * m + e] = min(commodities[i][2], edges[e][2])

    best_sol = None
    stack = [(lower_b, upper_b)]
    
    while stack:
        lb, ub = stack.pop()
        
        # Check quick upper bound feasibility
        infeasible = False
        for j in range(num_vars):
            if lb[j] > ub[j]:
                infeasible = True
                break
        if infeasible:
            continue
            
        sol = solve_lp(lb, ub)
        if sol is None:
            continue
            
        # Check if integer
        fractional_var = -1
        max_frac = 0.0
        for j in range(num_vars):
            val = sol[j]
            frac = abs(val - round(val))
            if frac > 1e-4:
                if frac > max_frac:
                    max_frac = frac
                    fractional_var = j
                    
        if fractional_var == -1:
            # Found integer solution!
            best_sol = [int(round(x)) for x in sol]
            break
            
        val = sol[fractional_var]
        # Branch
        # Branch 1: var <= floor(val)
        ub1 = list(ub)
        ub1[fractional_var] = int(val)
        
        # Branch 2: var >= ceil(val)
        lb2 = list(lb)
        lb2[fractional_var] = int(val) + 1
        
        # Push to stack (prefer closer to round(val))
        if val - int(val) > 0.5:
            stack.append((lb, ub1))
            stack.append((lb2, ub))
        else:
            stack.append((lb2, ub))
            stack.append((lb, ub1))

    if best_sol is not None:
        print("YES")
        for i in range(k):
            row_sol = [str(best_sol[i * m + e]) for e in range(m)]
            print(" ".join(row_sol))
    else:
        print("NO")

if __name__ == '__main__':
    solve()