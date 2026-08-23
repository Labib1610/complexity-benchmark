import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all possible assignments in lexicographical order
    # Using backtracking with constraint propagation
    assignment = [0] * (n + 1)  # 1-indexed
    
    def is_valid(node, color):
        # Check if assigning 'color' to 'node' violates any constraints
        for neighbor in adj[node]:
            if assignment[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in [1, 2, 3]:
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        
        return False
    
    # Special case: check if any node has more than 3 neighbors (impossible to color)
    for i in range(1, n + 1):
        if len(adj[i]) >= 3:
            # Need to check if neighbors form a triangle with this node
            neighbors = list(adj[i])
            # Count edges between neighbors
            edge_count = 0
            for j in range(len(neighbors)):
                for k in range(j + 1, len(neighbors)):
                    if neighbors[k] in adj[neighbors[j]]:
                        edge_count += 1
            # If neighbors form a triangle, we need 4 colors which is impossible
            if edge_count >= 3:  # All neighbors connected to each other
                print("NO")
                return
    
    if backtrack(1):
        print("YES")
        print(*assignment[1:])
    else:
        print("NO")

solve()