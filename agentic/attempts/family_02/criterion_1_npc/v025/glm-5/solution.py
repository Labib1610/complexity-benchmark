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
    
    # 3-SAT with exactly 3 literals per clause, n <= 90, m <= 400
    # Use DPLL with unit propagation and pure literal elimination
    
    # Convert to 0-indexed variables: var = abs(lit) - 1, sign = 1 if positive
    # assignment: list of -1 (unassigned), 0 (false), 1 (true)
    
    assignment = [-1] * n
    
    # Precompute clause literal lists
    clause_lits = []
    for a, b, c in clauses:
        lits = []
        for x in (a, b, c):
            var = abs(x) - 1
            sign = 1 if x > 0 else 0
            lits.append((var, sign))
        clause_lits.append(lits)
    
    # Watch lists or simple approach
    # For n=90, m=400, simple recursive DPLL should work
    
    def lit_satisfied(lit, assign):
        var, sign = lit
        val = assign[var]
        if val == -1:
            return None
        return (val == sign)
    
    def clause_status(clause, assign):
        # Returns ('sat', None), ('unsat', None), or ('unit', lit)
        unassigned = []
        for lit in clause:
            s = lit_satisfied(lit, assign)
            if s is True:
                return ('sat', None)
            elif s is None:
                unassigned.append(lit)
        if len(unassigned) == 0:
            return ('unsat', None)
        if len(unassigned) == 1:
            return ('unit', unassigned[0])
        return ('unknown', None)
    
    def find_pure_literal(assign):
        # A literal is pure if it appears in some clause but its negation doesn't
        # in any unsatisfied clause
        pos = set()
        neg = set()
        for clause in clause_lits:
            st, _ = clause_status(clause, assign)
            if st == 'sat':
                continue
            for var, sign in clause:
                if sign == 1:
                    pos.add(var)
                else:
                    neg.add(var)
        # Pure positive
        for var in pos:
            if var not in neg:
                return (var, 1)
        for var in neg:
            if var not in pos:
                return (var, 0)
        return None
    
    def find_unit_and_conflict(assign):
        units = []
        for clause in clause_lits:
            st, lit = clause_status(clause, assign)
            if st == 'unsat':
                return None  # conflict
            if st == 'unit':
                units.append(lit)
        return units
    
    def propagate(assign, var, val):
        # Set var = val and propagate
        # Returns list of (var, old_val) for backtracking, or None on conflict
        trail = []
        stack = [(var, val)]
        while stack:
            v, vl = stack.pop()
            if assign[v] == -1:
                assign[v] = vl
                trail.append((v, -1))
            elif assign[v] != vl:
                # Conflict
                for tv, tov in trail:
                    assign[tv] = tov
                return None
            else:
                continue
            # Check for new units
            units = find_unit_and_conflict(assign)
            if units is None:
                for tv, tov in trail:
                    assign[tv] = tov
                return None
            for lit in units:
                lv, lsign = lit
                if assign[lv] == -1:
                    stack.append((lv, lsign))
        return trail
    
    def dpll(assign):
        # Check all clauses
        all_sat = True
        for clause in clause_lits:
            st, _ = clause_status(clause, assign)
            if st == 'unsat':
                return False
            if st != 'sat':
                all_sat = False
        if all_sat:
            return True
        
        # Pure literal elimination
        pure = find_pure_literal(assign)
        if pure is not None:
            var, val = pure
            trail = propagate(assign, var, val)
            if trail is None:
                return False
            result = dpll(assign)
            if result:
                return True
            for tv, tov in trail:
                assign[tv] = tov
            return False
        
        # Pick unassigned variable (first one)
        var = -1
        for i in range(n):
            if assign[i] == -1:
                var = i
                break
        if var == -1:
            return True
        
        for val in (1, 0):
            trail = propagate(assign, var, val)
            if trail is None:
                continue
            result = dpll(assign)
            if result:
                return True
            for tv, tov in trail:
                assign[tv] = tov
        
        return False
    
    if dpll(assignment):
        print("YES")
        print(" ".join(str(assignment[i]) for i in range(n)))
    else:
        print("NO")

solve()