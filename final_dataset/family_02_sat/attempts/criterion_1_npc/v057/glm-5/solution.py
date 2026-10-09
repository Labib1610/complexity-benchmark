import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    idx = 2
    clauses = []
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        clauses.append((a, b, c))
    
    # 3-SAT with exactly 3 literals per clause, n <= 90, m <= 400.
    # Use DPLL with unit propagation and pure literal elimination.
    
    # Literal encoding: positive x -> x, negative x -> -x
    # assignment: dict var -> bool
    
    # Build occurrence lists
    pos_occ = [[] for _ in range(n+1)]  # clauses where var appears positive
    neg_occ = [[] for _ in range(n+1)]  # clauses where var appears negative
    clause_literals = []
    for ci, (a,b,c) in enumerate(clauses):
        lits = (a,b,c)
        clause_literals.append(lits)
        for lit in lits:
            v = abs(lit)
            if lit > 0:
                pos_occ[v].append(ci)
            else:
                neg_occ[v].append(ci)
    
    assignment = {}
    # Track clause satisfaction status
    # We'll use recursive DPLL
    
    # Precompute for each clause its literals
    # We'll pass down a set of unassigned clauses and current partial assignment
    
    # For efficiency, use mutable structures with backtracking
    
    class Solver:
        def __init__(self):
            self.clauses = clause_literals
            self.pos_occ = pos_occ
            self.neg_occ = neg_occ
            self.n = n
            self.assign = {}  # var -> bool
            # clause status: None = unknown, True = satisfied, False = unsatisfied
            self.status = [None]*m
            # count of unassigned literals per clause
            self.unassigned_count = [3]*m
            # for each clause, track which literals are still unassigned
            # we can recompute from assign
            
        def lit_value(self, lit):
            v = abs(lit)
            if v not in self.assign:
                return None
            val = self.assign[v]
            return val if lit > 0 else (not val)
        
        def clause_status(self, ci):
            # returns True if satisfied, False if conflict, None if unknown
            if self.status[ci] is not None:
                return self.status[ci]
            cnt_unassigned = 0
            for lit in self.clauses[ci]:
                val = self.lit_value(lit)
                if val is True:
                    self.status[ci] = True
                    return True
                if val is None:
                    cnt_unassigned += 1
            if cnt_unassigned == 0:
                self.status[ci] = False
                return False
            self.unassigned_count[ci] = cnt_unassigned
            return None
        
        def assign_var(self, v, val):
            self.assign[v] = val
        
        def unassign_var(self, v):
            del self.assign[v]
        
        def reset_status(self):
            self.status = [None]*m
            self.unassigned_count = [3]*m
        
        def find_unit(self):
            # find a clause with exactly one unassigned literal and not satisfied
            for ci in range(m):
                if self.status[ci] is True:
                    continue
                cnt = 0
                unit_lit = None
                for lit in self.clauses[ci]:
                    val = self.lit_value(lit)
                    if val is True:
                        self.status[ci] = True
                        break
                    if val is None:
                        cnt += 1
                        unit_lit = lit
                else:
                    if cnt == 0:
                        return ('conflict', None)
                    if cnt == 1:
                        return ('unit', unit_lit)
            return (None, None)
    
    # Simpler approach: recursive backtracking with unit propagation
    # Since n<=90, m<=400, and each clause has 3 literals, this should be fast enough
    # for typical cases, but worst case 3-SAT is exponential. However with these
    # constraints and typical test data, it should work.
    
    # Let's implement a cleaner DPLL
    
    def dpll(assign):
        # Unit propagation
        changed = True
        propagated = []
        while changed:
            changed = False
            for ci in range(m):
                a, b, c = clauses[ci]
                vals = []
                unassigned = []
                for lit in (a,b,c):
                    v = abs(lit)
                    if v in assign:
                        val = assign[v]
                        lit_val = val if lit > 0 else (not val)
                        vals.append(lit_val)
                    else:
                        unassigned.append(lit)
                        vals.append(None)
                if any(v is True for v in vals):
                    continue  # satisfied
                if len(unassigned) == 0:
                    # conflict, undo propagations
                    for v in propagated:
                        del assign[v]
                    return None
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    v = abs(lit)
                    assign[v] = (lit > 0)
                    propagated.append(v)
                    changed = True
        
        # Check all clauses
        all_satisfied = True
        for ci in range(m):
            a, b, c = clauses[ci]
            satisfied = False
            unassigned = []
            for lit in (a,b,c):
                v = abs(lit)
                if v in assign:
                    val = assign[v]
                    lit_val = val if lit > 0 else (not val)
                    if lit_val:
                        satisfied = True
                        break
                else:
                    unassigned.append(lit)
            if not satisfied:
                all_satisfied = False
                if len(unassigned) == 0:
                    for v in propagated:
                        del assign[v]
                    return None
                break
        
        if all_satisfied:
            return dict(assign)
        
        # Pick unassigned variable (first unassigned in first unsatisfied clause)
        # Find an unsatisfied clause with unassigned literals
        target_lit = None
        for ci in range(m):
            a, b, c = clauses[ci]
            satisfied = False
            unassigned = []
            for lit in (a,b,c):
                v = abs(lit)
                if v in assign:
                    val = assign[v]
                    lit_val = val if lit > 0 else (not val)
                    if lit_val:
                        satisfied = True
                        break
                else:
                    unassigned.append(lit)
            if not satisfied and unassigned:
                target_lit = unassigned[0]
                break
        
        if target_lit is None:
            for v in propagated:
                del assign[v]
            return None
        
        v = abs(target_lit)
        # Try True first
        assign[v] = True
        result = dpll(assign)
        if result is not None:
            return result
        assign[v] = False
        result = dpll(assign)
        if result is not None:
            return result
        del assign[v]
        for var in propagated:
            if var in assign:
                del assign[var]
        return None
    
    result = dpll({})
    if result is None:
        print("NO")
    else:
        print("YES")
        vals = [str(result.get(i, 0)) for i in range(1, n+1)]
        print(" ".join(vals))

solve()