import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Colors: 0 means uncolored, 1, 2, 3 are the three sealants
    color = [0] * (n + 1)
    
    # Check if the graph is 3-colorable using backtracking
    # We want the lexicographically smallest coloring
    
    def is_safe(node, c):
        # Check if assigning color c to node is safe
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        # Try colors 1, 2, 3 in order for lexicographically smallest
        for c in range(1, 4):
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0  # Backtrack
        
        return False
    
    # Since n <= 40, but we need to check if it's 3-colorable,
    # which is NP-complete in general. However, the constraints might allow it.
    # Let's try a more efficient approach by checking connected components.
    
    # For a graph to be 3-colorable, each connected component must be 3-colorable.
    # Also, if any component has chromatic number > 3, then it's impossible.
    
    visited = [False] * (n + 1)
    
    def dfs_check_bipartite(start):
        # This is not sufficient; we need actual 3-coloring check
        stack = [start]
        color[start] = 1
        visited[start] = True
        
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = 3 - color[node]  # Alternate between 1 and 2
                    stack.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    # Actually, let's just do backtracking on the entire graph since n <= 40
    # and the structure might make it solvable
    
    # But first, let's see if there's an odd cycle (which would make it not 2-colorable)
    # but we need 3-colorable
    
    # Let's implement a proper backtracking solution trying to color nodes 1 to n
    
    def solve_coloring():
        # Try to 3-color the graph with lexicographically smallest result
        for i in range(1, n + 1):
            if color[i] == 0:  # Not yet colored
                # We'll handle connected components during the search
                
                # For finding lexicographically smallest, we can try all possibilities
                # but that's too much. Instead, we use backtracking with early exit.
                pass
        
        # Start backtracking from node 1
        return backtrack(1)
    
    # More direct approach: try all colorings in lexicographical order via backtracking
    result = solve_coloring()
    
    if not result:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, color[1:])))

# Let's reimplement with a cleaner backtracking approach:

def solve_clean():
    n, m = map(int, input().split())
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    def is_valid(v, c):
        for u in adj[v]:
            if color[u] == c:
                return False
        return True
    
    def backtrack(v):
        if v > n:
            return True
            
        for c in [1, 2, 3]:
            if is_valid(v, c):
                color[v] = c
                if backtrack(v + 1):
                    return True
                color[v] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, color[1:])))
    else:
        print("NO")

solve_clean()