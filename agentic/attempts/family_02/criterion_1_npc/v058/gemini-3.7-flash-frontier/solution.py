import sys

def solve_sat():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    clauses = []
    idx = 2
    for _ in range(m):
        c = [int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])]
        idx += 3
        # Simplify clause: remove duplicate literals
        c = list(set(c))
        # If clause contains both x and -x, it is trivially satisfied, ignore
        has_tautology = False
        for lit in c:
            if -lit in c:
                has_tautology = True
                break
        if not has_tautology:
            clauses.append(c)
    
    # CDCL Solver
    # Literals are non-zero integers from -n to n (excluding 0)
    # Variable index: 1 to n
    
    # Check for empty clauses
    for c in clauses:
        if len(c) == 0:
            print("NO")
            return
            
    # Initial clauses
    num_clauses = len(clauses)
    
    # Data structures
    # assign: var -> 1 (True), -1 (False), 0 (Unassigned)
    assign = [0] * (n + 1)
    lit_val = lambda l: assign[abs(l)] if l > 0 else -assign[abs(l)]
    
    # trail and levels
    trail = []
    trail_pos = [0] * (n + 1)
    reason = [None] * (n + 1)  # clause that implied var
    level = [0] * (n + 1)
    decision_level = 0
    
    # Watched literals: watches[lit] = list of clause indices
    # We will map lit in [-n, n] to 0 .. 2n: pos lit -> 2*lit, neg lit -> 2*(-lit) + 1
    def lit_to_idx(l):
        return 2 * l if l > 0 else 2 * (-l) + 1
        
    watches = [[] for _ in range(2 * n + 2)]
    
    for ci, c in enumerate(clauses):
        if len(c) >= 2:
            watches[lit_to_idx(c[0])].append(ci)
            watches[lit_to_idx(c[1])].append(ci)
        elif len(c) == 1:
            watches[lit_to_idx(c[0])].append(ci)

    # Activity for VSIDS
    activity = [0.0] * (n + 1)
    var_inc = 1.0
    var_decay = 0.95
    
    for c in clauses:
        for l in c:
            activity[abs(l)] += 1.0

    def assign_lit(l, r):
        v = abs(l)
        val = 1 if l > 0 else -1
        assign[v] = val
        level[v] = decision_level
        reason[v] = r
        trail_pos[v] = len(trail)
        trail.append(l)

    # BCP (Boolean Constraint Propagation)
    def bcp(prop_head):
        while prop_head < len(trail):
            p = trail[prop_head]
            prop_head += 1
            false_lit = -p
            w_idx = lit_to_idx(false_lit)
            
            i = 0
            ws = watches[w_idx]
            while i < len(ws):
                ci = ws[i]
                c = clauses[ci]
                
                if len(c) == 1:
                    if lit_val(c[0]) == -1:
                        return ci, prop_head
                    i += 1
                    continue
                
                # Ensure false_lit is at c[1]
                if c[0] == false_lit:
                    c[0], c[1] = c[1], c[0]
                
                # If first watched lit is True, clause is satisfied
                if lit_val(c[0]) == 1:
                    i += 1
                    continue
                
                # Find a replacement for c[1]
                found = False
                for k in range(2, len(c)):
                    if lit_val(c[k]) != -1:
                        c[1], c[k] = c[k], c[1]
                        watches[lit_to_idx(c[1])].append(ci)
                        ws[i] = ws[-1]
                        ws.pop()
                        found = True
                        break
                
                if found:
                    continue
                
                # No replacement found
                i += 1
                if lit_val(c[0]) == -1:
                    # Conflict
                    return ci, prop_head
                else:
                    # Unit propagation
                    assign_lit(c[0], ci)
                    
        return None, prop_head

    # Unit propagation at level 0
    prop_head = 0
    for ci, c in enumerate(clauses):
        if len(c) == 1:
            val = lit_val(c[0])
            if val == -1:
                print("NO")
                return
            elif val == 0:
                assign_lit(c[0], None)
                
    confl, prop_head = bcp(prop_head)
    if confl is not None:
        print("NO")
        return

    def backtrack(target_level):
        nonlocal decision_level, prop_head
        while trail and level[abs(trail[-1])] > target_level:
            l = trail.pop()
            v = abs(l)
            assign[v] = 0
            reason[v] = None
        decision_level = target_level
        prop_head = len(trail)

    # Main CDCL loop
    while True:
        # Pick branching variable
        best_v = 0
        max_act = -1
        for v in range(1, n + 1):
            if assign[v] == 0 and activity[v] > max_act:
                max_act = activity[v]
                best_v = v
        
        if best_v == 0:
            # All variables assigned, SAT!
            print("YES")
            ans = [1 if assign[i] == 1 else 0 for i in range(1, n + 1)]
            print(*(ans))
            return
        
        decision_level += 1
        assign_lit(best_v, None)
        
        while True:
            confl, prop_head = bcp(prop_head)
            if confl is None:
                break
            
            if decision_level == 0:
                print("NO")
                return
            
            # Conflict analysis (1-UIP)
            c = clauses[confl]
            learnt = []
            seen = [False] * (n + 1)
            counter = 0
            backtrack_level = 0
            
            for l in c:
                v = abs(l)
                activity[v] += var_inc
                seen[v] = True
                if level[v] == decision_level:
                    counter += 1
                else:
                    learnt.append(l)
                    if level[v] > backtrack_level:
                        backtrack_level = level[v]
            
            t_idx = len(trail) - 1
            while counter > 1:
                while not seen[abs(trail[t_idx])]:
                    t_idx -= 1
                p = trail[t_idx]
                t_idx -= 1
                v = abs(p)
                seen[v] = False
                counter -= 1
                
                r_ci = reason[v]
                if r_ci is not None:
                    r_clause = clauses[r_ci]
                    for l in r_clause:
                        v2 = abs(l)
                        if not seen[v2] and v2 != v:
                            activity[v2] += var_inc
                            seen[v2] = True
                            if level[v2] == decision_level:
                                counter += 1
                            else:
                                learnt.append(l)
                                if level[v2] > backtrack_level:
                                    backtrack_level = level[v2]
            
            # Find the UIP
            while not seen[abs(trail[t_idx])]:
                t_idx -= 1
            uip = trail[t_idx]
            learnt = [-uip] + learnt
            
            # Decay activity
            var_inc /= var_decay
            
            # Add learnt clause
            ci = len(clauses)
            clauses.append(learnt)
            if len(learnt) >= 2:
                watches[lit_to_idx(learnt[0])].append(ci)
                watches[lit_to_idx(learnt[1])].append(ci)
            else:
                watches[lit_to_idx(learnt[0])].append(ci)
                
            backtrack(backtrack_level)
            assign_lit(learnt[0], ci)

solve_sat()