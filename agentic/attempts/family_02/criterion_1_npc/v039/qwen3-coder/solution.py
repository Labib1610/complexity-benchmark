from collections import defaultdict
import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    clauses = []
    for _ in range(m):
        clause = list(map(int, sys.stdin.readline().split()))
        clauses.append(clause)
    return n, m, clauses

def solve_2sat(n, clauses):
    # Convert to 2-SAT format
    # Each variable x_i corresponds to flag i being ENABLED (true) or DISABLED (false)
    # For a 3-SAT clause (a OR b OR c), we convert it to equivalent 2-SAT clauses:
    # (a OR b OR c) is equivalent to (a OR b OR new_var) AND (NOT new_var OR c)
    # But since we're dealing with 3-SAT directly, we'll use a different approach
    
    # We'll model this as a graph where each node represents a literal
    # and edges represent implications
    
    # For each 3-clause (a OR b OR c), we add the constraints:
    # (NOT a AND NOT b) => c
    # Which is equivalent to (NOT a => c) OR (NOT b => c)
    # But to make it work correctly in 2-SAT framework, we need to be more careful
    
    # Actually, let's implement a direct 3-SAT solver using brute force since n <= 90 but m <= 400
    # Wait, brute force won't work for n=90 (2^90 is too large)
    
    # Let's think differently. This is a 3-SAT problem. 
    # But since we need to output any solution, we can try to solve it with a SAT solver approach.
    
    # We'll use the implication graph approach for 3-SAT
    # For each clause (a OR b OR c), we create auxiliary variables
    
    # Simpler approach: Try all assignments? No, that's exponential.
    
    # Let's implement a proper 3-SAT solver using backtracking with unit propagation
    
    def is_satisfied(assignment):
        for clause in clauses:
            satisfied = False
            for lit in clause:
                var = abs(lit)
                desired = 1 if lit > 0 else 0
                if var in assignment and assignment[var] == desired:
                    satisfied = True
                    break
                elif var not in assignment:  # Variable not assigned yet
                    pass  # We'll check this later
            if not satisfied:
                # Check if all literals in clause are already assigned and none satisfy it
                all_assigned = True
                for lit in clause:
                    var = abs(lit)
                    if var not in assignment:
                        all_assigned = False
                        break
                
                if all_assigned:
                    # All variables in clause are assigned, but none satisfy it
                    clause_satisfied = False
                    for lit in clause:
                        var = abs(lit)
                        desired = 1 if lit > 0 else 0
                        if assignment[var] == desired:
                            clause_satisfied = True
                            break
                    if not clause_satisfied:
                        return False
        return True
    
    def backtrack(assignment, unassigned_vars):
        if not is_satisfied(assignment):
            return None
        
        if not unassigned_vars:
            return assignment.copy()
        
        # Pick a variable to assign
        var = unassigned_vars.pop()
        
        # Try setting it to 1 (ENABLED)
        assignment[var] = 1
        result = backtrack(assignment, unassigned_vars)
        if result is not None:
            return result
            
        # Try setting it to 0 (DISABLED)
        assignment[var] = 0
        result = backtrack(assignment, unassigned_vars)
        if result is not None:
            return result
            
        # Backtrack
        del assignment[var]
        unassigned_vars.add(var)
        return None
    
    # Initialize
    assignment = {}
    unassigned_vars = set(range(1, n+1))
    
    solution = backtrack(assignment, unassigned_vars)
    return solution

def main():
    n, m, clauses = read_input()
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # Solve using backtracking
    solution = solve_2sat(n, clauses)
    
    if solution is None:
        print("NO")
    else:
        print("YES")
        result = []
        for i in range(1, n+1):
            result.append(str(solution[i]))
        print(" ".join(result))

if __name__ == "__main__":
    main()