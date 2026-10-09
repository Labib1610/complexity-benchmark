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
        clauses.append((l1, l2, l3))
    
    assignment = [None] * (n + 1)  # 1-indexed, None = unassigned
    
    def evaluate_clause(clause, assignment):
        # clause is tuple of 3 literals
        for lit in clause:
            var = abs(lit)
            val = assignment[var]
            if val is not None:
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    return True
        return False
    
    def is_satisfied(clauses, assignment):
        for clause in clauses:
            if not evaluate_clause(clause, assignment):
                return False
        return True
    
    def unit_propagate(clauses, assignment):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unassigned = []
                satisfied = False
                for lit in clause:
                    var = abs(lit)
                    val = assignment[var]
                    if val is not None:
                        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                            satisfied = True
                            break
                    else:
                        unassigned.append(lit)
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return False  # conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    assignment[var] = 1 if lit > 0 else 0
                    changed = True
        return True
    
    def pure_literal_assign(clauses, assignment):
        # Find pure literals and assign them
        literals = set()
        for clause in clauses:
            for lit in clause:
                var = abs(lit)
                if assignment[var] is None:
                    literals.add(lit)
        # Check for pure literals
        for lit in list(literals):
            if -lit not in literals:
                var = abs(lit)
                if assignment[var] is None:
                    assignment[var] = 1 if lit > 0 else 0
        return True
    
    def backtrack(clauses, assignment):
        if not unit_propagate(clauses, assignment):
            return False
        # Check if all clauses satisfied
        if is_satisfied(clauses, assignment):
            return True
        # Choose an unassigned variable
        for var in range(1, n+1):
            if assignment[var] is None:
                # Try True
                assignment[var] = 1
                if backtrack(clauses, assignment):
                    return True
                # Try False
                assignment[var] = 0
                if backtrack(clauses, assignment):
                    return True
                assignment[var] = None
                return False
        return is_satisfied(clauses, assignment)
    
    if backtrack(clauses, assignment):
        print("YES")
        print(" ".join(str(assignment[i] if assignment[i] is not None else 0) for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()