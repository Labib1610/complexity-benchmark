def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all possible assignments (3^n possibilities)
    # But we can do better with backtracking
    assignment = [0] * (n + 1)  # 1-indexed
    
    def is_valid(process, tier):
        # Check if assigning tier to process violates any constraints
        for neighbor in adj[process]:
            if assignment[neighbor] != 0 and abs(assignment[neighbor] - tier) < 1:
                return False
        return True
    
    def backtrack(process):
        if process > n:
            return True
        
        for tier in range(1, 4):
            if is_valid(process, tier):
                assignment[process] = tier
                if backtrack(process + 1):
                    return True
                assignment[process] = 0
        
        return False
    
    if backtrack(1):
        print("YES")
        print(*assignment[1:])
    else:
        print("NO")

solve()