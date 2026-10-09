from collections import defaultdict
import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each rule, we have three literals (positive for ON, negative for OFF)
    rules = []
    for _ in range(m):
        rule = list(map(int, sys.stdin.readline().split()))
        rules.append(rule)
    
    # Try all possible assignments
    # Since n <= 90, we can't enumerate all 2^n assignments
    # But we can use the fact that this is a 3-SAT problem and try to solve it efficiently
    
    # Let's use a backtracking approach with constraint propagation
    
    # For each variable, we'll track possible values (0 or 1)
    # Initially, all variables can be either 0 or 1
    possible = [[0, 1] for _ in range(n + 1)]  # Index 0 unused
    
    # Convert rules to a more convenient format
    # Each rule is a disjunction of three literals
    # We'll represent literals as (variable, value) where variable is 1-indexed
    # Positive literal i means variable i should be 1
    # Negative literal -i means variable i should be 0
    
    def is_satisfied(rule, assignment):
        for literal in rule:
            var = abs(literal)
            required = 1 if literal > 0 else 0
            if assignment[var] == required:
                return True
        return False
    
    def backtrack(assignment, index):
        if index > n:
            # Check if all rules are satisfied
            for rule in rules:
                if not is_satisfied(rule, assignment):
                    return None
            return assignment[:]
        
        # Try each possible value for the current variable
        for value in possible[index]:
            assignment[index] = value
            result = backtrack(assignment, index + 1)
            if result is not None:
                return result
        
        return None
    
    # This approach might be too slow. Let's try a different approach.
    # Since each rule has exactly 3 literals, this is a 3-SAT problem.
    # For small instances, we can try all assignments.
    # But with n up to 90, that's infeasible.
    
    # Let's try a more intelligent approach:
    # For each rule, there are 7 out of 8 possible assignments that satisfy it.
    # We can try to find a solution by checking assignments systematically.
    
    # Since 2^90 is too large, let's implement a smarter backtracking
    # with early rule checking.
    
    def backtrack_smart(assignment, index):
        if index > n:
            return assignment[:]
        
        # Try each value
        for value in [0, 1]:
            assignment[index] = value
            
            # Check if this assignment violates any rule so far
            valid = True
            for rule in rules:
                # If all variables in the rule have been assigned,
                # check if the rule is satisfied
                all_assigned = True
                rule_satisfied = False
                for literal in rule:
                    var = abs(literal)
                    if var > index:  # Not yet assigned
                        all_assigned = False
                        break
                    required = 1 if literal > 0 else 0
                    if assignment[var] == required:
                        rule_satisfied = True
                        break
                
                if all_assigned and not rule_satisfied:
                    valid = False
                    break
            
            if valid:
                result = backtrack_smart(assignment, index + 1)
                if result is not None:
                    return result
        
        return None
    
    # Start backtracking
    assignment = [0] * (n + 1)
    result = backtrack_smart(assignment, 1)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(result[i]) for i in range(1, n + 1)))

solve()