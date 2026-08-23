import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    graph = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * n
    visited = [False] * n
    
    # Check if bipartite for each connected component
    for start in range(n):
        if visited[start]:
            continue
            
        queue = deque()
        queue.append(start)
        visited[start] = True
        color[start] = 1  # Start with color 1
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 3 - current_color  # 1 -> 2, 2 -> 1
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] != next_color:
                    print("NO")
                    return
    
    # If we reach here, a valid coloring exists
    # We need the lexicographically smallest sequence
    # That means we prefer color 1 over color 2 for vessel 1, then vessel 2, etc.
    # But we've already found a valid coloring. 
    # The BFS starting with color 1 for the first node ensures lexicographic minimality
    # in the sense that we can always flip the colors in a component to make the first 
    # node in that component (in terms of order 1,2,...,n) have color 1 if possible.
    # However, our BFS already starts with color 1, so it's optimal.
    
    # Actually, let's reconsider. For lexicographically smallest, we want the earliest 
    # vessels to be 1 if possible. Our current approach might not guarantee that because
    # we process components in order of their lowest vertex, but the coloring within a 
    # component depends on where we start the BFS.
    
    # Let's re-implement to ensure lexicographic minimality:
    # For each connected component, we try to assign color 1 to the earliest node in that component.
    
    final_color = [0] * n
    processed = [False] * n
    
    for i in range(n):
        if processed[i]:
            continue
            
        # Find all nodes in this component
        component = []
        queue = deque([i])
        processed[i] = True
        component.append(i)
        
        temp_processed = {i}
        edges = []  # Store edges in this component
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                edges.append((node, neighbor))
                if neighbor not in temp_processed:
                    temp_processed.add(neighbor)
                    processed[neighbor] = True
                    component.append(neighbor)
                    queue.append(neighbor)
        
        # Try to 2-color this component
        # We want the earliest node in component to be as small as possible in lex order
        # Since colors are 1 and 2, and we want lex smallest sequence,
        # we should try to assign 1 to the nodes in order 1,2,...,n if possible.
        
        # Let's do BFS from the node with minimum index in the component
        min_node = min(component)
        comp_color = {}
        queue = deque([min_node])
        comp_color[min_node] = 1
        
        valid = True
        while queue and valid:
            node = queue.popleft()
            current_c = comp_color[node]
            next_c = 3 - current_c
            
            for neighbor in graph[node]:
                if neighbor in temp_processed:  # It's in the same component
                    if neighbor not in comp_color:
                        comp_color[neighbor] = next_c
                        queue.append(neighbor)
                    elif comp_color[neighbor] != next_c:
                        print("NO")
                        return
        
        # Assign the colors to final_color
        for node in component:
            final_color[node] = comp_color[node]
    
    print("YES")
    print(' '.join(str(c) for c in final_color))

solve()