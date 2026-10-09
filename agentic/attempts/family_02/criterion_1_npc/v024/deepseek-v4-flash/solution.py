import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))
        c3 = int(next(it))
        clauses.append((c1, c2, c3))
    
    # DPLL solver
    assignment = [None] * (n + 1)  # 1-indexed, None = unassigned
    
    def evaluate_literal(lit, assign):
        var = abs(lit)
        val = assign[var]
        if val is None:
            return None
        if lit > 0:
            return val == 1
        else:
            return val == 0
    
    def clause_satisfied(clause, assign):
        for lit in clause:
            res = evaluate_literal(lit, assign)
            if res is True:
                return True
        return False
    
    def clause_unsat(clause, assign):
        for lit in clause:
            res = evaluate_literal(lit, assign)
            if res is None:
                return False
        return not clause_satisfied(clause, assign)
    
    def unit_clause(clause, assign):
        unassigned = []
        for lit in clause:
            res = evaluate_literal(lit, assign)
            if res is None:
                unassigned.append(lit)
            elif res is True:
                return None  # already satisfied
        if len(unassigned) == 1:
            return unassigned[0]
        return None
    
    def pure_literal(assign, clauses):
        # Find pure literals
        pos_count = {}
        neg_count = {}
        for clause in clauses:
            for lit in clause:
                var = abs(lit)
                if assign[var] is not None:
                    continue
                if lit > 0:
                    pos_count[var] = pos_count.get(var, 0) + 1
                else:
                    neg_count[var] = neg_count.get(var, 0) + 1
        pure = []
        for var in set(pos_count) | set(neg_count):
            if var in pos_count and var not in neg_count:
                pure.append((var, 1))
            elif var in neg_count and var not in pos_count:
                pure.append((var, 0))
        return pure
    
    def dpll(assign, clauses):
        # Unit propagation
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                if clause_satisfied(clause, assign):
                    continue
                if clause_unsat(clause, assign):
                    return False
                lit = unit_clause(clause, assign)
                if lit is not None:
                    var = abs(lit)
                    val = 1 if lit > 0 else 0
                    if assign[var] is not None and assign[var] != val:
                        return False
                    if assign[var] is None:
                        assign[var] = val
                        changed = True
        
        # Check if all clauses satisfied
        if all(clause_satisfied(cl, assign) for cl in clauses):
            return True
        
        # Pure literal elimination
        for var, val in pure_literal(assign, clauses):
            if assign[var] is None:
                assign[var] = val
        
        # Choose unassigned variable
        for var in range(1, n + 1):
            if assign[var] is None:
                # Try true
                assign[var] = 1
                if dpll(assign, clauses):
                    return True
                assign[var] = 0
                if dpll(assign, clauses):
                    return True
                assign[var] = None
                return False
        return True
    
    if dpll(assignment, clauses):
        print("YES")
        print(" ".join(str(1 if assignment[i] == 1 else 0) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()