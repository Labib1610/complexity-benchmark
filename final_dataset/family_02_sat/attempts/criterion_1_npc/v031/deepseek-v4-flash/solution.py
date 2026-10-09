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
        clauses.append([l1, l2, l3])
    
    assignment = [-1] * (n + 1)  # -1 unknown, 0 false, 1 true
    
    def simplify(clauses, assignment):
        # Remove satisfied clauses, simplify literals in remaining
        new_clauses = []
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                sat = False
                new_clause = []
                for lit in clause:
                    var = abs(lit)
                    val = assignment[var]
                    if val != -1:
                        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                            sat = True
                            break
                        else:
                            continue  # literal false, skip
                    else:
                        new_clause.append(lit)
                if sat:
                    continue
                if not new_clause:
                    return None  # contradiction
                new_clauses.append(new_clause)
            if len(new_clauses) != len(clauses):
                changed = True
                clauses = new_clauses
            else:
                # check if any clause changed due to removal of false literals
                changed = False
                # Actually we need to recompute per clause each pass
                # Let's just set clauses for next loop
                clauses = new_clauses
        return clauses
    
    def unit_propagate(clauses, assignment):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unassigned = []
                for lit in clause:
                    var = abs(lit)
                    val = assignment[var]
                    if val == -1:
                        unassigned.append(lit)
                    elif (lit > 0 and val == 1) or (lit < 0 and val == 0):
                        break
                else:
                    if len(unassigned) == 1:
                        lit = unassigned[0]
                        var = abs(lit)
                        val = 1 if lit > 0 else 0
                        if assignment[var] == -1:
                            assignment[var] = val
                            changed = True
                        elif assignment[var] != val:
                            return False
        return True
    
    def pure_literal(assignment):
        # Not necessary but can speed up; we'll skip for brevity
    
    def backtrack(clauses, assignment):
        clauses = simplify(clauses, assignment)
        if clauses is None:
            return False
        if not clauses:
            return True
        # Unit propagate
        if not unit_propagate(clauses, assignment):
            return False
        clauses = simplify(clauses, assignment)
        if clauses is None:
            return False
        if not clauses:
            return True
        
        # Choose variable with most occurrences
        freq = {}
        for clause in clauses:
            for lit in clause:
                var = abs(lit)
                freq[var] = freq.get(var, 0) + 1
        if not freq:
            return True
        var = max(freq, key=freq.get)
        # Try true
        assignment[var] = 1
        if backtrack(clauses, assignment):
            return True
        assignment[var] = 0
        if backtrack(clauses, assignment):
            return True
        assignment[var] = -1
        return False
    
    if backtrack(clauses, assignment):
        print("YES")
        print(" ".join(str(assignment[i]) for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()