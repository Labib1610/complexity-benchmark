import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    sigs = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        sigs.append((s, t, d))
        
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # LP Formulation:
    # Variables: x_{i, e} for i in range(k), e in range(m) -> k * m variables
    # Slacks for capacity constraints: m variables
    # Capacity constraints: for each e: sum_i x_{i, e} + slack_e = cap_e (m constraints)
    # Conservation constraints: for each i, for each node u in range(n - 1):
    #   sum_{e: u -> v} x_{i, e} - sum_{e: v -> u} x_{i, e} = b_{i, u}
    # where b_{i, s_i} += d_i, b_{i, t_i} -= d_i
    
    base_num_vars = k * m + m
    
    # Build constraint matrix: A x = b, x >= 0
    # Constraints list: (row_coeffs_dict, rhs)
    base_constraints = []
    
    # Capacity constraints
    for e in range(m):
        row = {}
        for i in range(k):
            row[i * m + e] = 1.0
        row[k * m + e] = 1.0  # slack
        base_constraints.append((row, float(edges[e][2])))
        
    # Flow conservation constraints (skip node n-1 as it's redundant)
    for i in range(k):
        s_i, t_i, d_i = sigs[i]
        b = [0.0] * n
        b[s_i] += d_i
        b[t_i] -= d_i
        
        for u in range(n - 1):
            row = {}
            for e, (eu, ev, _) in enumerate(edges):
                if eu == u:
                    row[i * m + e] = row.get(i * m + e, 0.0) + 1.0
                if ev == u:
                    row[i * m + e] = row.get(i * m + e, 0.0) - 1.0
            # Clean up zero entries
            row = {k_var: v for k_var, v in row.items() if abs(v) > 1e-9}
            base_constraints.append((row, b[u]))

    # Simplex solver for feasibility (Phase 1)
    def solve_lp(extra_bounds):
        # extra_bounds: list of (var_idx, '<=' or '>=', val)
        # Create full constraint list
        constraints = list(base_constraints)
        cur_num_vars = base_num_vars
        
        for var_idx, op, val in extra_bounds:
            row = {var_idx: 1.0}
            if op == '<=':
                row[cur_num_vars] = 1.0  # slack
                constraints.append((row, float(val)))
                cur_num_vars += 1
            else: # '>='
                row[cur_num_vars] = -1.0  # surplus
                constraints.append((row, float(val)))
                cur_num_vars += 1
                
        num_constraints = len(constraints)
        
        # Build tableau for Phase 1
        # Tableau size: (num_constraints + 1) rows, (cur_num_vars + 1) cols
        tableau = [[0.0] * (cur_num_vars + 1) for _ in range(num_constraints + 1)]
        basis = [-1] * num_constraints
        
        for i, (row_dict, rhs) in enumerate(constraints):
            row_idx = i + 1
            sign = 1.0
            if rhs < -1e-9:
                sign = -1.0
                rhs = -rhs
            tableau[row_idx][cur_num_vars] = rhs
            for var_idx, coeff in row_dict.items():
                tableau[row_idx][var_idx] = coeff * sign
                tableau[0][var_idx] -= coeff * sign
            tableau[0][cur_num_vars] -= rhs

        # Phase 1 Simplex
        EPS = 1e-8
        while True:
            # Find entering variable (most negative in row 0)
            entering = -1
            min_val = -EPS
            for j in range(cur_num_vars):
                if tableau[0][j] < min_val:
                    min_val = tableau[0][j]
                    entering = j
                    
            if entering == -1:
                break
                
            # Ratio test for leaving variable
            leaving = -1
            min_ratio = float('inf')
            for i in range(1, num_constraints + 1):
                if tableau[i][entering] > EPS:
                    ratio = tableau[i][cur_num_vars] / tableau[i][entering]
                    if ratio < min_ratio - EPS or (abs(ratio - min_ratio) <= EPS and (leaving == -1 or basis[i - 1] > basis[leaving - 1])):
                        min_ratio = ratio
                        leaving = i
                        
            if leaving == -1:
                # Unbounded in phase 1 (should not happen)
                break
                
            # Pivot on (leaving, entering)
            basis[leaving - 1] = entering
            pivot = tableau[leaving][entering]
            for j in range(cur_num_vars + 1):
                tableau[leaving][j] /= pivot
            for i in range(num_constraints + 1):
                if i != leaving and abs(tableau[i][entering]) > EPS:
                    factor = tableau[i][entering]
                    for j in range(cur_num_vars + 1):
                        tableau[i][j] -= factor * tableau[leaving][j]

        # Check feasibility: Phase 1 objective should be 0
        if abs(tableau[0][cur_num_vars]) > 1e-4:
            return None
            
        # Extract solution
        sol = [0.0] * cur_num_vars
        for i in range(1, num_constraints + 1):
            b_var = basis[i - 1]
            if 0 <= b_var < cur_num_vars:
                sol[b_var] = max(0.0, tableau[i][cur_num_vars])
                
        return sol

    # Branch and Bound
    target_vars = k * m
    
    def branch_and_bound(bounds):
        sol = solve_lp(bounds)
        if sol is None:
            return None
            
        # Check integer feasibility for target variables
        best_var = -1
        best_diff = -1.0
        for i in range(target_vars):
            val = sol[i]
            frac = val - int(val)
            diff = min(frac, 1.0 - frac)
            if diff > 1e-4 and diff > best_diff:
                best_diff = diff
                best_var = i
                
        if best_var == -1:
            # All target variables are integers!
            return [int(round(sol[i])) for i in range(target_vars)]
            
        val = sol[best_var]
        floor_val = int(val)
        ceil_val = floor_val + 1
        
        # Branch order: closer integer first
        if val - floor_val < ceil_val - val:
            branches = [
                (best_var, '<=', floor_val),
                (best_var, '>=', ceil_val)
            ]
        else:
            branches = [
                (best_var, '>=', ceil_val),
                (best_var, '<=', floor_val)
            ]
            
        for branch in branches:
            res = branch_and_bound(bounds + [branch])
            if res is not None:
                return res
                
        return None

    ans = branch_and_bound([])
    if ans is None:
        print("NO")
    else:
        print("YES")
        for i in range(k):
            row_flows = [ans[i * m + e] for e in range(m)]
            print(*(row_flows))

if __name__ == '__main__':
    solve()