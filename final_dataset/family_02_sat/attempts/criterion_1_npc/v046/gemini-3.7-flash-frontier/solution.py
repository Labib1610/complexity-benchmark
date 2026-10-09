import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    clauses = []
    idx = 2
    for _ in range(m):
        c1 = int(input_data[idx])
        c2 = int(input_data[idx+1])
        c3 = int(input_data[idx+2])
        idx += 3
        # Simplify clause: remove duplicate literals
        cl = list(set([c1, c2, c3]))
        # If clause contains both x and -x, it's trivially satisfied, ignore it
        has_tautology = False
        for lit in cl:
            if -lit in cl:
                has_tautology = True
                break
        if not has_tautology:
            clauses.append(cl)

    # Simple CDCL solver
    # State representation:
    # assignments: array of size n+1, values: 1 (True), -1 (False), 0 (Unassigned)
    # decision_level: array of size n+1
    # reason: array of size n+1 (clause that implied this variable, or -1 for decision)
    # trail: stack of assigned literals
    # trail_lim: stack of trail indices where new decision levels start

    # Watch lists: watchers[lit] = list of clause indices where `lit` is watched
    # For literal encoding: pos lit x -> 2*x, neg lit -x -> 2*x + 1
    def to_lit_idx(lit):
        if lit > 0:
            return 2 * lit
        else:
            return 2 * (-lit) + 1

    def lit_var(lit):
        return abs(lit)

    def lit_val(lit, assign):
        # returns 1 if satisfied, -1 if falsified, 0 if unassigned
        v = assign[abs(lit)]
        if v == 0:
            return 0
        return 1 if (v > 0 and lit > 0) or (v < 0 and lit < 0) else -1

    assign = [0] * (n + 1)
    dlevel = [0] * (n + 1)
    reason = [None] * (n + 1)
    trail = []
    trail_lim = []

    # Clauses array: each clause is a list of literals
    clause_db = []
    watchers = [[] for _ in range(2 * n + 2)]

    # VSIDS activity
    activity = [0.0] * (n + 1)
    var_inc = 1.0
    var_decay = 0.95

    # Check for empty clauses initially
    for cl in clauses:
        if len(cl) == 0:
            print("NO")
            return
        if len(cl) == 1:
            # Unit clause initially
            clause_db.append(cl)
        else:
            cid = len(clause_db)
            clause_db.append(cl)
            watchers[to_lit_idx(-cl[0])].append(cid)
            watchers[to_lit_idx(-cl[1])].append(cid)

    for cl in clause_db:
        for lit in cl:
            activity[abs(lit)] += 1.0

    q_head = 0

    def assign_lit(lit, r, level):
        var = abs(lit)
        assign[var] = 1 if lit > 0 else -1
        dlevel[var] = level
        reason[var] = r
        trail.append(lit)

    # Initial unit propagation on singletons
    for cid, cl in enumerate(clause_db):
        if len(cl) == 1:
            lit = cl[0]
            val = lit_val(lit, assign)
            if val == -1:
                print("NO")
                return
            elif val == 0:
                assign_lit(lit, cid, 0)

    def propagate():
        nonlocal q_head
        while q_head < len(trail):
            p = trail[q_head]
            q_head += 1
            # p was just assigned to True, so -p was falsified.
            # Clauses watching -p need to be updated.
            falsified_lit = -p
            falsified_idx = to_lit_idx(falsified_lit)
            
            ws = watchers[falsified_idx]
            watchers[falsified_idx] = []
            i = 0
            while i < len(ws):
                cid = ws[i]
                c = clause_db[cid]
                
                # Make sure falsified_lit is at c[1]
                if c[0] == falsified_lit:
                    c[0], c[1] = c[1], c[0]
                
                # If 0th literal is true, clause is satisfied
                if lit_val(c[0], assign) == 1:
                    watchers[falsified_idx].append(cid)
                    i += 1
                    continue
                
                # Look for a new watched literal
                found_new = False
                for k in range(2, len(c)):
                    if lit_val(c[k], assign) != -1:
                        c[1], c[k] = c[k], c[1]
                        watchers[to_lit_idx(-c[1])].append(cid)
                        found_new = True
                        break
                
                if found_new:
                    i += 1
                    continue
                
                # Did not find new watch; keep watching falsified_lit
                watchers[falsified_idx].append(cid)
                i += 1
                
                # Check status of c[0]
                v0 = lit_val(c[0], assign)
                if v0 == -1:
                    # Conflict! Put remaining watchers back
                    while i < len(ws):
                        watchers[falsified_idx].append(ws[i])
                        i += 1
                    return cid
                elif v0 == 0:
                    # Unit propagation
                    assign_lit(c[0], cid, len(trail_lim))
        return None

    def analyze(conflict_cid):
        nonlocal var_inc
        learnt = [0]
        path_c = 0
        p = None
        
        seen = [False] * (n + 1)
        cur_level = len(trail_lim)
        
        c = clause_db[conflict_cid]
        t_idx = len(trail) - 1
        
        while True:
            for lit in c:
                v = abs(lit)
                if not seen[v] and dlevel[v] > 0:
                    seen[v] = True
                    activity[v] += var_inc
                    if dlevel[v] >= cur_level:
                        path_c += 1
                    else:
                        learnt.append(lit)
            
            while not seen[abs(trail[t_idx])]:
                t_idx -= 1
            
            p = trail[t_idx]
            seen[abs(p)] = False
            path_c -= 1
            t_idx -= 1
            
            if path_c <= 0:
                break
            
            c = clause_db[reason[abs(p)]]
        
        learnt[0] = -p
        
        # Backtrack level is the max level among other literals in learnt
        bt_level = 0
        if len(learnt) > 1:
            max_i = 1
            for i in range(2, len(learnt)):
                if dlevel[abs(learnt[i])] > dlevel[abs(learnt[max_i])]:
                    max_i = i
            learnt[1], learnt[max_i] = learnt[max_i], learnt[1]
            bt_level = dlevel[abs(learnt[1])]
            
        return learnt, bt_level

    def cancel_until(level):
        nonlocal q_head
        if len(trail_lim) > level:
            bound = trail_lim[level]
            while len(trail) > bound:
                lit = trail.pop()
                v = abs(lit)
                assign[v] = 0
                reason[v] = None
            q_head = bound
            del trail_lim[level:]

    def pick_branch_lit():
        best_v = 0
        best_act = -1.0
        for v in range(1, n + 1):
            if assign[v] == 0:
                if activity[v] > best_act:
                    best_act = activity[v]
                    best_v = v
        if best_v == 0:
            return 0
        return best_v

    # Main CDCL loop
    init_conflict = propagate()
    if init_conflict is not None:
        print("NO")
        return

    nof_conflicts = 0
    max_conflicts = 100
    luby_u = 1
    luby_v = 1

    while True:
        confl = propagate()
        if confl is not None:
            nof_conflicts += 1
            if len(trail_lim) == 0:
                print("NO")
                return
            
            learnt, bt_level = analyze(confl)
            cancel_until(bt_level)
            
            var_inc /= var_decay
            
            if len(learnt) == 1:
                assign_lit(learnt[0], None, 0)
            else:
                cid = len(clause_db)
                clause_db.append(learnt)
                watchers[to_lit_idx(-learnt[0])].append(cid)
                watchers[to_lit_idx(-learnt[1])].append(cid)
                assign_lit(learnt[0], cid, bt_level)
        else:
            if nof_conflicts >= max_conflicts:
                # Restart
                cancel_until(0)
                if luby_u & -luby_u == luby_v:
                    luby_u += 1
                    luby_v = 1
                else:
                    luby_v *= 2
                max_conflicts = nof_conflicts + luby_v * 100
                continue
            
            lit = pick_branch_lit()
            if lit == 0:
                # All assigned, SAT!
                break
            trail_lim.append(len(trail))
            assign_lit(lit, None, len(trail_lim))

    # Output solution
    print("YES")
    res = []
    for i in range(1, n + 1):
        res.append("1" if assign[i] == 1 else "0")
    print(" ".join(res))

if __name__ == '__main__':
    solve()