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
        print(" ".join(["1"] * n))
        return
    
    clauses = []
    idx = 2
    for _ in range(m):
        clause = []
        for _ in range(3):
            num = int(data[idx])
            idx += 1
            clause.append(num)
        clauses.append(clause)
    
    # For each relay i, we have boolean variable x_i (1 <= i <= n)
    # x_i = True means Alpha channel, False means Beta channel
    # Clause (a b c) means at least one of them must be satisfied
    # If a = 5, it means x_5 should be True
    # If a = -5, it means x_5 should be False (i.e., not x_5)
    
    # We reduce this to 2-SAT by converting each 3-clause to equivalent 2-clauses
    # But actually, this is 3-SAT, and we need to solve it directly or enumerate since n<=90, m<=400
    # However, given constraints, let's try to model as 2-SAT or use other approach
    # Actually, this is just a satisfiability problem with 3-clauses (each clause has 3 literals)
    # This is 3-SAT, but small enough to possibly enumerate or use backtracking
    # Let's use a SAT solver approach or brute-force for small n
    
    # Since n <= 90, brute force won't work
    # We can model this as a 3-SAT and try to find a solution using backtracking with pruning
    
    # Let's build implication graph for 2-SAT, but we have 3-clauses
    # We can convert each 3-clause to equivalent 2-clauses:
    # (a or b or c) is equivalent to (a or b or y) and (not y or c) where y is new variable
    # But that increases variables. Let's instead implement a simple backtracking
    
    # Let's represent the problem and try to solve it with backtracking
    
    def is_satisfied(assignments):
        for clause in clauses:
            satisfied = False
            for lit in clause:
                var = abs(lit)
                desired = (lit > 0)
                if assignments[var] == desired:
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True
    
    # Try all possible assignments - not feasible for n=90
    # Need smarter approach
    
    # Let's model as SAT and use a heuristic: try greedy assignment
    # Or model as CSP and use backtracking with constraint propagation
    
    # Use backtracking with early termination
    assignment = [None] * (n + 1)  # index 0 unused
    
    def backtrack(var):
        if var == n + 1:
            return is_satisfied(assignment)
        
        for val in [True, False]:
            assignment[var] = val
            # Check if current partial assignment violates any clause completely
            # That is, check if there's a clause where all literals are already decided and none are satisfied
            ok = True
            for clause in clauses:
                unsat_count = 0
                unknown = False
                for lit in clause:
                    v = abs(lit)
                    if v >= var:
                        if v == var:
                            desired = (lit > 0)
                            if assignment[v] != desired:
                                unsat_count += 1
                            # else satisfied, so clause is OK
                        else:
                            unknown = True
                            break
                    else:
                        desired = (lit > 0)
                        if assignment[v] == desired:
                            # clause already satisfied
                            break
                        else:
                            unsat_count += 1
                
                if not unknown and unsat_count == 3:
                    ok = False
                    break
            
            if ok:
                if backtrack(var + 1):
                    return True
        assignment[var] = None
        return False
    
    # Start backtracking from variable 1
    if backtrack(1):
        print("YES")
        result = []
        for i in range(1, n+1):
            if assignment[i]:
                result.append('1')
            else:
                result.append('0')
        print(' '.join(result))
    else:
        print("NO")

if __name__ == "__main__":
    main()