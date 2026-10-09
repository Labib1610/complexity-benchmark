import sys

def solve():
    data = sys.stdin.read().strip().split()
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
        clauses.append((a, b, c)))
    
    # We need to assign each variable True (primary) or False (secondary)
    # Each clause is (x or y or z) where positive literal means variable True,
    # negative literal means variable False.

    
    # Use 2-SAT style implication graph, but with 3-literal clauses.

    # We can reduce 3-SAT to  ？ Actually we need to solve 3-SAT with n<=90, m<=400.

    # Since n is small (90), we can use backtracking with unit propagation and pure literal elimination.

    
    # Represent clauses as list of literals (signed ints)
    # We'll implement DPLL.

    
    # Variable values: 0 = unassigned, 1 = True (primary), -1 = False (secondary)
    assignment = [0] * (n + 1)
    
    # We'll store clauses as list of tuples of literals.

    
    def evaluate_literal(lit, assign):
        var = abs(lit)
        if assign[var] == 0:
            return None
        if lit > 0:
            return assign[var] == 1
        else:
            return assign[var] == -1
    
    def simplify(clauses, assign):
        # Remove satisfied clauses, propagate unit clauses, detect conflicts.
 
        changed = True
        while changed:
            changed = False
            new_clauses = []
            for clause in clauses:
                # Check if clause is satisfied
                sat = False
                unassigned = []
                for lit in clause:
                    val = evaluate_literal(lit, assign)
                    if val is True:
                        sat = True
                        break
                    elif val is None:
                        unassigned.append(lit)
                if sat:
                    continue
                if not unassigned:
                    # conflict
                    return None, False
                if len(unassigned) == 1:
                    # unit clause: force assignment
                    lit = unassigned[0]
                    var = abs(lit)
                    if assign[var] != 0:
                        # already assigned but not satisfied? Actually if it was assigned, it would have been evaluated.
                        # So this shouldn't happen.
                        return None, False
                    assign[var] = 1 if lit > 0 else -1
                    changed = True
                else:
                    new_clauses.append(clause)
            clauses = new_clauses
        return clauses, True
    
    # DPLL recursive
    def dpll(clauses, assign):
        clauses, ok = simplify(clauses, assign)
        if not ok:
            return False
        if not clauses:
            return True
        
        # Choose a variable from a clause with smallest size (most constrained)
        # Find unassigned variable in some clause
        best_var = None
        best_count = float('inf')
        for clause in clauses:
            for lit in clause:
                var = abs(lit)
                if assign[var] == 0:
                    # count occurrences in remaining clauses
                    cnt = 
                    for c in clauses:
                        for l in c:
                            if abs(l) == var:
                                cnt += 
                    if cnt < best_count:
                        best_count = cnt
                        best_var = var
        if best_var is None:
            # Shouldn't happen because clauses non-empty and all vars assigned? But maybe all clauses satisfied? Actually if clauses non-empty, there must be unassigned var.

            return True
        
        # Try True first
        assign[best_var] = 1
        if dpll([list(c) for c in clauses], assign):
            return True
        assign[best_var] = -1
        if dpll([list(c) for c in clauses], assign):
            return True
        assign[best_var] = 0
        return False
    
    # Copy clauses to list of lists
    clauses = [list(c) for c in clauses]
    
    if dpll(clauses, assignment):
        # Build output
        res = []
        for i in range(1, n+1):
            if assignment[i] == 1:
                res.append('1')
            else:
                res.append('0')
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(res) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()