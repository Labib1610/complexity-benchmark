import sys

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    
    tasks = []
    for _ in range(k):
        s = int(next(iterator)) - 1
        t = int(next(iterator)) - 1
        d = int(next(iterator))
        tasks.append((s, t, d))
        
    edges = []
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        cap = int(next(iterator))
        edges.append((u, v, cap))

    # Number of variables: k * m
    num_vars = k * m
    
    # Constraints:
    # 1. Flow conservation: for each task i, for each node u:
    #    sum_{e out of u} x_{i, e} - sum_{e into u} x_{i, e} = b_{i, u}
    #    where b_{i, u} = d_i if u == s_i, -d_i if u == t_i, else 0.
    # 2. Capacity: for each edge e:
    #    sum_i x_{i, e} <= cap_e
    # 3. Non-negativity: x_{i, e} >= 0
    
    # For k = 1, we can just use max flow or simplex.
    # We will build a standard Branch and Bound with LP relaxation using Simplex (Phase I & II).

    # Build LP matrices:
    # Variables: x_0, ..., x_{num_vars-1}
    # Equalities A_eq x = b_eq
    # Inequalities A_ub x <= b_ub
    # Bounds: 0 <= x_j <= cap_{j % m}
    
    # Let's represent inequalities as equalities with slack variables.
    
    A_rows = []
    b_vec = []
    
    # Flow conservation (k * (n - 1) independent equations, but we can just add all k * n equations)
    for i in range(k):
        s_i, t_i, d_i = tasks[i]
        for u in range(n):
            row = [0.0] * num_vars
            for e_idx, (eu, ev, _) in enumerate(edges):
                if eu == u:
                    row[i * m + e_idx] += 1.0
                if ev == u:
                    row[i * m + e_idx] -= 1.0
            
            val = 0.0
            if u == s_i:
                val += d_i
            if u == t_i:
                val -= d_i
            
            # Skip redundant row (e.g. at t_i, or keep all)
            if u == t_i:
                continue
            
            A_rows.append(row)
            b_vec.append(val)
            
    num_eq = len(A_rows)
    
    # Capacity constraints: for each edge e, sum_i x_{i, e} <= cap_e
    # Slack variable will be added during standard form conversion
    for e_idx in range(m):
        row = [0.0] * num_vars
        for i in range(k):
            row[i * m + e_idx] = 1.0
        A_rows.append(row)
        b_vec.append(float(edges[e_idx][2]))
        
    num_ub = m
    
    # Upper bounds on variables: x_{i, e} <= cap_e
    bounds = [edges[j % m][2] for j in range(num_vars)]

    # Exact simplex solver with Branch and Bound
    # To be fast and robust, let's use a standard tableau or dense Simplex.
    # Since n, m, k in CP problems requiring exact solutions are typically moderate (e.g. <= 50-100 vars):
    
    class Simplex:
        def __init__(self, A_eq, b_eq, A_le, b_le, var_bounds):
            # A_eq: list of rows
            # A_le: list of rows
            self.n_orig = len(var_bounds)
            self.var_bounds = list(var_bounds)
            
            # Convert everything to standard form: Ax = b, x >= 0
            # A_eq x = b_eq
            # A_le x + s = b_le (s >= 0)
            # Add bound constraints if any are finite? Or keep in tableau as <=
            
            # Build full system
            self.rows = []
            self.rhs = []
            
            # Equal rows
            for r, b in zip(A_eq, b_eq):
                if b < 0:
                    self.rows.append([-x for x in r])
                    self.rhs.append(-b)
                else:
                    self.rows.append(list(r))
                    self.rhs.append(b)
            
            # LE rows
            self.n_slack = len(A_le)
            for i, (r, b) in enumerate(zip(A_le, b_le)):
                if b < 0:
                    # -r x - s = -b => standard form with surplus/artificial
                    pass
                row = list(r) + [0.0] * self.n_slack
                row[self.n_orig + i] = 1.0
                self.rows.append(row)
                self.rhs.append(b)
                
            # Expand eq rows with slack zeros
            for i in range(len(A_eq)):
                self.rows[i].extend([0.0] * self.n_slack)
                
            self.total_vars = self.n_orig + self.n_slack

        def solve_lp(self, extra_bounds):
            # extra_bounds: list of (var_idx, is_upper_bound, val)
            # We can create a tableau and solve via Phase I / Phase II
            
            rows = [list(r) for r in self.rows]
            rhs = list(self.rhs)
            
            # Add extra bounds as <= or >= constraints
            extra_slacks = len(extra_bounds)
            for r in rows:
                r.extend([0.0] * extra_slacks)
                
            for idx, (v_idx, is_ub, val) in enumerate(extra_bounds):
                r = [0.0] * (self.total_vars + extra_slacks)
                if is_ub:
                    # x_v <= val  =>  x_v + s = val
                    r[v_idx] = 1.0
                    r[self.total_vars + idx] = 1.0
                    rows.append(r)
                    rhs.append(float(val))
                else:
                    # x_v >= val  =>  -x_v <= -val  =>  -x_v + s = -val  =>  x_v - s = val
                    # x_v - s = val
                    r[v_idx] = 1.0
                    r[self.total_vars + idx] = -1.0
                    rows.append(r)
                    rhs.append(float(val))
                    
            tot_v = self.total_vars + extra_slacks
            M = len(rows)
            
            # Phase I to find feasible solution:
            # Add artificial variables for all rows
            # min sum a_i
            tab = [[0.0] * (tot_v + M + 1) for _ in range(M + 1)]
            for i in range(M):
                if rhs[i] < -1e-9:
                    # Flip row
                    for j in range(tot_v):
                        tab[i][j] = -rows[i][j]
                    tab[i][tot_v + i] = 1.0
                    tab[i][-1] = -rhs[i]
                else:
                    for j in range(tot_v):
                        tab[i][j] = rows[i][j]
                    tab[i][tot_v + i] = 1.0
                    tab[i][-1] = rhs[i]
                    
            basis = [tot_v + i for i in range(M)]
            
            # Objective: min sum a_i  =>  obj row is sum of rows
            for j in range(tot_v + M + 1):
                s = 0.0
                for i in range(M):
                    s += tab[i][j]
                tab[M][j] = s
                
            # Simplex on Phase I
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

            while True:
                # Find entering column with max positive value in bottom row (since we maximize -sum a_i)
                col = -1
                max_c = 1e-7
                for j in range(tot_v + M):
                    if tab[M][j] > max_c:
                        max_c = tab[M][j]
                        col = j
                if col == -1:
                    break
                
                # Find leaving row
                row = -1
                min_ratio = 1e18
                for i in range(M):
                    if tab[i][col] > 1e-9:
                        ratio = tab[i][-1] / tab[i][col]
                        if ratio < min_ratio:
                            min_ratio = ratio
                            row = i
                if row == -1:
                    break
                pivot(row, col)
                
            if tab[M][-1] > 1e-5:
                return None  # Infeasible
                
            # If artificial variables are in basis with value 0, pivot them out if possible
            for i in range(M):
                if basis[i] >= tot_v:
                    for j in range(tot_v):
                        if abs(tab[i][j]) > 1e-9:
                            pivot(i, j)
                            break
                            
            # Extract solution
            sol = [0.0] * self.n_orig
            for i in range(M):
                if basis[i] < self.n_orig:
                    sol[basis[i]] = tab[i][-1]
            return sol

    A_eq = A_rows[:num_eq]
    b_eq = b_vec[:num_eq]
    A_le = A_rows[num_eq:]
    b_le = b_vec[num_eq:]
    
    solver = Simplex(A_eq, b_eq, A_le, b_le, bounds)
    
    # Branch and Bound
    best_sol = None
    
    def branch_and_bound(extra_bounds):
        nonlocal best_sol
        if best_sol is not None:
            return
        sol = solver.solve_lp(extra_bounds)
        if sol is None:
            return
        
        # Check if integer
        fractional_var = -1
        max_dist = 0.0
        for i in range(num_vars):
            val = sol[i]
            dist = abs(val - round(val))
            if dist > 1e-4:
                if dist > max_dist:
                    max_dist = dist
                    fractional_var = i
                    
        if fractional_var == -1:
            best_sol = [int(round(v)) for v in sol]
            return
            
        val = sol[fractional_var]
        floor_val = int(val)
        ceil_val = floor_val + 1
        
        # Branch on <= floor_val
        extra_bounds.append((fractional_var, True, floor_val))
        branch_and_bound(extra_bounds)
        extra_bounds.pop()
        
        if best_sol is not None:
            return
            
        # Branch on >= ceil_val
        extra_bounds.append((fractional_var, False, ceil_val))
        branch_and_bound(extra_bounds)
        extra_bounds.pop()

    branch_and_bound([])
    
    if best_sol is None:
        print("NO")
    else:
        print("YES")
        for i in range(k):
            row = best_sol[i * m : (i + 1) * m]
            print(*(max(0, x) for x in row))

if __name__ == '__main__':
    solve()