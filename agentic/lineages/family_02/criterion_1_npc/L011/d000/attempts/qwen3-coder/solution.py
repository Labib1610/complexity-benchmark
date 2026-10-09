from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # For each monitor, we have a clause: at least one of three literals must be true
    # This is a 3-SAT problem where each clause has exactly 3 literals
    # We'll convert this to 2-SAT by breaking 3-SAT clauses into multiple 2-SAT clauses
    
    # But let's think differently. Each clause is (a OR b OR c)
    # We can introduce auxiliary variables to reduce to 2-SAT:
    # (a OR b OR c) is equivalent to (a OR z) AND (-z OR b OR c)
    # Then (-z OR b OR c) becomes (-z OR y) AND (-y OR c)
    # But this gets complex. Let's use a direct approach with SAT solver concept.
    
    # Actually, since n <= 90 and m <= 400, and we're looking for any solution,
    # we can try a backtracking approach or use the fact that this is a satisfiability problem.
    
    # Let's model this as a graph 2-SAT style by converting 3-SAT to 2-SAT:
    # For clause (a OR b OR c), add edges:
    # (~a -> b OR c) which is (~a -> b) OR (~a -> c)
    # But to make it pure 2-SAT, we need to do Tseitin transformation.
    
    # Simpler approach: Try all possibilities with optimization
    # Since n can be up to 90, brute force won't work.
    
    # Let's implement a proper 2-SAT/implication graph approach by reducing 3-SAT to 2-SAT:
    
    # For each 3-clause (a OR b OR c), we introduce an auxiliary variable z:
    # Add clauses: (z OR a) AND (~z OR b OR c)
    # Then for (~z OR b OR c), introduce another aux var y:
    # Add clauses: (y OR ~z) AND (~y OR b OR c)
    # Continue until all are 2-clauses or 1-clauses.
    
    # But there's an even simpler way for implementation:
    # Use the implication graph approach directly for this variant.
    
    # However, given time constraints, let's implement a smart backtracking with pruning.
    
    # Better yet, let's see that this is essentially a MAX-SAT but we want ALL satisfied.
    # So it's a SAT problem. For smallish instances, we can use a recursive backtracking.
    
    # Given the constraints, let's try a backtracking solution with early pruning.
    
    # Represent clauses
    clauses = []
    for _ in range(m):
        line = list(map(int, input().split()))
        clause = []
        for x in line:
            if x > 0:
                clause.append((x-1, 1))  # valve x (0-indexed) in primary (1)
            else:
                clause.append((-x-1, 0)) # valve |x| (0-indexed) in secondary (0)
        clauses.append(clause)
    
    # assignment[i] = 0 means secondary, 1 means primary, -1 means unassigned
    assignment = [-1] * n
    
    def is_clause_satisfied(clause, assgn):
        for var, val in clause:
            if assgn[var] == val:
                return True
        return False
    
    def propagate_forced_assignments(clauses, assgn):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                unknown_count = 0
                unknown_literal = None
                satisfied = False
                
                for var, val in clause:
                    if assgn[var] == val:
                        satisfied = True
                        break
                    elif assgn[var] == -1:
                        unknown_count += 1
                        unknown_literal = (var, val)
                
                if satisfied:
                    continue
                    
                if unknown_count == 0:
                    return False  # Unsatisfiable clause
                    
                if unknown_count == 1:
                    var, val = unknown_literal
                    assgn[var] = val
                    changed = True
        
        return True
    
    def backtrack(index):
        if index == n:
            return True
            
        # Try primary position (1)
        assignment[index] = 1
        temp_assignment = assignment[:]
        if propagate_forced_assignments(clauses, temp_assignment):
            if backtrack(index + 1):
                assignment[:] = temp_assignment
                return True
        
        # Try secondary position (0)
        assignment[index] = 0
        temp_assignment = assignment[:]
        if propagate_forced_assignments(clauses, temp_assignment):
            if backtrack(index + 1):
                assignment[:] = temp_assignment
                return True
                
        assignment[index] = -1
        return False
    
    # Start solving
    if backtrack(0):
        print("YES")
        result = []
        for i in range(n):
            result.append(str(assignment[i]))
        print(" ".join(result))
    else:
        print("NO")

solve()