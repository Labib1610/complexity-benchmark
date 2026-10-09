import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Build implication graph for 2-SAT
    # Variable i (1-indexed): primary = True, secondary = False
    # Node 2*i = True, 2*i+1 = False (using 0-indexed: 2*(i-1) and 2*(i-1)+1)
    
    # For each monitor (clause): at least one of three literals must be true
    # (a or b or c) => add implications: ~a -> (b or c), ~b -> (a or c), ~c -> (a or b)
    # Which means: ~a -> b, ~a -> c, ~b -> a, ~b -> c, ~c -> a, ~c -> b
    # Actually for 3-SAT to 2-SAT: (a or b or c) is equivalent to:
    # (~a -> b or c) but that's still 3-SAT...
    # 
    # Wait, we need to handle 3-SAT here. But 3-SAT is NP-complete in general.
    # However, each clause has exactly 3 literals. Let me re-read the problem.
    #
    # Actually, the problem is: each monitor checks 3 conditions, and at least one must be met.
    # This is exactly 3-SAT which is NP-complete. But n <= 90, m <= 400.
    # 
    # Hmm, but this is a competitive programming problem. Let me think about whether
    # there's a special structure or if we need to use a different approach.
    #
    # Actually, wait - 3-SAT with n=90 variables... that's too many for brute force.
    # But maybe the constraints are small enough for some other approach?
    #
    # Let me reconsider. The problem says "exactly three conditions" per monitor.
    # This is 3-SAT. For n=90, brute force is 2^90 which is way too much.
    #
    # But wait, maybe we can use the structure. Let me think about this differently.
    # 
    # Actually, I think the intended solution might be 2-SAT if we can reduce it.
    # But 3-SAT can't be reduced to 2-SAT in general...
    #
    # Let me re-read: "A monitor will report a safe status if at least one of its 
    # three hardwired conditions is actively met"
    #
    # This is literally 3-SAT. With n=90 and m=400, we need an efficient algorithm.
    #
    # Hmm, but 3-SAT is NP-complete. For a competitive programming problem with
    # these constraints, maybe there's a smarter approach or the test cases are weak.
    #
    # Actually, let me think about this more carefully. Maybe we can use backtracking
    # with pruning, or maybe the problem has special structure.
    #
    # Actually, I realize that for 3-SAT, we can use the DPLL algorithm or CDCL.
    # With n=90 and m=400, a good SAT solver should handle this.
    #
    # Let me implement a simple DPLL with unit propagation and pure literal elimination.
    
    # Represent clauses as sets of literals
    # Literal: positive integer i means valve i is primary (True)
    # Negative integer -i means valve i is secondary (False)
    
    clauses = []
    for _ in range(m):
        clause = []
        for _ in range(3):
            val = int(next(it))
            clause.append(val)
        clauses.append(clause)
    
    # DPLL with unit propagation
    # assignment: dict from var (1-indexed) to bool
    
    def solve_sat(clauses, assignment):
        # Unit propagation
        changed = True
        clauses = [list(c) for c in clauses]
        while changed:
            changed = False
            new_clauses = []
            for clause in clauses:
                # Check if clause is satisfied
                satisfied = False
                remaining = []
                for lit in clause:
                    var = abs(lit)
                    if var in assignment:
                        val = assignment[var]
                        if (lit > 0 and val) or (lit < 0 and not val):
                            satisfied = True
                            break
                    else:
                        remaining.append(lit)
                if satisfied:
                    continue
                if len(remaining) == 0:
                    return None  # Conflict
                if len(remaining) == 1:
                    # Unit clause
                    lit = remaining[0]
                    var = abs(lit)
                    assignment[var] = (lit > 0)
                    changed = True
                else:
                    new_clauses.append(remaining)
            clauses = new_clauses
        
        if not clauses:
            return assignment
        
        # Choose a variable to branch on
        # Pick the variable that appears most frequently
        var_count = {}
        for clause in clauses:
            for lit in clause:
                var = abs(lit)
                var_count[var] = var_count.get(var, 0) + 1
        
        if not var_count:
            return assignment
        
        # Pick most frequent unassigned variable
        var = max(var_count, key=var_count.get)
        
        # Try True first
        for val in [True, False]:
            new_assignment = dict(assignment)
            new_assignment[var] = val
            result = solve_sat(clauses, new_assignment)
            if result is not None:
                return result
        
        return None
    
    result = solve_sat(clauses, {})
    
    if result is None:
        print("NO")
    else:
        print("YES")
        output = []
        for i in range(1, n + 1):
            output.append("1" if result.get(i, True) else "0")
        print(" ".join(output))

solve()