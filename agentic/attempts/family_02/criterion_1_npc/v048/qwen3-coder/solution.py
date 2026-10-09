from collections import defaultdict
import sys

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        clauses.append(clause)
    
    # Try all possible assignments
    for mask in range(1 << n):
        valid = True
        assignment = []
        for i in range(n):
            assignment.append((mask >> i) & 1)
        
        # Check all clauses
        for clause in clauses:
            satisfied = False
            for literal in clause:
                if literal > 0:
                    var_index = literal - 1
                    if assignment[var_index] == 1:
                        satisfied = True
                        break
                else:
                    var_index = -literal - 1
                    if assignment[var_index] == 0:
                        satisfied = True
                        break
            if not satisfied:
                valid = False
                break
        
        if valid:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()