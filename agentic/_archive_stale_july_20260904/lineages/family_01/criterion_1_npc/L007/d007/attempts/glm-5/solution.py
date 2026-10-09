import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Sort adjacency lists for deterministic processing
    for i in range(n):
        adj[i].sort()
    
    # Check if assignment is valid (all edges have energy -3)
    def is_valid(assignment):
        for u in range(n):
            cu = assignment[u]
            for v in adj[u]:
                if v > u:  # Check each edge once
                    cv = assignment[v]
                    if cu == cv:
                        return False
        return True
    
    # Try to find lexicographically smallest valid assignment
    assignment = [0] * n
    
    def dfs(pos):
        if pos == n:
            return True
        
        for c in range(1, 4):
            assignment[pos] = c
            valid = True
            for v in adj[pos]:
                if v < pos and assignment[v] == c:
                    valid = False
                    break
            if valid and dfs(pos + 1):
                return True
        
        return False
    
    if dfs(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()