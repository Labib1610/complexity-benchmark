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
        # Simplify clause: remove duplicate literals
        c = list(set(c))
        # If clause contains x and -x, it is always true, ignore it
        if any(-lit in c for lit in c):
            continue
        clauses.append(c)

    # Simple CDCL SAT Solver
    # Representation:
    # literals: positive = x, negative = -x
    
    assignment = {} # var -> bool
    trail = [] # list of lit
    level = {} # var -> int
    reason = {} # var -> clause (list of lit) or None
    decision_level = 0

    # Watched literals: lit -> list of clauses
    from collections import defaultdict
    watches = defaultdict(list)
    
    # Initialize clauses and watches
    cleaned_clauses = []
    for c in clauses:
        if len(c) == 0:
            print("NO")
            return
        cleaned_clauses.append(c)
        watches[c[0]].append(c)
        if len(c) > 1:
            watches[c[1]].append(c)
        else:
            watches[c[0]].append(c)

    # Activity for VSIDS
    activity = defaultdict(float)
    for c in cleaned_clauses:
        for lit in c:
            activity[abs(lit)] += 1.0
    var_inc = 1.0
    var_decay = 0.95

    def value(lit):
        v = abs(lit)
        if v not in assignment:
            return None
        val = assignment[v]
        return val if lit > 0 else not val

    def assign(lit, r=None):
        v = abs(lit)
        val = (lit > 0)
        assignment[v] = val
        level[v] = decision_level
        reason[v] = r
        trail.append(lit)

    def propagate():
        i = 0
        while i < len(trail):
            lit = trail[i]
            i += 1
            false_lit = -lit
            watch_list = watches[false_lit]
            watches[false_lit] = []
            
            j = 0
            while j < len(watch_list):
                c = watch_list[j]
                j += 1
                
                # Make false_lit the second watched literal: c[1]
                if c[0] == false_lit:
                    c[0], c[1] = c[1], c[0]
                
                # If the first watched literal is true, clause is satisfied
                if value(c[0]) is True:
                    watches[false_lit].append(c)
                    continue
                
                # Look for a new literal to watch
                found_new_watch = False
                for k in range(2, len(c)):
                    if value(c[k]) is not False:
                        c[1], c[k] = c[k], c[1]
                        watches[c[1]].append(c)
                        found_new_watch = True
                        break
                
                if found_new_watch:
                    continue
                
                # Clause is not satisfied and no new literal to watch
                watches[false_lit].append(c)
                
                # If c[0] is false, we have a conflict
                if value(c[0]) is False:
                    # Put back remaining watches
                    while j < len(watch_list):
                        watches[false_lit].append(watch_list[j])
                        j += 1
                    return c # Conflict clause
                elif value(c[0]) is None:
                    # Unit propagation
                    assign(c[0], c)
                else:
                    pass
        return None

    def analyze_conflict(conflict_clause):
        nonlocal var_inc
        learnt = []
        seen = set()
        counter = 0
        p = None
        c = conflict_clause
        
        index = len(trail) - 1
        while True:
            for lit in c:
                v = abs(lit)
                if v not in seen:
                    seen.add(v)
                    activity[v] += var_inc
                    if level[v] == decision_level:
                        counter += 1
                    else:
                        learnt.append(lit)
            
            while True:
                p = trail[index]
                index -= 1
                if abs(p) in seen and level[abs(p)] == decision_level:
                    break
            
            seen.remove(abs(p))
            counter -= 1
            if counter == 0:
                break
            c = reason[abs(p)]
            
        learnt_clause = [-p] + learnt
        
        # Determine backtrack level
        if len(learnt) == 0:
            backtrack_lvl = 0
        else:
            backtrack_lvl = max(level[abs(lit)] for lit in learnt)
            # Find the literal with the highest backtrack level and put it at index 1
            max_i = 1
            max_l = level[abs(learnt_clause[1])]
            for i in range(2, len(learnt_clause)):
                if level[abs(learnt_clause[i])] > max_l:
                    max_l = level[abs(learnt_clause[i])]
                    max_i = i
            learnt_clause[1], learnt_clause[max_i] = learnt_clause[max_i], learnt_clause[1]
            
        return learnt_clause, backtrack_lvl

    def backtrack(backtrack_level):
        nonlocal decision_level
        while trail and level[abs(trail[-1])] > backtrack_level:
            lit = trail.pop()
            v = abs(lit)
            del assignment[v]
            del level[v]
            del reason[v]
        decision_level = backtrack_level

    # Initial propagation (level 0)
    conflict = propagate()
    if conflict is not None:
        print("NO")
        return

    while len(assignment) < n:
        conflict = propagate()
        if conflict is not None:
            if decision_level == 0:
                print("NO")
                return
            learnt_clause, backtrack_lvl = analyze_conflict(conflict)
            backtrack(backtrack_lvl)
            
            # Add learnt clause
            cleaned_clauses.append(learnt_clause)
            watches[learnt_clause[0]].append(learnt_clause)
            if len(learnt_clause) > 1:
                watches[learnt_clause[1]].append(learnt_clause)
            else:
                watches[learnt_clause[0]].append(learnt_clause)
            
            # Unit propagate the UIP literal
            assign(learnt_clause[0], learnt_clause)
            
            var_inc /= var_decay
        else:
            if len(assignment) == n:
                break
            
            # Pick branching variable
            best_var = None
            best_act = -1
            for v in range(1, n + 1):
                if v not in assignment:
                    if activity[v] > best_act:
                        best_act = activity[v]
                        best_var = v
            
            decision_level += 1
            assign(best_var, None)

    print("YES")
    res = [1 if assignment.get(i, False) else 0 for i in range(1, n + 1)]
    print(*(res))

if __name__ == '__main__':
    solve()