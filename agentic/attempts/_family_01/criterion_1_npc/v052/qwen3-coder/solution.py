def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to 3-color the graph
    color = [0] * (n + 1)  # 0 means uncolored, 1, 2, 3 are the colors
    
    def is_bipartite(start):
        # Check if the component starting at 'start' can be 3-colored
        # We'll use a greedy approach with backtracking for small n
        stack = [start]
        color[start] = 1
        
        while stack:
            node = stack.pop()
            node_color = color[node]
            
            # Try colors 1, 2, 3 for neighbors
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    # Find a color different from node's color
                    used = set()
                    for nn in adj[neighbor]:
                        if color[nn] != 0:
                            used.add(color[nn])
                    
                    # Try to assign a color to neighbor
                    found_color = False
                    for c in range(1, 4):
                        if c != node_color and c not in used:
                            color[neighbor] = c
                            stack.append(neighbor)
                            found_color = True
                            break
                    
                    if not found_color:
                        # Need to backtrack - but for simplicity with small n,
                        # we'll just return that it's not possible with current assignment
                        pass
                elif color[neighbor] == node_color:
                    return False
        return True
    
    # For the general case, we need a proper 3-coloring algorithm
    # Since n <= 40, we can try a backtracking approach
    
    def backtrack(node):
        if node > n:
            return True
            
        if color[node] != 0:
            return backtrack(node + 1)
            
        # Get colors used by neighbors
        used = set()
        for neighbor in adj[node]:
            if color[neighbor] != 0:
                used.add(color[neighbor])
        
        # Try each available color
        for c in range(1, 4):
            if c not in used:
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0  # backtrack
                
        return False
    
    # Check if 3-coloring is possible
    if backtrack(1):
        print("YES")
        print(*color[1:])
    else:
        print("NO")

solve()