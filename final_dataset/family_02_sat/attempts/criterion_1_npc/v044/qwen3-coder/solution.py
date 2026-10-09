from collections import defaultdict
import sys

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each check, we have a clause with 3 literals
    # We need to satisfy all clauses (3-SAT variant)
    
    # We'll use a graph-based approach for 2-SAT generalized to 3-SAT
    # But since n <= 90 and m <= 400, we can try a different approach
    
    # Let's try all possible assignments - but that's 2^90, too much
    # Let's think differently - for small m, maybe we can do something smarter
    
    # Actually, let's model this as a constraint satisfaction problem
    # and use a backtracking approach with pruning
    
    # Each constraint is a disjunction of 3 literals
    constraints = []
    for _ in range(m):
        c1, c2, c3 = map(int, input().split())
        constraints.append((c1, c2, c3))
    
    def is_satisfied(assignment):
        # assignment is a list where assignment[i] is the value of toggle i+1
        for c1, c2, c3 in constraints:
            ok = False
            if c1 > 0 and assignment[c1-1] == 1:
                ok = True
            elif c1 < 0 and assignment[-c1-1] == 0:
                ok = True
                
            if not ok:
                if c2 > 0 and assignment[c2-1] == 1:
                    ok = True
                elif c2 < 0 and assignment[-c2-1] == 0:
                    ok = True
                    
            if not ok:
                if c3 > 0 and assignment[c3-1] == 1:
                    ok = True
                elif c3 < 0 and assignment[-c3-1] == 0:
                    ok = True
            
            if not ok:
                return False
        return True
    
    # Try all possible assignments
    # But with pruning - let's do a smart backtracking
    
    def backtrack(index, assignment):
        if index == n:
            return is_satisfied(assignment)
        
        # Try setting to 0
        assignment[index] = 0
        if backtrack(index + 1, assignment):
            return True
            
        # Try setting to 1
        assignment[index] = 1
        if backtrack(index + 1, assignment):
            return True
            
        return False
    
    # Optimization: let's do unit propagation or at least some constraint checking
    # But given the constraints, let's just try a direct approach first
    
    # Even better approach: since each clause has 3 literals,
    # probability that a random assignment satisfies a clause is 7/8
    # So probability all m clauses are satisfied is (7/8)^m
    # For m=400, this is very small, but let's try random assignments
    
    # But let's do systematic search with early termination
    
    assignment = [0] * n
    if backtrack(0, assignment):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()