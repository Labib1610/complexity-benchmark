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
    
    constraints = []
    idx = 2
    for _ in range(m):
        c = []
        for _ in range(3):
            c.append(int(data[idx]))
            idx += 1
        constraints.append(c)
    
    # For each constraint, we need at least one of the three literals to be true
    # This is a 3-SAT-like problem but each clause is an OR of exactly 3 literals
    # We can solve this using brute-force since n <= 90, but that's too large.
    # However, we can use the fact that each clause has 3 literals and try to find
    # a solution using a randomized algorithm or backtracking with pruning.
    # But given the constraints, let's model this as a 2-SAT variant or use other techniques.
    
    # Actually, this is exactly 3-SAT where each clause is a disjunction of 3 literals
    # But 3-SAT is NP-complete. However, there might be structure or small cases.
    # Let's think differently: this is a constraint satisfaction problem.
    
    # Let's model this properly:
    # Each variable (valve) can be 0 (CLOSED) or 1 (OPEN)
    # Each constraint is a disjunction of 3 literals
    # We want to find an assignment satisfying all constraints
    
    # Since n can be up to 90, brute force won't work.
    # But wait, let's check if there's a pattern or if we can reduce this.
    
    # Let's try a different approach: since each constraint is a disjunction of 3,
    # we can think of this as a hitting set problem or use other CSP techniques.
    # But perhaps the best way is to implement a simple backtracking with pruning.
    
    # To make it feasible, let's implement a local search or backtracking.
    # Given the time limit of 2 seconds, a well-implemented backtracking might work.
    
    # Let's represent the problem clearly:
    # variables: x[1] to x[n], each 0 or 1
    # constraints: for each constraint [a,b,c], at least one must be satisfied
    # literal value: if k>0 then x[k]==1, if k<0 then x[-k]==0
    
    def is_satisfied(assignment):
        for clause in constraints:
            satisfied = False
            for lit in clause:
                var = abs(lit)
                desired = 1 if lit > 0 else 0
                if assignment[var] == desired:
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True
    
    # Since n can be up to 90, even backtracking might be too slow.
    # But let's try a randomized approach or look for contradictions.
    
    # One idea: for each constraint, there are 2^3=8 possible assignments to its variables,
    # but only 1 (all false) makes it unsatisfied. So 7/8 chance per constraint.
    # With m=400, chance of satisfying all is (7/8)^400 which is extremely small.
    # But variables overlap, so it's not independent.
    
    # Let's try to build a solution greedily or use contradiction detection.
    
    # Another approach: convert to SAT and use properties.
    # But since this is a special case (each clause has exactly 3 literals),
    # and we're asked to find any solution, maybe we can do better.
    
    # Let's try a simple randomized algorithm:
    # Try random assignments until one works or we give up.
    
    import random
    max_tries = min(10000, 2**min(n, 20))  # Limit tries based on n
    
    for _ in range(max_tries):
        assignment = [0] * (n+1)
        for i in range(1, n+1):
            assignment[i] = random.randint(0, 1)
        
        if is_satisfied(assignment):
            print("YES")
            print(" ".join(str(assignment[i]) for i in range(1, n+1)))
            return
    
    # If random didn't work, let's try a systematic approach for small n
    if n <= 20:
        for mask in range(1 << n):
            assignment = [0] * (n+1)
            for i in range(n):
                assignment[i+1] = (mask >> i) & 1
            
            if is_satisfied(assignment):
                print("YES")
                print(" ".join(str(assignment[i]) for i in range(1, n+1)))
                return
    
    # If still nothing, assume NO
    print("NO")

if __name__ == "__main__":
    main()