from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    clauses = []
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        l3 = int(data[idx+2])
        idx += 3
        clauses.append((l1, l2, l3))
    
    # Convert to 3-SAT instance
    # Variables: x1, x2, ..., xn correspond to zones 1, 2, ..., n
    # xi = 1 means warm, xi = 0 means cool
    # Clause (l1, l2, l3) means at least one of them should be true
    # If li > 0, it's variable li
    # If li < 0, it's NOT |li|
    
    # We'll use a 2-SAT approach by reducing 3-SAT to 2-SAT via auxiliary variables
    # But since we have a small number of variables (< 90), we can try a different approach
    # Let's model this as a 3-CNF satisfiability problem and use a brute-force or implication graph approach
    
    # Since n <= 90, brute force is not feasible
    # We'll implement a 2-SAT solver and convert our 3-SAT to 2-SAT using auxiliary variables
    
    # However, there's a simpler way for this specific case:
    # Each clause is a disjunction of 3 literals
    # We can solve this using strongly connected components in the implication graph
    
    # Build implication graph for 3-SAT
    # For each clause (a OR b OR c), we add edges:
    # (~a => b OR c) which translates to (~a => b) OR (~a => c)
    # This is equivalent to (a OR b OR c) being true
    # To handle this in 2-SAT style, we introduce an auxiliary variable y
    # (a OR b OR c) <=> (~y OR a) AND (y OR b OR c)
    # But this gets complex. Instead, let's build a direct implication graph for 3-SAT
    
    # Actually, let's reduce 3-SAT to 2-SAT properly:
    # For clause (a OR b OR c), introduce new var y
    # Replace with (a OR b OR c) = (a OR y) AND (~y OR b OR c)
    # Then for (~y OR b OR c), introduce z
    # Replace with (~y OR z) AND (~z OR b OR c)
    # Continue until all clauses are 2-CNF
    
    # But this is getting too involved. Let's just implement a direct 3-SAT solver using SCC
    
    # Let's create implication graph for 3-SAT directly
    # For each clause (a OR b OR c), if all are false, then we have a contradiction
    # So we need to ensure that at least one literal in each clause is true
    
    # We can encode this as: for each clause (a OR b OR c)
    # Add constraints that enforce at least one is true
    # In implication graph terms:
    # (~a AND ~b) => c
    # (~a AND ~c) => b  
    # (~b AND ~c) => a
    
    # But implications with AND on LHS are not directly usable
    # We need to transform to 2-SAT
    
    # Better approach: for clause (a OR b OR c)
    # Introduce auxiliary variable y
    # Replace with clauses: (~a OR y) AND (~b OR y) AND (a OR b OR ~y) AND (y OR c)
    # Wait, that doesn't seem right either
    
    # Let me think differently. 
    # For clause (a OR b OR c), it's false only when a=0, b=0, c=0
    # So we want to prevent the case where all three are false
    # This is equivalent to saying at least one is true
    
    # In 2-SAT reduction:
    # (a OR b OR c) can be written as:
    # Introduce y1, then 
    # (a OR b OR c) <=> (a OR y1) AND (~y1 OR b OR c)
    # Then for (~y1 OR b OR c), introduce y2:
    # (~y1 OR y2) AND (~y2 OR b OR c)
    # And so on...
    
    # But this creates many new variables. Let's see if we can do better.
    
    # Actually, let's just implement a direct solution using the fact that
    # each clause must have at least one satisfied literal
    
    # We can try all 2^n assignments for n <= 90? No, that's too large
    
    # Let's use the standard approach: convert to 2-SAT by introducing auxiliary variables
    
    # For each 3-clause (a OR b OR c), we replace it with:
    # (y OR a) AND (~y OR b OR c) where y is a new variable
    # Then we recursively process (~y OR b OR c) 
    # But this can lead to exponential growth
    
    # There's a known linear transformation:
    # Clause (x1 OR x2 OR ... OR xk) can be converted to 2-SAT with k-2 new variables:
    # Introduce y1,...,y_{k-2}
    # Clauses: (x1 OR y1), (~y1 OR x2 OR y2), (~y2 OR x3 OR y3), ..., (~y_{k-3} OR x_{k-2} OR y_{k-2}), (~y_{k-2} OR x_{k-1} OR x_k)
    
    # For k=3: (x1 OR x2 OR x3) becomes with 1 new var y:
    # (x1 OR y) AND (~y OR x2 OR x3)
    # Then (~y OR x2 OR x3) needs another var z:
    # (~y OR z) AND (~z OR x2 OR x3)  
    # But (~z OR x2 OR x3) still has 3 literals...
    
    # Wait, the correct reduction for 3-SAT to 2-SAT for clause (a OR b OR c):
    # Introduce new variable y
    # Replace with: (a OR y) AND (b OR c OR ~y)
    # But (b OR c OR ~y) is still 3-SAT...
    
    # Hmm, I think I'm overcomplicating this.
    # Let's look up the standard reduction. 
    # For 3-CNF clause (x OR y OR z), introduce new boolean variable w
    # Replace with 4 2-CNF clauses:
    # (x OR w) AND (y OR w) AND (z OR ~w) AND (~x OR ~y OR ~z -> this is wrong)
    
    # No, the correct standard reduction from 3-SAT to 2-SAT is not straightforward because 2-SAT is in P but 3-SAT is NP-complete.
    
    # So we cannot polynomially reduce 3-SAT to 2-SAT unless P=NP.
    
    # Therefore, we need to solve 3-SAT directly.
    # For small instances, we could use backtracking with pruning.
    # But n=90 is too big.
    
    # Let's reconsider the problem. Maybe there's a special structure.
    
    # Actually, let's implement a randomized local search or use an off-the-shelf SAT solver approach.
    # But that's beyond the scope.
    
    # Let's try to implement a simple randomized algorithm:
    # Start with random assignment, then for each unsatisfied clause,
    # flip one of its variables randomly.
    
    # But this might not converge.
    
    # Let's instead implement a proper 3-SAT solver using the implication graph idea for conflict-driven learning.
    # But again, too complex.
    
    # Let me re-read the problem... 
    
    # Ah wait! Maybe I can model this as a CSP and use constraint satisfaction techniques.
    
    # Or even better, since this is a programming contest problem, maybe there's a clever insight.
    
    # Let's think of it this way:
    # Each clause is (l1 OR l2 OR l3)
    # Where li represents a literal (positive = variable, negative = negated variable)
    
    # This is exactly 3-SAT.
    
    # For 3-SAT with n variables and m clauses, we can:
    # 1. Try small cases with brute force (n <= 20 or so)
    # 2. Use randomized algorithms
    # 3. Look for special structures
    
    # Since n <= 90, brute force won't work.
    
    # Let's implement a simple randomized local search:
    
    def evaluate(clause, assignment):
        for lit in clause:
            var = abs(lit)
            val = assignment[var]
            if lit > 0 and val == 1:
                return True
            if lit < 0 and val == 0:
                return True
        return False
    
    def count_unsatisfied(clauses, assignment):
        count = 0
        for clause in clauses:
            if not evaluate(clause, assignment):
                count += 1
        return count
    
    import random
    
    # Simple randomized algorithm
    found = False
    best_assignment = None
    min_unsat = float('inf')
    
    if n == 0:
        print("YES")
        return
        
    for trials in range(min(10000, max(1000, 100000 // (n + 1)))):  # Adapt number of trials based on n
        assignment = [0] * (n + 1)  # index 0 unused
        for i in range(1, n + 1):
            assignment[i] = random.randint(0, 1)
            
        unsat = count_unsatisfied(clauses, assignment)
        if unsat < min_unsat:
            min_unsat = unsat
            best_assignment = assignment[:]
        if unsat == 0:
            found = True
            break
            
        # Local search: try flipping variables in unsatisfied clauses
        improved = True
        steps = 0
        max_steps = 1000
        while improved and unsat > 0 and steps < max_steps:
            improved = False
            steps += 1
            # Find an unsatisfied clause
            unsat_clauses = []
            for clause in clauses:
                if not evaluate(clause, assignment):
                    unsat_clauses.append(clause)
                    
            if not unsat_clauses:
                unsat = 0
                break
                
            clause = random.choice(unsat_clauses)
            # Pick a random literal from the clause and flip its variable
            lit = random.choice(clause)
            var = abs(lit)
            old_val = assignment[var]
            assignment[var] = 1 - assignment[var]
            new_unsat = count_unsatisfied(clauses, assignment)
            if new_unsat < unsat:
                unsat = new_unsat
                improved = True
                if unsat < min_unsat:
                    min_unsat = unsat
                    best_assignment = assignment[:]
                if unsat == 0:
                    found = True
                    break
            else:
                assignment[var] = old_val  # revert
                
    if found:
        print("YES")
        print(" ".join(str(best_assignment[i]) for i in range(1, n + 1)))
    else:
        # Try one more systematic approach for small n
        if n <= 20:
            # Brute force
            for mask in range(1 << n):
                assignment = [0] * (n + 1)
                for i in range(n):
                    assignment[i + 1] = (mask >> i) & 1
                if count_unsatisfied(clauses, assignment) == 0:
                    print("YES")
                    print(" ".join(str(assignment[i]) for i in range(1, n + 1)))
                    return
            print("NO")
        else:
            if min_unsat == 0:
                print("YES")
                print(" ".join(str(best_assignment[i]) for i in range(1, n + 1)))
            else:
                print("NO")

if __name__ == "__main__":
    main()