import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    clauses = []
    idx = 2
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        clauses.append((a, b, c))
    
    # 2-SAT: variable i (1..n) -> node 2*i for True, 2*i+1 for False
    # literal x>0 means var x is True; x<0 means var -x is False
    # clause (a,b,c): at least one true -> add implications (not a -> b), (not a -> c), etc.
    # But 3-clause: (a or b or c). Implications: not a -> (b or c). This is not directly 2-SAT.
    # We need to reduce 3-SAT to 2-SAT? No, 3-SAT is NP-complete in general.
    # Wait, re-read: "at least one of the three named conditions is met"
    # This is exactly 3-SAT (or 3-CNF). With n<=90, m<=400, this is general 3-SAT.
    # But 3-SAT is NP-complete... unless there's special structure.
    # Actually, let me reconsider. Each clause has exactly 3 literals. This is 3-SAT.
    # n<=90 is too large for brute force (2^90). Need a smarter approach.
    
    # Hmm, but this is a competitive programming problem. Let me think about whether
    # there's a polynomial solution. Actually, 3-SAT is NP-complete, so either:
    # 1. The constraints are small enough for exponential with pruning
    # 2. There's special structure I'm missing
    
    # n<=90, m<=400. 2^90 is way too large. But maybe DPLL with unit propagation
    # and good heuristics works for these sizes? Or maybe it's always 2-SAT reducible?
    
    # Let me re-read... "every requirement names three additive-references"
    # This is 3-SAT. Let me try a DPLL-style solver with watched literals.
    
    # Actually for n=90, maybe we can use a randomized approach (Schöning's algorithm)
    # or just a good DPLL with heuristics.
    
    # Let me try a simple DPLL with unit propagation and pure literal elimination.
    
    assignment = [0] * (n + 1)  # 0 = unassigned, 1 = true, -1 = false
    
    # Convert clauses to list of (lit, lit, lit) where lit is signed int
    # lit > 0 means var=lit is true, lit < 0 means var=-lit is false
    
    def get_val(lit, assignment):
        var = abs(lit)
        if assignment[var] == 0:
            return None
        if lit > 0:
            return assignment[var] == 1
        else:
            return assignment[var] == -1
    
    def unit_propagate(assignment, clauses):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                vals = [get_val(lit, assignment) for lit in clause]
                if any(v == True for v in vals):
                    continue
                unassigned = [lit for lit, v in zip(clause, vals) if v is None]
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    assignment[var] = 1 if lit > 0 else -1
                    changed = True
        return True
    
    def dpll(assignment, clauses, n):
        # Copy assignment
        assign = assignment[:]
        if not unit_propagate(assign, clauses):
            return None
        
        # Check if all satisfied
        all_sat = True
        unassigned_var = -1
        for clause in clauses:
            vals = [get_val(lit, assign) for lit in clause]
            if not any(v == True for v in vals):
                all_sat = False
                unassigned = [abs(lit) for lit, v in zip(clause, vals) if v is None]
                if unassigned:
                    unassigned_var = unassigned[0]
                    break
        
        if all_sat:
            return assign
        
        if unassigned_var == -1:
            return None
        
        for val in [1, -1]:
            new_assign = assign[:]
            new_assign[unassigned_var] = val
            result = dpll(new_assign, clauses, n)
            if result is not None:
                return result
        
        return None
    
    result = dpll(assignment, clauses, n)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        states = []
        for i in range(1, n+1):
            if result[i] == 1:
                states.append("1")
            else:
                states.append("0")
        print(" ".join(states))

solve()