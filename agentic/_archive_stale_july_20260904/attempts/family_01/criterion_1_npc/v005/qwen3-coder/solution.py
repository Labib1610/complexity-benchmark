import sys
from itertools import product

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Create adjacency list for conflicts
    conflicts = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        conflicts[u].append(v)
        conflicts[v].append(u)
    
    # Try all possible assignments
    for assignment in product([1, 2, 3], repeat=n):
        # Check if this assignment is valid
        valid = True
        for i in range(n):
            worker = i + 1
            shift = assignment[i]
            # Check conflicts for this worker
            for conflicted_worker in conflicts[worker]:
                if conflicted_worker <= n and assignment[conflicted_worker - 1] == shift:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()