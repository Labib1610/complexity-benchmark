import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # 3-edge coloring as SAT
    # Variable for edge e having color c (c in {0, 1, 2}):
    # var(e, c) = e * 3 + c + 1  (1-indexed, from 1 to 3m)
    
    num_vars = 3 * m
    clauses = []
    
    def var(e, c):
        return e * 3 + c + 1
    
    for e in range(m):
        # Edge e must have at least one color: (x_e0 or x_e1 or x_e2)
        clauses.append([var(e, 0), var(e, 1), var(e, 2)])
        # At most one color
        clauses.append([-var(e, 0), -var(e, 1)])
        clauses.append([-var(e, 0), -var(e, 2)])
        clauses.append([-var(e, 1), -var(e, 2)])
        
    for u in range(1, n + 1):
        if len(adj[u]) == 3:
            e1, e2, e3 = adj[u]
            for c in range(3):
                # For each color c, at least one incident edge has color c
                clauses.append([var(e1, c), var(e2, c), var(e3, c)])
                # At most one incident edge has color c
                clauses.append([-var(e1, c), -var(e2, c)])
                clauses.append([-var(e1, c), -var(e3, c)])
                clauses.append([-var(e2, c), -var(e3, c)])
        elif len(adj[u]) == 2:
            e1, e2 = adj[u]
            for c in range(3):
                clauses.append([-var(e1, c), -var(e2, c)])

    # CDCL SAT Solver implementation
    # 2-watched literals
    num_clauses = len(clauses)
    watches = [[] for _ in range(2 * num_vars + 2)]
    
    # literal encoding: lit > 0 -> 2*lit, lit < 0 -> 2*(-lit) + 1
    def lit_to_idx(lit):
        return (lit << 1) if lit > 0 else ((-lit) << 1 | 1)
    
    def not_lit(lit):
        return -lit
    
    clause_list = [list(c) for c in clauses]
    
    for ci, c in enumerate(clause_list):
        if len(c) == 1:
            watches[lit_to_idx(c[0])].append(ci)
        else:
            watches[lit_to_idx(c[0])].append(ci)
            watches[lit_to_idx(c[1])].append(ci)
            
    assign = [0] * (num_vars + 1)  # 0: unassigned, 1: True, -1: False
    trail = []
    trail_pos = [0] * (num_vars + 1)
    reason = [None] * (num_vars + 1)
    decision_level = 0
    level = [0] * (num_vars + 1)
    
    def val(lit):
        v = assign[abs(lit)]
        return v if lit > 0 else -v

    # Activity for VSIDS
    activity = [0.0] * (num_vars + 1)
    var_inc = 1.0
    var_decay = 0.95
    
    # Simple priority queue or list for unassigned variables
    # To be fast in Python, we can just pick the first unassigned variable with highest activity,
    # or iterate through variables.
    
    def propagate():
        nonlocal qhead
        while qhead < len(trail):
            p = trail[qhead]
            qhead += 1
            false_lit = -p
            idx_fl = lit_to_idx(false_lit)
            
            w_list = watches[idx_fl]
            watches[idx_fl] = []
            
            i = 0
            while i < len(w_list):
                ci = w_list[i]
                c = clause_list[ci]
                
                # Make sure false_lit is at c[1]
                if c[0] == false_lit:
                    c[0], c[1] = c[1], c[0]
                    
                first_lit = c[0]
                if val(first_lit) == 1:
                    watches[idx_fl].append(ci)
                    i += 1
                    continue
                    
                # Look for a new watch
                found = False
                for k in range(2, len(c)):
                    if val(c[k]) != -1:
                        c[1], c[k] = c[k], c[1]
                        watches[lit_to_idx(c[1])].append(ci)
                        found = True
                        break
                        
                if not found:
                    watches[idx_fl].append(ci)
                    if val(first_lit) == -1:
                        # Conflict
                        for j in range(i + 1, len(w_list)):
                            watches[idx_fl].append(w_list[j])
                        return ci
                    else:
                        # Unit propagation
                        assign[abs(first_lit)] = 1 if first_lit > 0 else -1
                        level[abs(first_lit)] = decision_level
                        reason[abs(first_lit)] = ci
                        trail_pos[abs(first_lit)] = len(trail)
                        trail.append(first_lit)
                i += 1
        return None

    def analyze(confl):
        nonlocal var_inc
        learnt = []
        path_cnt = 0
        p = 0
        idx_t = len(trail) - 1
        seen = [False] * (num_vars + 1)
        bt_level = 0
        c = confl
        
        while True:
            cl = clause_list[c]
            for lit in cl:
                v = abs(lit)
                if not seen[v] and lit != p:
                    seen[v] = True
                    activity[v] += var_inc
                    if level[v] == decision_level:
                        path_cnt += 1
                    else:
                        learnt.append(lit)
                        if level[v] > bt_level:
                            bt_level = level[v]
                            
            while True:
                p = trail[idx_t]
                idx_t -= 1
                if seen[abs(p)]:
                    break
            seen[abs(p)] = False
            path_cnt -= 1
            if path_cnt <= 0:
                break
            c = reason[abs(p)]
            
        learnt.insert(0, -p)
        return learnt, bt_level

    qhead = 0
    # Initial unit propagation
    if propagate() is not None:
        print("NO")
        return

    var_order = list(range(1, num_vars + 1))
    
    # Main CDCL loop
    while True:
        # Pick decision variable
        next_var = 0
        max_act = -1
        for v in range(1, num_vars + 1):
            if assign[v] == 0:
                if activity[v] > max_act:
                    max_act = activity[v]
                    next_var = v
                    
        if next_var == 0:
            # All variables assigned
            print("YES")
            ans = []
            for e in range(m):
                for c in range(3):
                    if assign[var(e, c)] == 1:
                        ans.append(str(c + 1))
                        break
            print(" ".join(ans))
            return
            
        decision_level += 1
        # Phase saving or default to True
        assign[next_var] = 1
        level[next_var] = decision_level
        reason[next_var] = None
        trail_pos[next_var] = len(trail)
        trail.append(next_var)
        
        while True:
            confl = propagate()
            if confl is None:
                break
            
            if decision_level == 0:
                print("NO")
                return
                
            learnt, bt_level = analyze(confl)
            var_inc /= var_decay
            
            # Backtrack to bt_level
            while len(trail) > 0 and level[abs(trail[-1])] > bt_level:
                top = trail.pop()
                assign[abs(top)] = 0
                reason[abs(top)] = None
            qhead = len(trail)
            decision_level = bt_level
            
            ci = len(clause_list)
            clause_list.append(learnt)
            if len(learnt) == 1:
                watches[lit_to_idx(learnt[0])].append(ci)
                assign[abs(learnt[0])] = 1 if learnt[0] > 0 else -1
                level[abs(learnt[0])] = bt_level
                reason[abs(learnt[0])] = ci
                trail_pos[abs(learnt[0])] = len(trail)
                trail.append(learnt[0])
            else:
                watches[lit_to_idx(learnt[0])].append(ci)
                watches[lit_to_idx(learnt[1])].append(ci)
                assign[abs(learnt[0])] = 1 if learnt[0] > 0 else -1
                level[abs(learnt[0])] = bt_level
                reason[abs(learnt[0])] = ci
                trail_pos[abs(learnt[0])] = len(trail)
                trail.append(learnt[0])

solve()