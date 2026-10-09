import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    if m == 0:
        print("YES")
        print(*(0 for _ in range(n)))
        return

    # Literal representation:
    # Variable i (0 <= i < n)
    # Positive literal +v: 2 * (v - 1)
    # Negative literal -v: 2 * (v - 1) + 1
    def to_lit(x):
        v = abs(x) - 1
        return 2 * v if x > 0 else 2 * v + 1

    clauses = []
    idx = 2
    for _ in range(m):
        c = [to_lit(int(input_data[idx])), to_lit(int(input_data[idx+1])), to_lit(int(input_data[idx+2]))]
        idx += 3
        # Simplify clause: remove duplicate literals
        c = list(set(c))
        # If clause contains both x and not x, it's always true, can be omitted
        tautology = False
        lits_set = set(c)
        for lit in c:
            if lit ^ 1 in lits_set:
                tautology = True
                break
        if not tautology:
            clauses.append(c)

    # CDCL Solver Implementation
    assign = [-1] * n  # variable -> 0 or 1 (0: false/corridor 0, 1: true/corridor 1)
    # literal value: for lit, positive lit wants var=1, neg lit wants var=0
    # lit & 1 == 0 -> wants 1; lit & 1 == 1 -> wants 0
    # lit_val(lit):
    #   if assign[lit >> 1] == -1: return -1 (unassigned)
    #   if assign[lit >> 1] == (1 - (lit & 1)): return 1 (true)
    #   else: return 0 (false)
    
    level = [-1] * n
    reason = [None] * n
    trail = []
    trail_lim = []
    
    # Watched literals
    watches = [[] for _ in range(2 * n)]
    
    # Activity for VSIDS
    activity = [0.0] * n
    var_inc = 1.0
    var_decay = 0.95

    # Check for empty clause
    for c in clauses:
        if len(c) == 0:
            print("NO")
            return

    # Add initial clauses
    learned_clauses = []
    for c in clauses:
        if len(c) == 1:
            pass # will handle in propagation
        else:
            watches[c[0] ^ 1].append(c)
            watches[c[1] ^ 1].append(c)

    def lit_val(lit):
        v = lit >> 1
        a = assign[v]
        if a == -1:
            return -1
        return 1 if a == (1 - (lit & 1)) else 0

    def assign_lit(lit, dlevel, r=None):
        v = lit >> 1
        val = 1 - (lit & 1)
        assign[v] = val
        level[v] = dlevel
        reason[v] = r
        trail.append(lit)

    def propagate():
        nonlocal qhead
        while qhead < len(trail):
            p = trail[qhead]
            qhead += 1
            # p was just assigned TRUE, so clauses watching p^1 might be affected
            # Wait: watches[p] are clauses watching literal `p` becoming false!
            # Since `p` is true, `p^1` became false. So we iterate over watches[p].
            # Let's verify: when lit p becomes true, (p^1) is false.
            # So clauses watching (p^1) need updating.
            ws = watches[p]
            watches[p] = []
            i = 0
            while i < len(ws):
                c = ws[i]
                # Make sure c[1] is the false literal (p ^ 1)
                if c[0] == (p ^ 1):
                    c[0], c[1] = c[1], c[0]
                
                # If first watch is true, clause is already satisfied
                if lit_val(c[0]) == 1:
                    watches[p].append(c)
                    i += 1
                    continue
                
                # Look for a new literal to watch
                found = False
                for k in range(2, len(c)):
                    if lit_val(c[k]) != 0:
                        c[1], c[k] = c[k], c[1]
                        watches[c[1] ^ 1].append(c)
                        found = True
                        break
                
                if not found:
                    watches[p].append(c)
                    i += 1
                    # Clause is unit or conflicting
                    if lit_val(c[0]) == 0:
                        # Conflict!
                        for j in range(i, len(ws)):
                            watches[p].append(ws[j])
                        return c
                    else:
                        # Unit propagation
                        if lit_val(c[0]) == -1:
                            assign_lit(c[0], len(trail_lim), c)
        return None

    def analyze(conflict):
        nonlocal var_inc
        learnt = []
        seen = [False] * n
        path_cnt = 0
        p = -1
        dlevel = len(trail_lim)
        
        c = conflict
        idx_t = len(trail) - 1
        
        while True:
            for lit in c:
                v = lit >> 1
                if not seen[v] and level[v] > 0:
                    seen[v] = True
                    activity[v] += var_inc
                    if level[v] >= dlevel:
                        path_cnt += 1
                    else:
                        learnt.append(lit)
            
            while not seen[trail[idx_t] >> 1]:
                idx_t -= 1
            
            p = trail[idx_t]
            v = p >> 1
            seen[v] = False
            path_cnt -= 1
            idx_t -= 1
            
            if path_cnt <= 0:
                break
            c = reason[v]
        
        learnt.insert(0, p ^ 1)
        
        # Determine backtrack level
        bt_level = 0
        if len(learnt) > 1:
            max_idx = 1
            max_lvl = level[learnt[1] >> 1]
            for j in range(2, len(learnt)):
                lvl = level[learnt[j] >> 1]
                if lvl > max_lvl:
                    max_lvl = lvl
                    max_idx = j
            learnt[1], learnt[max_idx] = learnt[max_idx], learnt[1]
            bt_level = max_lvl
            
        return learnt, bt_level

    def backtrack_to(target_level):
        while len(trail_lim) > target_level:
            limit = trail_lim.pop()
            while len(trail) > limit:
                lit = trail.pop()
                v = lit >> 1
                assign[v] = -1
                level[v] = -1
                reason[v] = None

    # Enqueue initial unit clauses
    qhead = 0
    for c in clauses:
        if len(c) == 1:
            if lit_val(c[0]) == 0:
                print("NO")
                return
            elif lit_val(c[0]) == -1:
                assign_lit(c[0], 0, None)
    
    conflict = propagate()
    if conflict is not None:
        print("NO")
        return

    # Main CDCL loop
    while True:
        # Check if all variables assigned
        # Pick unassigned variable with highest activity
        best_v = -1
        max_act = -1.0
        for v in range(n):
            if assign[v] == -1:
                if activity[v] > max_act:
                    max_act = activity[v]
                    best_v = v
        
        if best_v == -1:
            # All assigned -> SAT
            print("YES")
            print(*(assign[i] for i in range(n)))
            return
        
        # Decision
        trail_lim.append(len(trail))
        assign_lit(2 * best_v, len(trail_lim), None) # Try true (or false)
        
        while True:
            conflict = propagate()
            if conflict is None:
                break
            
            if len(trail_lim) == 0:
                print("NO")
                return
            
            learnt, bt_level = analyze(conflict)
            backtrack_to(bt_level)
            
            # Decay variable activities
            var_inc /= var_decay
            
            # Add learned clause
            if len(learnt) == 1:
                assign_lit(learnt[0], 0, None)
            else:
                watches[learnt[0] ^ 1].append(learnt)
                watches[learnt[1] ^ 1].append(learnt)
                assign_lit(learnt[0], bt_level, learnt)

solve()