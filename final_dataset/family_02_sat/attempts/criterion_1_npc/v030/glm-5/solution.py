import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        clauses.append((a, b, c))
    
    # For each protocol, at least one monitored state must be present.
    # Monitored state x present means:
    #   if x > 0: router x is in mode 1 (True)
    #   if x < 0: router |x| is in mode 0 (False)
    # So literal for x: (x > 0) ? router[x] : !router[|x|]
    # We need at least one literal true per clause => 3-SAT.
    # n <= 90, m <= 400. Use DPLL with unit propagation and pure literal.
    
    # Represent literals: positive means router index (1-based) set True,
    # negative means router index set False.
    # We'll work with assignment array of size n+1: None, True, False.
    
    # Build clause list as sets of literals for quick manipulation.
    # But for performance, use lists and track.
    
    # Since n is small (90), but 2^90 is too large. Need DPLL.
    # However, 3-SAT with 90 vars and 400 clauses might still be hard for naive DPLL.
    # Let's implement a reasonably efficient DPLL with:
    # - unit propagation
    # - pure literal elimination
    # - branching heuristic: most occurring variable
    
    # Actually, let's try a different approach: since each clause has exactly 3 literals,
    # and we need at least one true, this is exactly 3-SAT.
    # With n=90, m=400, ratio ~4.4, which is near satisfiability threshold.
    # DPLL with good heuristics should work.
    
    # Let's implement DPLL with watched literals or simple propagation.
    
    # For simplicity and correctness, implement recursive DPLL with unit propagation.
    
    from collections import defaultdict
    
    # Count occurrences
    pos_count = defaultdict(int)
    neg_count = defaultdict(int)
    for (a, b, c) in clauses:
        for lit in (a, b, c):
            if lit > 0:
                pos_count[lit] += 1
            else:
                neg_count[-lit] += 1
    
    # assignment: dict var -> bool
    assignment = {}
    
    # Convert clauses to list of lists
    clause_lists = [list(cl) for cl in clauses]
    
    def dpll(clauses, assignment):
        # Unit propagation
        changed = True
        while changed:
            changed = False
            new_clauses = []
            for cl in clauses:
                # Evaluate clause
                unassigned = []
                satisfied = False
                for lit in cl:
                    v = abs(lit)
                    if v in assignment:
                        val = assignment[v]
                        lit_val = val if lit > 0 else (not val)
                        if lit_val:
                            satisfied = True
                            break
                    else:
                        unassigned.append(lit)
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return None  # conflict
                if len(unassigned) == 1:
                    # unit clause
                    lit = unassigned[0]
                    v = abs(lit)
                    assignment[v] = (lit > 0)
                    changed = True
                else:
                    new_clauses.append(unassigned)
            if changed:
                clauses = new_clauses
            else:
                clauses = new_clauses
        
        # Pure literal elimination
        pos_cnt = defaultdict(int)
        neg_cnt = defaultdict(int)
        for cl in clauses:
            for lit in cl:
                if lit > 0:
                    pos_cnt[lit] += 1
                else:
                    neg_cnt[-lit] += 1
        for v in list(pos_cnt.keys()) + list(neg_cnt.keys()):
            if v in assignment:
                continue
            if pos_cnt[v] > 0 and neg_cnt[v] == 0:
                assignment[v] = True
                return dpll(clauses, assignment)
            if neg_cnt[v] > 0 and pos_cnt[v] == 0:
                assignment[v] = False
                return dpll(clauses, assignment)
        
        # Check if all satisfied
        if not clauses:
            return assignment
        
        # Branch: pick variable with most occurrences
        cnt = defaultdict(int)
        for cl in clauses:
            for lit in cl:
                cnt[abs(lit)] += 1
        if not cnt:
            return assignment
        var = max(cnt.keys(), key=lambda k: cnt[k])
        
        # Try True first
        a2 = dict(assignment)
        a2[var] = True
        result = dpll(clauses, a2)
        if result is not None:
            return result
        
        # Try False
        a2 = dict(assignment)
        a2[var] = False
        return dpll(clauses, a2)
    
    result = dpll(clause_lists, {})
    if result is None:
        print("NO")
    else:
        print("YES")
        vals = []
        for i in range(1, n+1):
            vals.append(1 if result.get(i, False) else 0)
        print(' '.join(map(str, vals)))

solve()