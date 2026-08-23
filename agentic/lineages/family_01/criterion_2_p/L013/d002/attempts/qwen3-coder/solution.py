import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color graph with 2 colors (1 and 2). This is essentially bipartite check.
    color = [0] * n  # 0 means unvisited, 1 and 2 are the two colors
    
    # For each connected component, we do BFS
    for i in range(n):
        if color[i] == 0:
            queue = deque()
            queue.append(i)
            color[i] = 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]  # flips 1->2 and 2->1
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite. Now we need the lex smallest assignment.
    # We want to assign 1's as early as possible. 
    # Since we colored with 1 and 2, we can just map 1->1 and 2->2.
    # But to get lex smallest, we should ensure that in each component,
    # the smaller color is mapped to 1.
    # However, since we started coloring with 1, and alternated, 
    # the current coloring already gives us a valid assignment.
    # But to make it lex smallest globally, we can remap the colors per component.
    
    # Actually, let's think differently. The above BFS ensures that adjacent nodes have different colors.
    # The bitwise AND of 1 and 2 is 0, so this satisfies the constraint.
    # To get the lex smallest, we can try to see if we can flip the colors in some components.
    
    # But the simplest way is to just output the color array directly, but ensuring that
    # in case we could flip a whole component to get a smaller lex order, we don't.
    # However, our BFS already starts with node 0 assigning color 1, which is good for lex.
    
    # So we can just output the color array as is, mapping 0->1 is already done.
    # Wait, no. Our initial color assignment was arbitrary start with 1.
    # To get truly lex smallest, we can do a second pass where for each component,
    # we decide whether to flip the colors based on which leads to smaller lex.
    
    # Let's re-do the coloring with a more lex-aware approach.
    color = [0] * n
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            # Start BFS from i, but we'll collect all nodes in component first
            component = []
            queue = deque()
            queue.append(i)
            visited[i] = True
            component.append(i)
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
                        component.append(v)
            
            # Now we have all nodes in component. Do BFS again to 2-color.
            # But we want the lex smallest. So we will always try to assign 1 to the node with smallest index.
            comp_color = [0] * n
            queue = deque()
            start_node = min(component)
            queue.append(start_node)
            comp_color[start_node] = 1
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if comp_color[v] == 0:
                        comp_color[v] = 3 - comp_color[u]
                        queue.append(v)
                    elif comp_color[v] == comp_color[u]:
                        # Should not happen if bipartite
                        continue
                        
            # Copy the component coloring to global color
            for u in component:
                color[u] = comp_color[u]
                
    # Final check for bipartiteness
    valid = True
    for u in range(n):
        for v in adj[u]:
            if color[u] == color[v]:
                valid = False
                break
        if not valid:
            break
            
    if not valid:
        print("NO")
    else:
        # Map colors 1,2 to output values 1,2
        result = [str(c) for c in color]
        print("YES")
        print(' '.join(result))

if __name__ == "__main__":
    main()