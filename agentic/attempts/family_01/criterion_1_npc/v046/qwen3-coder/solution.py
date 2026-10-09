import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list - technicians that cannot work together
    adj = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Try to 3-color the graph
    # 0 = unassigned, 1, 2, 3 = time blocks
    color = [0] * (n + 1)
    
    def is_safe(node, c):
        # Check if assigning color c to node is safe
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        # If already assigned (shouldn't happen in our logic but safe)
        if color[node] != 0:
            return backtrack(node + 1)
            
        for c in range(1, 4):  # Try colors 1, 2, 3
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0  # Backtrack
                
        return False
    
    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        print(*color[1:])
    else:
        print("NO")

solve()