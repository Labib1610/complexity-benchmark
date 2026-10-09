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
        c = [int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])]
        idx += 3
        # Remove duplicate literals in clause
        c = list(set(c))
        # If clause contains both x and -x, it's always true, can ignore
        has_tautology = False
        seen = set()
        for lit in c:
            if -lit in seen:
                has_tautology = True
                break
            seen.add(lit)
        if not has_tautology:
            clauses.append(c)

    # We implement a CDCL (Conflict-Driven Clause Learning) SAT Solver
    # Literals: positive/negative integers, e.g., +1, -1, ..., +n, -n
    
    # State:
    # assignment: array of size n + 1, values: 0 (unassigned), 1 (True), -1 (False)
    # level: assignment level of variable
    # reason: clause that implied this variable's value
    # trail: list of assigned literals in chronological order
    # trail_lim: start index of each decision level in trail
    
    assignment = [0] * (n + 1)
    level = [0] * (n + 1)
    reason = [None] * (n + 1)
    trail = []
    trail_lim = []
    
    # Activity for VSIDS
    activity = [0.0] * (n + 1)
    var_inc = 1.0
    var_decay = 0.95
    
    # Watched literals: watches[lit] is a list of clauses where lit is one of the watched literals
    watches = {lit: [] for lit in range(-n, n + 1) if lit != 0}
    
    all_clauses = []
    for c in clauses:
        if len(c) == 0:
            print("NO")
            return
        all_clauses.append(c)
        if len(c) == 1:
            pass # Will be handled by initial propagation
        else:
            watches[c[0]].append(c)
            watches[c[1]].append(c)

    def value(lit):
        var = abs(lit)
        val = assignment[var]
        if val == 0:
            return 0
        return 1 if (lit > 0 and val == 1) or (lit < 0 and val == -1) else -1

    def assign(lit, r, lvl):
        var = abs(lit)
        assignment[var] = 1 if lit > 0 else -1
        level[var] = lvl
        reason[var] = r
        trail.append(lit)

    def propagate(lvl):
        # Propagate unassigned literals on trail
        # Using a pointer along trail
        nonlocal qhead
        while qhead < len(trail):
            p = trail[qhead]
            qhead += 1
            false_lit = -p
            
            # We iterate over clauses watching false_lit
            ws = watches[false_lit]
            i = 0
            while i < len(ws):
                c = ws[i]
                # Ensure false_lit is at c[1]
                if c[0] == false_lit:
                    c[0], c[1] = c[1], c[0]
                
                # If first watch is satisfied, clause is satisfied, continue
                first = c[0]
                val_first = value(first)
                if val_first == 1:
                    i += 1
                    continue
                
                # Look for another literal to watch
                found = False
                for k in range(2, len(c)):
                    if value(c[k]) != -1:
                        c[1], c[k] = c[k], c[1]
                        watches[c[1]].append(c)
                        ws[i] = ws[-1]
                        ws.pop()
                        found = True
                        break
                
                if not found:
                    i += 1
                    if val_first == -1:
                        # Conflict!
                        return c
                    else:
                        # Unit propagation on first literal
                        assign(first, c, lvl)
        return None

    def analyze(conflict, lvl):
        learnt = []
        seen = [False] * (n + 1)
        counter = 0
        p = None
        c = conflict
        backtrack_level = 0
        
        index = len(trail) - 1
        while True:
            if c is not None:
                for lit in c:
                    var = abs(lit)
                    if not seen[var]:
                        seen[var] = True
                        activity[var] += var_inc
                        if level[var] == lvl:
                            counter += 1
                        elif level[var] > 0:
                            learnt.append(lit)
                            if level[var] > backtrack_level:
                                backtrack_level = level[var]
            
            while index >= 0 and not seen[abs(trail[index])]:
                index -= 1
            if index < 0:
                break
            p = trail[index]
            index -= 1
            seen[abs(p)] = False
            counter -= 1
            if counter == 0:
                learnt.append(-p)
                break
            c = reason[abs(p)]
            
        learnt[0], learnt[-1] = learnt[-1], learnt[0]
        return learnt, backtrack_level

    def cancel_until(target_lvl):
        nonlocal qhead
        while len(trail_lim) > target_lvl:
            lim = trail_lim.pop()
            while len(trail) > lim:
                p = trail.pop()
                assignment[abs(p)] = 0
                reason[abs(p)] = None
        qhead = len(trail)

    # Initial unit clauses
    qhead = 0
    for c in all_clauses:
        if len(c) == 1:
            lit = c[0]
            if value(lit) == -1:
                print("NO")
                return
            elif value(lit) == 0:
                assign(lit, None, 0)

    confl = propagate(0)
    if confl is not None:
        print("NO")
        return

    # Main CDCL loop
    while True:
        # Check if all variables assigned
        # Decision: pick unassigned variable with highest activity
        best_var = 0
        best_act = -1.0
        for var in range(1, n + 1):
            if assignment[var] == 0:
                if activity[var] > best_act:
                    best_act = activity[var]
                    best_var = var
        
        if best_var == 0:
            # All variables assigned successfully
            print("YES")
            res = [1 if assignment[i] == 1 else 0 for i in range(1, n + 1)]
            print(*(res))
            return
        
        # Decide
        trail_lim.append(len(trail))
        curr_lvl = len(trail_lim)
        assign(best_var, None, curr_lvl)
        
        while True:
            confl = propagate(curr_lvl)
            if confl is not None:
                if curr_lvl == 0:
                    print("NO")
                    return
                learnt, blevel = analyze(confl, curr_lvl)
                
                # Decay variable activities
                var_inc /= var_decay
                
                cancel_until(blevel)
                curr_lvl = blevel
                
                if len(learnt) == 1:
                    assign(learnt[0], None, 0)
                else:
                    watches[learnt[0]].append(learnt)
                    watches[learnt[1]].append(learnt)
                    all_clauses.append(learnt)
                    assign(learnt[0], learnt, blevel)
            else:
                break

if __name__ == '__main__':
    solve()