import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    idx = 3
    commodities = []
    for _ in range(k):
        s = int(input_data[idx]) - 1
        t = int(input_data[idx+1]) - 1
        d = int(input_data[idx+2])
        commodities.append((s, t, d))
        idx += 3

    edges = []
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        c = int(input_data[idx+2])
        edges.append((u, v, c))
        idx += 3

    # Total variables: k * m
    num_vars = k * m
    
    # We will build an LP/ILP model.
    # Constraints:
    # 1. Flow conservation for each commodity and node:
    #    sum_{e: u->v} x[i, e] - sum_{e: v->u} x[i, e] = b[i, u]
    #    (eq constraints)
    # 2. Capacity constraints for each edge e:
    #    sum_{i} x[i, e] <= c[e]
    #    (le constraints)
    # 3. Variable bounds: 0 <= x[i, e]

    # Simplex Tableau implementation
    # Standard form: minimize 0 (feasibility) subject to A x = b, x >= 0
    # Add slack variables for inequalities, artificial variables for equalities/Phase I.

    # Fast simplex solver for feasibility with Branch and Bound
    class Simplex:
        def __init__(self, A, b, eq_types):
            # eq_types: 0 for '=', 1 for '<='
            # b >= 0 assumed (if b < 0, multiply row by -1 and flip type if needed)
            m_rows = len(A)
            n_cols = len(A[0]) if m_rows > 0 else 0
            
            # Formulate Phase I
            # Variables: original (n_cols), slacks, artificials
            row_list = []
            rhs_list = []
            slacks = []
            artificials = []
            
            for i in range(m_rows):
                row = list(A[i])
                bi = b[i]
                if bi < 0:
                    row = [-x for x in row]
                    bi = -bi
                    t = 0 if eq_types[i] == 0 else -1 # '<=' becomes '>='
                else:
                    t = eq_types[i]
                
                row_list.append(row)
                rhs_list.append(bi)
                
                if t == 1: # <=
                    # add slack +1
                    slacks.append((i, 1))
                elif t == -1: # >=
                    # add slack -1, artificial +1
                    slacks.append((i, -1))
                    artificials.append(i)
                else: # ==
                    artificials.append(i)
            
            total_cols = n_cols + len(slacks) + len(artificials)
            self.m = m_rows
            self.n = total_cols
            self.tableau = [[0.0] * (total_cols + 1) for _ in range(m_rows + 1)]
            
            # Fill original coefficients
            for i in range(m_rows):
                for j in range(n_cols):
                    self.tableau[i][j] = float(row_list[i][j])
                self.tableau[i][-1] = float(rhs_list[i])
                
            # Fill slacks
            slack_idx = n_cols
            basis = [-1] * m_rows
            for r, sign in slacks:
                self.tableau[r][slack_idx] = float(sign)
                if sign == 1:
                    basis[r] = slack_idx
                slack_idx += 1
                
            # Fill artificials
            art_idx = slack_idx
            art_cols = []
            for r in artificials:
                self.tableau[r][art_idx] = 1.0
                basis[r] = art_idx
                art_cols.append(art_idx)
                art_idx += 1
                
            self.basis = basis
            self.n_orig = n_cols
            self.art_cols = art_cols

        def pivot(self, pr, pc):
            piv = self.tableau[pr][pc]
            inv_piv = 1.0 / piv
            for j in range(self.n + 1):
                self.tableau[pr][j] *= inv_piv
            self.tableau[pr][pc] = 1.0
            
            for i in range(self.m + 1):
                if i != pr:
                    factor = self.tableau[i][pc]
                    if abs(factor) > 1e-12:
                        for j in range(self.n + 1):
                            self.tableau[i][j] -= factor * self.tableau[pr][j]
                        self.tableau[i][pc] = 0.0
            self.basis[pr] = pc

        def solve_phase1(self):
            # Phase 1 objective: minimize sum of artificial variables
            for j in range(self.n + 1):
                self.tableau[self.m][j] = 0.0
                
            for c in self.art_cols:
                # find row where basis is c
                r = self.basis.index(c)
                for j in range(self.n + 1):
                    self.tableau[self.m][j] -= self.tableau[r][j]
            
            while True:
                # Find entering variable (most negative in cost row)
                pc = -1
                min_v = -1e-9
                for j in range(self.n):
                    if self.tableau[self.m][j] < min_v:
                        min_v = self.tableau[self.m][j]
                        pc = j
                if pc == -1:
                    break
                
                # Min ratio test
                pr = -1
                min_ratio = 1e18
                for i in range(self.m):
                    if self.tableau[i][pc] > 1e-9:
                        ratio = self.tableau[i][-1] / self.tableau[i][pc]
                        if ratio < min_ratio - 1e-12:
                            min_ratio = ratio
                            pr = i
                if pr == -1:
                    return False # Unbounded phase 1
                self.pivot(pr, pc)
            
            if abs(self.tableau[self.m][-1]) > 1e-6:
                return False # Infeasible
            return True

        def get_solution(self):
            sol = [0.0] * self.n_orig
            for i in range(self.m):
                if self.basis[i] < self.n_orig:
                    sol[self.basis[i]] = self.tableau[i][-1]
            return sol

    # Base constraints
    base_A = []
    base_b = []
    base_eq = []

    # 1. Conservation
    for i in range(k):
        s_i, t_i, d_i = commodities[i]
        for u in range(n):
            row = [0] * num_vars
            # Outgoing edges
            for e_idx, (u_e, v_e, _) in enumerate(edges):
                if u_e == u:
                    row[i * m + e_idx] += 1
                if v_e == u:
                    row[i * m + e_idx] -= 1
            
            val = 0
            if u == s_i:
                val += d_i
            if u == t_i:
                val -= d_i
            base_A.append(row)
            base_b.append(val)
            base_eq.append(0) # '='

    # 2. Capacity
    for e_idx, (_, _, cap) in enumerate(edges):
        row = [0] * num_vars
        for i in range(k):
            row[i * m + e_idx] = 1
        base_A.append(row)
        base_b.append(cap)
        base_eq.append(1) # '<='

    # Branch and Bound
    # Extra bounds stored as list of (var_idx, type, val) where type: 1 for <=, -1 for >=
    def solve_ilp(extra_bounds):
        A = [list(r) for r in base_A]
        b = list(base_b)
        eq_types = list(base_eq)

        for v_idx, b_type, val in extra_bounds:
            row = [0] * num_vars
            row[v_idx] = 1
            if b_type == 1: # <=
                A.append(row)
                b.append(val)
                eq_types.append(1)
            else: # >=
                # row >= val -> -row <= -val
                A.append([-x for x in row])
                b.append(-val)
                eq_types.append(1)

        sp = Simplex(A, b, eq_types)
        if not sp.solve_phase1():
            return None
        return sp.get_solution()

    def branch(extra_bounds):
        sol = solve_ilp(extra_bounds)
        if sol is None:
            return None
        
        # Find non-integer variable
        best_frac = -1
        best_var = -1
        for j in range(num_vars):
            val = sol[j]
            frac = abs(val - round(val))
            if frac > 1e-4:
                # pick variable closest to 0.5
                if best_var == -1 or abs(frac - 0.5) < abs(best_frac - 0.5):
                    best_frac = frac
                    best_var = j

        if best_var == -1:
            # All integer!
            return [int(round(x)) for x in sol]

        val = sol[best_var]
        floor_v = int(val)
        ceil_v = floor_v + 1

        # Branch <= floor_v
        res = branch(extra_bounds + [(best_var, 1, floor_v)])
        if res is not None:
            return res
        # Branch >= ceil_v
        res = branch(extra_bounds + [(best_var, -1, ceil_v)])
        if res is not None:
            return res

        return None

    # Run Branch and Bound
    solution = branch([])

    if solution is None:
        print("NO")
    else:
        print("YES")
        for i in range(k):
            row = solution[i * m : (i + 1) * m]
            print(*(max(0, x) for x in row))

if __name__ == '__main__':
    solve()