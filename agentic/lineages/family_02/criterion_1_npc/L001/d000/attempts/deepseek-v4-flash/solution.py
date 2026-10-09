import sys
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    clauses = []
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        clause = []
        for lit in (l1, l2, l3):
            var = abs(lit) - 1
            is_neg = lit < 0
            clause.append((var, is_neg))
        clauses.append(clause)
    
    # DPLL solver
    assignment = [None] * n
    
    def evaluate(clause, assign):
        for var, is_neg in clause:
            val = assign[var]
            if val is None:
                continue
            if val == (not is_neg):
                return True
        return False
    
    def unit_propagate(clauses, assign):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unassigned = []
                satisfied = False
                for var, is_neg in clause:
                    val = assign[var]
                    if val is not None:
                        if val == (not is_neg):
                            satisfied = True
                            break
                    else:
                        unassigned.append((var, is_neg))
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    var, is_neg = unassigned[0]
                    assign[var] = (not is_neg)
                    changed = True
        return True
    
    def pure_literal_eliminate(clauses, assign):
        # Find pure literals
        pos = set()
        neg = set()
        for clause in clauses:
            for var, is_neg in clause:
                if assign[var] is not None:
                    continue
                if is_neg:
                    neg.add(var)
                else:
                    pos.add(var)
        pure = (pos - neg) | (neg - pos)
        for var in pure:
            if assign[var] is None:
                assign[var] = var in pos
        return pure
    
    def dpll(clauses, assign):
        # Unit propagation
        if not unit_propagate(clauses, assign):
            return False
        # Pure literal
        pure_literal_eliminate(clauses, assign)
        # Check if all satisfied
        all_sat = True
        for clause in clauses:
            if not evaluate(clause, assign):
                all_sat = False
                break
        if all_sat:
            return True
        # Choose unassigned variable
        for var in range(n):
            if assign[var] is None:
                break
        else:
            return True
        # Try both values
        for val in (True, False):
            assign[var] = val
            if dpll(clauses, assign):
                return True
            assign[var] = None
        return False
    
    if dpll(clauses, assignment):
        print("YES")
        print(" ".join("1" if assignment[i] else "0" for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()