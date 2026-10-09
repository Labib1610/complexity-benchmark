import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each clause (group), we have 3 literals
    # Positive literal i means proposal i is enacted (1)
    # Negative literal -i means proposal i is rejected (0)
    
    clauses = []
    for _ in range(m):
        clause = list(map(int, sys.stdin.readline().split()))
        clauses.append(clause)
    
    # Try all 2^n possible assignments
    for mask in range(1 << n):
        # mask represents the assignment: bit i is 1 if proposal i+1 is enacted
        valid = True
        
        for clause in clauses:
            satisfied = False
            for literal in clause:
                if literal > 0:
                    # Proposal |literal| should be enacted (1)
                    if (mask >> (literal - 1)) & 1:
                        satisfied = True
                        break
                else:
                    # Proposal |literal| should be rejected (0)
                    if not ((mask >> (-literal - 1)) & 1):
                        satisfied = True
                        break
            
            if not satisfied:
                valid = False
                break
        
        if valid:
            print("YES")
            result = []
            for i in range(n):
                result.append(str((mask >> i) & 1))
            print(" ".join(result))
            return
    
    print("NO")

solve()