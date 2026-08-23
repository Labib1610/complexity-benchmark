import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # The constraint is |a_u^2 - a_v^2| = 3
    # Since a_u, a_v ∈ {1, 2}, we have squares {1, 4}
    # So |a_u^2 - a_v^2| ∈ {|1-1|=0, |1-4|=3, |4-1|=3, |4-4|=0}
    # So we need exactly one endpoint to have value 1 and the other to have value 2
    
    # This means the graph must be bipartite
    # Color the graph with 2 colors, where color 0 means amplitude 1, color 1 means amplitude 2
    
    color = [-1] * (n + 1)  # -1 means unvisited
    visited = [False] * (n + 1)
    
    # Check if the graph is bipartite
    for start in range(1, n + 1):
        if not visited[start]:
            queue = deque([start])
            color[start] = 0
            visited[start] = True
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # Graph is bipartite, so a solution exists
    # For lexicographically smallest, we want nodes 1,2,3,... to have value 1 if possible
    # That means we prefer color 0 for earlier nodes
    
    # But we already have a valid coloring. We just need to make sure it's lex smallest
    # Let's re-color to ensure this property
    
    result = [0] * (n + 1)
    
    # For each component, decide whether to flip colors
    visited_check = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if not visited_check[start]:
            # Collect all nodes in this component
            component = []
            queue = deque([start])
            visited_check[start] = True
            component.append(start)
            
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if not visited_check[neighbor]:
                        visited_check[neighbor] = True
                        component.append(neighbor)
                        queue.append(neighbor)
            
            # For this component, check if flipping colors gives better lex order
            # Try both assignments and pick the lexicographically smaller one
            
            # Assignment 1: color -> amplitude (0->1, 1->2)
            assignment1 = [0] * (n + 1)
            for node in component:
                assignment1[node] = 1 if color[node] == 0 else 2
                
            # Assignment 2: flipped colors (0->2, 1->1)  
            assignment2 = [0] * (n + 1)
            for node in component:
                assignment2[node] = 2 if color[node] == 0 else 1
            
            # Compare lexicographically
            should_flip = False
            for node in sorted(component):
                if assignment2[node] < assignment1[node]:
                    should_flip = True
                    break
                elif assignment2[node] > assignment1[node]:
                    should_flip = False
                    break
            
            if should_flip:
                for node in component:
                    color[node] = 1 - color[node]
    
    # Generate final result
    for i in range(1, n + 1):
        result[i] = 1 if color[i] == 0 else 2
    
    print("YES")
    print(" ".join(map(str, result[1:])))

solve()