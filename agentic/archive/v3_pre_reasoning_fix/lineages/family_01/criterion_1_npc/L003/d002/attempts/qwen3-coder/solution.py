import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list for the graph
    adj = [[] for _ in range(n+1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Try to 3-color the graph with colors 1, 2, 3
    # We want the lexicographically smallest assignment
    color = [0] * (n+1)  # color[i] represents the priority of task i
    
    # For each connected component, we'll do BFS/DFS to check 3-colorability
    # and assign the lex smallest coloring
    
    visited = [False] * (n+1)
    
    for start in range(1, n+1):
        if visited[start]:
            continue
            
        # BFS to get the component
        component = []
        queue = [start]
        visited[start] = True
        component.append(start)
        
        while queue:
            node = queue.pop()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    component.append(neighbor)
                    queue.append(neighbor)
        
        # Now we need to 3-color this component with lex smallest result
        # We can try all possible colorings but that's exponential
        # Instead, we use a greedy approach that tries to assign the smallest
        # available color to each node in order
        
        # But to get the globally lex smallest, we might need backtracking
        # However, since n <= 40 and it's a general graph, exact solution 
        # might be too slow. Let's try a greedy method that assigns colors
        # in order and picks the smallest available one that doesn't conflict.
        
        # Actually, let's model this properly. This is a graph 3-coloring problem.
        # Since we want the lexicographically smallest solution, we can use 
        # backtracking with pruning.
        
        # But given constraints, let's implement a backtracking solution
        # that tries colors 1,2,3 in order for each node to ensure lex order.
        
        def is_safe(node, c):
            for neighbor in adj[node]:
                if color[neighbor] == c:
                    return False
            return True
        
        # Sort component for consistent processing
        component.sort()
        
        # Backtrack to assign colors to this component
        def backtrack(nodes, idx):
            if idx == len(nodes):
                return True
                
            node = nodes[idx]
            for c in [1, 2, 3]:  # Try in lex order
                if is_safe(node, c):
                    color[node] = c
                    if backtrack(nodes, idx + 1):
                        return True
                    # No need to unassign since we return immediately when found
            return False
            
        # Check if this component can be colored
        if not backtrack(component, 0):
            print("NO")
            return
            
    # If we reach here, all components were successfully colored
    print("YES")
    print(' '.join(map(str, color[1:])))

if __name__ == "__main__":
    main()