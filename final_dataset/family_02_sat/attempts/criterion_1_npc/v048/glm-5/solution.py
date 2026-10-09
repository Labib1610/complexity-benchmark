import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Each interlock is a clause (x1 v x2 v x3)
    # We need to find an assignment satisfying all clauses.
    # This is a 3-SAT problem.
    # n <= 90, m <= 400. 2^n is too large.
    # We use a randomized local search algorithm (Schöning's algorithm variant).
    
    # Convert clauses to a list of tuples (emitter_index, required_value)
    # Emitter indices are 1-based in input, we use 0-based internally.
    clauses = []
    for _ in range(m):
        clause = []
        for _ in range(3):
            val = int(next(it))
            idx = abs(val) - 1
            pol = 1 if val > 0 else 0
            clause.append((idx, pol))
        clauses.append(clause)
    
    # If m=0, any configuration works.
    if m == 0:
        print("YES")
        print(" ".join(['0'] * n))
        return

    # Check for trivial unsatisfiability: 
    # A clause (x v x v !x) simplifies to x.
    # A clause (!x v !x v x) simplifies to !x.
    # A clause (x v x v x) simplifies to x.
    # A clause (!x v !x v !x) simplifies to !x.
    # If we have both x and !x as unit clauses, it's UNSAT.
    # However, the local search handles this, and explicit checking is tricky 
    # because clauses are not necessarily unit.
    # The local search is robust enough for these constraints.
    
    # Parameters for local search
    # Max iterations: Schöning's suggests (4/3)^m * poly(m).
    # With m=400, (4/3)^400 is huge.
    # However, we can cap iterations. 
    # In practice, for random 3-SAT near phase transition, ~O(2^n) is needed,
    # but for m=400, n=90, it's over-constrained or easy.
    # Let's set a generous time limit based iteration count.
    # 2 seconds in Python allows roughly 10^7 simple operations.
    # Each walk takes O(m). Let's try around 200,000 to 500,000 walks.
    
    import random
    
    # Initialize assignment randomly
    # We can try multiple restarts.
    
    MAX_WALKS = 400000
    
    # Current assignment
    assignment = [0] * n
    
    # Pre-calculate which variables are in which clauses to speed up "affected clauses" calculation?
    # Or just iterate all clauses to find unsatisfied ones. m=400 is small.
    
    for _ in range(MAX_WALKS):
        # 1. Random Initial Assignment
        for i in range(n):
            assignment[i] = random.randint(0, 1)
        
        # 2. Local Search Loop
        # Limit steps per walk to avoid infinite loop on a bad start
        # Schöning's uses 3n steps. Let's use something related to n*m or just a constant.
        # With m=400, checking all clauses is fast.
        
        # We iterate until satisfied or stuck.
        # To prevent infinite loops on satisfied (which breaks) or unsatisfied (stuck),
        # we limit steps.
        # A dynamic limit: if we haven't solved it in ~m steps, restart.
        
        for step in range(n * 10 + 100): 
            # Find all unsatisfied clauses
            unsat_indices = []
            for i, clause in enumerate(clauses):
                satisfied = False
                for idx, pol in clause:
                    if assignment[idx] == pol:
                        satisfied = True
                        break
                if not satisfied:
                    unsat_indices.append(i)
            
            if not unsat_indices:
                # All satisfied
                print("YES")
                print(" ".join(map(str, assignment)))
                return
            
            # Pick a random unsatisfied clause
            clause_idx = random.choice(unsat_indices)
            clause = clauses[clause_idx]
            
            # Pick a random variable in that clause and flip it
            var_idx, _ = random.choice(clause)
            assignment[var_idx] = 1 - assignment[var_idx]

    print("NO")

if __name__ == '__main__':
    solve()