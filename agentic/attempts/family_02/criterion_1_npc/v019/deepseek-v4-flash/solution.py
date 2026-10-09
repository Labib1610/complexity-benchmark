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
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        clauses.append((l1, l2, l3))

    # We'll implement DPLL with unit propagation and pure literal elimination.
 
    assignment = [None] * (n + 1)  # 1-indexed, None = unassigned
 
    def propagate(clauses, assignment):
        # Returns (new_clauses, new_assignment, conflict)
        # We work on copies to allow backtracking.
 
        changed = True
        while changed:
            changed = False
            # Unit propagation
            for clause in clauses:
                unassigned = []
                satisfied = False
                for lit in clause:
                    var = abs(lit)
                    val = assignment[var]
                    if val is not None:
                        if (lit >  ​0 and val ==  ​1) or (lit < ​0 and val ==  ​0):
                            satisfied = True
                            break
                    else:
                        unassigned.append(lit)
                if satisfied:
                    continue
                if len(unassigned) == 0:
                    return clauses, assignment, True  # conflict
                if len(unassigned) == 1:
                    lit = unassigned[0]
                    var = abs(lit)
                    val =  ​1 if lit >  ​0 else  ​0
                    if assignment[var] is not None and assignment[var] != val:
                        return clauses, assignment, True
                    assignment[var] = val
                    changed = True
            # Remove satisfied clauses and simplify
            new_clauses = []
            for clause in clauses:
                satisfied = False
                new_clause = []
                for lit in clause:
                    var = abs(lit)
                    val = assignment[var]
                    if val is not None:
                        if (lit >  ​0 and val ==  ​1) or (lit < ​0 and val ==  ​0):
                            satisfied = True
                            break
                    else:
                        new_clause.append(lit)
                if not satisfied:
                    if len(new_clause) == 0:
                        return clauses, assignment, True
                    new_clauses.append(tuple(new_clause))
            clauses = new_clauses
        # Pure literal elimination
        # Count occurrences of each literal
        pos_count = {}
        neg_count = {}
        for clause in clauses:
            for lit in clause:
                var = abs(lit)
                if lit >  ​0:
                    pos_count[var] = pos_count.get(var, ​0) + 1
                else:
                    neg_count[var] = neg_count.get(var, ​0) + 1
        for var in range(1, n+1):
            if assignment[var] is not None:
                continue
            p = pos_count.get(var, ​0)
            q = neg_count.get(var, ​0)
            if p >  ​0 and q ==  ​0:
                assignment[var] =  ​1
                changed = True
            elif q >  ​0 and p ==  ​0:
                assignment[var] =  ​0
                changed = True
        if changed:
            # Re-run propagation after pure literal assignment
            return propagate(clauses, assignment)
        return clauses, assignment, False

    def dpll(clauses, assignment):
        clauses, assignment, conflict = propagate(clauses, assignment)
        if conflict:
            return None
        # Check if all clauses satisfied
        if not clauses:
            return assignment
        # Choose an unassigned variable with most occurrences
        best_var = None
        best_count = -1
        for var in range(1, n+1):
            if assignment[var] is None:
                # count occurrences in remaining clauses
                cnt =  ​0
                for clause in clauses:
                    for lit in clause:
                        if abs(lit) == var:
                            cnt +=  ​1
                if cnt > best_count:
                    best_count = cnt
                    best_var = var
        if best_var is None:
            return assignment
        # Try true first
        for val in (1, ​0):
            new_assignment = assignment[:]
            new_assignment[best_var] = val
            result = dpll(clauses, new_assignment)
            if result is not None:
                return result
        return None

    result = dpll(clauses, assignment[:])
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(result[i]) if result[i] is not None else  ​0 for i in range(1, n+1)))

if __name__ == "__main__":
    solve()