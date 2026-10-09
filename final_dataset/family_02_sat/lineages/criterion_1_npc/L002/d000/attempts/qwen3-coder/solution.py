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
        clauses.append((l1, l2, l3))
        idx += 3
    
    # We need to solve 3-SAT where each clause must have at least one literal true
    # Variable x_i corresponds to node i being in phase 1 (if x_i = True) or phase 0 (if x_i = False)
    # For a literal k:
    #   if k > 0, the literal is x_k
    #   if k < 0, the literal is NOT x_{|k|}
    
    # We'll use a brute-force approach for small n, but since n can be up to 90,
    # we need a more efficient method. However, given the constraints and that this
    # is a typical competitive programming problem, let's try to model it as 2-SAT
    # if possible or use a SAT solver approach. But since it's 3-SAT, and n is up to 90,
    # a randomized or heuristic approach might be needed. But let's first see if we can
    # model some constraints as 2-SAT or find a pattern.
    
    # Let's try a randomized approach or backtracking with pruning.
    # But given the large n, let's attempt to use a known algorithm or insight.
    
    # This is exactly 3-SAT. Each clause is a disjunction of 3 literals.
    # We can try to solve it using a SAT solver approach or randomized assignment.
    # Since we're in competitive programming, let's try a randomized approach first.
    
    # However, let's think differently. This is a classic 3-SAT problem.
    # We can model it and try to solve with a backtracking algorithm with pruning.
    # But with n=90 and m=400, that might be too slow.
    
    # Let's try a randomized approach: try random assignments and check.
    # But that might not be reliable. Let's instead implement a proper 3-SAT solver.
    
    # We'll implement a simple backtracking with unit propagation and pure literal elimination.
    # But for performance, let's limit the number of random restarts or use a heuristic.
    
    # Let's model the problem properly.
    # Variables: x_1, ..., x_n where x_i = True means node i is in Phase 1.
    # Clause: (l1 or l2 or l3) where l_i is a literal.
    
    # Let's use a known approach: try to solve with a SAT solver logic.
    # We'll implement a simple DPLL-style algorithm.
    
    # First, let's build the formula
    # We'll represent literals as integers: positive for x_i, negative for not x_i
    
    # Let's try a different approach: since this is a competitive programming problem,
    # there might be a pattern or the test cases might be solvable with heuristics.
    
    # Let's try a greedy randomized approach: assign random values and check.
    # But to be safe, let's implement a proper backtracking.
    
    # For now, let's implement a backtracking solution with some optimizations.
    
    # Let's represent the problem as a 3-SAT instance and solve it.
    # We'll use a recursive backtracking with unit propagation.
    
    # Let's define a function to evaluate if a clause is satisfied given an assignment
    def is_satisfied(clause, assignment):
        for lit in clause:
            var = abs(lit)
            if var == 0:
                continue
            if lit > 0:
                if assignment.get(var, -1) == 1:
                    return True
            else:
                if assignment.get(var, -1) == 0:
                    return True
        return False
    
    # Let's try all 2^n assignments for small n, but n can be 90, so that's impossible.
    # We need a smarter approach.
    
    # This is a known NP-complete problem. In competitive programming, often there's
    # a heuristic or the problem is designed to be solvable with a specific approach.
    
    # Let's try a randomized approach with many trials.
    import random
    
    def check(assignment):
        for clause in clauses:
            satisfied = False
            for lit in clause:
                var = abs(lit)
                if lit > 0:
                    if assignment[var] == 1:
                        satisfied = True
                        break
                else:
                    if assignment[var] == 0:
                        satisfied = True
                        break
            if not satisfied:
                return False
        return True
    
    # Try random assignments
    for _ in range(10000): # Heuristic: try 10000 random assignments
        assignment = [0] * (n+1)
        for i in range(1, n+1):
            assignment[i] = random.randint(0,1)
        if check(assignment):
            print("YES")
            print(" ".join(map(str, assignment[1:])))
            return
    
    # If random didn't work, try a more systematic approach.
    # But for now, let's assume that if 10000 random trials didn't work,
    # it's likely unsatisfiable or needs a better algorithm.
    
    # Let's implement a simple backtracking with pruning.
    def solve():
        assignment = [-1] * (n+1) # -1 means unassigned
        
        def is_clause_satisfied(clause):
            for lit in clause:
                var = abs(lit)
                if lit > 0:
                    if assignment[var] == 1:
                        return True
                else:
                    if assignment[var] == 0:
                        return True
            return False
        
        def is_current_state_ok():
            for clause in clauses:
                # If all literals are assigned and none are true, then it's bad
                all_assigned = True
                for lit in clause:
                    var = abs(lit)
                    if assignment[var] == -1:
                        all_assigned = False
                        break
                
                if all_assigned:
                    satisfied = False
                    for lit in clause:
                        var = abs(lit)
                        if lit > 0:
                            if assignment[var] == 1:
                                satisfied = True
                                break
                        else:
                            if assignment[var] == 0:
                                satisfied = True
                                break
                    if not satisfied:
                        return False
            return True
        
        def backtrack(var):
            if var == n+1:
                # Check all clauses
                for clause in clauses:
                    satisfied = False
                    for lit in clause:
                        v = abs(lit)
                        if lit > 0:
                            if assignment[v] == 1:
                                satisfied = True
                                break
                        else:
                            if assignment[v] == 0:
                                satisfied = True
                                break
                    if not satisfied:
                        return False
                return True
            
            # Try 0
            assignment[var] = 0
            if is_current_state_ok():
                if backtrack(var + 1):
                    return True
            
            # Try 1
            assignment[var] = 1
            if is_current_state_ok():
                if backtrack(var + 1):
                    return True
            
            # Backtrack
            assignment[var] = -1
            return False
        
        if backtrack(1):
            print("YES")
            print(" ".join(map(str, assignment[1:])))
        else:
            print("NO")
    
    solve()

if __name__ == "__main__":
    main()