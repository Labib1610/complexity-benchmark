import sys
from collections import defaultdict

# Set recursion depth just in case
sys.setrecursionlimit(20000)

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
        cap = int(next(it))
        edges.append((u, v, cap))

    # Fast path: check simple capacity bounds
    total_demand = sum(d for _, _, d in orders)
    
    # Variables: x[i][j] for commodity i, edge j.
    # Total vars = k * m
    num_vars = k * m
    
    def var_idx(comm, edge):
        return comm * m + edge

    # Constraints:
    # 1. Capacity constraints: sum_{i} x[i][j] <= cap[j] for each j
    # 2. Flow conservation: sum_{out} x[i][e] - sum_{in} x[i][e] = demand (s: +d, t: -d, else 0)
    # 3. Non-negativity and integer constraints on all x[i][j].
    
    # We can use a Branch and Bound solver with Simplex, or if small, DFS.
    # Let's write a Two-Phase Simplex / Branch & Bound solver.

    class Simplex:
        def __init__(self, A, b, c):
            # Maximize c^T x subject to A x <= b, x >= 0
            # A is list of lists, b is list, c is list
            self.m = len(A)
            self.n = len(c)
            self.A = [row[:] for row in A]
            self.b = b[:]
            self.c = c[:]
            
        def solve(self):
            # Standard tableau form for Two-Phase Simplex
            # Convert to: Maximize c^T x s.t. A x <= b, x >= 0
            # Tableau:
            # Row 0: objective 1 (Phase 1)
            # Row 1: objective 2 (Phase 2)
            # Rows 2..m+1: constraints
            m = self.m
            n = self.n
            
            # Add slack variables
            # For each constraint i: sum A[i][j] x_j + s_i = b_i
            # If b_i < 0, multiply by -1, add artificial variable.
            # Actually, standard Phase 1:
            # If b_i < 0, multiply row by -1.
            # Add artificial variable a_i to each row with b_i < 0 (or all rows).
            
            tableau = []
            # We will use dual simplex or phase 1 with artificial variables where needed.
            # Let's set up Phase 1 directly:
            # Variables: n original vars, m slack vars, and k_art artificial vars.
            
            # Let's standardize: b_i >= 0
            signs = [1] * m
            for i in range(m):
                if self.b[i] < -1e-9:
                    signs[i] = -1
                    self.b[i] = -self.b[i]
                    for j in range(n):
                        self.A[i][j] = -self.A[i][j]
            
            # Rows: m constraints
            # Vars: n (x) + m (slack) + m (art)
            # To keep it simple: art variable for each constraint
            # Tableau size: (m + 2) x (n + m + m + 1)
            # Actually, slack for <= (when sign=1) is +1, when sign=-1 is -1.
            
            T = [[0.0] * (n + 2 * m + 1) for _ in range(m + 2)]
            
            for i in range(m):
                for j in range(n):
                    T[i + 2][j] = self.A[i][j]
                if signs[i] == 1:
                    T[i + 2][n + i] = 1.0  # slack
                else:
                    T[i + 2][n + i] = -1.0 # surplus
                T[i + 2][n + m + i] = 1.0  # artificial
                T[i + 2][-1] = self.b[i]
                
            # Phase 2 objective: maximize c^T x -> minimize -c^T x
            for j in range(n):
                T[1][j] = -self.c[j]
                
            # Phase 1 objective: minimize sum of artificial vars
            # Phase 1 obj row: - sum of rows with artificial vars
            for i in range(m):
                for col in range(n + 2 * m + 1):
                    T[0][col] -= T[i + 2][col]
            # Artificial vars have coefficient 0 in row 0 after elimination
            for i in range(m):
                T[0][n + m + i] = 0.0
                
            basis = [n + m + i for i in range(m)]
            
            # Pivot helper
            def pivot(r, c):
                inv = 1.0 / T[r][c]
                for j in range(len(T[0])):
                    T[r][j] *= inv
                for i in range(len(T)):
                    if i != r and abs(T[i][c]) > 1e-11:
                        factor = T[i][c]
                        for j in range(len(T[0])):
                            T[i][j] -= factor * T[r][j]
                basis[r - 2] = c

            # Phase 1
            while True:
                # Find entering variable
                c_min = -1e-9
                pivot_col = -1
                for j in range(n + 2 * m):
                    if T[0][j] < c_min:
                        c_min = T[0][j]
                        pivot_col = j
                if pivot_col == -1:
                    break
                # Find leaving variable
                min_ratio = float('inf')
                pivot_row = -1
                for i in range(m):
                    if T[i + 2][pivot_col] > 1e-9:
                        ratio = T[i + 2][-1] / T[i + 2][pivot_col]
                        if ratio < min_ratio - 1e-11:
                            min_ratio = ratio
                            pivot_row = i + 2
                if pivot_row == -1:
                    return None  # Unbounded phase 1 (should not happen)
                pivot(pivot_row, pivot_col)
                
            if abs(T[0][-1]) > 1e-6:
                return None  # Infeasible
                
            # Drive artificial variables out of basis if any
            for i in range(m):
                if basis[i] >= n + m:
                    # Try to pivot with a non-artificial column
                    for j in range(n + m):
                        if abs(T[i + 2][j]) > 1e-9:
                            pivot(i + 2, j)
                            break
                            
            # Phase 2
            while True:
                c_min = -1e-9
                pivot_col = -1
                for j in range(n + m):
                    if T[1][j] < c_min:
                        c_min = T[1][j]
                        pivot_col = j
                if pivot_col == -1:
                    break
                min_ratio = float('inf')
                pivot_row = -1
                for i in range(m):
                    if T[i + 2][pivot_col] > 1e-9:
                        ratio = T[i + 2][-1] / T[i + 2][pivot_col]
                        if ratio < min_ratio - 1e-11:
                            min_ratio = ratio
                            pivot_row = i + 2
                if pivot_row == -1:
                    # Unbounded, but here variables are bounded so any feasible solution works
                    break
                pivot(pivot_row, pivot_col)
                
            # Extract solution
            sol = [0.0] * n
            for i in range(m):
                if basis[i] < n:
                    sol[basis[i]] = T[i + 2][-1]
            return sol

    # Build base constraints:
    # We have equality constraints: sum_out - sum_in = demand
    # And inequality constraints: sum x <= cap
    # Represent equality A_eq x = b_eq as two inequalities: A_eq x <= b_eq and -A_eq x <= -b_eq
    
    base_A = []
    base_b = []
    
    # 1. Capacity constraints
    for j in range(m):
        row = [0.0] * num_vars
        for i in range(k):
            row[var_idx(i, j)] = 1.0
        base_A.append(row)
        base_b.append(float(edges[j][2]))
        
    # 2. Flow conservation constraints
    # For each commodity i and junction v:
    for i in range(k):
        s_i, t_i, d_i = orders[i]
        for v in range(n):
            row = [0.0] * num_vars
            # departing edges from v
            for e_idx, (u_e, v_e, _) in enumerate(edges):
                if u_e == v:
                    row[var_idx(i, e_idx)] += 1.0
                if v_e == v:
                    row[var_idx(i, e_idx)] -= 1.0
            
            target = 0.0
            if v == s_i:
                target += d_i
            if v == t_i:
                target -= d_i
                
            # row <= target
            base_A.append(row)
            base_b.append(target)
            # -row <= -target
            base_A.append([-x for x in row])
            base_b.append(-target)
            
    c = [0.0] * num_vars # Feasibility only
    
    # Branch and Bound
    # Stack for DFS
    stack = [(base_A, base_b)]
    
    found_sol = None
    
    while stack:
        cur_A, cur_b = stack.pop()
        solver = Simplex(cur_A, cur_b, c)
        sol = solver.solve()
        
        if sol is None:
            continue
            
        # Check integrality
        first_frac = -1
        max_frac_dist = 0.0
        for idx, val in enumerate(sol):
            dist = abs(val - round(val))
            if dist > 1e-4:
                if dist > max_frac_dist:
                    max_frac_dist = dist
                    first_frac = idx
                    
        if first_frac == -1:
            # Integer solution found!
            found_sol = [int(round(v)) for v in sol]
            break
            
        val = sol[first_frac]
        floor_val = float(int(val)) if val >= 0 else float(int(val) - 1)
        ceil_val = floor_val + 1.0
        
        # Branch 1: x[first_frac] <= floor_val
        row1 = [0.0] * num_vars
        row1[first_frac] = 1.0
        new_A1 = [r[:] for r in cur_A] + [row1]
        new_b1 = cur_b[:] + [floor_val]
        
        # Branch 2: x[first_frac] >= ceil_val  =>  -x[first_frac] <= -ceil_val
        row2 = [0.0] * num_vars
        row2[first_frac] = -1.0
        new_A2 = [r[:] for r in cur_A] + [row2]
        new_b2 = cur_b[:] + [-ceil_val]
        
        # Push branches to stack
        stack.append((new_A2, new_b2))
        stack.append((new_A1, new_b1))
        
    if found_sol is None:
        print("NO")
    else:
        print("YES")
        for i in range(k):
            row = [found_sol[var_idx(i, j)] for j in range(m)]
            print(*(row))

if __name__ == '__main__':
    solve()