def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(set)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Try all possible assignments with backtracking
    # We want the lexicographically smallest one
    assignment = [0] * (n + 1)
    
    def is_valid(person, schedule):
        for neighbor in adj[person]:
            if assignment[neighbor] == schedule:
                return False
        return True
    
    def backtrack(person):
        if person > n:
            return True
            
        for schedule in [1, 2, 3]:
            if is_valid(person, schedule):
                assignment[person] = schedule
                if backtrack(person + 1):
                    return True
                assignment[person] = 0
        
        return False
    
    if backtrack(1):
        print("YES")
        print(*assignment[1:])
    else:
        print("NO")

solve()