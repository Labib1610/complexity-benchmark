from itertools import combinations

def solve():
    n, m = map(int, input().split())
    conflicts = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts[u].add(v)
        conflicts[v].add(u)
        
    def backtrack(assignment, idx):
        if idx == n:
            return True
        
        for vault in (1, 2, 3):
            valid = True
            for neighbor in range(1, n + 1):
                if neighbor != idx + 1 and assignment[neighbor - 1] == vault and (idx + 1) in conflicts[neighbor]:
                    valid = False
                    break
            
            if valid:
                assignment[idx] = vault
                if backtrack(assignment, idx + 1):
                    return True
                assignment[idx] = 0
        
        return False
    
    assignment = [0] * n
    if backtrack(assignment, 0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()